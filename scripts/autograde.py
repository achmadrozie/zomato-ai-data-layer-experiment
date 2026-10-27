"""Grade every final answer against the reference values, deterministically.

The reference values in experiments/gold_25_results.json come from running the
author-only gold_25.local.sql (use --refresh-gold to regenerate; needs Snowflake
credentials). Every attempt is checked by the same rules: each requested number must
appear in the final answer within the rubric tolerance, the required identities and
statements must be present, and a clarification or failed attempt scores 0. Q22-Q24
score 0 in arms A-E because the eligibility rules are supplied only in F. The checker
never looks at the arm or model, and the tool traces are not used for scoring.

    python3 scripts/autograde.py            # report disagreements with stored grades
    python3 scripts/autograde.py --write    # overwrite the grade files with these scores
"""

import argparse
import json
import re
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPERIMENTS = ROOT / "experiments"
RUN = EXPERIMENTS / "run.local"
GOLD_SQL = EXPERIMENTS / "gold_25.local.sql"
GOLD_RESULTS = EXPERIMENTS / "gold_25_results.json"
GROUPS = {
    "gpt-4.1": ("af_25_v2_rep{}", "af_25_v2_grades.json", ""),
    "gpt-6-luna": ("af_25_luna_rep{}", "af_25_luna_grades.json", "luna_"),
}


def refresh_gold():
    import decimal
    import datetime
    import os
    import snowflake.connector
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")
    parts = re.split(r"^-- (Q\d\d)\s*$", GOLD_SQL.read_text(), flags=re.M)
    blocks = {"Q01-05": parts[0]}
    blocks.update({parts[i]: parts[i + 1] for i in range(1, len(parts), 2)})
    conn = snowflake.connector.connect(
        account=os.environ["SNOWFLAKE_ACCOUNT"], user=os.environ["SNOWFLAKE_USER"],
        password=os.environ["SNOWFLAKE_PASSWORD"], warehouse="ZOMATO_WH",
        database="ZOMATO_DLR", schema="CORE", role="DBT_LAYER_REFACTOR_ROLE",
        session_parameters={"STATEMENT_TIMEOUT_IN_SECONDS": 300})

    def plain(value):
        if isinstance(value, decimal.Decimal):
            return float(value)
        if isinstance(value, (datetime.date, datetime.datetime)):
            return str(value)
        return value

    result = {}
    cursor = conn.cursor()
    for key, block in blocks.items():
        cursor.execute(re.sub(r"^--.*$", "", block, flags=re.M).strip().rstrip(";"))
        result[key] = {"cols": [c[0] for c in cursor.description],
                       "rows": [[plain(v) for v in row] for row in cursor.fetchall()]}
    GOLD_RESULTS.write_text(json.dumps(result, indent=1) + "\n")


G = json.loads(GOLD_RESULTS.read_text()) if GOLD_RESULTS.exists() else {}


def rows(key):
    return G[key]["rows"]


# ---------- requirements: ("n", value, tol, signed?) / ("t", regex) ----------
def N(v, tol=0.01, signed=False, pct=False): return ("n", float(v), tol, signed, pct)
def C(v): return ("n", float(v), 0.5, False, False)           # exact integer
def T(rx): return ("t", rx)

def build():
    R = {}
    q = rows("Q01-05")[0]
    R["Q01"] = [C(q[0])]; R["Q02"] = [N(q[1])]; R["Q03"] = [N(q[2])]
    R["Q04"] = [N(q[3],pct=True)]; R["Q05"] = [N(q[4])]
    a, b = rows("Q06")
    R["Q06"] = [T("dec"), N(a[2]), N(b[2]), N(a[2]-b[2])]
    j, d = rows("Q07")
    R["Q07"] = [C(j[1]), C(d[1]), N(j[2]), N(d[2]), N(j[3]), N(d[3]),
                N((d[1]-j[1])/j[1]*100,pct=True), N((d[3]-j[3])/j[3]*100,pct=True)]
    R["Q08"] = [x for r in rows("Q08") for x in (T(re.escape(r[0].lower())), C(r[1]), N(r[2]), N(r[3]))]
    r = rows("Q09")[0]
    R["Q09"] = [T("hyderabad"), C(r[1]), N(r[3],pct=True), N(r[5],pct=True)]
    b_, d_ = rows("Q10")
    R["Q10"] = [N(b_[2]), N(d_[2]), N(b_[2]-d_[2], 0.005), T("bangalore")]
    R["Q11"] = [C(x[1]) for x in rows("Q11")] + [N(rows("Q11")[1][3],pct=True), N(rows("Q11")[1][4]),
                T(r"undefined|n/a|not defined|null|none|no rated|not available|cannot be computed|zero rated|0 rated|no ratings|—|no observations")]
    r = rows("Q12")[0]; R["Q12"] = [N(r[0]), N(r[1]), N(r[2],pct=True)]
    R["Q13"] = [x for r in rows("Q13") for x in (T(re.escape(r[0].lower())), C(r[1]), N(r[3],pct=True))]
    q14 = rows("Q14"); tot_units = sum(r[2] for r in q14)
    R["Q14"] = [x for r in q14 for x in (C(r[1]), C(r[2]), N(r[3],pct=True))] + [C(tot_units)]
    q15 = {r[0]: r for r in rows("Q15")}
    R["Q15"] = [N(q15["Multiple lines"][3], pct=True), N(q15["Multiple lines"][2]), N(q15["One line"][2]),
                T(r"no (item )?line|without|no item|zero|0 orders|\b0\b")]
    r = rows("Q16")[0]; R["Q16"] = [C(r[1]), N(r[2]), N(r[3]), T(r"not offset|do not offset|don't offset|no offset|never offset|nothing offset|do not cancel|no cancel|not net|all (are )?positive|same sign|same direction|only positive|one-directional|no negative|equal")]
    R["Q17"] = [T(r"\b0\b|zero|no (non-zero )?(difference|discrepanc|mismatch)|reconcile")]
    R["Q18"] = [x for r in rows("Q18") for x in (T(re.escape(r[0].lower())), C(r[1]), N(r[2]), N(r[3]))]
    R["Q19"] = [N(r[3]) for r in rows("Q19")] + [T("saturday")]
    r = rows("Q20")[0]
    R["Q20"] = [C(r[2]), C(r[3]), N(r[4]), N(r[5]), N(r[6]), N(r[7]), N(r[8], 0.05, True),
                N(r[9], 0.05, True), N(r[10], 0.05, True)]
    r = rows("Q21")[0]
    R["Q21"] = [N(r[1], 0.01, True), T(r"\b12\b|twelve"), T(r"not|cannot|can't|does not|doesn't|no\b|insufficient")]
    r = rows("Q22")[0]; R["Q22"] = [C(r[0]), N(r[1]), N(r[2])]
    R["Q23"] = [x for r in rows("Q23") for x in (T(re.escape(r[0].lower())), N(r[1]), N(r[2],pct=True))]
    h1, h2 = rows("Q24"); R["Q24"] = [C(h1[1]), C(h2[1])]
    r = rows("Q25")[0]
    R["Q25"] = [T("hyderabad"), N(r[2],pct=True), N(r[3]), N(r[5],pct=True), N(r[6]), T(r"not|cannot|can't|does not|insufficient")]
    return R

REQ = build()
SCALES = {"": 1, "k": 1e3, "thousand": 1e3, "lakh": 1e5, "lakhs": 1e5, "m": 1e6, "mn": 1e6, "million": 1e6,
          "crore": 1e7, "crores": 1e7, "cr": 1e7, "b": 1e9, "bn": 1e9, "billion": 1e9}
NUM = re.compile(r"(?<![\w.])([-−–]?)\s*(?:(?:INR|Rs\.?|₹)\s*)?(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)(?:\s*(thousand|lakhs?|million|mn|billion|bn|crores?|cr|k|m|b)(?![A-Za-z]))?", re.I)

def numbers(text):
    out = []
    for m in NUM.finditer(text):
        v = float(m.group(2).replace(",", ""))
        neg = m.group(1) in ("-", "−", "–") or bool(re.search(r"[-−–]\s*(INR|Rs\.?|₹)\s*$", text[max(0,m.start(2)-8):m.start(2)]))
        sc = SCALES.get((m.group(3) or "").lower(), 1)
        out.append((-v if neg else v, v, sc))
    return out

def check(qid, text):
    t = text.lower(); nums = numbers(text); miss = []
    for req in REQ[qid]:
        if req[0] == "t":
            if not re.search(req[1], t): miss.append(("text", req[1][:30]))
        else:
            _, val, tol, signed, pct = req
            ok = False
            for sv, av, sc in nums:
                cand = sv if signed else av
                if sc == 1:
                    ok |= abs(cand - (val if signed else abs(val))) <= tol
                    if pct: ok |= abs(cand * 100 - (val if signed else abs(val))) <= tol
            if not ok: miss.append(("num", round(val, 6)))
    return miss


def attempts(group):
    pattern, _, _ = GROUPS[group]
    for rep in (1, 2, 3):
        for path in sorted((RUN / pattern.format(rep) / "attempts").glob("*.json")):
            yield rep, json.loads(path.read_text())


def grade(attempt):
    if attempt["status"] != "completed" or attempt.get("outcome") != "answer":
        return 0, [("outcome", attempt.get("outcome") or attempt["status"])]
    if attempt["question_id"] in ("Q22", "Q23", "Q24") and attempt["arm"] != "F":
        return 0, [("policy", "rule supplied only in arm F")]
    miss = check(attempt["question_id"], attempt.get("final_answer") or "")
    return int(not miss), miss


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--write", action="store_true", help="overwrite the grade files")
    parser.add_argument("--refresh-gold", action="store_true",
                        help="re-run gold_25.local.sql and rewrite gold_25_results.json")
    args = parser.parse_args()
    if args.refresh_gold:
        refresh_gold()
        raise SystemExit("gold_25_results.json refreshed; re-run without --refresh-gold")
    for group, (_, grade_file, prefix) in GROUPS.items():
        stored = json.loads((RUN / grade_file).read_text())
        new = {key: {} for key in stored}
        for rep, attempt in attempts(group):
            key = f"{attempt['arm']}-{attempt['question_id']}"
            score, miss = grade(attempt)
            new[key][rep] = score
            if score != stored[key][f"{prefix}rep{rep}"]:
                print(f"{group} {key} rep{rep}: stored={stored[key][f'{prefix}rep{rep}']} "
                      f"autograde={score} {miss}")
        if args.write:
            out = {}
            for key, reps in new.items():
                scores = [reps[r] for r in (1, 2, 3)]
                entry = {f"{prefix}rep{r}": s for r, s in zip((1, 2, 3), scores)}
                if prefix:
                    entry[f"{prefix}mean"] = round(statistics.mean(scores), 6)
                    entry[f"{prefix}std"] = round(statistics.stdev(scores), 6)
                else:
                    entry["mean"] = round(statistics.mean(scores), 4)
                out[key] = entry
            (RUN / grade_file).write_text(json.dumps(out, indent=2) + "\n")
            print(f"wrote {grade_file}")


if __name__ == "__main__":
    main()
