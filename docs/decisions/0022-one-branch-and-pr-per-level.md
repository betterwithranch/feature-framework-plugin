# 0022. One branch and PR per level

Status: accepted, 2026-11-02

## Context

The user chose one branch and PR per level so the work can be tracked.

## Decision

Each level of the framework's own build is on its own branch, with its own pull request against `main`. Work on the next level starts when the user approves the level.
