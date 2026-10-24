# Experiment results

The committed `run.local` JSON files contain each question attempt and its manual grade. The directory name predates this decision to retain results. Runtime logs, macOS files, and the local gold SQL remain ignored.

Run `python3 scripts/summarize_experiments.py` from the repository root for the mean and sample standard deviation of correctness (0 or 1), end-to-end latency in seconds, and completion tokens per attempt. The baseline has one repetition (150 attempts); v2 and Luna have three (450 attempts each). Averages are across attempts, so questions with several repetitions contribute once per repetition.

To estimate model cost, pass `--input-price` and `--output-price`, each in USD per million tokens. The estimate sums prompt and completion tokens from all recorded model steps. It excludes Snowflake charges, taxes, discounts, cached-token rates, and any other pricing category absent from the attempt records. Supply the rates that applied to the model and period being analyzed; the script does not assume historical prices.
