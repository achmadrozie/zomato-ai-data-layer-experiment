# Experiment results

The committed `run.local` JSON files contain each question attempt and its manual grade. The directory name predates this decision to retain results. Runtime logs, macOS files, and the local gold SQL remain ignored.

The main comparison contains **900 attempts**: 25 questions × 6 arms × 3 repetitions × 2 models. The `af_25_v2_rep{1,2,3}` runs are the three `gpt-4.1` repetitions; `af_25_luna_rep{1,2,3}` are the three `gpt-6-luna` repetitions. The earlier `af_25` run contains 150 preliminary `gpt-4.1` attempts and is retained for the original audit, but is excluded from the main comparison.

Run `python3 scripts/summarize_experiments.py` from the repository root for the mean and sample standard deviation of correctness (0 or 1), end-to-end latency in seconds, and completion tokens per attempt. It reports only the 900 main attempts. Averages are across attempts, so questions with several repetitions contribute once per repetition.

To estimate model cost, pass `--input-price` and `--output-price`, each in USD per million tokens. The estimate sums prompt and completion tokens from all recorded model steps. It excludes Snowflake charges, taxes, discounts, cached-token rates, and any other pricing category absent from the attempt records. Supply the rates that applied to the model and period being analyzed; the script does not assume historical prices.
