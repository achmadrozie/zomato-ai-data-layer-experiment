# Experiment results

The committed `run.local` JSON files contain each question attempt and its score. The directory name predates this decision to retain results. Runtime logs, macOS files, and the local gold SQL remain ignored.

The comparison contains **900 attempts**: 25 questions × 6 arms × 3 repetitions × 2 models. The `af_25_v2_rep{1,2,3}` runs are the three `gpt-4.1` repetitions; `af_25_luna_rep{1,2,3}` are the three `gpt-6-luna` repetitions.

## Files

| File | Role |
| --- | --- |
| `questions_25.json` | The frozen questions. `stratum` is evaluator metadata. |
| `answers_25.md` | Author reference answers and scoring rules. Evaluator-only. |
| `gold_25.local.sql` | Executable gold SQL (ignored by git). |
| `gold_25_results.json` | Output of the gold SQL run on 25 October 2026; identical to `answers_25.md`. Input of the grader. |
| `run.local/af_*_rep*/attempts/` | Every action, tool result, final answer, usage, and timing per attempt. |
| `run.local/af_25_v2_grades.json`, `run.local/af_25_luna_grades.json` | Official score (0 or 1) per arm × question × repetition. |

## Scoring

Official scores come from `python3 scripts/autograde.py`. It checks each final answer against `gold_25_results.json` with the tolerances in `answers_25.md`, applies the same rules to every attempt, and ignores the arm and model. A clarification or failed attempt scores 0, and Q22–Q24 score 0 in arms A–E. Run it without `--write` to confirm that the stored grades still match; add `--refresh-gold` (needs Snowflake credentials) to regenerate `gold_25_results.json` from `gold_25.local.sql`.

Per-arm scores are in [`RESULTS.md`](RESULTS.md). Tolerances are applied literally: for example, on Q12 (top-ten GMV of about 3.55 million) a 4 INR difference scores 0 against the INR 0.01 tolerance. Accepting it would raise the `gpt-4.1` total by 2.7 points.

Limits of the grader: it checks that every required value is present and correct and that required statements appear, but cannot detect a correct number used for the wrong population. The author wrote the questions, the reference answers, and the grader's requirements, so scoring is not independent of the author. The question text does not define GMV; the reference uses `SALES_AMOUNT`, and one `gpt-6-luna` attempt (A-Q02 r2) chose `SUBTOTAL` and scored 0.

## Summary

Run `python3 scripts/summarize_experiments.py` from the repository root for the mean and sample standard deviation of correctness (0 or 1), end-to-end latency in seconds, and completion tokens per attempt. Averages are across attempts, so questions with several repetitions contribute once per repetition.

To estimate model cost, pass `--input-price` and `--output-price`, each in USD per million tokens. The estimate sums prompt and completion tokens from all recorded model steps. It excludes Snowflake charges, taxes, discounts, cached-token rates, and any other pricing category absent from the attempt records. Supply the rates that applied to the model and period being analyzed; the script does not assume historical prices.

### Cost command used in the article

```
python3 scripts/summarize_experiments.py --input-price 2 --output-price 8      # gpt-4.1 (af_25_v2_*)
python3 scripts/summarize_experiments.py --input-price 0.10 --output-price 0.50 # gpt-6-luna (af_25_luna_*)
```

Prices are USD per million tokens as quoted by the author for October 2026; they are not recorded in the attempt files, so confirm them against the provider's price list before reusing the cost figures.

Standard deviations everywhere (reports, `luna_std` in the grades file, summary script) are **sample** SDs (n−1) over the three repetitions.

Identifiers (Snowflake account host, local paths, AWS account ID) were replaced with placeholders in the current files; earlier commits still contain them.
