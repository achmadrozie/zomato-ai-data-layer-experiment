# Context layer

The context treatment is a versioned business glossary. It records definitions, units, grains, and known limits without changing the agent's task instructions or adding query tools.

The candidate payload is [`v1/business_glossary.md`](v1/business_glossary.md). [`v1/manifest.yml`](v1/manifest.yml) identifies its exact bytes and the repository revision reviewed when it was authored. Only the payload file is supplied to experiment arm E. This README, the manifest, review reports, experiment design, benchmark questions, gold SQL, and expected results are not payload files.

The glossary is derived from the implemented core, metric, and mart definitions. It contains no question-specific answers or SQL examples. Arm D already discovers metric definitions through the semantic interface; D versus E therefore measures the additional effect of a consolidated glossary, including information that may overlap semantic discovery.

Status is candidate until the experiment design and prerequisite data-model decisions have been reviewed. A frozen run records a context version and SHA-256. Editing a candidate requires updating the manifest hash. After freezing a version, a content change creates a new version rather than modifying the old payload.

Design and pending decisions are in [`docs/experiment_design.md`](../docs/experiment_design.md). Gold-answer authoring follows that review.
