# 0077. Each review finding goes to the user for approval

Status: replaced by 0078, 2026-11-11

## Context

Review findings on the Outcome were being fixed when a decision record, a goal or an earlier answer seemed to settle them ([decision 0029](0029-four-review-rounds-per-approved-version.md), `docs/goals.md` "Decide or ask"). Asked how review findings should be handled (FF-77), the user chose B: "do one review at a time. provide the feedback on what failed, how the failure aligns with the existing decisions on the record, and what the change is. Ask for the clarification about the decisions if they are unclear or missing to make the change. Otherwise, just state for approval."

## Decision

- The reviews run one at a time.
- For each failure, the agent reports what failed, how the failure aligns with the decisions on record, and the change it proposes.
- Where those decisions are unclear or missing, the agent asks the user to clarify them. Otherwise it states the change for approval.
- No change to the Outcome or its review rules is made without the user's approval, including a fix that applies an existing decision.

## Consequences

- For review findings at the Outcome level, it replaces `docs/goals.md` "Decide or ask" and the part of [decision 0029](0029-four-review-rounds-per-approved-version.md) that lets a fix applying something agreed go without approval ([decision 0061](0061-a-later-decision-replaces-an-earlier-one-it-disagrees-with.md)).
