# A planning marker guards code

- While the `feature` skill plans a feature, it keeps a marker naming the feature in the git directory of the current worktree, which is never committed. The marker is removed when Slices passes.
- While the marker exists, the agent's edits to the project's code and tests are refused. Nothing else is blocked: commits, other branches and other worktrees are unaffected.
- Planning on one branch and building on another is supported.
