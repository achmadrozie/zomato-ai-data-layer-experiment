"""Grade and report final answers for the A vs E full-answer trial.

Commands:
  python score.py list                 List all completed attempts with their final answers.
  python score.py list --arm A         Filter by arm.
  python score.py list --question Q01  Filter by question.
  python score.py report               Print score summary from grades.local.json.

Grading is manual: after reading the answers with `list`, record each grade in
run.local/grades.local.json as a list of objects:

  [
    {"id": "A-Q01-r1", "correct": true,  "note": ""},
    {"id": "E-Q01-r1", "correct": false, "note": "wrong scope — used all orders not delivered"},
    ...
  ]

`report` reads that file and prints per-arm accuracy, per-question 0/N scores,
and run-level scores. Mark clarification/abstention responses separately with
"correct": null and "abstention": true so they are excluded from numeric accuracy.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
ATTEMPTS_DIR = HERE / "run.local" / "attempts"
GRADES_FILE = HERE / "run.local" / "grades.local.json"


def _load_attempts(arm: str | None, question: str | None) -> list[dict]:
    if not ATTEMPTS_DIR.exists():
        return []
    attempts = []
    for path in sorted(ATTEMPTS_DIR.glob("*.json")):
        a = json.loads(path.read_text())
        if a.get("status") != "completed":
            continue
        if arm and a.get("arm") != arm:
            continue
        if question and a.get("question_id") != question:
            continue
        attempts.append(a)
    return attempts


def cmd_list(args: argparse.Namespace) -> None:
    attempts = _load_attempts(args.arm, args.question)
    if not attempts:
        print("No completed attempts found.")
        return
    for a in attempts:
        plan = a.get("plan", {})
        plan_kind = plan.get("kind", "?")
        result_error = a.get("result_error")
        print(f"\n{'='*72}")
        print(f"ID:       {a['id']}")
        print(f"Question: {a['question']}")
        print(f"Plan:     {plan_kind}", end="")
        if plan_kind == "sql":
            print(f"\n          {plan.get('query', '')[:120]}...")
        elif plan_kind == "metricflow":
            print(f"  metric={plan.get('metric')}  group_by={plan.get('group_by')!r}")
        else:
            print(f"  reason={plan.get('reason')}")
        if result_error:
            print(f"Error:    {result_error}")
        print(f"Answer:\n{a.get('final_answer', '(none)')}")


def cmd_report(args: argparse.Namespace) -> None:
    if not GRADES_FILE.exists():
        print(f"Grades file not found: {GRADES_FILE}")
        print("Create it manually after grading with `list`.")
        return

    grades = {g["id"]: g for g in json.loads(GRADES_FILE.read_text())}
    attempts = _load_attempts(None, None)

    arm_correct: dict[str, list[bool]] = defaultdict(list)
    arm_abstentions: dict[str, int] = defaultdict(int)
    question_arm_correct: dict[tuple[str, str], list[bool]] = defaultdict(list)

    ungraded = []
    for a in attempts:
        aid = a["id"]
        if aid not in grades:
            ungraded.append(aid)
            continue
        g = grades[aid]
        arm = a["arm"]
        qid = a["question_id"]
        if g.get("abstention"):
            arm_abstentions[arm] += 1
            continue
        correct = bool(g["correct"])
        arm_correct[arm].append(correct)
        question_arm_correct[(qid, arm)].append(correct)

    if ungraded:
        print(f"Warning: {len(ungraded)} attempt(s) have no grade — excluded from scores.")
        for uid in ungraded:
            print(f"  {uid}")
        print()

    print("=== Arm accuracy (mean correctness, excluding abstentions) ===")
    for arm in sorted(arm_correct):
        scores = arm_correct[arm]
        pct = 100 * sum(scores) / len(scores) if scores else float("nan")
        print(f"  Arm {arm}: {sum(scores)}/{len(scores)}  ({pct:.0f}%)"
              f"  abstentions={arm_abstentions[arm]}")

    print("\n=== Per-question scores (correct/attempts per arm) ===")
    questions_seen = sorted({qid for (qid, _) in question_arm_correct})
    arms_seen = sorted({arm for (_, arm) in question_arm_correct})
    header = f"{'QID':<8}" + "".join(f"  {'Arm '+a:<10}" for a in arms_seen)
    print(f"  {header}")
    for qid in questions_seen:
        row = f"  {qid:<8}"
        for arm in arms_seen:
            scores = question_arm_correct.get((qid, arm), [])
            if scores:
                row += f"  {sum(scores)}/{len(scores):<9}"
            else:
                row += f"  {'—':<10}"
        print(row)


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")

    p_list = sub.add_parser("list", help="List completed attempts and their answers")
    p_list.add_argument("--arm", choices=["A", "B", "C", "D", "E", "F"])
    p_list.add_argument("--question", metavar="QID")

    sub.add_parser("report", help="Print score summary from grades.local.json")

    args = parser.parse_args()
    if args.command == "list":
        cmd_list(args)
    elif args.command == "report":
        cmd_report(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
