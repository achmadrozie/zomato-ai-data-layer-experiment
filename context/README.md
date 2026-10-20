# Context layer

The candidate [`business context`](v1/business_glossary.md) is a short set of reporting policies and interpretation notes. It omits the metric catalogue already available through semantic discovery.

Only that Markdown file is supplied to arm E. Its [`manifest`](v1/manifest.yml) records the version, payload hash/size, and reviewed code revision. This README, design/review reports, questions, and gold answers are outside the payload.

CTX-01–03 are proposed experiment policies using existing data fields. They need user review before benchmark use; they are not assertions about Zomato's real policies. The unavailable Bolt partner-market flag is an example, not an implemented filter.

The [`experiment design`](../docs/experiment_design.md) separates policy-required questions from data-answerable questions and allows justified clarification in arms lacking a policy. Context remains candidate until the policies and design are reviewed. Updating a candidate requires a new payload hash; changing a frozen payload requires a new version.
