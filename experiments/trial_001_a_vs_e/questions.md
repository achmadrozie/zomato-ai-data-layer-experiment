# Trial 001 questions

Ask each question once in arm A and once in arm E, with the same model and settings. The 2025 period means `order_date >= 2025-01-01` and `< 2026-01-01`, using the recorded order-date field. INR is specified only in the monetary questions. These are the exact prompts from `questions.json`; do not add metric formulas to the evaluated agent's prompt.

| ID | Question | Requested unit |
| --- | --- | --- |
| Q1 | How many orders were placed during 2025? Use the recorded order date and report a count. | orders |
| Q2 | What was GMV in INR during 2025, by recorded order date? | INR |
| Q3 | What was AOV in INR during 2025, by recorded order date? | INR per delivered order |
| Q4 | What was the cancellation rate, as a percentage, during 2025, by recorded order date? | percent |
| Q5 | What was ordered quantity per order during 2025, by recorded order date? Report units per order. | units per order |

The local author-only reference is `reference.local.md`, supported by `gold.local.sql`. Both are Git-ignored and must remain outside evaluated agents' access.
