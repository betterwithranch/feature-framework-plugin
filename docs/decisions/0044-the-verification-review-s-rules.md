# 0044. The Verification review's rules

Status: accepted, 2026-11-06

## Context

The user approved these rules as worded (FF-55).

## Decision

1. Together, the scenarios and measures citing a requirement describe a check of every part of it. 2. The scenario or measure describes a check of the result the requirement states. 3. What it describes as passing includes every way the requirement allows the user to get that result. 4. The starting state describes everything the scenario depends on; nothing is left for the work being verified to produce first. 5. What it describes as passing is what the user sees, not the system's own record that it succeeded. 6. It states the expected result. 7. What it describes as passing depends on no other scenario or measure. Each is judged by the description's own words, not by imagined runs. Replaces criteria 4 and 5.
