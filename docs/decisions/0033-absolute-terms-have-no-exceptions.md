# 0033. Absolute terms have no exceptions

Status: accepted, 2026-11-04

## Context

The user said "a description that says "every" or "never" shouldn't have exceptions. those terms are absolute. if there are exceptions, different non-absolute terms should be used".

## Decision

An absolute term (every, never, only, always, all, none) means no exceptions. A requirement with exceptions is written in non-absolute terms. An absolute requirement that another requirement makes an exception to is a contradiction.
