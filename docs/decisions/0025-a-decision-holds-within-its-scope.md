# 0025. A decision holds within its scope

Status: accepted, 2026-11-03

## Context

The user said the next feature "should use the previous decision as guidance for a preference, but it shouldn't apply it to other cases that aren't part of the original decision's scope."

## Decision

A decision applies only within its stated scope: "all files use streaming" covers a second file; "file 1 uses streaming" doesn't. The work's decision in one feature is guidance, a preferred default, for the same decision in a later feature, which is made again and recorded again, citing the earlier one. An agreement or codified rule whose scope already covers the later case leaves nothing to decide.
