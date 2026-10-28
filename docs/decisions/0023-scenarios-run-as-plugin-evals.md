# Scenarios run as plugin evals

- The framework's own scenarios are checked with `claude plugin eval`, as Anthropic documents it.
- Each scenario becomes eval cases graded at the turns that matter, replaying a recorded conversation up to that turn. There is no simulated user across a whole build.
- A case's fixture project is built by its scaffold script. No separate sample repository exists; product features run their scenarios on the product itself.
- The tool's defaults apply: 3 runs per case and a threshold of 1.0. The suite runs on demand with a cost ceiling, not in CI.
