# 0051. Settings hold no prompts; prompts and docs are separate

Status: accepted, 2026-11-04

## Context

Documentation and agent prompts have different audiences.

## Decision

Settings files hold no prompts. Each prompt is its own file that settings references. Agent prompts and human docs are separate files, each written for its reader: a prompt gives an agent direct instructions; a doc explains to a person. Duplication between them is kept to a minimum, and no hook points at a human doc.
