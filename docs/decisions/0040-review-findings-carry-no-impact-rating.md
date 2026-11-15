# 0040. Review findings carry no impact rating

Status: accepted, 2026-11-06

## Context

The user chose FF-51 and said "the model should be capable of judging that a 1 in 5 users will encounter this as consequential and a 1 in 10,000 users will encounter this as inconsequential".

## Decision

Findings carry no impact rating. Every review uses one drop rule: leave out a finding that few users would ever meet or that changes nothing for them, judged, not scored. The high/medium impact line was added without approval and is removed.
