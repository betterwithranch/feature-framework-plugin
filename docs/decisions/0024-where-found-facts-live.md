# 0024. Where found facts live

Status: accepted, 2026-11-03

## Context

The user said facts "don't belong in all levels" and, where recorded, "need to be reviewed by an independent agent ... and would then be reviewed by the user"; he agreed the levels as proposed.

## Decision

A fact the work found in the project appears only in a level that allows it. Outcome: none; a project fact there means design leaked up. Behaviour: only facts about what users get today, where the new behaviour keeps or changes it, nothing about code. Design: the main home, facts about the code, data, services and interfaces the design builds on. Slices: Design's facts carried over, plus facts about how the project is built and tested, no new design facts. Build: no document; the code and tests are the record. In every level that allows them, a fact is marked as the work's, checked against the project by that level's review before the user is asked to approve, and seen by the user at approval. A wrong fact is a finding.
