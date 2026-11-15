# 0027. Complete requirements and verification

Status: accepted, 2026-11-03

## Context

The user chose this standard for a complete requirement, and said "we shouldn't reference design at all in outcome level 1. We should reference requirements and verification."

## Decision

A requirement is complete when its verification can be written in full and run, with nothing left to ask the user. A verification is complete when it names what is checked, how, and what result passes. Anything missing from either is asked, one question at a time, unless the work can find it out. A level's document speaks of requirements, how they're verified, and "a level"; the Outcome names no lower level, nothing a lower level holds, and no found facts per level.
