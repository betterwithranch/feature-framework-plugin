# 0004. Cover feature development only

Status: accepted, 2026-10-27

## Context

Spikes, performance work, data migrations and infrastructure changes have different goals and checks from feature work.

## Decision

The framework is for feature development. Exploratory work, performance optimisation, data migrations, infrastructure and tooling changes made for other reasons are non-goals. Work a feature needs, such as a migration for its own data, is part of the feature. A question only an experiment can answer is handed off, and only its answer comes back.

## Consequences

Other kinds of change need their own process.
