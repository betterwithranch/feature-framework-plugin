# Goals

The goals every change to this repo serves.

1. Autonomy. A feature goes from agreed intent to working code without the user being pulled back into details.
2. Level discipline. Work stays at the current level, and moves down a level only when the current one passes its review and the user approves it. Questions for a lower level wait for that level.
3. Production-ready features, not prototypes. Invariants and design decisions are settled before the build or marked as non-goals.
4. MVP first. The framework is the smallest one that carries its own build, applied to a product feature after that. No level is refined beyond what the next level needs.
5. Fix instructions, not cases. When a gate gives wrong or unstable results, the skill is changed so it converges, rather than judging case by case.

How the agent decides or asks is in its prompt, [`hooks/prompts/goals.md`](../hooks/prompts/goals.md), and who decides what is in `skills/references/decisions.md`.
