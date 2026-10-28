# A planning marker guards code

- While the `feature` skill plans a feature, it keeps a marker naming the feature in the git directory of the current worktree, which is never committed. The marker is removed when Slices passes.
- While the marker exists, changes to the project's code and tests are stopped as early as possible: refused before a tool runs where that can be known, and caught right after any tool call that made one, however it was made.
- Nothing else is blocked: commits, other branches and other worktrees are unaffected. Planning on one branch and building on another is supported.
