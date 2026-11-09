# 0012. Run each gate review three times and act on the union

Status: accepted, 2026-10-28

## Context

A single review run missed findings that another run of the same prompt caught.

## Decision

Each gate review runs three times independently. Every finding from any run is acted on. A finding that only some runs raise shows where the review instructions need to be clearer.

## Consequences

A review passes when all three runs report no findings.
