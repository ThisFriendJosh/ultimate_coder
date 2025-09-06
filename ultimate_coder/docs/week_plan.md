# Weekly Plan Template
## Sections
- Objectives
- Key readings
- Build tasks
- Tests & acceptance
- Hardening (perf, security, docs)
- Milestones
- Deliverables
- Risk assessment
- Demo & retro
- Retrospective notes

## Example: Algorithms sprint
Aligned module: **CS Fundamentals – Algorithms** (see `ultimate_coder.yaml`).
- Objectives: Build the "Schedule optimizer" using sorting and dynamic programming.
- Key readings: CLRS chapters on sorting and dynamic programming; internal notes on scheduling.
- Build tasks: Implement baseline sorter; extend to dynamic programming scheduler; expose CLI.
- Tests & acceptance: Unit tests verify optimal schedules for sample inputs.
- Hardening (perf, security, docs): Profile for \(O(n \log n)\) sorting, validate inputs, document algorithm.
- Milestones: Baseline sorter by mid-week; dynamic program with docs by week end.
- Deliverables: CLI schedule optimizer with tests and short README.
- Risk assessment: Incorrect DP transitions or slow sorter; mitigate with complexity review and peer feedback.
- Demo & retro: Show scheduler on real data; reflect on algorithm choices.
- Retrospective notes: Capture insights on optimization and future refactors.

## Example: DevOps sprint
Aligned module: **DevOps – Git→CI/CD** (see `ultimate_coder.yaml`).
- Objectives: Wire up repository with basic CI pipeline to automate build and tests.
- Key readings: Docs on Git hooks and CI platforms (e.g., GitHub Actions).
- Build tasks: Add workflow file, lint step, and test runner; integrate badge in README.
- Tests & acceptance: Pipeline runs on pushes and reports success.
- Hardening (perf, security, docs): Enable caching, run static analysis, note pipeline behavior.
- Milestones: Workflow skeleton by mid-week; green pipeline with badge by week end.
- Deliverables: `ci.yml` workflow, status badge, and contributing note.
- Risk assessment: Misconfigured jobs or missing dependencies; mitigate with local dry runs and minimal steps.
- Demo & retro: Review latest run in UI; discuss CI/CD gains.
- Retrospective notes: Log setup challenges and next automation targets.
=======
 
+## Sections
 - Objectives
 - Key readings
 - Build tasks
 - Tests & acceptance
 - Hardening (perf, security, docs)
+- Milestones
+- Deliverables
+- Risk assessment
 - Demo & retro
+- Retrospective notes
+
+## Example: Algorithms sprint
+Aligned module: **CS Fundamentals – Algorithms** (see `ultimate_coder.yaml`).
+- Objectives: Build the "Schedule optimizer" using sorting and dynamic programming.
+- Key readings: CLRS chapters on sorting and dynamic programming; internal notes on scheduling.
+- Build tasks: Implement baseline sorter; extend to dynamic programming scheduler; expose CLI.
+- Tests & acceptance: Unit tests verify optimal schedules for sample inputs.
+- Hardening (perf, security, docs): Profile for \(O(n \log n)\) sorting, validate inputs, document algorithm.
+- Milestones: Baseline sorter by mid-week; dynamic program with docs by week end.
+- Deliverables: CLI schedule optimizer with tests and short README.
+- Risk assessment: Incorrect DP transitions or slow sorter; mitigate with complexity review and peer feedback.
+- Demo & retro: Show scheduler on real data; reflect on algorithm choices.
+- Retrospective notes: Capture insights on optimization and future refactors.
+
+## Example: DevOps sprint
+Aligned module: **DevOps – Git→CI/CD** (see `ultimate_coder.yaml`).
+- Objectives: Wire up repository with basic CI pipeline to automate build and tests.
+- Key readings: Docs on Git hooks and CI platforms (e.g., GitHub Actions).
+- Build tasks: Add workflow file, lint step, and test runner; integrate badge in README.
+- Tests & acceptance: Pipeline runs on pushes and reports success.
+- Hardening (perf, security, docs): Enable caching, run static analysis, note pipeline behavior.
+- Milestones: Workflow skeleton by mid-week; green pipeline with badge by week end.
+- Deliverables: `ci.yml` workflow, status badge, and contributing note.
+- Risk assessment: Misconfigured jobs or missing dependencies; mitigate with local dry runs and minimal steps.
+- Demo & retro: Review latest run in UI; discuss CI/CD gains.
+- Retrospective notes: Log setup challenges and next automation targets.
 
EOF
)
