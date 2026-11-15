# 0038. Only an absolute term rules out exceptions

Status: accepted, 2026-11-06

## Context

Asked whether a rule stated generally also holds in every case (FF-48), the user chose B, keeping [decision 0033](0033-absolute-terms-have-no-exceptions.md): "if a rule is meant to not have exceptions, it should use absolute terms and no exceptions. there should be no "convention-based" approach like general rules do X. That is an extra rule to follow with no extra value."

## Decision

Clarifies [decision 0033](0033-absolute-terms-have-no-exceptions.md). Only an absolute term rules out exceptions. A requirement without one is not contradicted by an exception elsewhere. A requirement meant to have no exceptions uses an absolute term. A review finding that calls a requirement without an absolute term contradicted by an exception is dropped.
