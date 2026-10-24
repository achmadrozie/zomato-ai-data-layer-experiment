"""Summarize committed experiment attempts and manually assigned grades."""

import argparse
import json
import statistics
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "experiments" / "run.local"
GROUPS = {
    "baseline": (["af_25"], "af_25/grades.local.json"),
    "v2": ([f"af_25_v2_rep{i}" for i in range(1, 4)], "af_25_v2_grades.json"),
    "luna": ([f"af_25_luna_rep{i}" for i in range(1, 4)], "af_25_luna_grades.json"),
}


def score(grades, group, key, rep):
    entry = grades[key]
    if group == "baseline":
        return entry[0]
    if group == "luna":
        return entry[f"luna_rep{rep}"]
    return entry[f"rep{rep}"]


def mean_std(values):
    return statistics.mean(values), statistics.stdev(values) if len(values) > 1 else 0.0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-price", type=float, help="USD per 1M prompt tokens")
    parser.add_argument("--output-price", type=float, help="USD per 1M completion tokens")
    args = parser.parse_args()
    if (args.input_price is None) != (args.output_price is None):
        parser.error("provide both token prices or neither")

    for group, (runs, grade_path) in GROUPS.items():
        grades = json.loads((ROOT / grade_path).read_text())
        records = []
        for rep, run in enumerate(runs, 1):
            for path in sorted((ROOT / run / "attempts").glob("*.json")):
                attempt = json.loads(path.read_text())
                key = f"{attempt['arm']}-{attempt['question_id']}"
                stats = [step.get("model_stats") or {} for step in attempt["steps"]]
                records.append({
                    "score": score(grades, group, key, rep),
                    "seconds": attempt["total_seconds"],
                    "prompt": sum(s.get("prompt_tokens") or 0 for s in stats),
                    "completion": sum(s.get("completion_tokens") or 0 for s in stats),
                })
        if not records:
            raise ValueError(f"no attempts found for {group}")
        print(f"{group}: {len(records)} attempts")
        for label, field in (("correctness", "score"), ("latency_seconds", "seconds"),
                             ("completion_tokens", "completion")):
            avg, std = mean_std([record[field] for record in records])
            print(f"  {label}: mean={avg:.4f}, sample_std={std:.4f}")
        if args.input_price is not None:
            costs = [(r["prompt"] * args.input_price + r["completion"] * args.output_price)
                     / 1_000_000 for r in records]
            avg, std = mean_std(costs)
            print(f"  estimated_model_cost_usd: total={sum(costs):.4f}, "
                  f"mean={avg:.6f}, sample_std={std:.6f}")


if __name__ == "__main__":
    main()
