# Level 1 Outcome: every review finding, 2026-11-02 to 2026-11-06

Built from the 87 review-run transcripts in this session (subagent logs) and git history. Findings and dropped items were extracted per run by four extraction agents into JSON, checked against each report's own totals; the clustering, the cause and the call on each finding are mine and marked so. No fixes are proposed.

Calls (mine): **gap** = a real gap in the document; **misread** = the reviewer misread text the document settles; **open** = a rule the criteria left open, so runs could go either way.

## Totals

- Runs: 87. Reports: 79. Stopped before reporting (killed by me when the text changed or the process changed): 8 (runs 22, 23, 24, 58, 59, 60, 69, 73).
- Clean runs (all six criteria pass): 19 (runs 7, 8, 9, 10, 12, 13, 14, 15, 28, 32, 36, 52, 54, 63, 65, 76, 79, 80, 81).
- Findings: 130. Dropped items listed by the reports: 1027.
- Distinct issues (clusters, mine): 70.

### Per gate

| Gate | Runs | Reports | Clean | Findings | Dropped |
|---|---|---|---|---|---|
| Gate A, runs 1–24 (2026-11-02/03): first Outcome, then the interview write-in | 24 | 21 | 8 | 43 | 251 |
| Gate B, runs 25–51 (2026-11-03/04): after Craig's level 1 decisions were written in | 27 | 27 | 3 | 54 | 379 |
| Gate C, runs 52–81 (2026-11-04/05): D48–D54 era, single review then round | 30 | 25 | 8 | 23 | 318 |
| Gate D, runs 82–87 (2026-11-06): the D56 rewrite (R1–R40, glossary) | 6 | 6 | 0 | 10 | 79 |

### Per criterion (findings)

| Criterion | Findings | of which high |
|---|---|---|
| 1 | 3 | 0 |
| 2 | 4 | 0 |
| 3 | 2 | 2 |
| 4 | 37 | 33 |
| 5 | 66 | 0 |
| 6 | 18 | 17 |

### Per call (mine)

| Call | Findings | Clusters |
|---|---|---|
| real gap in the document | 107 | 59 |
| reviewer misread text the document settles | 1 | 1 |
| a rule the criteria left open | 22 | 10 |

### Caused by an earlier fix of mine

27 of 130 findings were caused by an earlier fix of mine (my call; per finding, from the cluster's cause): by gate A: 6, B: 1, C: 15, D: 5. Runs: 16 F1, 16 F7, 17 F1, 17 F7, 18 F1, 18 F6, 40 F5, 53 F1, 55 F1, 56 F2, 57 F1, 61 F1, 61 F2, 62 F1, 62 F2, 67 F1, 67 F2, 68 F1, 70 F1, 72 F1, 77 F1, 78 F1, 83 F1, 84 F1, 84 F2, 86 F1, 87 F3.

### Raised in one run, dropped in another

12 clusters were raised as findings in some runs and dropped in others: T4, T17, T25, T26, T30, T31, T56, T63, T65, T66, T68, T69. Counts of dropping runs are keyword matches over the dropped items (approximate; see the last section).

## Review inputs

Every run got one of six prompt texts, plus skills/review-outcome/SKILL.md and skills/references/outcome.md as they stood at its commit. All runs in one round got the same prompt and the same files; the document differed only between rounds. Prompts are below with commit hashes shown as `commit X`; the instruction file text for each blob is in the appendix.

### Prompt a770bc: runs 1–48 (48 runs)

```
You are an independent reviewer at the Outcome gate. Read exactly these three files in /home/user/feature-framework-plugin and nothing else: skills/review-outcome/SKILL.md (your instructions), skills/references/outcome.md (the definition), docs/spec/1-outcome.md (the document under review). Do not read git history, other docs, other skills or decision records, and do not judge the document against any discussion. Follow the skill's Method, Findings and Output sections exactly and return the full output (trace map, criteria 1-6 PASS/FINDINGS, findings with id, criterion, quoted evidence, what it changes, impact; dropped items with reasons).
```

### Prompt bf572b: runs 49–54 (6 runs)

```
You are an independent reviewer at the Outcome gate. Read exactly these three files in /home/user/feature-framework-plugin and nothing else: skills/review-outcome/SKILL.md (your instructions), skills/references/outcome.md (the definition), docs/spec/1-outcome.md (the document under review). Do not read git history, other docs, other skills or decision records, and do not judge the document against any discussion. Follow the skill's Method, Findings and Output sections exactly and return the full output (trace map, criteria 1-6 PASS/FINDINGS, findings with id, criterion, quoted evidence, what it changes, impact; dropped items with reasons). For each finding also name the exact line of the definition or skill it relies on.
```

### Prompt a17e9e: runs 55–72 (17 runs)

```
You are an independent reviewer. In /home/user/feature-framework-plugin (commit X), follow skills/review-outcome/SKILL.md exactly, reviewing docs/spec/1-outcome.md against skills/references/outcome.md (the review skill links to it; also read skills/references/decisions.md if the document's definitions point there). Read only those files; don't read docs/decisions.md, git history or any other file. Do not edit anything. Produce the skill's Output section. For each finding, also give the line number(s) of the instruction (in outcome.md or the review skill) that the finding relies on.
```

### Prompt 1e6c31: runs 61–61 (1 runs)

```
You are an independent reviewer. In /home/user/feature-framework-plugin, follow skills/review-outcome/SKILL.md exactly, reviewing docs/spec/1-outcome.md as it is on disk now (the working tree, including uncommitted changes) against skills/references/outcome.md (the review skill links to it; also read skills/references/decisions.md if the document's definitions point there). Read only those files; don't read docs/decisions.md, git history or any other file. Do not edit anything. Produce the skill's Output section. For each finding, also give the line number(s) of the instruction (in outcome.md or the review skill) that the finding relies on.
```

### Prompt 9f7acd: runs 73–81 (9 runs)

```
You are an independent reviewer. In /home/user/feature-framework-plugin (commit X), follow skills/review-outcome/SKILL.md exactly (ignore its Rounds section; you are one run), reviewing docs/spec/1-outcome.md against skills/references/outcome.md (the review skill links to it; also read skills/references/decisions.md if the document's definitions point there). Read only those files; don't read docs/decisions.md, git history or any other file. Do not edit anything. Produce the skill's Output section. For each finding, also give the line number(s) of the instruction (in outcome.md or the review skill) that the finding relies on.
```

### Prompt 9f9588: runs 82–87 (6 runs)

```
You are an independent reviewer. In /home/user/feature-framework-plugin (commit X), follow skills/review-outcome/SKILL.md exactly (ignore its Rounds section; you are one run), reviewing docs/spec/1-outcome.md against skills/references/outcome.md (the review skill links to it; also read skills/references/decisions.md if the document points there). Read only those files; don't read docs/decisions.md, git history or any other file. Do not edit anything. Produce the skill's Output section. For each finding, also give the line number(s) of the instruction (in outcome.md or the review skill) that the finding relies on.
```

## Runs

| Run | Time (UTC) | Commit | Gate | Prompt | SKILL.md | outcome.md | Criteria | Findings | Dropped |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-11-02 23:26 | 4605655 | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4F 5F 6F | 4 | 14 |
| 2 | 2026-11-02 23:26 | 4605655 | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4F 5F 6F | 5 | 12 |
| 3 | 2026-11-02 23:26 | 4605655 | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4F 5P 6F | 2 | 12 |
| 4 | 2026-11-02 23:33 | e4a4d92 | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4F 5P 6P | 1 | 13 |
| 5 | 2026-11-02 23:33 | e4a4d92 | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5F 6P | 1 | 13 |
| 6 | 2026-11-02 23:33 | e4a4d92 | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4F 5F 6P | 2 | 11 |
| 7 | 2026-11-02 23:39 | a36bf1f | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5P 6P | 0 | 18 |
| 8 | 2026-11-02 23:39 | a36bf1f | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5P 6P | 0 | 10 |
| 9 | 2026-11-02 23:39 | a36bf1f | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5P 6P | 0 | 10 |
| 10 | 2026-11-02 23:47 | 847802b | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5P 6P | 0 | 14 |
| 11 | 2026-11-02 23:47 | 847802b | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4F 5P 6P | 1 | 13 |
| 12 | 2026-11-02 23:47 | 847802b | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5P 6P | 0 | 10 |
| 13 | 2026-11-02 23:53 | 9c62834 | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5P 6P | 0 | 13 |
| 14 | 2026-11-02 23:53 | 9c62834 | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5P 6P | 0 | 10 |
| 15 | 2026-11-02 23:53 | 9c62834 | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5P 6P | 0 | 12 |
| 16 | 2026-11-03 20:29 | dd487b5 | A | a770bc | 7cab4de | 42a5119 | 1F 2P 3P 4F 5F 6F | 7 | 9 |
| 17 | 2026-11-03 20:29 | dd487b5 | A | a770bc | 7cab4de | 42a5119 | 1F 2P 3P 4F 5F 6F | 7 | 10 |
| 18 | 2026-11-03 20:29 | dd487b5 | A | a770bc | 7cab4de | 42a5119 | 1F 2P 3P 4F 5F 6F | 6 | 10 |
| 19 | 2026-11-03 20:35 | b563f13 | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4F 5P 6P | 2 | 13 |
| 20 | 2026-11-03 20:35 | b563f13 | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5F 6P | 3 | 13 |
| 21 | 2026-11-03 20:35 | b563f13 | A | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4F 5F 6P | 2 | 11 |
| 22 | 2026-11-03 20:42 | 2cb2dcb | A | a770bc | 7cab4de | 42a5119 | no report | 0 | 0 |
| 23 | 2026-11-03 20:42 | 2cb2dcb | A | a770bc | 7cab4de | 42a5119 | no report | 0 | 0 |
| 24 | 2026-11-03 20:42 | 2cb2dcb | A | a770bc | 7cab4de | 42a5119 | no report | 0 | 0 |
| 25 | 2026-11-03 22:49 | 39a0f70 | B | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4F 5F 6P | 3 | 13 |
| 26 | 2026-11-03 22:49 | 39a0f70 | B | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4F 5F 6P | 3 | 13 |
| 27 | 2026-11-03 22:49 | 39a0f70 | B | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4F 5F 6P | 5 | 15 |
| 28 | 2026-11-03 22:58 | 877b935 | B | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5P 6P | 0 | 13 |
| 29 | 2026-11-03 22:58 | 877b935 | B | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5P 6F | 1 | 14 |
| 30 | 2026-11-03 22:58 | 877b935 | B | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5F 6P | 2 | 14 |
| 31 | 2026-11-03 23:07 | dd7b7d0 | B | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5F 6P | 1 | 17 |
| 32 | 2026-11-03 23:07 | dd7b7d0 | B | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5P 6P | 0 | 21 |
| 33 | 2026-11-03 23:07 | dd7b7d0 | B | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5F 6P | 1 | 18 |
| 34 | 2026-11-04 16:28 | ec102df | B | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4F 5P 6P | 1 | 21 |
| 35 | 2026-11-04 16:28 | ec102df | B | a770bc | 7cab4de | 42a5119 | 1P 2F 3P 4P 5P 6P | 1 | 13 |
| 36 | 2026-11-04 16:28 | ec102df | B | a770bc | 7cab4de | 42a5119 | 1P 2P 3P 4P 5P 6P | 0 | 17 |
| 37 | 2026-11-04 17:41 | 3e512e3 | B | a770bc | 7cab4de | 16aa743 | 1P 2P 3P 4P 5F 6P | 1 | 13 |
| 38 | 2026-11-04 17:41 | 3e512e3 | B | a770bc | 7cab4de | 16aa743 | 1P 2F 3P 4P 5F 6P | 2 | 13 |
| 39 | 2026-11-04 17:41 | 3e512e3 | B | a770bc | 7cab4de | 16aa743 | 1P 2P 3P 4P 5F 6P | 1 | 12 |
| 40 | 2026-11-04 18:24 | bd73aa3 | B | a770bc | 7cab4de | 16aa743 | 1P 2P 3P 4P 5F 6P | 5 | 10 |
| 41 | 2026-11-04 18:24 | bd73aa3 | B | a770bc | 7cab4de | 16aa743 | 1P 2P 3P 4P 5F 6P | 1 | 10 |
| 42 | 2026-11-04 18:24 | bd73aa3 | B | a770bc | 7cab4de | 16aa743 | 1P 2P 3P 4P 5F 6P | 2 | 12 |
| 43 | 2026-11-04 18:32 | 89876c0 | B | a770bc | 7cab4de | 16aa743 | 1P 2P 3P 4F 5P 6P | 1 | 18 |
| 44 | 2026-11-04 18:32 | 89876c0 | B | a770bc | 7cab4de | 16aa743 | 1P 2F 3P 4P 5F 6F | 3 | 11 |
| 45 | 2026-11-04 18:32 | 89876c0 | B | a770bc | 7cab4de | 16aa743 | 1P 2P 3P 4F 5P 6P | 1 | 12 |
| 46 | 2026-11-04 20:59 | 9b2f71a | B | a770bc | 7cab4de | 16aa743 | 1P 2F 3P 4F 5F 6P | 3 | 17 |
| 47 | 2026-11-04 20:59 | 9b2f71a | B | a770bc | 7cab4de | 16aa743 | 1P 2P 3P 4F 5F 6P | 3 | 13 |
| 48 | 2026-11-04 20:59 | 9b2f71a | B | a770bc | 7cab4de | 16aa743 | 1P 2P 3P 4F 5F 6F | 3 | 12 |
| 49 | 2026-11-04 21:33 | a52ab6f | B | bf572b | 611f58f | ec1968e | 1P 2P 3P 4P 5F 6P | 2 | 13 |
| 50 | 2026-11-04 21:33 | a52ab6f | B | bf572b | 611f58f | ec1968e | 1P 2P 3P 4F 5F 6P | 5 | 12 |
| 51 | 2026-11-04 21:33 | a52ab6f | B | bf572b | 611f58f | ec1968e | 1P 2P 3P 4F 5F 6P | 3 | 12 |
| 52 | 2026-11-04 22:37 | 8573a3c | C | bf572b | 2792413 | 545e7b8 | 1P 2P 3P 4P 5P 6P | 0 | 15 |
| 53 | 2026-11-04 22:37 | 8573a3c | C | bf572b | 2792413 | 545e7b8 | 1P 2P 3P 4P 5F 6F | 2 | 19 |
| 54 | 2026-11-04 22:37 | 8573a3c | C | bf572b | 2792413 | 545e7b8 | 1P 2P 3P 4P 5P 6P | 0 | 11 |
| 55 | 2026-11-04 22:46 | 03a00aa | C | a17e9e | 2792413 | 00d00e2 | 1P 2P 3P 4P 5F 6P | 1 | 10 |
| 56 | 2026-11-04 22:46 | 03a00aa | C | a17e9e | 2792413 | 00d00e2 | 1P 2P 3P 4P 5F 6F | 2 | 9 |
| 57 | 2026-11-04 22:46 | 03a00aa | C | a17e9e | 2792413 | 00d00e2 | 1P 2P 3P 4P 5F 6P | 2 | 13 |
| 58 | 2026-11-04 22:53 | 2f2d6d8 | C | a17e9e | 2792413 | 00d00e2 | no report | 0 | 0 |
| 59 | 2026-11-04 22:53 | 2f2d6d8 | C | a17e9e | 2792413 | 00d00e2 | no report | 0 | 0 |
| 60 | 2026-11-04 22:53 | 2f2d6d8 | C | a17e9e | 2792413 | 00d00e2 | no report | 0 | 0 |
| 61 | 2026-11-04 22:56 | 22b52d3 (working tree before commit) | C | 1e6c31 | 2792413 | 00d00e2 | 1P 2P 3P 4P 5F 6P | 2 | 8 |
| 62 | 2026-11-04 23:02 | 8e70a8c | C | a17e9e | 2792413 | 00d00e2 | 1P 2P 3P 4F 5P 6F | 2 | 15 |
| 63 | 2026-11-04 23:09 | 9fa0d81 | C | a17e9e | 2792413 | 00d00e2 | 1P 2P 3P 4P 5P 6P | 0 | 16 |
| 64 | 2026-11-04 23:16 | 9fa0d81 | C | a17e9e | 2792413 | 00d00e2 | 1P 2P 3P 4P 5F 6P | 1 | 15 |
| 65 | 2026-11-04 23:16 | 9fa0d81 | C | a17e9e | 2792413 | 00d00e2 | 1P 2P 3P 4P 5P 6P | 0 | 11 |
| 66 | 2026-11-04 23:16 | 9fa0d81 | C | a17e9e | 2792413 | 00d00e2 | 1P 2P 3P 4P 5F 6P | 1 | 15 |
| 67 | 2026-11-04 23:22 | 4dbd3de | C | a17e9e | 2792413 | 00d00e2 | 1P 2P 3P 4P 5P 6F | 2 | 11 |
| 68 | 2026-11-04 23:28 | 45c5bdd | C | a17e9e | 2792413 | 00d00e2 | 1P 2P 3P 4P 5F 6P | 1 | 12 |
| 69 | 2026-11-04 23:31 | e72a1d0 | C | a17e9e | 2792413 | 00d00e2 | no report | 0 | 0 |
| 70 | 2026-11-04 23:40 | 68ad628 | C | a17e9e | 2792413 | 00d00e2 | 1P 2P 3P 4P 5P 6F | 1 | 12 |
| 71 | 2026-11-04 23:47 | 5deb96f | C | a17e9e | 5ac0393 | 00d00e2 | 1P 2P 3P 4P 5F 6P | 1 | 13 |
| 72 | 2026-11-04 23:54 | c144812 | C | a17e9e | 808b23d | a1155df | 1P 2P 3P 4P 5F 6P | 1 | 12 |
| 73 | 2026-11-04 23:59 | 8741933 | C | 9f7acd | 421336d | a1155df | no report | 0 | 0 |
| 74 | 2026-11-05 00:02 | df3dcc1 | C | 9f7acd | cc8b1d0 | e407f70 | 1P 2P 3P 4P 5F 6P | 1 | 12 |
| 75 | 2026-11-05 00:05 | c74f108 | C | 9f7acd | cc8b1d0 | e407f70 | 1P 2P 3P 4F 5P 6P | 1 | 12 |
| 76 | 2026-11-05 00:09 | 6a08a16 | C | 9f7acd | cc8b1d0 | e407f70 | 1P 2P 3P 4P 5P 6P | 0 | 12 |
| 77 | 2026-11-05 00:15 | 6a08a16 | C | 9f7acd | cc8b1d0 | e407f70 | 1P 2P 3P 4P 5F 6P | 1 | 12 |
| 78 | 2026-11-05 00:15 | 6a08a16 | C | 9f7acd | cc8b1d0 | e407f70 | 1P 2P 3P 4P 5F 6P | 1 | 10 |
| 79 | 2026-11-05 00:19 | 91babdc | C | 9f7acd | cc8b1d0 | e407f70 | 1P 2P 3P 4P 5P 6P | 0 | 10 |
| 80 | 2026-11-05 00:23 | 91babdc | C | 9f7acd | cc8b1d0 | e407f70 | 1P 2P 3P 4P 5P 6P | 0 | 15 |
| 81 | 2026-11-05 00:23 | 91babdc | C | 9f7acd | cc8b1d0 | e407f70 | 1P 2P 3P 4P 5P 6P | 0 | 18 |
| 82 | 2026-11-06 20:45 | 3948a73 | D | 9f9588 | 2b1bf0b | c834139 | 1P 2P 3P 4P 5P 6F | 1 | 15 |
| 83 | 2026-11-06 20:51 | 4bc74af | D | 9f9588 | 2b1bf0b | c834139 | 1P 2P 3P 4P 5F 6F | 2 | 13 |
| 84 | 2026-11-06 20:57 | 757428e | D | 9f9588 | 2b1bf0b | c834139 | 1P 2P 3P 4P 5F 6P | 2 | 14 |
| 85 | 2026-11-06 21:03 | e763ee9 (working tree before commit) | D | 9f9588 | 2b1bf0b | c834139 | 1P 2P 3P 4P 5P 6F | 1 | 10 |
| 86 | 2026-11-06 21:08 | 6e9d907 | D | 9f9588 | 2b1bf0b | c834139 | 1P 2P 3P 4P 5F 6P | 1 | 13 |
| 87 | 2026-11-06 21:14 | ea5e697 | D | 9f9588 | 2b1bf0b | c834139 | 1P 2P 3F 4P 5F 6P | 3 | 14 |

## Findings

One row per finding. `What happened`, `Later runs`, `Caused by` and `Call` come from the cluster (next section) and are mine.

| Run | Commit | Id | Crit | Impact | Items | Quote | Finding | Cluster | What happened | Later runs | Caused by (mine) | Call (mine) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 4605655 | F1 | 4 | high | C3b; S9; S12 | played back, in the work's own words, what it understood you want at that level | No scenario fails if the playback repeats the user's words verbatim, so the 'own words' part of the claim is untested. | T1 | fixed e4a4d92/a36bf1f (round 1-2 fixes) | raised in 1,2,3; not again until 19 (same gap for instructions) | — | gap |
| 1 | 4605655 | F2 | 6 | high | S10; C6a; S13; M6 | the fact is never asked, and both are in that level's document | S10 requires an unasked found fact in the level document, while C6a, S13 and M6 forbid statements the user didn't say or agree. | T2 | fixed e4a4d92; returned 16-18 after the interview write-in, fixed b563f13 | raised again in 16,17,18 | — | gap |
| 1 | 4605655 | F3 | 5 | medium | S3; C2b; preamble | A level's first draft fails its review | Whether the first draft fails review is the work's output, not set by the scenario, so the fail-and-rework path may never be exercised. | T3 | fixed a36bf1f/9c62834 | family recurs as T25 | — | gap |
| 1 | 4605655 | F4 | 5 | medium | S12; M3; C5; preamble | judged by an LLM judge against the framework's readability rules | The readability rules standard comes from the work being judged and is not fixed with the scenario before the run. | T4 | fixed a36bf1f (rules come with the scenario) | dropped in many later runs | — | open |
| 2 | 4605655 | F1 | 4 | high | C3b; S9 | played back, in the work's own words, what it understood you want at that level | A verbatim-echo playback fails no check, so 'in the work's own words' is untested. | T1 | fixed e4a4d92/a36bf1f (round 1-2 fixes) | raised in 1,2,3; not again until 19 (same gap for instructions) | — | gap |
| 2 | 4605655 | F2 | 5 | medium | S3; C2b | A level's first draft fails its review | Nothing sets the first draft to fail; if it passes, the starting state never occurs and the review-gating part of C2b goes unexercised. | T3 | fixed a36bf1f/9c62834 | family recurs as T25 | — | gap |
| 2 | 4605655 | F3 | 5 | medium | S8; C7; S3 | You're asked which reading is meant before any level document is written | S8 fails a faithful work that defers a later-level ambiguity as C7 and S3 require. | T5 | fixed a36bf1f | recurs as T45 (53) and T51 (62) | — | gap |
| 2 | 4605655 | F4 | 5 | medium | S10; C8a; M1 | At each level, the decision is asked before the level's document is written | Once agreed at level 1, S10 requires the decision re-asked at every level, which C8a forbids and M1 counts against. | T6 | fixed a36bf1f |  | — | gap |
| 2 | 4605655 | F5 | 6 | high | S10; C6a; S13; M6 | the fact is never asked, and both are in that level's document | S10 requires an unasked found fact in the document while C6a, S13 and M6 forbid it. | T2 | fixed e4a4d92; returned 16-18 after the interview write-in, fixed b563f13 | raised again in 16,17,18 | — | gap |
| 3 | 4605655 | F1 | 4 | high | C3b; scenario 9; scenario 12; scenario 11 | played back, in the work's own words, what it understood you want at that level | No scenario fails when the playback merely repeats the user's description verbatim, so misreadings may not surface before writing. | T1 | fixed e4a4d92/a36bf1f (round 1-2 fixes) | raised in 1,2,3; not again until 19 (same gap for instructions) | — | gap |
| 3 | 4605655 | F2 | 6 | medium | scenario 10; C6a; scenario 13; measure 6 | the decision is asked before the level's document is written, the fact is never asked, and both are in that level's document | Scenario 10 requires an unasked found fact in the document, contradicting the claim, scenario 13 and measure 6. | T2 | fixed e4a4d92; returned 16-18 after the interview write-in, fixed b563f13 | raised again in 16,17,18 | — | gap |
| 4 | e4a4d92 | F1 | 4 | high | C3b; C3c; C3d; S8; S9; S10; S12; S3; S11; S13; M4 | The document is written only after you confirm the playback | Playback, choice and confirmation are checked only at the first level, so a work skipping them at later levels passes all scenarios. | T7 | fixed 847802b | same coverage-by-case request recurs (T12, T39) until D49/D51 made it not a finding | — | open |
| 5 | e4a4d92 | F1 | 5 | medium | S9; C3; C4 | The playback states what the work understood in words other than yours | If the work puts the ambiguous term as a choice first as C3 requires, there's nothing to correct, so S9's check can't be satisfied. | T8 | fixed 847802b |  | — | gap |
| 6 | e4a4d92 | F1 | 4 | high | C3b; C3d; S9; S10; S3; S11; S13 | The document is written only after you confirm the playback | Playback and confirmation are checked only at the first level; later levels could skip them with no scenario failing. | T7 | fixed 847802b | same coverage-by-case request recurs (T12, T39) until D49/D51 made it not a finding | — | open |
| 6 | e4a4d92 | F2 | 5 | medium | S9; C3c; S8 | you correct it, the level's document is written only after you confirm the corrected playback | If the work asks about the ambiguous term up front as C3c requires, no correction exists, so S9's check fails or is unsatisfiable. | T8 | fixed 847802b |  | — | gap |
| 11 | 847802b | F1 | 4 | high | C2b; approval definition; S3; S11 | Work moves to the next level only when the current one passes its review and you approve it | Every scenario starts with the review already passing, so no check fails if work advances on approval alone after a failed or skipped review. | T9 | fixed 9c62834 |  | — | gap |
| 16 | dd487b5 | F1 | 6 | high | C8; S16; S10 | A fact the work found appears only where its level allows it: none in Outcome | S10 requires a found fact in every level document including Outcome, which C8 forbids and S16 fails. | T2 | fixed e4a4d92; returned 16-18 after the interview write-in, fixed b563f13 | raised again in 16,17,18 | 16-18: dd487b5 (my write-in of the interview) | gap |
| 16 | dd487b5 | F2 | 4 | high | C3a; S15 | Before the work acts on anything from you that could change the project, it tells you what it understood | Only ambiguous mid-level instructions are checked; acting on an unambiguous project-changing instruction without playback fails no scenario. | T10 | fixed b563f13 | raised 16,17,18 together | — | gap |
| 16 | dd487b5 | F3 | 4 | high | C5; S12 | You're asked one question at a time, and the next waits for your answer. | S12 checks one question per message, but sending several before an answer fails no check. | T11 | fixed b563f13 (S12 'no question before the one before is answered') | raised 16,17,18 | — | gap |
| 16 | dd487b5 | F4 | 4 | high | C8; S16; S17 | in Slices, Design's facts and how the project is built and tested | Only Design's found facts and review are checked; Slices facts and Behaviour/Slices reviews have no check. | T12 | fixed b563f13/2cb2dcb by per-level checks; later removed by the level-1 vocabulary rule (D38 era) | raised 16-19; contradicted by D49/D51 later (structure not a finding) | — | open |
| 16 | dd487b5 | F5 | 4 | high | C3b | A plain answer to the work's own question is acted on without that. | No check fails if plain answers are played back and held for confirmation. | T13 | fixed b563f13 | returns as T50 (61) | — | gap |
| 16 | dd487b5 | F6 | 5 | medium | measure (unplayed changes); C3b | Changes to the project made on something from you that wasn't played back and confirmed: target zero. | The measure counts changes on plain answers, which C3b exempts from playback; the exception isn't carried. | T14 | fixed b563f13 | raised 16,17,18 | — | gap |
| 16 | dd487b5 | F7 | 1 | medium | measure (questions per level) | Questions asked per level: tracked, no target. | A measure without a target, tracing to no claim, contrary to the definition requiring a target. | T15 | fixed b563f13 (measure gets 'tracked, no target' then removed) | raised 16,17,18 | 16-18: dd487b5 (my write-in added the measure) | gap |
| 17 | dd487b5 | F1 | 6/5 | high | C (found facts); S16; S10 | A fact the work found appears only where its level allows it: none in Outcome | S10 requires a found fact in the Outcome document, which the claim and S16 forbid; the work can't satisfy both. | T2 | fixed e4a4d92; returned 16-18 after the interview write-in, fixed b563f13 | raised again in 16,17,18 | 16-18: dd487b5 (my write-in of the interview) | gap |
| 17 | dd487b5 | F2 | 4 | high | C5a; S12; M4 | You're asked one question at a time, and the next waits for your answer | A second question sent separately before the first is answered breaks the claim but fails no check. | T11 | fixed b563f13 (S12 'no question before the one before is answered') | raised 16,17,18 | — | gap |
| 17 | dd487b5 | F3 | 4 | high | C (found facts); S16 | in Behaviour, only what users get today; … in Slices, Design's facts and how the project is built and tested | No scenario checks Slices' allowance, and Behaviour is checked only for code facts, not the users-get-today limit. | T12 | fixed b563f13/2cb2dcb by per-level checks; later removed by the level-1 vocabulary rule (D38 era) | raised 16-19; contradicted by D49/D51 later (structure not a finding) | — | open |
| 17 | dd487b5 | F4 | 4 | high | C (fact review); S16; S17 | Before you approve a level, its review checks each found fact against the project, and a wrong fact is a finding | Found-fact review is exercised only at Design; Behaviour and Slices reviews are unchecked. | T12 | fixed b563f13/2cb2dcb by per-level checks; later removed by the level-1 vocabulary rule (D38 era) | raised 16-19; contradicted by D49/D51 later (structure not a finding) | — | open |
| 17 | dd487b5 | F5 | 4 | high | C3a; S15; M5 | Before the work acts on anything from you that could change the project, it tells you what it understood | S15 only brings about an ambiguous instruction, so skipping playback on clear instructions passes every scenario. | T10 | fixed b563f13 | raised 16,17,18 together | — | gap |
| 17 | dd487b5 | F6 | 5 | medium | C3b; measure (unplayed changes) | Changes to the project made on something from you that wasn't played back and confirmed: target zero | A change on a plain answer, allowed without playback, counts against the measure; exception not carried. | T14 | fixed b563f13 | raised 16,17,18 | — | gap |
| 17 | dd487b5 | F7 | 1/4 | medium | M14 | Questions asked per level: tracked, no target. | One measure has no target and traces to no claim. | T15 | fixed b563f13 (measure gets 'tracked, no target' then removed) | raised 16,17,18 | 16-18: dd487b5 (my write-in added the measure) | gap |
| 18 | dd487b5 | F1 | 6 | high | C8; S10; S16 | A fact the work found appears only where its level allows it: none in Outcome | S10 requires a found fact in the Outcome document while C8 forbids any there and S16 checks for none. | T2 | fixed e4a4d92; returned 16-18 after the interview write-in, fixed b563f13 | raised again in 16,17,18 | 16-18: dd487b5 (my write-in of the interview) | gap |
| 18 | dd487b5 | F2 | 5 | medium | C3; M5; S6; S7 | A plain answer to the work's own question is acted on without that. | M5 counts code changed on a plain answer as an unplayed change, though C3 allows it. | T14 | fixed b563f13 | raised 16,17,18 | — | gap |
| 18 | dd487b5 | F3 | 4 | high | C5; S12; M4 | You're asked one question at a time, and the next waits for your answer. | Separate single-question messages sent before an answer pass S12; 'waits for your answer' is unchecked. | T11 | fixed b563f13 (S12 'no question before the one before is answered') | raised 16,17,18 | — | gap |
| 18 | dd487b5 | F4 | 4 | high | C8; S16 | in Behaviour, only what users get today; ... in Slices, Design's facts and how the project is built and tested. | No check fails for Slices facts outside the allowance or Behaviour non-code facts beyond what users get today. | T12 | fixed b563f13/2cb2dcb by per-level checks; later removed by the level-1 vocabulary rule (D38 era) | raised 16-19; contradicted by D49/D51 later (structure not a finding) | — | open |
| 18 | dd487b5 | F5 | 4 | high | C3; S15; S9 | Before the work acts on anything from you that could change the project, it tells you what it understood | S15 covers only ambiguous instructions; acting on a clear mid-level instruction without playback fails no scenario. | T10 | fixed b563f13 | raised 16,17,18 together | — | gap |
| 18 | dd487b5 | F6 | 1 | medium | M14 | Questions asked per level: tracked, no target. | One measure lacks the required target and checks no claim. | T15 | fixed b563f13 (measure gets 'tracked, no target' then removed) | raised 16,17,18 | 16-18: dd487b5 (my write-in added the measure) | gap |
| 19 | b563f13 | F1 | 4 | high | claim (playback of instructions); scenario 15; scenario 9 | it tells you what it understood, in its own words, and waits for you to confirm | Scenario 15 passes a verbatim playback of a project-changing instruction; 'in its own words' is checked only for level playbacks. | T16 | fixed 2cb2dcb |  | — | gap |
| 19 | b563f13 | F2 | 4 | high | C8; scenario 16 | A fact the work found appears only where its level allows it | Scenario 16 checks 'only' for Outcome and Behaviour but not Design or Slices, so a users-get-today fact there fails no check. | T12 | fixed b563f13/2cb2dcb by per-level checks; later removed by the level-1 vocabulary rule (D38 era) | raised 16-19; contradicted by D49/D51 later (structure not a finding) | — | open |
| 20 | b563f13 | F1 | 5 | medium | S10; C4; C3 | your plain answer is acted on without a playback | The check can't separate the per-answer playback C3 exempts from the level playback C4 requires, so it fails correct runs or demands skipping playback. | T17 | partly fixed 2cb2dcb/877b935; R3 rewordings 2f2d6d8, 22b52d3, 363af74; R8 fixed 3b17c96 | recurs 20,21,27,30 then 56 (R3 vs R4), 61, 87; dropped as settled in ~20 runs (19-86) | — | gap |
| 20 | b563f13 | F2 | 5 | medium | S16; C8 | Design holds the second and not the third, Slices holds the second and third | C8 only permits the code fact in Design and Slices, but the check requires it in both, failing compliant runs. | T18 | fixed 2cb2dcb |  | — | gap |
| 20 | b563f13 | F3 | 5 | medium | S18; C11; S4; preamble | You build a feature in which the work made a decision scoped to one of its parts | The scoped decision and its expected citation come from the work under test, not the scenario, so C11 may go unexercised. | T19 | fixed 877b935/dd7b7d0 | recurs as T52 (64,66), T65 (84) | — | gap |
| 21 | b563f13 | F1 | 4 | high | claim (work's decisions stay the work's); claim (agreements carry over); S18 | The work's decisions in it stay the work's. | S18 uses a part outside the first decision's scope, so no check distinguishes a work's decision from one turned into an agreement by approval. | T20 | fixed 2cb2dcb; returned 62 | raised 21, again 62 | — | gap |
| 21 | b563f13 | F2 | 5 | medium | S10; A4 | your plain answer is acted on without a playback | Every level is played back before writing, so the check either fails behaviour A4 requires or has nothing to observe. | T17 | partly fixed 2cb2dcb/877b935; R3 rewordings 2f2d6d8, 22b52d3, 363af74; R8 fixed 3b17c96 | recurs 20,21,27,30 then 56 (R3 vs R4), 61, 87; dropped as settled in ~20 runs (19-86) | — | gap |
| 25 | 39a0f70 | F1 | 4 | high | C14; S19; S18 | The next feature makes the same decision again, with the earlier one as its preferred default | For your decisions only S19 applies, and its check does not fail if the earlier answer is not offered as the preferred default. | T21 | fixed 877b935 | raised 25,26,27 (all 3 runs) | — | gap |
| 25 | 39a0f70 | F2 | 4 | high | C2; S3; S11 | Each level produces one document. | No scenario fails when a level produces more than one document; S3 and S11 pass with several documents. | T22 | fixed 877b935 (S22) |  | — | gap |
| 25 | 39a0f70 | F3 | 5 | medium | S10; C10; S16 | the requirement and its verification are completed with what the work found, marked as found | S10's second case does not set a level allowing found facts, so its verdict depends on an unset starting condition and can contradict C10. | T23 | fixed 877b935 | raised 25,27 | — | gap |
| 26 | 39a0f70 | F1 | 4 | high | A11a; S9 | A level's document uses the project's terms with the project's meanings. | Only S9 touches terms and only in a clash case; no check fails if the work names a project concept with its own term. | T24 | fixed 877b935 (S21) | raised 26,27 | — | gap |
| 26 | 39a0f70 | F2 | 4 | high | A14b; S18; S19 | The next feature makes the same decision again, with the earlier one as its preferred default | S19 checks only that you are asked; the preferred-default part is unchecked for your decisions. | T21 | fixed 877b935 | raised 25,26,27 (all 3 runs) | — | gap |
| 26 | 39a0f70 | F3 | 5 | medium | S14; A2c | The level's review reports no findings before you're asked to approve it | Read literally, S14's check fails whenever the review finds the defect its starting state guarantees, misjudging a correct run. | T25 | flip-flopped: 0cb5b9e required the report; 8e70a8c (D52) dropped it; c74f108 S17 dropped the report; e763ee9 added 'asked once it passes' | 26 (check fails when review finds it), 37-39 (review never required to report), 50, 61, 74, 84; dropped in many runs | — | open |
| 27 | 39a0f70 | F1 | 4 | high | C14; S19; S18 | The next feature makes the same decision again, with the earlier one as its preferred default | For your decisions only S19 applies and it does not check the earlier answer is offered as preferred default. | T21 | fixed 877b935 | raised 25,26,27 (all 3 runs) | — | gap |
| 27 | 39a0f70 | F2 | 4 | high | C11; S9; M11 | A level's document uses the project's terms with the project's meanings. | S9 fails only when the project's word is used for your meaning; using another word for a project meaning passes everything. | T24 | fixed 877b935 (S21) | raised 26,27 | — | gap |
| 27 | 39a0f70 | F3 | 5 | medium | S10; C10; S16 | the requirement and its verification are completed with what the work found, marked as found | S10 sets no level, so at a level not allowing found facts the check requires behaviour C10 forbids. | T23 | fixed 877b935 | raised 25,27 | — | gap |
| 27 | 39a0f70 | F4 | 5 | medium | S10; C3; C4 | in the second you're asked nothing | A faithful run plays back and may interview, which the check counts as being asked, so it fails required behaviour. | T17 | partly fixed 2cb2dcb/877b935; R3 rewordings 2f2d6d8, 22b52d3, 363af74; R8 fixed 3b17c96 | recurs 20,21,27,30 then 56 (R3 vs R4), 61, 87; dropped as settled in ~20 runs (19-86) | — | gap |
| 27 | 39a0f70 | F5 | 5 | medium | S4; S18; S19 | Nothing in that level, your scripted answers or the rule is asked again | S4's guarded level is written by the work being judged, so its starting state is left to the work rather than set. | T19 | fixed 877b935/dd7b7d0 | recurs as T52 (64,66), T65 (84) | — | gap |
| 29 | 877b935 | F1 | 6 | high | C6; C15; S1; M14 | Nothing is guessed. A fact is looked up, a decision is asked, a reading is asked | C6 lists no 'work decides' path, so all decisions are asked, contradicting C15, S1 and M14 which forbid asking the work's decisions. | T26 | 29: fixed dd7b7d0; 82: R15 fixed 4bc74af | raised 29, then 82; R15's text passed 3 clean runs (79-81) and was dropped in ~25 runs | — | gap |
| 30 | 877b935 | F1 | 5 | medium | S15; A4 | your answer is acted on without being played back | The level playback A4 requires restates the answer, so S15's check fails a work behaving as A4 requires. | T17 | partly fixed 2cb2dcb/877b935; R3 rewordings 2f2d6d8, 22b52d3, 363af74; R8 fixed 3b17c96 | recurs 20,21,27,30 then 56 (R3 vs R4), 61, 87; dropped as settled in ~20 runs (19-86) | — | gap |
| 30 | 877b935 | F2 | 5 | medium | S14; S22; S11 | When code starts, each level has produced exactly one document | S14 and S22 are conditioned on events the work must cause; a run never reaching them passes without the user getting the result. | T27 | fixed dd7b7d0 |  | — | gap |
| 31 | dd7b7d0 | F1 | 5 | medium | S10; A4a; A5a; C13 | in the second you're asked nothing beyond the playback | S10's starting state doesn't rule out other needed questions, so a correct run asking a needed decision or clarity question fails. | T28 | fixed ec102df | raised 31,33 | — | gap |
| 33 | dd7b7d0 | F1 | 5 | medium | S10; C4a; C5 | in the second you're asked nothing beyond the playback | S10 doesn't rule out other needed decisions, so its check fails a correct run that also asks an unrelated needed decision. | T28 | fixed ec102df | raised 31,33 | — | gap |
| 34 | ec102df | F1 | 4 | high | C7; S10 | A requirement is complete when its verification can be written in full and run, with nothing left to ask you. | Only S10 traces to C7 and covers 'written'; no scenario fails if a verification that can't be run is treated as complete. | T29 | fixed 3e512e3 (S23) | raised 34, 50 | — | gap |
| 35 | ec102df | F1 | 2 | medium | Scenarios preamble | Each runs several times on a sample project with a scripted user, and passes only if every run passes. | The run count and aggregation rule are a procedure for how checks run, which belongs to how tests are built. | T30 | fixed by instruction 3e512e3/2ce9279 (pass bar stated once is allowed) | raised 35,44,46; dropped in ~70 runs | — | open |
| 37 | 3e512e3 | F1 | 5 | medium | S14; A2c; S17 | its review reports no findings at the time you're asked | S14's check reads only the review's own report, so a review that never reports the planted defect passes. | T25 | flip-flopped: 0cb5b9e required the report; 8e70a8c (D52) dropped it; c74f108 S17 dropped the report; e763ee9 added 'asked once it passes' | 26 (check fails when review finds it), 37-39 (review never required to report), 50, 61, 74, 84; dropped in many runs | — | open |
| 38 | 3e512e3 | F1 | 2 | medium | definitions paragraph; decision classification link | Which decisions are yours and which are the work's is set by the [decision classification](../../skills/references/decisions.md). | Fixing the classification at a specific file path is where something lives, which belongs to later levels. | T31 | kept per D20; dropped since | raised 38; dropped in ~50 runs | — | misread |
| 38 | 3e512e3 | F2 | 5 | medium | S14; S17 | You start from a level whose document has a defect its review finds | Whether the review finds the defect is left to the work and the check never requires it reported or fixed. | T25 | flip-flopped: 0cb5b9e required the report; 8e70a8c (D52) dropped it; c74f108 S17 dropped the report; e763ee9 added 'asked once it passes' | 26 (check fails when review finds it), 37-39 (review never required to report), 50, 61, 74, 84; dropped in many runs | — | open |
| 39 | 3e512e3 | F1 | 5 | medium | S14; C2; S17 | its review reports no findings at the time you're asked | A review reporting nothing from the start passes every clause; whether the defect is found is left to the work. | T25 | flip-flopped: 0cb5b9e required the report; 8e70a8c (D52) dropped it; c74f108 S17 dropped the report; e763ee9 added 'asked once it passes' | 26 (check fails when review finds it), 37-39 (review never required to report), 50, 61, 74, 84; dropped in many runs | — | open |
| 40 | bd73aa3 | F1 | 5 | medium | S4; C13; C16 | A codified rule exists, an earlier level of the second feature is approved | Nothing makes the second feature need the rule, so 'not asked again' and 'follows all three' pass vacuously for the rule. | T32 | fixed 1d7d23a |  | — | gap |
| 40 | bd73aa3 | F2 | 5 | medium | S7; C13; C16; C17 | You're asked about the conflict | Claims don't require this question; work that follows your agreed decision without asking meets the claims but fails S7. | T33 | fixed 1d7d23a/b7b609f (D42) | raised 40,47,50 | — | gap |
| 40 | bd73aa3 | F3 | 5 | medium | S10; S23; C5; C7; C3 | you're asked for exactly that thing, in a message of its own | Claims require one question at a time, not a message of its own; a question with a playback meets claims but fails. | T34 | fixed 1d7d23a | raised 40,42 | — | gap |
| 40 | bd73aa3 | F4 | 5 | medium | S5; S20; C6 | Nothing is asked after code starts | S5 doesn't rule out an unassigned point arising after code starts, so correctly asking about it fails the check. | T35 | fixed 1d7d23a, 2cb26bc, a81dcfe | raised 40,49,50,51 | — | gap |
| 40 | bd73aa3 | F5 | 5 | medium | M16; C18 | Results you get under one of Claude Code and Codex but not the other: target zero. | A real feature runs under one runner, so the measure reads zero whether or not C18 holds. | T36 | fixed 89876c0 |  | 40: bd73aa3 (my both-hosts measure) | gap |
| 41 | bd73aa3 | F1 | 5 | medium | S12; C5 | judged by an LLM judge against the readability rules | Answerability is judged against readability rules, so a readable question lacking what you need still passes. | T37 | fixed 9b2f71a | raised 41,44 | — | gap |
| 42 | bd73aa3 | F1 | 5 | medium | S10; S23; C7; C5; C3 | you're asked for exactly that thing, in a message of its own | Claims require one question at a time, not a sole-content message, so a question with other content fails allowed behaviour. | T34 | fixed 1d7d23a | raised 40,42 | — | gap |
| 42 | bd73aa3 | F2 | 5 | medium | S13; C9; C16 | judged by an LLM judge against the transcript | Existing sample-project agreements aren't excluded; statements from them would count unsupported against the transcript. | T38 | fixed 9b2f71a |  | — | gap |
| 43 | 89876c0 | F1 | 4 | medium | C8; S12; C15; C11; M4 | Every document and message meant for a person is readable at a glance. | S12 checks only documents 'you're sent'; decision and clash records kept where you can see them have no failing scenario. | T39 | fixed 2cb26bc (S12 widened) | raised 43,45,46,47,48 | — | gap |
| 44 | 89876c0 | F1 | 6 | high | C17; C6; S5 | If one of your decisions still blocks it, you're asked, and only then. | An unassigned point after code starts is put to you per C6 but not asked per C17's 'only then'. | T42 | fixed 2cb26bc (R17 wording) | raised 44,48; family returns as T62/T66 | — | gap |
| 44 | 89876c0 | F2 | 5 | medium | S12; C5 | judged by an LLM judge against the readability rules | Answerability judged against readability rules lets a readable but insufficient question pass. | T37 | fixed 9b2f71a | raised 41,44 | — | gap |
| 44 | 89876c0 | F3 | 2 | medium | Scenarios preamble | The scripted user answers questions, confirms or corrects playbacks and approves levels as its script says. | These sentences say how scenarios are scripted and tests built, which the definition excludes from an Outcome. | T30 | fixed by instruction 3e512e3/2ce9279 (pass bar stated once is allowed) | raised 35,44,46; dropped in ~70 runs | — | open |
| 45 | 89876c0 | F1 | 4 | medium | C8; S12; M4 | Every document and message meant for a person is readable at a glance. | S12 covers only what is sent; unsent documents like decision records or PR descriptions have no failing scenario. | T39 | fixed 2cb26bc (S12 widened) | raised 43,45,46,47,48 | — | gap |
| 46 | 9b2f71a | F1 | 4 | high | A8; S12 | Every document and message meant for a person is readable at a glance. | S12 covers only documents meant for you; nothing fails if those meant for other people are unreadable. | T39 | fixed 2cb26bc (S12 widened) | raised 43,45,46,47,48 | — | gap |
| 46 | 9b2f71a | F2 | 5 | medium | S12 | including the records kept where you can see them | S12's starting state calls for no work's decisions or clashes, so records need not exist and the readability check passes vacuously. | T40 | fixed 2cb26bc |  | — | gap |
| 46 | 9b2f71a | F3 | 2 | medium | Scenarios preamble | The scripted user answers questions, confirms or corrects playbacks and approves levels as its script says. | These sentences fix how scenarios are scripted and tests built, which the definition leaves to later levels. | T30 | fixed by instruction 3e512e3/2ce9279 (pass bar stated once is allowed) | raised 35,44,46; dropped in ~70 runs | — | open |
| 47 | 9b2f71a | F1 | 4 | high | C8; S12; M4 | Every document and message meant for a person is readable at a glance. | S12 covers only documents meant for you; others are measured but no scenario check fails. | T39 | fixed 2cb26bc (S12 widened) | raised 43,45,46,47,48 | — | gap |
| 47 | 9b2f71a | F2 | 4, 5 | medium | S7; C13; C16; C17; C5; M14 | You're asked about the conflict | No claim requires asking about the conflict; following your decision fails S7, and asking could violate C5 if the work owns it. | T33 | fixed 1d7d23a/b7b609f (D42) | raised 40,47,50 | — | gap |
| 47 | 9b2f71a | F3 | 5 | medium | S19; C14; C13; S18; S20 | a second feature where the same decision arises for a part outside that scope | S19 doesn't rule out a covering agreement or rule, so asking would be wrong yet its check requires it. | T41 | fixed 2cb26bc | raised 47,48 | — | gap |
| 48 | 9b2f71a | F1 | 4 | high | C8; S12 | Every document and message meant for a person is readable at a glance. | S12 judges only documents meant for you; e.g. pull requests for others have no checking scenario. | T39 | fixed 2cb26bc (S12 widened) | raised 43,45,46,47,48 | — | gap |
| 48 | 9b2f71a | F2 | 5 | medium | S19; C14; C13; S18 | a second feature where the same decision arises for a part outside that scope | S19 doesn't rule out a covering agreement, so its 'asked' check would fail correct behaviour. | T41 | fixed 2cb26bc | raised 47,48 | — | gap |
| 48 | 9b2f71a | F3 | 6 | high | C17; C6; C7; S23; S5 | If one of your decisions still blocks it, you're asked, and only then. | A non-decision gap after code starts must be asked under C6/C7 but C17 forbids it; S5 follows C17. | T42 | fixed 2cb26bc (R17 wording) | raised 44,48; family returns as T62/T66 | — | gap |
| 49 | a52ab6f | F1 | 5 | medium | S5; R17; R6; S23 | Nothing is asked after code starts | S5 doesn't rule out a non-decision gap only you can supply, so a work correctly asking after code starts fails. | T35 | fixed 1d7d23a, 2cb26bc, a81dcfe | raised 40,49,50,51 | — | gap |
| 49 | a52ab6f | F2 | 5 | medium | S16; R10; S17 | and the level's review checked it against the project before you were asked to approve that level | With a correct fact, 'review checked it' is only observable from the review's own account, testing implementation not user-observed behaviour. | T43 | fixed c7d8cc4 (D48) + a81dcfe | raised 49,50,51 (all 3 runs) | — | gap |
| 50 | a52ab6f | F1 | 4 | high | R7; S10; S23 | A verification is complete when it names what is checked, how, and what result passes. | No scenario says which of the three parts is missing, so the work could treat a verification lacking one as complete undetected. | T29 | fixed 3e512e3 (S23) | raised 34, 50 | — | gap |
| 50 | a52ab6f | F2 | 5 | medium | S5; R17; S10; S23 | Nothing is asked after code starts | S5 doesn't rule out a non-decision blocker only you can supply, so it can fail a run that correctly asks. | T35 | fixed 1d7d23a, 2cb26bc, a81dcfe | raised 40,49,50,51 | — | gap |
| 50 | a52ab6f | F3 | 5 | medium | S7; R17; L26 definitions | existing code that nothing you agreed decided conflicts with one of your decisions | The conflicting code may come from the work's own decision, which isn't yours to settle, so R17 forbids asking yet S7 requires it. | T33 | fixed 1d7d23a/b7b609f (D42) | raised 40,47,50 | — | gap |
| 50 | a52ab6f | F4 | 5 | medium | S14; R2; R10 | You start from a level whose document has a defect its review finds | Starting state is defined by the judged review's output; the check holds by construction and fails a run R2 allows if missed. | T25 | flip-flopped: 0cb5b9e required the report; 8e70a8c (D52) dropped it; c74f108 S17 dropped the report; e763ee9 added 'asked once it passes' | 26 (check fails when review finds it), 37-39 (review never required to report), 50, 61, 74, 84; dropped in many runs | — | open |
| 50 | a52ab6f | F5 | 5 | medium | S16; R10; S17 | the level's review checked it against the project before you were asked to approve that level | With a correct fact, only the review's own trace shows it checked, testing implementation not user-observed behaviour. | T43 | fixed c7d8cc4 (D48) + a81dcfe | raised 49,50,51 (all 3 runs) | — | gap |
| 51 | a52ab6f | F1 | 4 | medium | R3; S15; S8; R4 | Anything that could be read more than one way is put to you as a choice, on its own, after the playback. | For instructions, no scenario checks the reading choice comes after the playback; S8 covers only level answers. | T44 | fixed a81dcfe (S15) |  | — | gap |
| 51 | a52ab6f | F2 | 5 | medium | S16; S17; R10 | and the level's review checked it against the project before you were asked to approve that level | With a correct fact, only the work's own trace proves the check, testing implementation not observed behaviour. | T43 | fixed c7d8cc4 (D48) + a81dcfe | raised 49,50,51 (all 3 runs) | — | gap |
| 51 | a52ab6f | F3 | 5 | medium | S5; R17; R7; S23 | Nothing is asked after code starts | S5 never rules out something only you can supply, so a work correctly asking after code starts fails. | T35 | fixed 1d7d23a, 2cb26bc, a81dcfe | raised 40,49,50,51 | — | gap |
| 53 | 8573a3c | F1 | 6 | high | R3; R12; S3; S8 | Anything that could be read more than one way is put to you as a choice, on its own, after the playback. | R3 requires asking an ambiguous reading after the playback now, while R12 forbids answering a later-level question early; which applies is undetermined. | T45 | fixed 03a00aa (R3 scoped) | 53 only; 52,54 clean | 53: a52ab6f (D50 made absolute terms findings) | gap |
| 53 | 8573a3c | F2 | 5 | medium | S10; R10; R9; S16 | completed with what the work found, marked as found | S10 requires marking the fact as found while R10 requires marking it as the work's, so S10 could fail a compliant run. | T46 | fixed 03a00aa |  | — | gap |
| 55 | 03a00aa | F1 | 5 | medium | S15; R3; R6; S8 | Anything that could be read more than one way about what the current level decides | S15 requires the reading question after the playback even for ambiguity outside the level's decisions, failing behaviour R3 and R6 allow. | T47 | fixed 2f2d6d8 | 55,56,57 (all 3 runs) | 03a00aa (my R3 scoping) | gap |
| 56 | 03a00aa | F1 | 6 | high | R3; R4; L9; L10; L26; S15 | A plain answer to the work's own question is acted on without that | Interview answers are plain answers, so R3 lets the document be written without playback while R4 requires playback first. | T48 | fixed 2f2d6d8 then 22b52d3/363af74 | 56 | — | gap |
| 56 | 03a00aa | F2 | 5 | medium | S15; R3; R6 | for the second it asks which reading is meant in a message of its own, after the playback | S15 doesn't limit ambiguity to what the level decides, so it can fail asking the reading inside the playback, which R3 allows. | T47 | fixed 2f2d6d8 | 55,56,57 (all 3 runs) | 03a00aa (my R3 scoping) | gap |
| 57 | 03a00aa | F1 | 5 | medium | S15; R3; R6 | about what the current level decides | S15's starting state doesn't confine ambiguity to level decisions, so it fails asking the reading before playback, which R3 and R6 allow. | T47 | fixed 2f2d6d8 | 55,56,57 (all 3 runs) | 03a00aa (my R3 scoping) | gap |
| 57 | 03a00aa | F2 | 5 | medium | S18; R14 | cites the first as its preferred default | S18 checks the work's citation rather than what it decided, passing cite-only runs and failing uncited re-decisions R14 allows. | T49 | fixed 2f2d6d8 | 57 | — | gap |
| 61 | 22b52d3 (working tree before commit) | F1 | 5 | medium | R3; S15; M6 | your answer is acted on without a playback of its own. | R3 permits but doesn't forbid playing back a plain answer, yet S15 fails a run that does. | T50 | fixed 363af74 (FF-14 wording restored) | 61 | 22b52d3 (my R3 wording) | gap |
| 61 | 22b52d3 (working tree before commit) | F2 | 5 | medium | R2; S14; R10; S17 | you're asked to approve the level only after a later review reports no findings. | S14 fails a review missing a defect, which R2 allows, and trusts the later review's own no-findings report rather than checking the defect is gone. | T25 | flip-flopped: 0cb5b9e required the report; 8e70a8c (D52) dropped it; c74f108 S17 dropped the report; e763ee9 added 'asked once it passes' | 26 (check fails when review finds it), 37-39 (review never required to report), 50, 61, 74, 84; dropped in many runs | 61: 0cb5b9e; 74: 8e70a8c pattern; 84: c74f108 (my S17 change) | open |
| 62 | 8e70a8c | F1 | 4 | high | R13; R14; S18; S1 | The work's decisions in it stay the work's. | No scenario gives a later feature reason to decide differently, so treating the work's decisions as binding passes every scenario untested. | T20 | fixed 2cb2dcb; returned 62 | raised 21, again 62 | 62: 2f2d6d8 (my S18 rewrite dropped the case) | gap |
| 62 | 8e70a8c | F2 | 6 | high | S10; R7; R12 | Anything missing from either is asked | If a verification's missing piece belongs to a later level, S10/R7 require asking now while R12 forbids answering early. | T51 | fixed 9fa0d81 (scope to the level) | 62 | 03a00aa (added 'any/anything' to the absolute terms) | gap |
| 64 | 9fa0d81 | F1 | 5 | medium | S11; R2; S14; S17 | A level passes its review, you withhold approval for several turns, then approve it | S11's starting state doesn't set up a passed level, so it relies on the work's review passing and could misjudge R2's approval wait. | T52 | fixed 4dbd3de | 64,66 (2 of 3 runs; 65 clean) | — | gap |
| 66 | 9fa0d81 | F1 | 5 | medium | S11; R2; S14; S17 | A level passes its review, you withhold approval for several turns, then approve it | S11 doesn't set up a passed level and depends on the work producing one, so it may not check R2's approval gate. | T52 | fixed 4dbd3de | 64,66 (2 of 3 runs; 65 clean) | — | gap |
| 67 | 4dbd3de | F1 | 6 | high | R13; R18; R21; S1; S10; S23 | Anything missing from either is asked, one question at a time, unless the work can find it out. | R13 literally requires asking anything missing, including later-level points and the work's decisions, which R18 and R21 forbid. | T53 | my rewording 45c5bdd reverted; fixed 68ad628 (FF-44 A) | 67 | 03a00aa (absolute 'anything') | gap |
| 67 | 4dbd3de | F2 | 6 | high | R16; R13; R11 | A fact the work found appears only in a level that allows it | At a non-allowing level missing a findable fact, R11/R13 forbid asking, R13 requires completion, R16 forbids writing it. | T53 | my rewording 45c5bdd reverted; fixed 68ad628 (FF-44 A) | 67 | 03a00aa (absolute 'anything') | gap |
| 68 | 45c5bdd | F1 | 5 | medium | S18; R15; L26; S5; S20 | nothing you agreed or codified covers it | S18 doesn't rule out that the decision becomes the user's or unassigned in the second feature, so it fails asking as R15 requires. | T54 | fixed e72a1d0 | 68 | 9fa0d81 (my S18 second case) | gap |
| 70 | 68ad628 | F1 | 6 | high | L13; L18; L26; S23; R7; R12; R2 | with nothing left to ask you | 'Nothing left to ask' is absolute but R12 defers later-level points, so early requirements can't be complete and levels may not pass. | T55 | fixed 5deb96f | 70 | 68ad628 (scoping only the last sentence) | gap |
| 71 | 5deb96f | F1 | 5 | medium | S14; S17; R2; R10; L26 | You aren't asked to approve the level while its document fails that standard | Requirements don't forbid asking for approval early, so S14 and S17 fail a compliant run that asks early but doesn't move on. | T56 | fixed c144812 (R2 FF-4 + 'allows' defined) | 71; dropped in ~8 runs before | — | open |
| 72 | c144812 | F1 | 5 | medium | S18; R14 | in the second it is the choice the scenario sets for that reason | S18 fails behaviour R14 allows (keeping the default or picking another option) whenever it differs from the scenario's preset choice. | T57 | fixed 8741933 | 72 | 9fa0d81 (my S18 second case) | gap |
| 74 | df3dcc1 | F1 | 5 | medium | S17; R10 | Its review reports the wrong fact as a finding, and you aren't asked to approve the level while it holds one | S17's first half checks the work's own review report; a run removing the wrong fact earlier gets R10's result yet fails. | T58 | fixed c74f108 | 74 | — | gap |
| 75 | c74f108 | F1 | 4 | high | L8; S3; S11; S14; L10 | Work moves to the next level only when the current one passes its review and you approve it. | Gate scenarios only check no next-level document is written; a run could interview and play back the next level before approval and pass. | T59 | fixed 6a08a16 | 75 | — | gap |
| 77 | 6a08a16 | F1 | 5 | medium | S15; R3 | the project changes only after you confirm, and only in the reading you confirmed | S15's absolute 'only after you confirm' fails a run that acts on the plain answer immediately, which R3 allows. | T60 | fixed 91babdc | 77,78 (2 of 3; 76 clean) | c144812 (the 'allows' rule made it a finding) | gap |
| 78 | 6a08a16 | F1 | 5 | medium | S15; R3 | the project changes only after you confirm, and only in the reading you confirmed | The 'only after you confirm' clause isn't limited to the instructions, so S15 fails a run acting on the plain answer as R3 requires. | T60 | fixed 91babdc | 77,78 (2 of 3; 76 clean) | c144812 (the 'allows' rule made it a finding) | gap |
| 82 | 3948a73 | F1 | 6 | high | R15; R33; S1; M14 | anything the work can't settle one of those ways is put to the user | R15's absolute 'anything' sends the work's own decisions to the user, contradicting R33, S1 and M14. | T61 | fixed 4bc74af | 82 | — | gap |
| 83 | 4bc74af | F1 | 6 | high | R37; R38; S6; S7 | Once code starts, the work proceeds with everything it needs. | R37's absolute 'everything' says nothing is lacking after code starts; R38 makes an exception allowing asking, a contradiction. | T62 | fixed 757428e | 83 | 3948a73 (my split of one bullet into R37/R38) | gap |
| 83 | 4bc74af | F2 | 5 | medium | S23; R16 | The user is asked for exactly that thing before the requirement is treated as complete | 'Treated as complete' is the work's internal state, so the check judges R16's timing against the work's self-report. | T63 | fixed 757428e | 83; dropped as later-level in ~22 runs (44-82) | — | open |
| 84 | 757428e | F1 | 5 | medium | S17; R21 | The user isn't asked to approve the level while it holds the wrong fact | S17 only forbids an event, so a run that never checks the fact and never asks for approval passes; R21 lacks a failing verification. | T64 | fixed e763ee9 | 84 | c74f108 (my S17 change removed the report clause) | gap |
| 84 | 757428e | F2 | 5 | medium | S4; R28 | an earlier level of it is approved with the user's answer to a question | S4's starting state doesn't set up the second feature's earlier level, so the check relies on what the work produced earlier. | T65 | fixed e763ee9 | 84; S4's setup dropped in ~40 runs | 3948a73 (my rewrite reordered S4's sentence) | gap |
| 85 | e763ee9 (working tree before commit) | F1 | 6 | high | R2; S1; R38; R37; S6 | the user's decisions are made before code starts | R2 has no exception, yet R38, R37 and S6 allow a user decision after code starts, leaving build-time asking ambiguous. | T66 | fixed 6e9d907, then reverted 6e82d4d after D58 (not a finding) | 85; dropped as 'no absolute term' in many runs | — | open |
| 86 | 6e9d907 | F1 | 5 | medium | S1; R2 | Each of the user's decisions, wherever written, was made by the user before code starts | S1 neither rules out nor carries R2's after-code-starts exception, so it fails a run doing what R2 allows. | T67 | fixed ea5e697, reverted 6e82d4d | 86 | 6e9d907 (my R2 carve-out) | gap |
| 87 | ea5e697 | F1 | 3 | high | R8; R7; S8; R10 | is put to the user as a choice, on its own, after the playback | For an ambiguous plain answer R8 doesn't say which playback; the readings give different exchanges and different S8 checks. | T68 | fixed 3b17c96 | 87; dropped in ~3 runs (83,84,86) | — | open |
| 87 | ea5e697 | F2 | 3 | high | R20; R22; S21; glossary | A found fact appears only in a level that allows found facts, marked as the work's. | Unclear whether a found project term is a found fact; if so, R22/S21 require what R20's 'only' forbids. | T69 | decided D59 (FF-49 A), glossary | 87; dropped in 83,84 | — | open |
| 87 | ea5e697 | F3 | 5 | medium | S10; S16; S23; R16; R20; glossary | the requirement and its verification are completed with what the work found | Pass bars require completed requirements/verifications that no verified requirement requires, so they fail allowed runs. | T70 | fixed 3b17c96 (R40) | 87 | 3948a73 (my rewrite moved the completeness sentence to the glossary) | gap |

## Clusters (mine)

| Cluster | Issue | Findings in runs | What happened | Later runs | Caused by | Call |
|---|---|---|---|---|---|---|
| T1 | Playback 'in its own words' untested | 1, 2, 3 | fixed e4a4d92/a36bf1f (round 1-2 fixes) | raised in 1,2,3; not again until 19 (same gap for instructions) |  | gap |
| T2 | S10 needs a found fact the user never said, against the 'said or agreed' rule | 1, 2, 3, 16, 17, 18 | fixed e4a4d92; returned 16-18 after the interview write-in, fixed b563f13 | raised again in 16,17,18 | 16-18: dd487b5 (my write-in of the interview) | gap |
| T3 | S3/S14: the failing draft is the work's output, not set up | 1, 2 | fixed a36bf1f/9c62834 | family recurs as T25 |  | gap |
| T4 | Readability rules not fixed before the run | 1 | fixed a36bf1f (rules come with the scenario) | dropped in many later runs |  | open |
| T5 | S8 fails deferring a later-level ambiguity | 2 | fixed a36bf1f | recurs as T45 (53) and T51 (62) |  | gap |
| T6 | S10 re-asks an agreed decision at every level | 2 | fixed a36bf1f |  |  | gap |
| T7 | Playback/confirmation checked only at the first level | 4, 6 | fixed 847802b | same coverage-by-case request recurs (T12, T39) until D49/D51 made it not a finding |  | open |
| T8 | S9 unsatisfiable if the ambiguous term is asked up front | 5, 6 | fixed 847802b |  |  | gap |
| T9 | No scenario has a review that fails, so approval-only advance passes | 11 | fixed 9c62834 |  |  | gap |
| T10 | Only ambiguous instructions checked; clear-instruction playback untested | 16, 17, 18 | fixed b563f13 | raised 16,17,18 together |  | gap |
| T11 | Several single-question messages before an answer pass | 16, 17, 18 | fixed b563f13 (S12 'no question before the one before is answered') | raised 16,17,18 |  | gap |
| T12 | Found-fact coverage per level (Behaviour, Slices) | 16, 17, 18, 19 | fixed b563f13/2cb2dcb by per-level checks; later removed by the level-1 vocabulary rule (D38 era) | raised 16-19; contradicted by D49/D51 later (structure not a finding) |  | open |
| T13 | Plain answers played back: no check | 16 | fixed b563f13 | returns as T50 (61) |  | gap |
| T14 | Measure counts changes on plain answers that need no playback | 16, 17, 18 | fixed b563f13 | raised 16,17,18 |  | gap |
| T15 | Measure without a target | 16, 17, 18 | fixed b563f13 (measure gets 'tracked, no target' then removed) | raised 16,17,18 | 16-18: dd487b5 (my write-in added the measure) | gap |
| T16 | S15 passes a verbatim playback of an instruction | 19 | fixed 2cb2dcb |  |  | gap |
| T17 | Which playback: an answer's own vs the level's | 20, 21, 27, 30 | partly fixed 2cb2dcb/877b935; R3 rewordings 2f2d6d8, 22b52d3, 363af74; R8 fixed 3b17c96 | recurs 20,21,27,30 then 56 (R3 vs R4), 61, 87; dropped as settled in ~20 runs (19-86) | 56/61: 2f2d6d8 and 22b52d3 (my R3 rewordings) | gap |
| T18 | S16 requires the code fact in both Design and Slices | 20 | fixed 2cb2dcb |  |  | gap |
| T19 | Starting state relies on the work (S18 scope, S4 guarded level) | 20, 27 | fixed 877b935/dd7b7d0 | recurs as T52 (64,66), T65 (84) |  | gap |
| T20 | The work's decisions staying the work's is untested | 21, 62 | fixed 2cb2dcb; returned 62 | raised 21, again 62 | 62: 2f2d6d8 (my S18 rewrite dropped the case) | gap |
| T21 | S19 doesn't check the earlier answer is offered as default | 25, 26, 27 | fixed 877b935 | raised 25,26,27 (all 3 runs) |  | gap |
| T22 | One document per level unchecked | 25 | fixed 877b935 (S22) |  |  | gap |
| T23 | S10 doesn't set a level that allows found facts | 25, 27 | fixed 877b935 | raised 25,27 |  | gap |
| T24 | Project terms: no check for naming a concept with the work's own term | 26, 27 | fixed 877b935 (S21) | raised 26,27 |  | gap |
| T25 | S14: does the review have to report the defect, and can its own report be trusted | 26, 37, 38, 39, 50, 61 | flip-flopped: 0cb5b9e required the report; 8e70a8c (D52) dropped it; c74f108 S17 dropped the report; e763ee9 added 'asked once it passes' | 26 (check fails when review finds it), 37-39 (review never required to report), 50, 61, 74, 84; dropped in many runs | 61: 0cb5b9e; 74: 8e70a8c pattern; 84: c74f108 (my S17 change) | open |
| T26 | The rule 'anything not settled is put to the user' sends the work's own decisions to the user | 29 | 29: fixed dd7b7d0; 82: R15 fixed 4bc74af | raised 29, then 82; R15's text passed 3 clean runs (79-81) and was dropped in ~25 runs | 82: not caused by a fix; the text was unchanged from 91babdc, which 3 runs passed | gap |
| T27 | S14/S22 conditioned on events the work must cause | 30 | fixed dd7b7d0 |  |  | gap |
| T28 | S10 doesn't rule out other needed questions | 31, 33 | fixed ec102df | raised 31,33 |  | gap |
| T29 | Completeness: the 'and run' part / which part is missing has no scenario | 34, 50 | fixed 3e512e3 (S23) | raised 34, 50 |  | gap |
| T30 | Preamble: run counts and scripted user read as how tests are built | 35, 44, 46 | fixed by instruction 3e512e3/2ce9279 (pass bar stated once is allowed) | raised 35,44,46; dropped in ~70 runs |  | open |
| T31 | The link to the decision classification read as 'where anything lives' | 38 | kept per D20; dropped since | raised 38; dropped in ~50 runs |  | misread |
| T32 | S4: nothing makes the second feature need the rule | 40 | fixed 1d7d23a |  |  | gap |
| T33 | S7: no requirement says the conflict is asked | 40, 47, 50 | fixed 1d7d23a/b7b609f (D42) | raised 40,47,50 |  | gap |
| T34 | 'Message of its own' vs 'one question at a time' | 40, 42 | fixed 1d7d23a | raised 40,42 |  | gap |
| T35 | S5 doesn't rule out a point only the user can settle after code starts | 40, 49, 50, 51 | fixed 1d7d23a, 2cb26bc, a81dcfe | raised 40,49,50,51 |  | gap |
| T36 | Runner measure reads zero on real features | 40 | fixed 89876c0 |  | 40: bd73aa3 (my both-hosts measure) | gap |
| T37 | Answerability judged only against readability rules | 41, 44 | fixed 9b2f71a | raised 41,44 |  | gap |
| T38 | S13 doesn't exclude existing agreements | 42 | fixed 9b2f71a |  |  | gap |
| T39 | Readability of records and documents for others has no scenario | 43, 45, 46, 47, 48 | fixed 2cb26bc (S12 widened) | raised 43,45,46,47,48 |  | gap |
| T40 | S12 records may not exist | 46 | fixed 2cb26bc |  |  | gap |
| T41 | S19 doesn't rule out a covering agreement | 47, 48 | fixed 2cb26bc | raised 47,48 |  | gap |
| T42 | 'Asked only then' after code starts vs 'anything unsettled is put to the user' | 44, 48 | fixed 2cb26bc (R17 wording) | raised 44,48; family returns as T62/T66 |  | gap |
| T43 | S16: that the review checked a correct fact is only visible in its own trace | 49, 50, 51 | fixed c7d8cc4 (D48) + a81dcfe | raised 49,50,51 (all 3 runs) |  | gap |
| T44 | For instructions, no check the reading choice comes after the playback | 51 | fixed a81dcfe (S15) |  |  | gap |
| T45 | R3 'anything ambiguous asked now' vs R12 'later level answered later' | 53 | fixed 03a00aa (R3 scoped) | 53 only; 52,54 clean | 53: a52ab6f (D50 made absolute terms findings) | gap |
| T46 | S10 'marked as found' vs R10 'marked as the work's' | 53 | fixed 03a00aa |  |  | gap |
| T47 | S15 not limited to what the level decides | 55, 56, 57 | fixed 2f2d6d8 | 55,56,57 (all 3 runs) | 03a00aa (my R3 scoping) | gap |
| T48 | R3 plain answer without playback vs R4 document after playback | 56 | fixed 2f2d6d8 then 22b52d3/363af74 | 56 |  | gap |
| T49 | S18 checks a citation, not the decision | 57 | fixed 2f2d6d8 | 57 |  | gap |
| T50 | R3 'needs no playback of its own' allows a playback S15 fails | 61 | fixed 363af74 (FF-14 wording restored) | 61 | 22b52d3 (my R3 wording) | gap |
| T51 | S10/R7 ask now what R12 defers | 62 | fixed 9fa0d81 (scope to the level) | 62 | 03a00aa (added 'any/anything' to the absolute terms) | gap |
| T52 | S11 relies on the work producing a passed level | 64, 66 | fixed 4dbd3de | 64,66 (2 of 3 runs; 65 clean) |  | gap |
| T53 | R7 'anything missing is asked' vs R12/R15/R10 | 67 | my rewording 45c5bdd reverted; fixed 68ad628 (FF-44 A) | 67 | 03a00aa (absolute 'anything') | gap |
| T54 | S18 doesn't say the decision stays the work's | 68 | fixed e72a1d0 | 68 | 9fa0d81 (my S18 second case) | gap |
| T55 | R7 'nothing left to ask you' vs R12 | 70 | fixed 5deb96f | 70 | 68ad628 (scoping only the last sentence) | gap |
| T56 | S14/S17 'not asked to approve while…' — no requirement forbids asking early | 71 | fixed c144812 (R2 FF-4 + 'allows' defined) | 71; dropped in ~8 runs before |  | open |
| T57 | S18 case 2 expects a preset choice R14 doesn't force | 72 | fixed 8741933 | 72 | 9fa0d81 (my S18 second case) | gap |
| T58 | S17 checks the review's own report | 74 | fixed c74f108 | 74 |  | gap |
| T59 | Gate scenarios only check the next document | 75 | fixed 6a08a16 | 75 |  | gap |
| T60 | S15 'only after you confirm' catches the plain answer | 77, 78 | fixed 91babdc | 77,78 (2 of 3; 76 clean) | c144812 (the 'allows' rule made it a finding) | gap |
| T61 | R15 sends the work's decisions to the user | 82 | fixed 4bc74af | 82 | not caused by a fix (see T26) | gap |
| T62 | R37 'everything it needs' vs R38 | 83 | fixed 757428e | 83 | 3948a73 (my split of one bullet into R37/R38) | gap |
| T63 | S23 'treated as complete' is the work's own state | 83 | fixed 757428e | 83; dropped as later-level in ~22 runs (44-82) |  | open |
| T64 | S17 passes a run that never checks and stalls | 84 | fixed e763ee9 | 84 | c74f108 (my S17 change removed the report clause) | gap |
| T65 | S4 relies on the work producing the second feature's level | 84 | fixed e763ee9 | 84; S4's setup dropped in ~40 runs | 3948a73 (my rewrite reordered S4's sentence) | gap |
| T66 | R2 'decisions before code starts' vs R38 | 85 | fixed 6e9d907, then reverted 6e82d4d after D58 (not a finding) | 85; dropped as 'no absolute term' in many runs |  | open |
| T67 | S1 fails what R2's new exception allows | 86 | fixed ea5e697, reverted 6e82d4d | 86 | 6e9d907 (my R2 carve-out) | gap |
| T68 | R8: which playback for an ambiguous plain answer | 87 | fixed 3b17c96 | 87; dropped in ~3 runs (83,84,86) |  | open |
| T69 | Is a project term a found fact | 87 | decided D59 (FF-49 A), glossary | 87; dropped in 83,84 |  | open |
| T70 | Pass bars require completeness no requirement asks for | 87 | fixed 3b17c96 (R40) | 87 | 3948a73 (my rewrite moved the completeness sentence to the glossary) | gap |

## Topics raised in some runs and dropped in others (keyword match over dropped items, approximate)

| Topic | Runs that dropped it |
|---|---|
| plain answer / which playback (R3,R4,R7,R8) | 22: 19, 20, 21, 30, 32, 33, 34, 43, 44, 47, 50, 57, 65, 67, 72, 74, 76, 80, 81, 83, 84, 86 |
| review reports defect / review own report (S14,S16,S17) | 26: 9, 13, 15, 16, 17, 20, 26, 27, 28, 29, 31, 33, 52, 54, 55, 56, 57, 62, 63, 65, 66, 67, 68, 70, 71, 72 |
| asking after code starts (R2/R17/R38, S5,S6,S7) | 56: 1, 2, 3, 5, 7, 10, 13, 14, 16, 19, 25, 26, 27, 29, 31, 32, 33, 34, 35, 36, 41, 42, 44, 46, 49, 50, 51, 52, 53, 54, 55, 56, 57, 61, 62, 63, 64, 66, 67, 68, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87 |
| treated as complete (S23) | 23: 44, 51, 52, 54, 56, 57, 61, 62, 63, 64, 66, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82 |
| S4 second feature setup | 43: 1, 5, 8, 9, 10, 11, 13, 14, 15, 19, 20, 25, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 40, 47, 50, 51, 52, 53, 54, 55, 56, 57, 61, 63, 64, 65, 67, 68, 72, 74, 77, 80, 81 |
| S15 only after confirm / plain answer | 9: 38, 46, 47, 51, 55, 71, 74, 75, 76 |
| asked to approve early (S14,S17) | 10: 62, 67, 68, 70, 75, 76, 78, 79, 80, 81 |
| work's decisions asked (C6/R15, S1, M14) | 28: 5, 16, 18, 21, 28, 32, 34, 35, 38, 42, 43, 44, 45, 46, 49, 50, 52, 53, 54, 57, 64, 77, 78, 83, 84, 85, 86, 87 |
| project terms vs found facts (R20,R22,S21) | 13: 36, 48, 53, 54, 62, 67, 72, 79, 80, 82, 83, 84, 87 |
| preamble: run count / scripted user / tests fail before | 73: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 61, 62, 63, 64, 65, 66, 68, 70, 71, 72, 75, 76, 77, 78, 80, 81, 82, 85, 86, 87 |
| decision classification link (where anything lives) | 53: 1, 2, 3, 6, 7, 8, 9, 10, 12, 15, 16, 17, 21, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 62, 65, 66, 67, 74, 80, 81, 82, 83, 84, 86, 87 |
| R14/R16 scope vs carry over | 39: 17, 18, 19, 20, 21, 25, 27, 28, 29, 30, 31, 34, 35, 36, 38, 40, 43, 46, 47, 48, 49, 50, 51, 52, 57, 61, 62, 63, 65, 66, 71, 72, 74, 76, 78, 79, 81, 82, 86 |
| Build as a level / exactly one document | 26: 19, 26, 27, 31, 32, 42, 43, 47, 48, 49, 50, 52, 53, 54, 57, 63, 64, 67, 71, 74, 75, 76, 80, 81, 82, 87 |
| readability rules / readable at a glance undefined | 51: 1, 2, 3, 5, 6, 7, 8, 9, 11, 13, 15, 16, 17, 18, 19, 20, 21, 25, 26, 27, 28, 29, 30, 31, 32, 33, 36, 37, 39, 41, 42, 43, 44, 45, 46, 48, 49, 51, 57, 62, 63, 64, 65, 68, 71, 76, 78, 82, 83, 84, 87 |

## Appendix A: every dropped item

| Run | Commit | Crit | Items | Quote | Why dropped (report's reason, summarised) | Relies on |
|---|---|---|---|---|---|---|
| 1 | 4605655 | 2 | preamble | Each runs on a sample project with a scripted user | States the check's kind and starting state, not how tests are built; not extra. |  |
| 1 | 4605655 | 6 | definitions 'Code starts'; 'A level is approved' | A level is approved when you say so | Definitions needed for the claims to be clear; criterion 6 treats definitions as part of the document. |  |
| 1 | 4605655 |  | decision classification link | decision classification | A definition by reference; doesn't change what the user gets. |  |
| 1 | 4605655 |  | S7 | existing code that nothing you agreed decided conflicts with one of your decisions | Wording only; the meaning is determinable. |  |
| 1 | 4605655 |  | S8; C7 | before any level document is written | Which level the ambiguity belongs to is scenario scripting; the text shows no later-level ambiguity. |  |
| 1 | 4605655 |  | C2a; C11b | decisions are made before code starts | C11b is an explicit exception and S1 lets all decisions be drawn out first, so no contradiction shown. |  |
| 1 | 4605655 |  | S4 | except for clarity | Clarity allowance carried into the check, conflict ruled out; telling clarity from re-ask is test construction. |  |
| 1 | 4605655 |  | S5; C8a | Nothing is asked after code starts | Clarity allowance ruled out by unambiguous description and user holding all decisions. |  |
| 1 | 4605655 |  | S6 |  | A decision the feature needs blocks; text shows nothing otherwise. |  |
| 1 | 4605655 |  | C3c; S8 | Anything that could be read more than one way | A scenario need not cover every instance of the claim. |  |
| 1 | 4605655 |  | M7 | Approved levels later changed because the work read you wrong | Traces to C3b/C3c/C6a; it checks a claim. |  |
| 1 | 4605655 |  | C5 | Readable at a glance | Lack of definition is left to a later level. |  |
| 1 | 4605655 |  | S13 | a point the work must settle | Which side a point falls on is set by the classification at a later level. |  |
| 1 | 4605655 |  | S1; preamble | the code has passing tests | The check also requires acceptance tests to pass, and the preamble rules out relying only on the work's tests. |  |
| 2 | 4605655 | 2 | preamble | sample project with a scripted user | Supplies the required automated check and pass bar; construction is left to a later level. |  |
| 2 | 4605655 | 2 | decision classification link | set by the decision classification | Defers a definition, which is allowed; not a statement of where parts live. |  |
| 2 | 4605655 |  | S12; M3 | the framework's readability rules | A definition left to a later level; built faithfully it is fixed before the run. |  |
| 2 | 4605655 |  | S1; S12 |  | The work editing the classification or readability rules to pass is a way to game a check, not shown by the text. |  |
| 2 | 4605655 | 3 | C9b | This holds wherever a decision is written | A reader knows the result: both kinds of decision keep their owner wherever written. |  |
| 2 | 4605655 | 6 | C8a; C11b | and only then | C11b narrows C8a after code starts; not a contradiction. |  |
| 2 | 4605655 |  | M5 | Levels started | Missing definition left to a later level; S3 checks the result. |  |
| 2 | 4605655 |  | C3c; S8; S1; M8 | Anything that could be read more than one way | A picked reading of a later ambiguous answer would fail S1 and count against M8, so no gap shown. |  |
| 2 | 4605655 |  | S1 | the code has passing tests | Paired with acceptance tests, and the paragraph rules out relying only on the work's tests. |  |
| 2 | 4605655 |  | S6 | one of your decisions | In context of S5 it implies a needed decision. |  |
| 2 | 4605655 |  | S3 | as its script says | Scripted user asking a question is covered by the script wording. |  |
| 2 | 4605655 |  | S7 | existing code that nothing you agreed decided conflicts with one of your decisions in them | Parseable; wording only. |  |
| 3 | 4605655 | 2 | preamble | Acceptance tests fail before the work and pass after it | States check kind and pass bar the definition requires, not how a scenario is scripted. |  |
| 3 | 4605655 | 2 | decision classification link | decision classification | Delegates a definition to a later level and doesn't change what you get. |  |
| 3 | 4605655 | 5 | scenario 12; measure 3 | the framework's readability rules | Built faithfully the rules exist before the run; lax rules would be gaming the text doesn't show. |  |
| 3 | 4605655 | 4 | C2b | Work moves to the next level only when the current one passes its review | Approval definition includes passing review, so scenarios 3 and 11 cover it. |  |
| 3 | 4605655 | 4 | C3c; scenario 8 | Anything that could be read more than one way is put to you as a choice | One scenario covers the claim; which level exercises it is scripting. |  |
| 3 | 4605655 | 5 | measure 5; scenario 3 | Levels started before you approved | Scenario 3's no-early-question check covers an early start; nothing contradicts. |  |
| 3 | 4605655 | 5 | scenario 3 | the work asks no question before its level | The clarity allowance concerns things already agreed; the check isn't shown counting against it. |  |
| 3 | 4605655 | 1/5 | scenario 13 | no statement in it can be read two ways | Every check is stated automated; how it's built is a later level. |  |
| 3 | 4605655 | 5 | measure 7 | Approved levels later changed because the work read you wrong | How a measure is taken belongs to a later level. |  |
| 3 | 4605655 | 5 | scenario 1 | the code has passing tests | Paired with acceptance tests; the section rules out relying only on the work's tests. |  |
| 3 | 4605655 | 6 | scenario 7; C11b | If one of your decisions still blocks it, you're asked, and only then | A conflict with your decision reads as that decision blocking; no contradiction. |  |
| 3 | 4605655 | 3 | scenario 2 | It surfaces | Starting state fixes the result; wording doesn't change what you get. |  |
| 4 | e4a4d92 |  | C2b; S3; S11 | passes its review | Approval is defined as after passing review, so S3/S11 cover moving on without review. |  |
| 4 | e4a4d92 | 2 | decision classification reference | set by the decision classification | A pointer to an existing definition, not where the feature lives or a new definition. |  |
| 4 | e4a4d92 | 2 | preamble | no check relies only on tests written by the work being judged | States properties criterion 5 requires, not how tests are built. |  |
| 4 | e4a4d92 |  | S7; C9b; S1 | You're asked about the conflict | Whose decision resolves the conflict depends on the external classification; no conflict shown. |  |
| 4 | e4a4d92 |  | S10; C6a | both are in its document | C6a treats a found fact as document content; not shown to fail allowed behaviour. |  |
| 4 | e4a4d92 |  | S13 | something agreed | Agreed is defined and approvals scripted; a badly built check isn't shown. |  |
| 4 | e4a4d92 |  | S11 | A level passes its review | Levels come with the scenario per the header; not shown. |  |
| 4 | e4a4d92 |  | S13 | no statement ... can be read two ways | Check construction belongs to a later level; the header says checks are automated. |  |
| 4 | e4a4d92 |  | C3c; C4; M9 |  | Which reading of your own words is meant is your decision; no contradiction. |  |
| 4 | e4a4d92 |  | S6; S7; C2a; C11b | decisions are made before code starts | Supplied states exercise C11b's fallback; no contradiction. |  |
| 4 | e4a4d92 |  | M5; S3; S11 | Levels started | S3's no-early-question check fails an early next-level interview; no gap. |  |
| 4 | e4a4d92 |  | S7 | existing code that nothing you agreed decided conflicts with one of your decisions in them | Wording only; doesn't change what the user gets. |  |
| 4 | e4a4d92 |  | M7 |  | Traces to C3b/C3c/C6b as their measured effect; no finding. |  |
| 5 | e4a4d92 | 2 | decision classification pointer | set by the decision classification | A pointer to an existing definition, not a design decision or location. |  |
| 5 | e4a4d92 | 2 | definitions 'Code starts'; 'A level is approved' | Code starts means the first change to the project's code or tests | Definitions needed for clarity; the definition allows definitions. |  |
| 5 | e4a4d92 | 2 | preamble | no check relies only on tests written by the work being judged | States properties criterion 5 demands, not how tests are built. |  |
| 5 | e4a4d92 | 4 | C2; S3; S11 | passes its review | Scripted user approves only after review passes, so S3/S11 ordering checks fail a skipped review. |  |
| 5 | e4a4d92 | 4 | C3; S9 | the level's document | S9 doesn't restrict which level; how many levels are inspected is check construction. |  |
| 5 | e4a4d92 | 5 | S10; C6 | the fact marked as the work's | C6 gives a found fact as the example of the work's marked content; not shown. |  |
| 5 | e4a4d92 | 5 | S7 | You're asked about the conflict | Whether the conflict is the user's decision is set by the external classification. |  |
| 5 | e4a4d92 | 6 | C8; C11; S5 | except for clarity | A clarity question after code starts is a still-blocking decision; reconcilable, and S5 rules it out. |  |
| 5 | e4a4d92 | 6 | C2; S6; C11 | one of your decisions left unmade | C11's 'still blocks' frames this as the handled exception. |  |
| 5 | e4a4d92 | 4 | M5; S3 | Levels started | S3's in-order check covers starting the next level early. |  |
| 5 | e4a4d92 | 4 | M7 | Approved levels later changed because the work read you wrong | Measures misreadings surviving playback and confirmation; traces loosely. |  |
| 5 | e4a4d92 | 5 | S3; C3; C8 | the work asks no question before its level | Such questions belong to the current level; not shown. |  |
| 5 | e4a4d92 | 3 | S7; S4 | follows all three | Awkward wording but readable; doesn't change what the user gets. |  |
| 6 | e4a4d92 | 2 | preamble | Every check is automated: acceptance tests, transcript analysis or an LLM judge | Names check kinds and a required property; doesn't state how tests are built. |  |
| 6 | e4a4d92 | 2 | decision classification link | set by the decision classification | A pointer to a definition, not where feature work lives. |  |
| 6 | e4a4d92 | 3 | C5; S12 | readable at a glance | Threshold left to readability rules coming with S12; a later-level definition. |  |
| 6 | e4a4d92 |  | S1 | the code has passing tests | Trivial tests would be gaming a check, not shown, and acceptance tests also apply. |  |
| 6 | e4a4d92 |  | S3 |  | Relying on the review passing honestly is a badly built or gamed check, not shown. |  |
| 6 | e4a4d92 |  | S10 | its fact is never asked | Whether confirming a playback counts as asking is not shown. |  |
| 6 | e4a4d92 | 6 | S6; C2a; C11b | approved with one of your decisions left unmade | C11b explicitly provides for this case; no contradiction. |  |
| 6 | e4a4d92 |  | S13 | a point the work must settle | Either path satisfies the check as written; no misjudgement shown. |  |
| 6 | e4a4d92 |  | M7 | because the work read you wrong | Attribution rule is measure construction, a later level. |  |
| 6 | e4a4d92 | 4 | C3c; S1; S5; S8 | Anything that could be read more than one way | Picking a reading of an ambiguous answer fails S1/S5; S8 covers the explicit case. |  |
| 6 | e4a4d92 | 4/6 | C2b; S3; S11; M5 | moves to the next level | S3's no-early-question check fails an early next-level interview; no gap shown. |  |
| 7 | a36bf1f | 2 | preamble | Every check is automated: acceptance tests, transcript analysis or an LLM judge | Names the kind of check, not how it's built. |  |
| 7 | a36bf1f | 2 | preamble | Acceptance tests fail before the work and pass after it; no check relies only on tests written by the work | States what the check is and that the work can't satisfy it, not test construction. |  |
| 7 | a36bf1f | 2/3 | decision classification link | decision classification | A reference to a definition, not where feature artefacts live; reader still knows the result. |  |
| 7 | a36bf1f | 3 | S12 | the readability rules | Rules come with the scenario; definition belongs to a later level. |  |
| 7 | a36bf1f | 3 | levels |  | Levels not enumerated is a later-level definition; reader knows the result. |  |
| 7 | a36bf1f | 4 | C2b; S3; S11 | passes its review | Approval defined as after review passes; S3/S11 fail if work moves on without approval. |  |
| 7 | a36bf1f | 4 | M7 | Approved levels later changed because the work read you wrong | Measures C3c/C6b. |  |
| 7 | a36bf1f | 5/6 | S7; C11; C8 | and only then | Conflict resolution is the user's blocking decision; S7 checks C11b/C9a. |  |
| 7 | a36bf1f | 5 | S5 | nothing conflicts with them | 'Them' reads as the levels, ruling the exception out; no misjudging check shown. |  |
| 7 | a36bf1f | 5 | S6 | one of your decisions left unmade | Code must follow the answer, so it depends on it and blocks. |  |
| 7 | a36bf1f | 5 | S10; C8; C4 | its fact is never asked | Clarity allowance covers agreed or codified things; a project fact is neither. |  |
| 7 | a36bf1f | 5 | S13; S1; S10 |  | Marking user decisions as the work's is gaming; S1/S10 cover it. |  |
| 7 | a36bf1f | 5 | S3 | the work asks no question before its level | Possible vacuity is scenario scripting, not shown. |  |
| 7 | a36bf1f | 5 | S11 | A level passes its review | Check is about timing; scenario fails if work never produces a passing level. |  |
| 7 | a36bf1f | 5 | M5 | Levels started | Matches C2 wording; doesn't misjudge the result. |  |
| 7 | a36bf1f | 2 | C3b | played back, in the work's own words | Stated as an observable result, not a design decision. |  |
| 7 | a36bf1f |  | S5; S7 | existing code that nothing you agreed decided conflicts with | Wording and style only. |  |
| 7 | a36bf1f | 4 | C3c; S8 | put to you as a choice | Form of the question doesn't change what the user gets. |  |
| 8 | a36bf1f | 2 | definitions 'Code starts'; 'A level is approved' | A level is approved when you say so | Definitions aren't excluded and removing them changes no result. |  |
| 8 | a36bf1f | 2 | preamble | Every check is automated: acceptance tests, transcript analysis or an LLM judge | Names check kind, pass bar and inputs, not how scenarios are scripted. |  |
| 8 | a36bf1f | 2/3 | decision classification link |  | A pointer to a later-level definition; reader still knows the result. |  |
| 8 | a36bf1f | 3/5 | C5; S12 | readable at a glance | What counts as readable is a later-level definition; rules come with the scenario. |  |
| 8 | a36bf1f | 5 | S3 | the work asks no question before its level | No allowed question the check would fail is shown. |  |
| 8 | a36bf1f | 5 | S6 | one of your decisions left unmade | Code must follow the answer, so it's a dependency; no non-blocking case shown. |  |
| 8 | a36bf1f | 5 | S1 | the code has passing tests | Gaming a check; acceptance tests that come with the scenario also required. |  |
| 8 | a36bf1f |  | S13; M3 |  | How a check is built belongs to a later level. |  |
| 8 | a36bf1f | 5/6 | S4; C3 |  | Double-asking through later playbacks not shown; C3 scopes playback to the level. |  |
| 8 | a36bf1f |  | S10; C3c | its fact is never asked | The starting state doesn't set an ambiguous fact; not shown. |  |
| 9 | a36bf1f |  | S7; C11 | existing code that nothing you agreed decided conflicts with one of your decisions | Whether the conflict blocks depends on the external classification; no mismatch shown. |  |
| 9 | a36bf1f |  | S5 | nothing conflicts with them | 'Them' reads as the levels, ruling out the conflict exception; wording only. |  |
| 9 | a36bf1f |  | S6; C11 | one of your decisions left unmade | Being one of your decisions implies it blocks; not shown failing allowed behaviour. |  |
| 9 | a36bf1f |  | S10 | both are in its document | A fact the level needs implies inclusion; not shown counting against allowed behaviour. |  |
| 9 | a36bf1f |  | preamble | no check relies only on tests written by the work | Borders on test construction but states pass bar and independence; wording only. |  |
| 9 | a36bf1f |  | decision classification link | skills/references/decisions.md | A pointer to a deferred definition, not where anything lives. |  |
| 9 | a36bf1f |  | terms | readable at a glance | Terms needing definitions or rules are left to a later level. |  |
| 9 | a36bf1f |  | S9 | judged by an LLM judge | Which clauses the judge covers is check construction, a later level. |  |
| 9 | a36bf1f |  | S4 | except for clarity | Telling a clarity question from a re-ask is check construction, a later level. |  |
| 9 | a36bf1f |  | C2b; S3 | passes its review | Approval definition and S3's script subsume the review-pass condition; no gap shown. |  |
| 10 | 847802b | 2 | preamble | Acceptance tests fail before the work and pass after it; no check relies only on tests written by the work being judged | Supplies pass bar and criterion 5 properties; doesn't change what the user gets. |  |
| 10 | 847802b | 2 | decision classification link |  | A definition C9/C4 depend on, not an implementation location. |  |
| 10 | 847802b | 5 | S3; C7 | the work asks no question before its level | 'Its' reads as each question's own level, matching C7; not shown. |  |
| 10 | 847802b | 5 | S4 | A codified rule exists | Acceptance tests must fail before the work, so the rule must bear on the feature; not shown. |  |
| 10 | 847802b |  | S2; C4; S10 | you hold | Parallels S10's only-you-hold, so not findable in the project; not shown. |  |
| 10 | 847802b | 6 | S6; S7; C2; C11 | decisions made before code starts | Scenarios set those states and C11 covers them; no contradiction. |  |
| 10 | 847802b |  | S7; C11 | only then | Whether resolution is the user's decision is set by the external classification; not shown. |  |
| 10 | 847802b |  | S8; C3 | asked which reading is meant | 'Which reading' implies readings are offered; not shown. |  |
| 10 | 847802b |  | S9; S4; S13; M7 | read you wrong | How checks tell cases apart belongs to a later level. |  |
| 10 | 847802b |  | M5; S3; S11 | Levels started | A measure broader than its scenarios isn't a contradiction. |  |
| 10 | 847802b |  | S6; S5 |  | Extra questions after code starts are covered by S5; a scenario need not re-check. |  |
| 10 | 847802b |  | C8; C11; S5; M1 | and only then | S5 rules clarity out, M1 carries it, and a blocking clarity question is a blocking decision. |  |
| 10 | 847802b |  | C3; C9 | Anything that could be read more than one way | C3 concerns your intent within the playback; tension not shown. |  |
| 10 | 847802b |  | C8; C10 | Approving a level makes everything in it agreed | 'Agreed' and 'codified' are distinct terms; no contradiction. |  |
| 11 | 847802b | 2 | preamble | Every check is automated: acceptance tests, transcript analysis or an LLM judge | Names check types and pass bar; doesn't say how scenarios are scripted. |  |
| 11 | 847802b | 2/3 | decision classification reference | is set by the decision classification | A definition by reference; reader knows the result. |  |
| 11 | 847802b | 3 | C5; S12 | readable at a glance | Readability rules come with the scenario; left to a later level. |  |
| 11 | 847802b |  | M5; S3; S11 | Levels started before you approved | Measure and scenario checking the same claim at different points isn't a contradiction. |  |
| 11 | 847802b |  | S2; C3a; S10 | It surfaces before code starts | S10 covers the before-document part; no need to re-check. |  |
| 11 | 847802b |  | S6; C11 | You're asked about it | Code following the answer implies a needed decision; blocking is interpretation for later levels. |  |
| 11 | 847802b |  | S7; C8a; C11b |  | Whether the conflict blocks is interpretation the Outcome leaves open. |  |
| 11 | 847802b |  | S4 | A codified rule exists | The acceptance-test check implies the rule applies; rest is check construction. |  |
| 11 | 847802b | 5 | S11; S3 | passes its review | Level comes with the scenario; remaining concern is the same as F1, reported there. | starting state left to the work |
| 11 | 847802b |  | M7; C3b; C6a | Approved levels later changed because the work read you wrong | Checks the result of C3b/C6a, so it traces. |  |
| 11 | 847802b |  | preamble; C3d |  | Correction is a scripted-user capability, not a claim part; no scenario needed. |  |
| 11 | 847802b |  | S13 | no statement in it can be read two ways | How it's judged is check construction; preamble says checks are automated. |  |
| 11 | 847802b | 6 | C2a; C11b; S6 | your decisions are made before code starts | C11 is the stated fallback and S6 starts from supplied levels. |  |
| 12 | 847802b | 2 | preamble | The scripted user answers questions, confirms or corrects playbacks and approves levels as its script says | Shared pass bar naming the actor; doesn't say how scripts are built. |  |
| 12 | 847802b | 2 | preamble | Acceptance tests, any levels a scenario starts from, and the rules a judge applies come with the scenario | States the required check properties, not how tests are built. |  |
| 12 | 847802b | 2/3 | decision classification link | set by the decision classification | A definition by reference; result clear without it. |  |
| 12 | 847802b | 5 | S1; C1 | the code has passing tests | Also requires acceptance tests; preamble forbids relying only on the work's tests. |  |
| 12 | 847802b | 5 | S7; C11b; C8a | You're asked about the conflict | Classification of the conflict is left to a later level; no failing check shown. |  |
| 12 | 847802b | 5 | S9 | nothing in it follows the project's meaning | Scoped to the user's answer term; a badly built check isn't shown. |  |
| 12 | 847802b | 5 | S12; S1; M8 |  | Vacuous pass with no questions doesn't break the claim; decisions covered by S1/M8. |  |
| 12 | 847802b | 6 | C2a; S6; C11b | your decisions are made before code starts | C11b states the exception; no contradiction. |  |
| 12 | 847802b | 6 | C3c; C7; S8 | what that level decides | S8 scopes ambiguity to the level, so both hold. |  |
| 12 | 847802b | 5 | S10 | the fact marked as the work's | User volunteering the fact isn't shown by the text. |  |
| 13 | 9c62834 |  | S7; A11; A9 | You're asked about the conflict | Whose decision the conflict is depends on the external classification; no gap shown. |  |
| 13 | 9c62834 |  | S4 | A codified rule exists | Stated as starting state and nothing says the work creates it; not shown. |  |
| 13 | 9c62834 |  | S14 | review reports no findings | Review output could be gamed, but the premise makes finding the defect given; gaming not shown. |  |
| 13 | 9c62834 |  | S13 | must settle to write a level | Vacuous pass not shown; the point must be settled to write the level. |  |
| 13 | 9c62834 |  | A2; S3; S11; S14; M5 | work moves to the next level | S3 and M5 cover early interviewing; when a level begins is a later-level definition. |  |
| 13 | 9c62834 | 6 | A2; S6; S7; A11 |  | Defective starting states are scripted, so A11's residual case doesn't contradict A2. |  |
| 13 | 9c62834 | 6 | A8b; A10b; A10c |  | 'Agreed' and 'codified' are distinct terms; no contradiction. |  |
| 13 | 9c62834 |  | S5; A8; A11 | Nothing is asked after code starts | Clarity allowance ruled out by starting state; A11 limits post-code questions. |  |
| 13 | 9c62834 | 2 | preamble |  | States pass bar and pre-run set-up criterion 5 needs; wording only. |  |
| 13 | 9c62834 | 2 | decision classification pointer; D1 |  | Definitions by reference are part of the document; not extra. |  |
| 13 | 9c62834 |  | S12; M3 | Readability rules | Rules come with the scenario; definition is a later level. |  |
| 13 | 9c62834 |  | S9 | nothing in it follows the project's meaning | Counting against legitimate use elsewhere is speculative, not shown. |  |
| 13 | 9c62834 | 4 | M7; A3b; A3c; A6 | Approved levels later changed because the work read you wrong | Traces only indirectly but does check a claim. |  |
| 14 | 9c62834 | 2 | preamble | Acceptance tests fail before the work and pass after it; no check relies only on tests written by the work being judged | States pass bar and check properties, not how scenarios are scripted. |  |
| 14 | 9c62834 | 2 | D3 decision classification | Which decisions are yours and which are the work's is set by the decision classification | A definition of a term, not a design or location decision. |  |
| 14 | 9c62834 | 4 | A3c; S8 | one of your answers | The claim doesn't distinguish answer from description; one instance suffices. |  |
| 14 | 9c62834 | 5 | S6; A11 |  | Acceptance tests depend on the answer, so the code needs it; no misjudgment shown. |  |
| 14 | 9c62834 | 5 | S14 | reports no findings before you're asked to approve it | Words presuppose an ask and a report; vacuous-case handling is test construction. |  |
| 14 | 9c62834 | 5 | S9; A6a | nothing in it follows the project's meaning | Scenario doesn't bring about a work-marked project-usage fact; speculative. |  |
| 14 | 9c62834 | 5 | S13; A9b; S1 |  | Asking the user to settle the work's point is covered by S1. |  |
| 14 | 9c62834 | 5 | S4 | except for clarity | Telling clarity from re-ask is check construction. |  |
| 14 | 9c62834 | 6 | A8; A11; S5 | you're asked, and only then | A11 narrows A8 after code starts; S5 rules out the exception. |  |
| 14 | 9c62834 | 3 | S7 | existing code that nothing you agreed decided conflicts with one of your decisions in them | Dense phrasing but the result is clear; wording only. |  |
| 15 | 9c62834 | 2 | preamble | Each runs several times on a sample project with a scripted user ... as its script says | Scenario mechanics and pass bar, not how scenarios are scripted; doesn't change what the user gets. |  |
| 15 | 9c62834 | 2 | decision classification link | skills/references/decisions.md | A pointer to a definition, not where anything in the work lives. |  |
| 15 | 9c62834 | 4 | C3c; S8 | as a choice | Asking which of two readings is meant presents them; question form is wording. |  |
| 15 | 9c62834 | 5 | S1 | the code has passing tests | Conjoined with acceptance tests that come with the scenario. |  |
| 15 | 9c62834 | 5 | S13; C6a; S1; M8 |  | Marking statements as the work's is what C6a allows; misuse caught by S1/M8. |  |
| 15 | 9c62834 | 5 | S14 | The level's review reports no findings | Natural reading requires a report; vacuous pass not shown. |  |
| 15 | 9c62834 | 5 | S4 |  | Scripted answers and the approved level are set by the script, so the starting state is set. |  |
| 15 | 9c62834 | 5 | S13 | against the transcript | Transcript analysis is a declared check kind; how the judge separates cases is test construction. |  |
| 15 | 9c62834 | 6 | C2a; S6; C11b | decisions are made before code starts | C11b states the exception; not a contradiction. |  |
| 15 | 9c62834 | 3/5 | M5 | started | What counts as a level started needs a definition at a later level. |  |
| 15 | 9c62834 | 5 | M4; S14 |  | Whether a post-review fix needs re-confirmed playback needs a later-level definition. |  |
| 15 | 9c62834 | 3 | C5; C8 | readable at a glance | Readability rules come with the scenario; clarity threshold is a later level. |  |
| 16 | dd487b5 | 2 | preamble | Acceptance tests fail before the work and pass after it | Shows checks are automated and set before the run; not extra. |  |
| 16 | dd487b5 | 2 | decision classification link | decision classification | A pointer to a definition; removing it changes nothing. |  |
| 16 | dd487b5 |  | S14 | no findings | Relying on the work's own review is gaming, not shown. |  |
| 16 | dd487b5 |  | S5; C3a | Nothing is asked after code starts | The script fixes what is given; no conflict shown. |  |
| 16 | dd487b5 |  | S12 | readable at a glance | A definition for a later level; rules come with the scenario. |  |
| 16 | dd487b5 |  | S5 | nothing conflicts with them | Wording; doesn't change the result. |  |
| 16 | dd487b5 |  | S10 |  | Fact kind at Behaviour is covered inside F1. |  |
| 16 | dd487b5 | 2 | C8 |  | Per-level fact kinds state observable results in documents; left in. |  |
| 16 | dd487b5 |  | C6; S12 | meant for a person | Wording; not shown to change the result. |  |
| 17 | dd487b5 | 2 | preamble |  | Serves the required automated check and pass bar, not how tests are built. |  |
| 17 | dd487b5 |  | S18 | cite the first | A citation is the observable form of a preferred default in a visible record. |  |
| 17 | dd487b5 |  | S14 |  | Relying on the work's own review is gaming, not shown. |  |
| 17 | dd487b5 |  | decision classification link | is set by the decision classification | A definition by reference; what counts as yours is a later level. |  |
| 17 | dd487b5 |  | S7 | existing code that nothing you agreed decided conflicts with | Wording; doesn't change what the user gets. |  |
| 17 | dd487b5 |  | S9 | nothing in it follows the project's meaning | Counting against a Behaviour found fact is not shown. |  |
| 17 | dd487b5 |  | terms | readable at a glance | Undefined terms needing definitions belong to a later level. |  |
| 17 | dd487b5 | 6 | C2a; C14b; S6 | decisions are made before code starts | A stated exception for an abnormal starting state; not a contradiction. |  |
| 17 | dd487b5 | 6 | C11a; C13b | A decision holds only within its stated scope | Resolved by the 'unless an agreement ... covers the case' clause; interpretation left to later levels. |  |
| 17 | dd487b5 | 2 | C3c | on its own, after the playback | A result the user observes, not procedure detail. |  |
| 18 | dd487b5 | 2 | preamble; S12; S13 | judged by an LLM judge | Reads as test construction but doesn't change what the user gets and states criterion 5 needs; wording. |  |
| 18 | dd487b5 | 2 | decision classification pointer | set by the decision classification | A definition reference; changes nothing the user gets; wording. |  |
| 18 | dd487b5 |  | S13; S1; S10; C12 |  | Work marking your decision as its own is covered by S1 and S10. |  |
| 18 | dd487b5 |  | S15; S8; C3c | on its own | S8 covers the choice-on-its-own part of C3c. |  |
| 18 | dd487b5 |  | S12; M3 | readability rules | Judge rules belong to a later level. |  |
| 18 | dd487b5 | 6 | S6; C2a; C14b |  | A scenario sets its own starting state and C14b provides for it; not a contradiction. |  |
| 18 | dd487b5 |  | S3; C2 | code starts only after you approve every level | Follows from C2; not a finding. |  |
| 18 | dd487b5 | 3 | terms | readable at a glance | Interpretive terms are narrowed by later levels; not findings. |  |
| 18 | dd487b5 | 4 | C10c; S18 | The work's decisions in it stay the work's | S18's check plausibly fails if the decision had become agreed; not clearly shown. |  |
| 18 | dd487b5 | 6 | C11; C13; C10b | A decision holds only within its stated scope | Resolved by C10b and C11's 'unless' clause; no contradiction. |  |
| 19 | b563f13 | 2 | preamble | Acceptance tests fail before the work and pass after it | Names check kind, pass bar and independence the definition requires; doesn't change what the user gets. |  |
| 19 | b563f13 |  | decision classification pointer |  | A definition left to a later level; result clear without it. |  |
| 19 | b563f13 |  | terms | readable at a glance | What exactly counts as X belongs to a later level. |  |
| 19 | b563f13 | 5 | scenario 12 | each question gives you enough to answer it | Rules come with the scenario; misjudging sufficiency not shown. |  |
| 19 | b563f13 | 5 | scenario 18 | cite the first as its preferred default | Recording the default is within the room the Outcome leaves. |  |
| 19 | b563f13 | 5 | scenario 16; C8 | Slices holds the second | The 'feature needs all three' starting state lets a faithful build make Slices need it. |  |
| 19 | b563f13 | 4 | measure (approved levels changed) | Approved levels later changed because the work read you wrong | Checks the playback and ambiguity claims C3, C4, C7b. |  |
| 19 | b563f13 | 5/6 | C3b; scenario 10; C4 | acted on without a playback | Consistent reading exists: no per-answer playback, level playback still precedes the document. |  |
| 19 | b563f13 | 6 | C2; C14b; scenarios 5, 6 | your decisions are made before code starts | Stated as the exception; scenarios 5 and 6 separate the cases. |  |
| 19 | b563f13 | 6 | C11; C13b; scenario 4 | Agreements carry over to later features | Reconcilable as carrying over within scope; scenario 4 sets applicable answers. |  |
| 19 | b563f13 | 6 | C14b; scenario 7 | and only then | A conflict with your decision is a decision blocking the work. |  |
| 19 | b563f13 | 4 | C2; scenarios 3, 11, 14 | moves to the next level | Scenario 3's no-early-question check covers the next level's interview. |  |
| 19 | b563f13 | 2 | C8a |  | Per-level allowances state what the user observes; no change to what they get. |  |
| 20 | b563f13 |  | S6; C14; C12 | one of your decisions left unmade | The work can't make your decisions, so an unmade one blocks by definition. |  |
| 20 | b563f13 |  | S14 | reports no findings before you're asked to approve it | Natural reading is the review state at the ask; wording only. |  |
| 20 | b563f13 |  | preamble | no check relies only on tests written by the work being judged | Establishes no person needed and work can't satisfy checks, as required. |  |
| 20 | b563f13 |  | decision classification reference |  | A definition counted as part of the Outcome; correctness not judged here. |  |
| 20 | b563f13 |  | terms | readable at a glance | What exactly counts is a later level; the result is clear. |  |
| 20 | b563f13 |  | S9; C3; S8 |  | S9 doesn't forbid putting the term as a choice, and S8 checks it. |  |
| 20 | b563f13 |  | S13; S3 | asks no question before its level | How a check tells cases apart is test construction. |  |
| 20 | b563f13 |  | S17 |  | The scenario sets its own starting state; the check is unaffected. |  |
| 20 | b563f13 |  | S7; C14 |  | Whether resolving the conflict is your decision is set by the classification; not shown. |  |
| 20 | b563f13 |  | C3; S15; S9 | in its own words | S9 checks 'words other than yours'; a scenario need not re-check. |  |
| 20 | b563f13 |  | C8 |  | Per-level fact rule states results observable in each document. |  |
| 20 | b563f13 |  | C11; C13; S4 | holds only within its stated scope | Reconciled by the 'unless' clause and S4's applicable answers. |  |
| 20 | b563f13 | 6 | C3; C4; S10 |  | Reconcilable as per-answer vs per-level playback; the defect is S10's check wording (F1). |  |
| 21 | b563f13 | 2 | preamble | no check relies only on tests written by the work being judged | States pass bar and required check properties, not how scenarios are scripted. |  |
| 21 | b563f13 | 2 | S9; S12; S13 | judged by an LLM judge | Names the check kind, not how it's built. |  |
| 21 | b563f13 | 2/3 | decision classification link | decision classification | A pointer to the rule; removing it changes nothing the user gets. |  |
| 21 | b563f13 | 1/3 | S12; M3 | readable at a glance | A later-level definition; rules come with the scenario. |  |
| 21 | b563f13 | 3 | term | plain answer | What counts as plain is a later-level definition. |  |
| 21 | b563f13 | 3 | scenarios preamble; S11 | several turns | Thresholds belong to a later level. |  |
| 21 | b563f13 | 5 | S6; A14 | one of your decisions left unmade | Acceptance tests tie the decision to the code, so it's one the code needs. |  |
| 21 | b563f13 | 4 | claim (scope); A13 | A decision holds only within its stated scope | No claim says code follows the work's decisions, so nothing to trace. |  |
| 21 | b563f13 | 4 | M10; A3; A4; A7 | Approved levels later changed because the work read you wrong | Measures the result A3, A4 and A7 secure. |  |
| 21 | b563f13 | 2 | A8; S16 |  | Placement rules are user-observable results, each with a scenario. |  |
| 21 | b563f13 | 6 | A3b; A4 |  | Readable as consistent; the check-level consequence is F2. |  |
| 25 | 39a0f70 |  | C4; S1; S10; S20 | you're interviewed about what that level needs | No scenario names an interview, but S1, S10, S20 fail if level needs are not asked; no gap shown. |  |
| 25 | 39a0f70 |  | C8; S12 | Every document and message you're sent | Level documents are presented for approval, so 'sent' reads as covering them; not shown. |  |
| 25 | 39a0f70 |  | S14 | reports no findings before you're asked to approve it | Starting state makes 'no findings at the time you're asked' the faithful reading; not shown. |  |
| 25 | 39a0f70 |  | S3 | the work asks no question before its level | 'Its' reads as the question's own level; wording only. |  |
| 25 | 39a0f70 |  | decision classification link |  | Link to the decision classification is a pointer to a definition, not something changing what the user gets. |  |
| 25 | 39a0f70 |  | Scenarios preamble |  | Preamble sets starting state and check independence, not how tests are built. |  |
| 25 | 39a0f70 |  | S10; C3; S15 | you're asked nothing | The document distinguishes playback from a question (S15), so a playback is not asking. |  |
| 25 | 39a0f70 |  | C17; S7; C13 | only then | C13's conflict exception and a conflict that blocks the work read consistently with S7 asking. |  |
| 25 | 39a0f70 |  | S12 | each question gives you enough to answer it, judged by an LLM judge against the readability rules | Whether readability rules cover sufficiency is how the check is built. |  |
| 25 | 39a0f70 |  | C16; C14; S4; S19 | Agreements carry over to later features | Carry-over within scope reads consistently with scope limits; S4 and S19 agree. |  |
| 25 | 39a0f70 |  | C8; C13; C17 | readable at a glance | Thresholds and definitions for 'readable at a glance', 'for clarity', 'blocks' belong to a later level. |  |
| 25 | 39a0f70 |  | S6; S7; C2; C17 |  | S6/S7 starting states with unmade decision or conflict exercise C17's exception, not a contradiction with C2. |  |
| 25 | 39a0f70 |  | S1 | the code has passing tests | Possibly satisfied by the work's own tests, but the preamble pairs it with scenario acceptance tests; not shown. |  |
| 26 | 39a0f70 |  | A2b; S11 | one is written after | Counting 'one' document is wording that doesn't change what the user gets. |  |
| 26 | 39a0f70 |  | A7b; S10 |  | S10 leaves exactly one thing missing, so once supplied verification is complete; more is how the check is built. |  |
| 26 | 39a0f70 |  | Scenarios preamble | Every check is automated: acceptance tests, transcript analysis or an LLM judge | Preamble states checks are automated and set by the scenario, as criterion 5 requires, not how scenarios are scripted. | criterion 2 'how tests are built' |
| 26 | 39a0f70 |  | A7 bullet 7 definitions |  | Definitions of complete requirement and verification state observable results, not thresholds or procedures. | criterion 2 |
| 26 | 39a0f70 |  | decision classification link |  | Names what sets a term's meaning, not where the feature's output lives. | criterion 2 'where anything lives' |
| 26 | 39a0f70 |  | S10; A10a | completed with what the work found, marked as found | Scenario does not fix the level, and a faithful build picks one allowing found facts. |  |
| 26 | 39a0f70 |  | S16 | no level that doesn't allow found facts holds it | Whether the fact tempts an earlier level is how the test is built; check observes every level. | criterion 5, second bullet |
| 26 | 39a0f70 |  | A13a; A17b | you're asked, and only then | No quoted text shows a case that is both a clarity question and not a blocking decision. | criterion 6 |
| 26 | 39a0f70 |  | S18; A14b | cites the first as its preferred default | Citing is how the default is observable; claim does not allow an uncited default. | criterion 5, third bullet |
| 26 | 39a0f70 |  | S3; A12; A4a | the work asks no question before its level | A12 and A4a cover questions belonging to a level. |  |
| 26 | 39a0f70 |  | S12; decision classification | readability rules | Rules a judge applies come with the scenario and definitions belong to a later level. | criterion 3 |
| 26 | 39a0f70 |  | S14 |  | Not checking the defect was fixed rather than review silenced is a badly built check, not shown by the text. |  |
| 26 | 39a0f70 |  | S5; A7c | Nothing is asked after code starts | Starting state says levels hold all your decisions, so no text shows the conflicting case. |  |
| 27 | 39a0f70 |  | C2; S3; S11 | Each level produces one document | No check counts documents per level, but the count doesn't change what the user gets. |  |
| 27 | 39a0f70 |  | decision classification link | Which decisions are yours and which are the work's is set by the | A pointer resolving a term the claims use, not something extra. |  |
| 27 | 39a0f70 |  | Scenarios preamble; S12; S13; S15 | acceptance tests, transcript analysis or an LLM judge | States checks are automated and preset as criteria require; how they are built is a later level. |  |
| 27 | 39a0f70 |  | C7; definitions paragraph | A requirement is complete when | Definitions of terms the claims use serve clarity, not extra behaviour rules. |  |
| 27 | 39a0f70 |  | C14 | A decision holds only within its stated scope | When a scope ends for a decision with none stated is a rule for a later level. |  |
| 27 | 39a0f70 |  | C8; C13; S12; M4 | codified | Undefined 'codified' and 'readability rules' are later-level definitions; the reader knows the result. |  |
| 27 | 39a0f70 |  | S7; C17 | you're asked, and only then | Whether such a conflict blocks is set by the decision classification; text doesn't show a wrong check. |  |
| 27 | 39a0f70 |  | S14 | The level's review reports no findings before you're asked to approve it | The document defines passing review no other way; no contradiction shown. |  |
| 27 | 39a0f70 |  | S18; C14 | cites the first as its preferred default | Citing is how the default is observable in the record. |  |
| 27 | 39a0f70 |  | S16 | no level that doesn't allow found facts holds it | What the scripted user says is how the scenario is scripted, a later level. |  |
| 27 | 39a0f70 |  | S15; C3 | in words other than yours | Wording difference from 'in its own words' doesn't change the result. |  |
| 27 | 39a0f70 |  | S12 | judged by an LLM judge against the readability rules | Whether the rules cover sufficiency is how the judge is built. |  |
| 27 | 39a0f70 |  | S5; C13 | Nothing is asked after code starts | Clarity exception ruled out by 'each can be read only one way'. |  |
| 27 | 39a0f70 |  | S6; C17; S5 | only then | S6 not checking you're asked only when blocked is covered by S5. |  |
| 27 | 39a0f70 |  | C4; S1; S5; S20 | you're interviewed | No scenario names an interview, but S1, S5, S20 fail if decisions aren't drawn out first. |  |
| 28 | 877b935 |  | C3; C11; S9 | put to you as a choice, on its own, after the playback | Clash named in playback vs separate choice message is form; user gets same result either way. |  |
| 28 | 877b935 |  | C13; C14; C16; S1; S4 | codified | Undefined 'codified' is a later-level definition and is used consistently. |  |
| 28 | 877b935 |  | C7; S10 | A verification is complete when it names what is checked, how, and what result passes | S10's 'completed' takes meaning from this definition; how the check tells completeness is test construction. |  |
| 28 | 877b935 |  | definitions paragraph |  | Definitions make claims readable and state observable results; not shown as extra. |  |
| 28 | 877b935 |  | S12; C8; M4 | Every document and message you're sent | Level documents are presented for approval, so 'sent' covers them; wording only. |  |
| 28 | 877b935 |  | S14 | The level's review reports no findings at the time you're asked to approve it | A review reporting nothing would be gaming the check, which the text does not show. |  |
| 28 | 877b935 |  | S1; C6; C15 | you're asked to make none of the work's decisions | The residual clause does not cover the work's own decisions; telling them apart is test construction. |  |
| 28 | 877b935 |  | C2; S6; C17 | your decisions are made before code starts | C17 'still blocks' states the residual case; S6 starts from a given state. |  |
| 28 | 877b935 |  | C16; C14; S4; S19 | Agreements carry over to later features | Read together agreements carry over within scope; no contradiction shown. |  |
| 28 | 877b935 |  | M2 |  | What the work does needing a findable fact at a level not allowing found facts is a later-level rule. |  |
| 28 | 877b935 |  | S15; C3 | in words other than yours | Wording that doesn't change what the user gets. |  |
| 28 | 877b935 |  | Scenarios preamble | Each runs several times | The number of runs is a threshold for a later level. |  |
| 28 | 877b935 |  | S12; M4 | the readability rules | What counts as readable is a later-level definition; rules come with the scenario. |  |
| 29 | 877b935 |  | S6; C17b | only then | Whether an unmade decision the tests depend on 'blocks' is a later-level definition. |  |
| 29 | 877b935 |  | S7; C16; C17a | You're asked about the conflict | Whether a conflict with existing code 'blocks' is a later-level definition. |  |
| 29 | 877b935 |  | C7; C10 | unless the work can find it out | Which levels allow found facts and hold verifications is a later-level point. |  |
| 29 | 877b935 |  | C16b; C14 | Agreements carry over | Reconcilable as carrying over within scope; S4 and S19 show both sides. |  |
| 29 | 877b935 |  | definitions paragraph; decision classification link |  | Definitions named under criterion 6; the link resolves a term, not where output lives. | criterion 6 |
| 29 | 877b935 |  | Scenarios preamble | fail before the work and pass after it | States what makes checks sound under criterion 5, not how tests are built. | criterion 5 |
| 29 | 877b935 |  | S14 | a defect its review finds | No claim promises review finds general defects; whether 'reports no findings' needs a report is interpretation. |  |
| 29 | 877b935 |  | S10 | asked nothing beyond the playback | 'One thing more' rules out any other gap, so a reading question isn't permitted there. |  |
| 29 | 877b935 |  | C11; C9 | a distinct phrase for yours | Confirmed through the playback, so it is agreed. |  |
| 29 | 877b935 |  | C11; C3c | on its own | A choice applies only when the reading can't be told; narrowing is for a later level. |  |
| 29 | 877b935 |  | C7; S10 | A verification is complete when it names what is checked, how, and what result passes | A definition S10 applies, not a claim needing its own scenario. |  |
| 29 | 877b935 |  | C8; S12; C14 | readable at a glance | Room for interpretation in these terms; judge rules come with the scenario. |  |
| 29 | 877b935 |  | S12 | no message asks more than one question | A playback asks one thing; consistent. |  |
| 29 | 877b935 |  | S1 | the code has passing tests | Paired with acceptance tests and the rule that no check relies only on the work's tests. |  |
| 30 | 877b935 |  | A3; A4; M6; M7 | A plain answer ... is acted on without that | Reconcilable as per-answer vs per-level playback; not a contradiction. |  |
| 30 | 877b935 |  | S15; S8 | after the playback | S8 checks ordering; a scenario need not re-check. |  |
| 30 | 877b935 |  | A14; A16 | stated scope | Default scope when none is stated is a later-level rule. |  |
| 30 | 877b935 |  | Scenarios preamble |  | States properties criterion 5 requires, not how tests are built. | criterion 2 'how tests are built' |
| 30 | 877b935 |  | decision classification link |  | A pointer to a definition, not where any part of the feature lives. | criterion 2 'where anything lives' |
| 30 | 877b935 |  | A7; A5; A10 |  | At a level not allowing found facts, what a verification holds is for a later level. |  |
| 30 | 877b935 |  | S12 | Every document and message you're sent | Possibly excluding written documents is wording. |  |
| 30 | 877b935 |  | S14 |  | Whether the scripted user can answer a question the fix needs is how the scenario is scripted. |  |
| 30 | 877b935 |  | S16 | no level that doesn't allow found facts holds it | Would flag the fact if you had said it, but the script sets what you say. |  |
| 30 | 877b935 |  | S8 |  | Order when playback itself must state a reading is a procedure for a later level. |  |
| 30 | 877b935 |  | S1 | the code has passing tests | Same check also requires acceptance tests that come with the scenario. |  |
| 30 | 877b935 |  | A9; A13 |  | Whether confirming a playback makes a statement 'agreed' is a later-level definition. |  |
| 30 | 877b935 |  | S15; A4 |  | S15 depends on the work asking a question, which A4's interview brings about. |  |
| 30 | 877b935 |  | A8; S12 | readable at a glance | Threshold is for a later level; S12 defers to readability rules from the scenario. |  |
| 31 | dd7b7d0 |  | Scenarios preamble | Acceptance tests fail before the work and pass after it | States properties criterion 5 asks of checks, not how tests are built. | criterion 2 |
| 31 | dd7b7d0 |  | Scenarios preamble | Each runs several times on a sample project with a scripted user | Names the actor and pass bar; how the script is written is later-level. | criterion 2 |
| 31 | dd7b7d0 |  | definitions paragraph | A verification is complete when | Definitions fix meanings of terms the claims use; criterion 6 expects them. | criterion 6 |
| 31 | dd7b7d0 |  | decision classification link | set by the decision classification | A citation of an existing definition, not placement of anything. | criterion 2 'where anything lives' |
| 31 | dd7b7d0 |  | S1 | the code has passing tests | Conjoined with acceptance tests pass; a way to game it is not shown. |  |
| 31 | dd7b7d0 |  | S14 |  | Which defect is planted and that the review finds it is how the test is built. |  |
| 31 | dd7b7d0 |  | S7; A17b; A6 | You're asked about the conflict | Whether the conflict blocks depends on the decision classification; read against A17b/A6 the check is sound. |  |
| 31 | dd7b7d0 |  | S18; A14b | cites the first as its preferred default | Citing is how a check observes the default; telling cases apart is test building. |  |
| 31 | dd7b7d0 |  | S6; A2a; A17b | decisions are made before code starts | Not a contradiction; A17b states the fallback and the scenario sets that state. |  |
| 31 | dd7b7d0 |  | A16b; A14a; S4; S19 | Agreements carry over to later features | Reconciled by 'unless an agreement or codified rule already covers the case'. |  |
| 31 | dd7b7d0 |  | A17b; A3a; S5 | you're asked, and only then | A playback answers your instruction, not the work's need; S5's script gives none. |  |
| 31 | dd7b7d0 |  | S11; S3 |  | S3 'levels in order' fails if the next level's interview starts before approval. |  |
| 31 | dd7b7d0 |  | S4 | build it | First feature's build is itself judged in the check and its levels come with the scenario. |  |
| 31 | dd7b7d0 |  | C13; A8; A10; Scenarios preamble | codified | 'Codified', 'readable at a glance', found-fact levels and 'several' runs are later-level definitions and thresholds. |  |
| 31 | dd7b7d0 |  | A7 | and run | No scenario runs a verification; whether it can run is later-level. |  |
| 31 | dd7b7d0 |  | S12; A8 | Every document and message you're sent | Wording that doesn't change what the user gets. |  |
| 31 | dd7b7d0 |  | S16 | no level that doesn't allow found facts holds it | Case where you state the fact yourself is not brought about by the scenario; speculative. |  |
| 32 | dd7b7d0 |  | decision classification link |  | A pointer to a definition outside the Outcome; does not change what the user gets. | criterion 2 |
| 32 | dd7b7d0 |  | Scenarios preamble | acceptance tests fail before the work and pass after it | Pass-bar and check-soundness statements, not how a test is built. | criterion 2 |
| 32 | dd7b7d0 |  | C7 | names what is checked, how, and what result passes | A result the user observes in a level document, not how the Outcome's checks are built. | criterion 2 |
| 32 | dd7b7d0 |  | C3; S8; S15 | on its own, after the playback | An order the user observes, not a procedure. | criterion 2 |
| 32 | dd7b7d0 |  | C8; S12; M4 | Readable at a glance | Threshold is a later-level point; result is clear. | criterion 3 |
| 32 | dd7b7d0 |  | C2; C10; C12 |  | Which levels exist, allow found facts, own questions are later-level definitions. | criterion 3 |
| 32 | dd7b7d0 |  | definitions paragraph | a result in the list above or in a level's document | Self-reference is redundant; either reading gives the same result. | criterion 3 |
| 32 | dd7b7d0 |  | C6; C15; S1; M14 | anything the work can't settle one of those ways is put to you | 'Settle' covers the work making its own decision; S1 and M14 fix the reading. | criterion 6 |
| 32 | dd7b7d0 |  | C13; C14; S4; S19 | nothing already agreed ... asked again | Scope resolves the tension; S4 and S19 have distinct starting states. | criterion 6 |
| 32 | dd7b7d0 |  | C6; C17; S20 |  | No text puts an unassigned point after code starts; S20 places them before the document. | criterion 6 |
| 32 | dd7b7d0 |  | C7; C10; S10 |  | Neither claim says when verification must be complete; S10 is scoped to a level allowing found facts. | criterion 6 |
| 32 | dd7b7d0 |  | C3; C4; S15 | without a playback of its own | S15 reconciles per-answer and level playbacks. | criterion 6 |
| 32 | dd7b7d0 |  | S10 | asked nothing beyond the playback | Could fail a legitimate interview question, but how the scripted user supplies the rest is test building. | criterion 5 |
| 32 | dd7b7d0 |  | S6 | one of your decisions left unmade | Acceptance tests on your answer make it a decision the code depends on. | criterion 5 |
| 32 | dd7b7d0 |  | S11 | one is written after | Fails if the level is the last, but choosing the level is scripting. | criterion 5 |
| 32 | dd7b7d0 |  | S14; S17 |  | Starting state fixes that the review finds the defect; lenient re-review is gaming, not a finding. | criterion 5 |
| 32 | dd7b7d0 |  | S4 | build it | Levels, answers and rule are set; first feature's code has its own acceptance tests. | criterion 5 |
| 32 | dd7b7d0 |  | S12; C3 | no question is sent before you answer the one before it | 'After the playback' permits waiting for confirmation first; no contradiction. | criterion 6 |
| 32 | dd7b7d0 |  | S12; C8 | documents and messages you're sent | Wording; a faithful build includes level documents. | criterion 4 |
| 32 | dd7b7d0 |  | C7; S10 | completed | Judged against the claim, 'completed' carries runnable and named parts; not a gap. | criterion 4 |
| 32 | dd7b7d0 |  | M6; S11 |  | Counting an unprompted approval acted on without playback is odd but consistent, not a contradiction. | criterion 5 |
| 33 | dd7b7d0 |  | decision classification link | Which decisions are yours and which are the work's is set by the | Where the classification is kept doesn't change what the user gets. | criterion 2 |
| 33 | dd7b7d0 |  | Scenarios preamble | runs several times on a sample project with a scripted user | Names check type, pass bar and starting states; how script or judge is built is not stated. | criterion 2 |
| 33 | dd7b7d0 |  | definitions paragraph | A requirement is complete when | Criterion 6 admits definitions; these state observable content, not procedure. | criterion 6 |
| 33 | dd7b7d0 |  | S3 | the work asks no question before its level | Coherent reading matches the later-level question claim. | criterion 3 |
| 33 | dd7b7d0 |  | S1 | the code has passing tests | Check also requires acceptance tests pass. |  |
| 33 | dd7b7d0 |  | S14 | its review reports no findings at the time you're asked | Gaming by a weak review is not shown by the text. |  |
| 33 | dd7b7d0 |  | S6 | one of your decisions left unmade | Reads as a decision the feature needs, i.e. one that blocks. |  |
| 33 | dd7b7d0 |  | S18 | cites the first as its preferred default | Citing is how the default is observable in a record. |  |
| 33 | dd7b7d0 |  | S12 | document ... you're sent | Documents put to you for approval are sent to you; wording. |  |
| 33 | dd7b7d0 |  | S15; C3 | in words other than yours | Equivalent to 'in its own words' for an LLM judge. |  |
| 33 | dd7b7d0 |  | M3 | Readings of your words ... taken without asking you | 'Reading' means one of several interpretations, so unambiguous readings aren't counted. |  |
| 33 | dd7b7d0 |  | C2a; C17b | If one of your decisions still blocks it, you're asked | 'Still' frames an exception when levels missed one; not a contradiction. | criterion 6 |
| 33 | dd7b7d0 |  | C3b; C3c | A plain answer ... acted on without that | 'Plain' reads as unambiguous; no contradiction. |  |
| 33 | dd7b7d0 |  | C7c; C12 | Anything missing from either is asked | Reconcilable by asking the missing thing at its level. | criterion 6 |
| 33 | dd7b7d0 |  | S4 |  | Second feature's level is run output, not starting state; the scenario supplies the rest. |  |
| 33 | dd7b7d0 |  | Scenarios preamble; C8; S12 | Each runs several times | Run count, 'readable at a glance', readability rules are later-level thresholds. |  |
| 33 | dd7b7d0 |  | S2 |  | Depending on the work asking the question is how the scripted user is scripted. |  |
| 33 | dd7b7d0 |  | S5 | Nothing is asked after code starts | Clarity/conflict allowances ruled out by the starting state. |  |
| 34 | ec102df |  | definitions paragraph |  | Terms claims depend on; criterion 6 admits definitions; removing them wouldn't change what the user gets. | criterion 2 |
| 34 | ec102df |  | decision classification link |  | Identifies which classification applies, not where built work lives; wording only. | criterion 2 'where anything lives' |
| 34 | ec102df |  | C7 | names what is checked, how, and what result passes | Defines the term the observable result depends on; not shown as narrowing beyond the Outcome. | criterion 2 |
| 34 | ec102df |  | Scenarios preamble |  | States kind of check and pass bar, not how scenarios are scripted. | criterion 2 'how tests are built' |
| 34 | ec102df |  | C3; C4; S15 | A plain answer ... is acted on without that | Per-answer playback is exempted, level playback still required; no contradiction. | criterion 6 |
| 34 | ec102df |  | C7; S10 | A verification is complete when it names what is checked, how, and what result passes | S10's 'completed' carries the claim's definition. | criterion 4 |
| 34 | ec102df |  | C4; S1; S20 | you're interviewed about what that level needs | Covered indirectly by S1 and S20. | criterion 4 |
| 34 | ec102df |  | C4; S8; S9 |  | S8 and S9 fail if there is no level playback or the document precedes confirmation. | criterion 4 |
| 34 | ec102df |  | C8; S12 | Every document and message you're sent | A document you're asked to approve is one you are sent; not shown. | criterion 4 |
| 34 | ec102df |  | S7 |  | Whether a conflict is a block or your decision is set by the decision classification; not shown. | criterion 5 |
| 34 | ec102df |  | S6; C17 | only then | A decision the code must follow blocks; starting state brings about the block. |  |
| 34 | ec102df |  | S3; C13 | the work asks no question before its level | A clarity question needed now is this level's question; not shown. | criterion 5 |
| 34 | ec102df |  | S13; S1 |  | Marking everything as its own is gaming a check, also caught by S1. | criterion 5 |
| 34 | ec102df |  | S1 | the code has passing tests | Paired with acceptance tests and the preamble rule. | criterion 5 |
| 34 | ec102df |  | S18; C14; C15 | cites the first as its preferred default | Citing is the visible form of recording; not shown to count against allowed behaviour. | criterion 5 |
| 34 | ec102df |  | C10; C7; C12; S10; S16 | appears only in a level that allows it | C12 defers to the allowing level; no contradiction shown. | criterion 6 |
| 34 | ec102df |  | C13; C14; S4; S19 | The next feature makes the same decision again | Reconciled by scope and 'unless an agreement ... covers the case'. | criterion 6 |
| 34 | ec102df |  | C2; S6; C17 | decisions are made before code starts | C17 is an explicit fallback; S6 sets that state. | criterion 6 |
| 34 | ec102df |  | M12 | Approved levels later changed because the work read you wrong | Traces to C3/C6/C9. | criterion 4 |
| 34 | ec102df |  | M5; S12; C3 | no message asks more than one question | Playback then choice is sequential by C3; consistent. | criterion 6 |
| 34 | ec102df |  | C14 | stated scope | How scope is stated is a later-level point. | criterion 3 |
| 35 | ec102df |  | Scenarios preamble | Acceptance tests, any levels a scenario starts from, and the rules a judge applies come with the scenario | States checks need no person and results are preset, as criterion 5 requires; not extra. | criterion 5 |
| 35 | ec102df |  | definitions paragraph |  | Criterion 6 names definitions as Outcome content. | criterion 6 |
| 35 | ec102df |  | decision classification link |  | Reference to an existing artifact, not where anything will live. |  |
| 35 | ec102df |  | C7; S10 | A verification is complete when it names what is checked, how, and what result passes | A definition supporting the result; S10 checks both cases. |  |
| 35 | ec102df |  | C4; S8; S1; S13; S20 | interviewed | S8 fails if interview or playback is skipped; combined with others the part is traced. |  |
| 35 | ec102df |  | S14 | a defect its review finds | The traced claim is sequencing, not review quality. |  |
| 35 | ec102df |  | S18; C14 | cites the first as its preferred default | Citation is the observable form of the default. |  |
| 35 | ec102df |  | C6; C15; S1; M14 | anything the work can't settle one of those ways is put to you | Sensible reading is the work makes its own decisions; literal reading is wording only. |  |
| 35 | ec102df |  | C14; C16; S4; S19 | A decision holds only within its stated scope | Reconciled by 'stated scope' and the coverage clause. |  |
| 35 | ec102df |  | C2; S6; C17 | decisions are made before code starts | C17 states the fallback explicitly. |  |
| 35 | ec102df |  | S5; C13; C17 | Nothing is asked after code starts | C17 restricts post-code questions and the starting state rules out clarity cases. |  |
| 35 | ec102df |  | S2; S13; M3 | It surfaces | Guessing is checked by S13 and M3; a scenario need not re-check another's claim. |  |
| 35 | ec102df |  | S1; S5 |  | Acceptance tests built to depend on the work's decisions is a badly built check, not shown. |  |
| 36 | ec102df |  | decision classification link |  | Cross-reference to a definition; where it lives doesn't change what the user gets. | criterion 2 |
| 36 | ec102df |  | C7 |  | Definitions of complete requirement/verification are permitted and state the bar observable as what is asked. | criterion 2 |
| 36 | ec102df |  | Scenarios preamble | acceptance tests ... come with the scenario | Serves the pass bar and criterion 5; not how tests are built. | criterion 2 |
| 36 | ec102df |  | C7; S10; S1 | written in full and run | S10's 'completed' invokes the definition and S1 covers running; no gap shown. | criterion 4 |
| 36 | ec102df |  | S7; C17 | You're asked about the conflict | Reads as C17's blocking decision, so it checks a claim. | criterion 4 |
| 36 | ec102df |  | C4; S20; S1; S8; S9 | interviewed | No plain-level scenario, but S20, S1, S8, S9 fail if interview or playback is skipped. | criterion 4 |
| 36 | ec102df |  | S5; C13 | Nothing is asked after code starts | Starting state rules out the clarity allowance. | criterion 5c |
| 36 | ec102df |  | S3 | the work asks no question before its level | A clarity question about the current level belongs to it; no misjudgment shown. | criterion 5c |
| 36 | ec102df |  | S15; C3 | in words other than yours | Wording; same result. | criterion 5 |
| 36 | ec102df |  | S13; S21; C11 | something you said | A reworded statement of yours is still something you said; telling apart is test building. | criterion 5 |
| 36 | ec102df |  | S18; C14 | cites the first as its preferred default | Same observable result. | criterion 5 |
| 36 | ec102df |  | S19 | your new answer | Set by the script before the run. | criterion 5e |
| 36 | ec102df |  | S6; S14; S17 |  | Levels a scenario starts from come with the scenario. | criterion 5f |
| 36 | ec102df |  | C2; C17; S6 | decisions made before code starts | C17 is the fallback S6 sets up, not a contradiction. | criterion 6 |
| 36 | ec102df |  | C13; C16; C14; S4; S19 | Agreements carry over | Reconciled by C14's coverage clause; S4 and S19 embody both. | criterion 6 |
| 36 | ec102df |  | C5; C10 | found fact only in a level that allows it | What happens at a disallowing level is left to a later level. | criterion 6 |
| 36 | ec102df |  | S12; C14; C15 | readability rules | Leave room a later level narrows; result is clear. | criterion 3 |
| 37 | 3e512e3 |  | A4a; S1; S13; S20 | you're interviewed about what that level needs | Observable part covered by S1, S13, S20; what an interview contains is a later level. |  |
| 37 | 3e512e3 |  | Scenarios preamble | Every check is automated: acceptance tests, transcript analysis or an LLM judge | States what a check is and that it's not satisfiable by the work, as criterion 5 requires. | criterion 2 'how tests are built' |
| 37 | 3e512e3 |  | Scenarios preamble | on a sample project with a scripted user | It is the scenarios' starting state and lets no check need a person. | criterion 2 |
| 37 | 3e512e3 |  | definitions paragraph |  | Criterion 6 names definitions as Outcome content. | criterion 2 |
| 37 | 3e512e3 |  | decision classification link |  | Names an existing project rule, not where any part of the feature lives. | criteria 2 and 3 |
| 37 | 3e512e3 |  | S6; A17b | one of your decisions left unmade | Which decision is unmade is set by the script; text doesn't show a non-blocking one. | criterion 5 |
| 37 | 3e512e3 |  | S10; A7b; A4a; A4c | before the requirement and its verification are written | Timing follows from A4a and A4c. | criterion 5 |
| 37 | 3e512e3 |  | A2a; S6; A17b | decisions are made before code starts | 'Still blocks' states the exception; not a contradiction. | criterion 6 |
| 37 | 3e512e3 |  | S4 | an earlier level of the second feature is approved, including your answer | The thing checked is your scripted answer, which the scenario sets. | criterion 5 |
| 37 | 3e512e3 |  | S16 | the level's review checked it against the project | How that is observed is how the check is built. | criterion 5 |
| 37 | 3e512e3 |  | A17a | the work proceeds with everything it needs | Next sentence fixes the reading; wording only. | criterion 3 |
| 37 | 3e512e3 |  | A8; A10a | readable at a glance | What exactly counts belongs to a later level. | criterion 3 |
| 37 | 3e512e3 |  | S13 | judged by an LLM judge against the transcript | What the judge reads is how the check is built. | criterion 5 |
| 38 | 3e512e3 |  | C4; S9; S8; S10; S20 | interviewed ... and then played back | Observable result covered by S9 and S8/S10/S20. |  |
| 38 | 3e512e3 |  | C7; S10; S23 | A verification is complete when it names what is checked, how, and what result passes | A definition; the operative result is checked by S10 and S23. | criterion 6 |
| 38 | 3e512e3 |  | Scenarios preamble | no check relies only on tests written by the work being judged | States checks are preset and not satisfiable by the work, not how tests are built. | criterion 5 |
| 38 | 3e512e3 |  | S3 | the work asks no question before its level | 'Its' reads as each question's own level; the other reading contradicts C4/C5. |  |
| 38 | 3e512e3 |  | S7; C17; C6 | You're asked about the conflict | A conflict is a point the work can't settle, so asking is required. |  |
| 38 | 3e512e3 |  | S15 | in words other than yours | A faithful judge reads it as paraphrase; strict reading is a badly built check. |  |
| 38 | 3e512e3 |  | S15 | the project changes only after you confirm | In context the confirm clause is about the two instructions; no misjudgement. |  |
| 38 | 3e512e3 |  | C14; C13; C16; S4; S19 |  | Reconciled by S4 and S19; agreements cover cases within stated scope. |  |
| 38 | 3e512e3 |  | S14; C5 | You're asked to approve the level | Approval is your decision and C5 says you're asked for your decisions. |  |
| 38 | 3e512e3 |  | S6; C17 |  | The check requires code to follow the answer, so the decision bears on the code. |  |
| 38 | 3e512e3 |  | S13 | no statement in it can be read two ways | Naming no check kind is how a check is built, a later level. |  |
| 38 | 3e512e3 |  | C2; S6; C17 | decisions are made before code starts | C17's 'still' states the exception. |  |
| 38 | 3e512e3 |  | C10; C8; S12; C14; S23 | a level that allows [found facts] | Definitions, rules and thresholds left to later levels. |  |
| 39 | 3e512e3 |  | Scenarios preamble; decision classification link | acceptance tests, transcript analysis or an LLM judge | A definition by reference and check-type list don't change what the user gets. | criterion 2 |
| 39 | 3e512e3 |  | C2; S6; C17; S1 | your decisions are made before code starts | Goal plus fallback; no contradiction. |  |
| 39 | 3e512e3 |  | S1 | the code has passing tests | Paired with acceptance tests; preamble bars relying on the work's tests. |  |
| 39 | 3e512e3 |  | S6; C17; S5 | You're asked about it | Timing nuance S5 covers from the other side; not shown. |  |
| 39 | 3e512e3 |  | S18; C14 | cites the first as its preferred default | Citation is the only observable form; wording. |  |
| 39 | 3e512e3 |  | C4; S8; S1; S20 |  | Plain-case interview and playback traced via S8, S1, S20. |  |
| 39 | 3e512e3 |  | C7; S10; S23 |  | Which verification piece is left missing is scripting; traced. |  |
| 39 | 3e512e3 |  | S12; C8 | Every document and message you're sent | Whether a level document counts as sent is how a check tells cases apart. |  |
| 39 | 3e512e3 |  | S13 |  | Missing earlier-feature agreements in the transcript depends on test building; not shown. |  |
| 39 | 3e512e3 |  | S8; C3; C5 | after the playback | Choice order vs one question at a time is not a contradiction. |  |
| 39 | 3e512e3 |  | S14; S11; S22 |  | Needing unscripted or scripted user answers is scripting, left to test building. |  |
| 39 | 3e512e3 |  | C8; S12; C13; C10 | Readable at a glance | Definitions the Outcome leaves to later levels. |  |
| 40 | bd73aa3 |  | Scenarios preamble |  | Scripted-user and test sentences establish no person is needed and set the pass bar. | criterion 2 'how tests are built' |
| 40 | bd73aa3 |  | decision classification link |  | Points to where a definition is set; wording. | criterion 2 'where anything lives' |
| 40 | bd73aa3 |  | S10; C7 | before the requirement and its verification are written | No claim allows writing before the question, so no allowance is failed. |  |
| 40 | bd73aa3 |  | C7; C10 | unless the work can find it out | Which levels allow found facts is left to a later level. |  |
| 40 | bd73aa3 |  | S13 | against the transcript | Its starting state has no carried-over agreements, so this is speculative. |  |
| 40 | bd73aa3 |  | definitions paragraph | A requirement is a result in the list above | Self-reference; wording only. |  |
| 40 | bd73aa3 |  | C14; C16; S4; S19 | holds only within its stated scope | Reconcile through scope; S4 and S19 consistent. |  |
| 40 | bd73aa3 |  | S4; Scenarios preamble | except for clarity | How clarity is judged and how many 'several times' means belong to a later level. |  |
| 40 | bd73aa3 |  | C4; S9 |  | Document-after-confirm checked at one level only, but S9 covers it. |  |
| 40 | bd73aa3 |  | C4; S9 |  | Corrected playback path not exercised; it is a later-level procedure. |  |
| 41 | bd73aa3 |  | C3; C4; S15 | is acted on without that | C4's level-wide playback is separate; S15 shows they fit. |  |
| 41 | bd73aa3 |  | decision classification link |  | A reference defining a term; removing it doesn't change what the user gets. | criterion 2 'where anything lives' |
| 41 | bd73aa3 |  | Scenarios preamble |  | Check kinds and scripted user set starting state and soundness bar. | criterion 2 'how tests are built' |
| 41 | bd73aa3 |  | S2; S1; S13 | It surfaces before code starts | 'Surfaces' means revealed when asked; guessing covered by S1 and S13; gaming not shown. |  |
| 41 | bd73aa3 |  | S13 | against the transcript | Depends on how the check is built, not shown by text. |  |
| 41 | bd73aa3 |  | M16 | Results you get under one of Claude Code and Codex but not the other | Possibly hard to observe, but the text doesn't show it misjudging. |  |
| 41 | bd73aa3 |  | S15; C3 | in words other than yours | Wording only. |  |
| 41 | bd73aa3 |  | C7; C10 |  | Levels not allowing found facts is a rule for a later level. |  |
| 41 | bd73aa3 |  | C7; C17 | only then | Non-decision input after code starts is an edge case for a later level. |  |
| 41 | bd73aa3 |  | S12; Scenarios preamble; C14 | Readability rules | Undefined terms are left to later levels. |  |
| 42 | bd73aa3 |  | S10; C4 | before the requirement and its verification are written | Under C4 the order the check requires doesn't misjudge allowed behaviour. |  |
| 42 | bd73aa3 |  | S14 | a defect its review finds | A faithful build sets a defect the review covers; rest is check construction. |  |
| 42 | bd73aa3 |  | S12 | against the readability rules | Whether the rules cover enough context is a later-level check-construction point. |  |
| 42 | bd73aa3 |  | S12; C8 | document and message you're sent | Narrower scope doesn't misjudge; the measure covers the rest. |  |
| 42 | bd73aa3 |  | C7; S10 | one thing more | Which verification part is missing is scripting, a later level. |  |
| 42 | bd73aa3 |  | C17; C3 | you're asked, and only then | A playback is a confirmation, not a question. |  |
| 42 | bd73aa3 |  | S1; S20 | you're asked to make none of the work's decisions | An unassigned point isn't one of the work's decisions. |  |
| 42 | bd73aa3 |  | S5; C17 | Nothing is asked after code starts | C17 and starting state exclude blocking needs; choosing levels is construction. |  |
| 42 | bd73aa3 |  | C5; C10; C12 |  | A fact can wait for the allowing level; no contradiction. |  |
| 42 | bd73aa3 |  | Scenarios preamble | Every check is automated | Sets the pass bar and keeps results out of the work's hands. |  |
| 42 | bd73aa3 |  | decision classification link |  | A pointer to a definition, not where anything lives. |  |
| 42 | bd73aa3 |  | C7 | A requirement is complete when | States an observable result; wording, not extra. |  |
| 43 | 89876c0 |  | Scenarios preamble | Acceptance tests fail before the work and pass after it | States what checks must be, not how tests are built. | criterion 2 |
| 43 | 89876c0 |  | S12; S13 | LLM judge | Naming the check kind is part of having an automated check. | criterion 2 |
| 43 | 89876c0 |  | decision classification link |  | A definition the document relies on, not where anything lives. | criterion 2 |
| 43 | 89876c0 |  | C8; S12 | readable at a glance | The readability rules are left to a later level. | criterion 3 |
| 43 | 89876c0 |  | C14 | A decision holds only within its stated scope | Where no scope is stated is a rule for a later level. | criterion 3 |
| 43 | 89876c0 |  | C2; C17 |  | C17 is a fallback for a still-blocking decision; no contradiction. | criterion 6 |
| 43 | 89876c0 |  | C3; C4; S15 | a playback of its own | S15 keeps per-answer and level playbacks apart. | criterion 6 |
| 43 | 89876c0 |  | C5; M2; C10 |  | The fact can be found at an allowing level; which levels is for later. | criterion 6 |
| 43 | 89876c0 |  | M3; C6; C3 | Readings of your words ... taken without asking you | A reading means picking between interpretations; no allowance counted against. | criterion 5 |
| 43 | 89876c0 |  | S23; C7 | the verification runs once you supply it | A faithful check runs the verification itself, so the wording doesn't misjudge. | criterion 5 |
| 43 | 89876c0 |  | S22 | exactly one document | Documents and decisions are listed separately, so a faithful check counts level documents. | criterion 5 |
| 43 | 89876c0 |  | S18 | cites the first as its preferred default | How the check sees the default is test building. | criterion 5 |
| 43 | 89876c0 |  | S16 | no level that doesn't allow found facts holds it | The script is set by the scenario; not shown. | criterion 5 |
| 43 | 89876c0 |  | S3; C2 | the work asks no question before its level | Traces to C2. | criterion 4 |
| 43 | 89876c0 |  | S1 | asked to make none of the work's decisions | An unassigned point is not the work's decision. | criterion 5 |
| 43 | 89876c0 |  | C7; S10 | names what is checked, how, and what result passes | S10 tests a missing part generically; details later. | criterion 4 |
| 43 | 89876c0 |  | C3; S15; S8 | after the playback | S8 already checks the order. | criterion 4 |
| 43 | 89876c0 |  | M9 |  | Gaming by marking everything as the work's is not shown by the text. | criterion 5 |
| 44 | 89876c0 |  | decision classification link |  | Only points to the definition; wording. |  |
| 44 | 89876c0 |  | C7; C10 | unless the work can find it out | No contradiction shown; which level supplies the fact is later. |  |
| 44 | 89876c0 |  | C6; C3; M3 | a reading is asked | What counts as a 'reading' is a later-level definition. |  |
| 44 | 89876c0 |  | S23 | before the requirement is treated as complete | What counts as 'treated as complete' is a later-level definition. |  |
| 44 | 89876c0 |  | C8; S12 | Readable at a glance | Threshold and rules are left to a later level. |  |
| 44 | 89876c0 |  | Scenarios preamble | Several times | Number of runs left to a later level; pass bar stated. |  |
| 44 | 89876c0 |  | S16 | no level that doesn't allow found facts holds it | What counts as 'holding' a fact is a later-level definition. |  |
| 44 | 89876c0 |  | S15; C4 | acted on without a playback of its own | 'Of its own' carries C4's requirement. |  |
| 44 | 89876c0 |  | S5; C13 | Nothing is asked after code starts | Starting state rules out the clarity/conflict exception. |  |
| 44 | 89876c0 |  | S1 |  | Counting an unassigned point asked after code starts depends on F1, not separate. |  |
| 44 | 89876c0 |  | S12; S13 |  | Ways an LLM judge or transcript analysis could be gamed are not shown. |  |
| 45 | 89876c0 |  | M3; C6; C3 | Readings of your words … taken without asking you | A 'reading' means a choice between readings, so the measure matches the claim. |  |
| 45 | 89876c0 |  | S15; S8 | after the playback | S8 checks that part of C3. |  |
| 45 | 89876c0 |  | Scenarios preamble | Every check is automated: acceptance tests, transcript analysis or an LLM judge | States properties the criteria require of checks. |  |
| 45 | 89876c0 |  | decision classification link |  | Wording that doesn't change what the user gets. |  |
| 45 | 89876c0 |  | definitions paragraph; C7 | A requirement is a result in the list above or in a level's document | Bringing this document's list under C7 doesn't change what the user gets. |  |
| 45 | 89876c0 |  | C7; S10; S23 | names what is checked, how, and what result passes | S10 and S23 cover a missing part generically. |  |
| 45 | 89876c0 |  | S18 | cites the first as its preferred default | How a check tells cases apart is test building. |  |
| 45 | 89876c0 |  | S12 | gives you enough to answer it | What the readability rules contain belongs to a later level. |  |
| 45 | 89876c0 |  | S1; S20 |  | An unassigned point isn't one of the work's decisions. |  |
| 45 | 89876c0 |  | C2; C17; C13; S5; S6 | decisions are made before code starts | S6 sets the blocking case, S5 rules out clarity; no contradiction. |  |
| 45 | 89876c0 |  | Scenarios preamble | Run several times | Exact number is a later-level threshold. |  |
| 45 | 89876c0 |  | S14; S17 |  | Passing if never asked to approve is consistent with C2 and C10. |  |
| 46 | 9b2f71a |  | decision classification link |  | Cites a definition the claims depend on; doesn't say where the feature lives. | criterion 2 'where anything lives' |
| 46 | 9b2f71a |  | A7; definitions paragraph |  | Criterion 6 expects definitions and these make the claims clear. | criterion 6 |
| 46 | 9b2f71a |  | A4; S9; S8 | written only after you confirm | S8 checks the playback at every level; the claim part has a scenario. |  |
| 46 | 9b2f71a |  | A7 | names what is checked, how, and what result passes | Exact definition left to a later level. |  |
| 46 | 9b2f71a |  | S10; S16 |  | Passing on a wrong found fact is covered by S16. |  |
| 46 | 9b2f71a |  | S14; S17; S22 |  | Restriction checks; progress covered by S22; gaming not shown. |  |
| 46 | 9b2f71a |  | S18 | cite | How a check tells cases apart is test building. |  |
| 46 | 9b2f71a |  | S6; S7 |  | Acceptance tests depend on the answer, so the decision affects the code. |  |
| 46 | 9b2f71a |  | S10; A7 | before the requirement and its verification are written | A7's silence is not an allowance. |  |
| 46 | 9b2f71a |  | A17 | only then | Settling a reading or conflict is your decision; no contradiction. |  |
| 46 | 9b2f71a |  | A7; A10; A12 | unless the work can find it out | A7 sets no completion timing; A12 lets it complete later. |  |
| 46 | 9b2f71a |  | A14; A16 | holds only within its stated scope | They fit with scope; default scope is later. |  |
| 46 | 9b2f71a |  | S1; D | asked to make none of the work's decisions | Unassigned points count as yours by definition. |  |
| 46 | 9b2f71a |  | S12; A3 |  | A3 puts playbacks and choices in separate messages; rules are later-level. |  |
| 46 | 9b2f71a |  | S14 | a defect its review finds | Wording; the scenario sets the defect. |  |
| 46 | 9b2f71a |  | A8; A10 | readable at a glance | Reader knows the result; exact definitions are later. |  |
| 46 | 9b2f71a |  | A10; M2 |  | Facts needed at a disallowing level is speculative. |  |
| 47 | 9b2f71a |  | decision classification link |  | Points to a definition; doesn't change what the user gets. | criterion 2 'where anything lives' |
| 47 | 9b2f71a |  | Scenarios preamble | Acceptance tests fail before the work and pass after it | A soundness condition on checks. | criterion 2 'how tests are built' |
| 47 | 9b2f71a |  | Scenarios preamble | Several times | A threshold for a later level. |  |
| 47 | 9b2f71a |  | C13; C3; C8 | Codified | Undefined terms belong to a later level. |  |
| 47 | 9b2f71a |  | C16; C14; S4; S19 | Agreements carry over to later features | Reconcile within scope. |  |
| 47 | 9b2f71a |  | C3; C4; S15 | a plain answer ... is acted on without that | S15's 'of its own' shows the intended reading. |  |
| 47 | 9b2f71a |  | S14 | a defect its review finds | The scenario supplies the defective document. |  |
| 47 | 9b2f71a |  | S18; S19 | cites the first as its preferred default | How a check tells the default was used is test building. |  |
| 47 | 9b2f71a |  | S10 | something the sample project already shows | Level allows found facts and the check says 'marked as found', so a faithful build makes it a fact. |  |
| 47 | 9b2f71a |  | S2 | reveal it only when asked | How the scripted user is scripted is a later level. |  |
| 47 | 9b2f71a |  | C10; C5 |  | No text shows a level needing a disallowed fact. |  |
| 47 | 9b2f71a |  | S6 |  | Check requires code to follow your answer, so the decision affects code. |  |
| 47 | 9b2f71a |  | S17; S14; C10 |  | Progress after findings is covered by S14, not C10's result. |  |
| 48 | 9b2f71a |  | Scenarios preamble | acceptance tests, transcript analysis or an LLM judge | Doesn't change what the user gets and keeps checks sound. | criterion 2 |
| 48 | 9b2f71a |  | decision classification link |  | Wording only. | criterion 2 'where anything lives' |
| 48 | 9b2f71a |  | S15 |  | Acting on an answer during a level writes the level document, so the exception is brought about. | criterion 5 |
| 48 | 9b2f71a |  | S22 | exactly one document | Documents and decisions listed separately; what counts is later-level. |  |
| 48 | 9b2f71a |  | C14; C16 |  | A decision with no stated scope needs a later-level definition. |  |
| 48 | 9b2f71a |  | S8 |  | Choosing readings that reach the code is test building. |  |
| 48 | 9b2f71a |  | S13; C9; C15; S1 |  | The work settling and marking your point meets C9; C15 is covered by S1. |  |
| 48 | 9b2f71a |  | S3; C12 | the work asks no question before its level | 'Its' reads as each question's own level. |  |
| 48 | 9b2f71a |  | C5; C10; C12 |  | Such a fact can wait for its level. |  |
| 48 | 9b2f71a |  | S21 |  | A synonym for the project's term is wording. |  |
| 48 | 9b2f71a |  | S19; C14 |  | Out-of-scope part isn't agreed, so asking is consistent. |  |
| 48 | 9b2f71a |  | C8; C5; C10 | Readable at a glance | Thresholds and definitions left to later levels. |  |
| 49 | a52ab6f |  | decision classification link | ../../skills/references/decisions.md | A location that doesn't change what the user gets. | definition L14 (criterion 2); skill L18 |
| 49 | a52ab6f |  | Scenarios preamble | Acceptance tests fail before the work and pass after it | Restates normal testing standards and what comes with the scenario, which the definition allows. | definition L16, L18 |
| 49 | a52ab6f |  | S14 | a defect its review finds | The starting state supplies the defect; phrase describes its kind. | definition L32 |
| 49 | a52ab6f |  | R14; R16 | holds only within its stated scope | Agreements carry over within scope; what counts as in scope is later-level. | definition L20 |
| 49 | a52ab6f |  | R2; R17; S1 | your decisions are made before code starts | R2 uses no absolute term and R17 is a fallback. |  |
| 49 | a52ab6f |  | S22; R11; R15; S12 | exactly one document | Records can sit inside the level document; where things live is later-level. |  |
| 49 | a52ab6f |  | R3; S12 | no question is sent before you answer the one before it | Both met by waiting; no contradiction. |  |
| 49 | a52ab6f |  | R5; R10; R12 |  | No text shows a disallowing level that needs a fact; R12 sends points to their level. |  |
| 49 | a52ab6f |  | S15; R3 | in words other than yours | How the judge tells cases apart is test building. | definition L16 |
| 49 | a52ab6f |  | S18 | cites the first as its preferred default | How the verification observes the default is later-level; wording. | definition L16 |
| 49 | a52ab6f |  | S10; R10 | marked as found | Wording vs 'marked as the work's' doesn't change what the user gets. | skill L18 |
| 49 | a52ab6f |  | R8; Scenarios preamble | readable at a glance | Definition and threshold left to a later level. | definition L20; skill L17 |
| 49 | a52ab6f |  | R10 | its review checks each found fact against the project | Process wording not raised as requirement finding; its verification effect is covered by F2. |  |
| 50 | a52ab6f |  | decision classification link |  | Arguably 'where anything lives' but wording that doesn't change what the user gets. | skill L18 |
| 50 | a52ab6f |  | Scenarios preamble | Acceptance tests fail before the work and pass after it | A testing standard naming no build steps. |  |
| 50 | a52ab6f |  | R2; R17; S6; S7 | decisions are made before code starts | R17 covers the case R2's aim wasn't met; not a contradiction. |  |
| 50 | a52ab6f |  | R3; R4 | plain answer ... acted on without that | R3's exemption covers a separate playback from R4's. |  |
| 50 | a52ab6f |  | R7; R10 | unless the work can find it out | Disallowing level needs a rule for a later level. | definition L20 |
| 50 | a52ab6f |  | R17 | and only then | Confirming a playback is something only you can settle; consistent. |  |
| 50 | a52ab6f |  | S15; R4 |  | The question is R4's interview; if none is asked the scenario fails correctly. |  |
| 50 | a52ab6f |  | C13; R8; S23 | codified | Terms needing definitions or thresholds belong to a later level. | definition L20; skill L17 |
| 50 | a52ab6f |  | S12; R2 | document meant for someone other than you | Text doesn't show that document is a level document. |  |
| 50 | a52ab6f |  | S13; R9 | against ... what is agreed or codified | Pass condition matches R9. |  |
| 50 | a52ab6f |  | S18; R15 | cites the first as its preferred default | Record is visible under R15; telling cases apart is later-level. | definition L16 |
| 50 | a52ab6f |  | R16; R14; S4; S19 | Agreements carry over | Consistent; S4 and S19 exercise both. |  |
| 51 | a52ab6f |  | decision classification link | ../../skills/references/decisions.md | A location, but doesn't change what the user gets. | SKILL L18 |
| 51 | a52ab6f |  | Scenarios preamble | Acceptance tests fail before the work and pass after it | Names what comes with the scenario, which the definition allows. | outcome.md L16 |
| 51 | a52ab6f |  | R8; Scenarios preamble | Readable at a glance | Vague, but thresholds belong to a later level. | outcome.md L20; SKILL L17 |
| 51 | a52ab6f |  | R2; R17 | your decisions are made before code starts | R2 is a purpose clause with no absolute term; not a contradiction. | outcome.md L38 |
| 51 | a52ab6f |  | R7; R10; R12 |  | Disallowing-level fact case isn't shown and could resolve at a later level. | outcome.md L20 |
| 51 | a52ab6f |  | R14; R16; S4; S19 | holds only within its stated scope | Agree once scope is applied. |  |
| 51 | a52ab6f |  | S12; R2 | document meant for someone other than you | Text doesn't show it's a level document. |  |
| 51 | a52ab6f |  | S14 | a defect its review finds | Defect comes with the starting level; what a review must catch is later-level. |  |
| 51 | a52ab6f |  | S15 | the project changes only after you confirm | In context limited to 'on either instruction'; wording. | SKILL L18 |
| 51 | a52ab6f |  | S23 | before the requirement is treated as complete | How a verification tells this is later-level. | outcome.md L16, L20 |
| 51 | a52ab6f |  | S3 |  | How the scripted user knows a review passed is scripting, a later level. | outcome.md L16 |
| 51 | a52ab6f |  | S1; R17; R2 | Each of your decisions ... before code starts | Only R2's allowances count and it has none; unassigned-point case is speculation. | outcome.md L34; SKILL L19 |
| 52 | 8573a3c |  | S14; S17; R2 | you're asked to approve the level only after a later review reports no findings | Approval-request timing seemed stricter than R2; dropped since R2 states no allowance to ask early and L26 orders approval after passing. | Definition L34; skill L19 |
| 52 | 8573a3c |  | S14 | no findings | Treating a review pass as no findings is a definition left to a later level. | Definition L20; skill L17 |
| 52 | 8573a3c |  | L26 |  | Link path to the decision classification might be 'where anything lives'; removing it doesn't change what the user gets. | Skill L18 |
| 52 | 8573a3c |  | L28 | The scripted user answers… as its script says | Scripted-user and fail-before/pass-after lines describe what comes with the scenario and normal testing standards; wording only. | Definition L16, L18; skill L18 |
| 52 | 8573a3c |  | S18; R14 | cites the first as its preferred default | R14 doesn't require a citation, but how a verification tells cases apart is how tests are built. | Definition L16; skill L19 |
| 52 | 8573a3c |  | S18; R15 |  | S18 reads the work's own record, but the record is a user-facing result R15 requires, not a self-report of success. | Definition L33 |
| 52 | 8573a3c |  | S15; R3 | Words other than yours | Wording mismatch with R3's 'its own words' could at most be built badly, not a finding. | Skill L19 |
| 52 | 8573a3c |  | S23 | Before the requirement is treated as complete | The observable sign of 'treated as complete' is left to a later level. | Definition L20 |
| 52 | 8573a3c |  | S10; S16; S17 |  | Which levels allow found facts is defined by a later level and not something the work produces before the event. | Definition L30, L32 |
| 52 | 8573a3c |  | R5; R10; R7 | can be written | A needed fact at a level not allowing found facts is no contradiction because R7 says 'can be written', not 'is written'. | Definition L38 |
| 52 | 8573a3c |  | R14; R16; S4; S19 | only within its stated scope | Read together, carrying over applies within the stated scope; S4 and S19 are consistent with that. | Definition L38 |
| 52 | 8573a3c |  | R3; R12 | Anything that could be read more than one way… | 'After the playback' can mean the later level's own playback, so R3 and R12 don't contradict. | Definition L20, L38 |
| 52 | 8573a3c |  | R2; R17 | your decisions are made before code starts | R2 is a purpose clause without an absolute term, so R17's fallback is not an exception to an absolute. | Definition L38 |
| 52 | 8573a3c |  | S12; S22 | meant for someone other than you | S12's extra document and S22's 'exactly one document' are different scenarios, so no contradiction. | Definition L38 |
| 52 | 8573a3c |  | R13; S5; S4 | each can be read only one way | R13's clarification allowance in 'nothing asked' scenarios is ruled out by S5's starting state or carried by S4. | Definition L34 |
| 53 | 8573a3c |  | L26 | ../../skills/references/decisions.md | Link to decisions.md says where something lives, but removing it wouldn't change what the user gets. | definition l.14; skill l.18 |
| 53 | 8573a3c |  | R2; R17 | your decisions are made before code starts | R2 uses no absolute term and R17 is a fallback for what still blocks, not an exception. | definition l.38 |
| 53 | 8573a3c |  | S6; S7 |  | Whether something blocks is 'how much work stops', which the definition leaves to a later level. | definition l.20; skill l.17 |
| 53 | 8573a3c |  | S10; R7; R4 | before the requirement and its verification are written | S10's timing comes from R4, which already requires the interview before the document is written. |  |
| 53 | 8573a3c |  | S14; S17 |  | Equating passing review with no findings is a later-level definition, and R10 makes the finding the result. | definition l.20 |
| 53 | 8573a3c |  | S18; R14; R15 | cites the first as its preferred default | For the work's decision, the record is the only observable form of R14's preferred default, so this isn't stricter. |  |
| 53 | 8573a3c |  | S15; R3 | in words other than yours | Wording that doesn't change what the user gets. | skill l.18 |
| 53 | 8573a3c |  | S13; R9 | against … what is agreed or codified | Whether codified counts as agreed is a definition left to a later level. | definition l.20 |
| 53 | 8573a3c |  | R5; R7; R10 |  | No requirement says every requirement completes within its level, so no contradiction; resolution left to a later level. | definition l.20 |
| 53 | 8573a3c |  | R9; R12 | no statement read two ways | A general statement isn't one with two readings, and leaving the point out satisfies both. | skill l.19 |
| 53 | 8573a3c |  | R17; R3 | only then | Confirming a new instruction is something only the user can settle that blocks the action, so they read together. |  |
| 53 | 8573a3c |  | R16; R13 | follows everything agreed or codified | Conflicting agreed items case is speculative; R13 already handles conflicts and nothing sets it up. |  |
| 53 | 8573a3c |  | R18 | enforces itself the same way | Mechanism reading leaves observed behaviour the same under both; shared pass bar verifies it; mechanism is later. |  |
| 53 | 8573a3c |  | L28 | acceptance tests must fail before the work and pass after it | These state testing standards and soundness the definition requires, not how tests are built. | definition l.18, l.33 |
| 53 | 8573a3c |  | L28 | The scripted user | The scripted user is what comes with the scenario, which the definition allows. | definition l.16 |
| 53 | 8573a3c |  | S4 |  | First feature's approved levels come from the starting state and its build is part of the scenario's event. | definition l.32 |
| 53 | 8573a3c |  | S21; R9; R10 |  | Whether a project term counts as a found fact or statement is a later-level definition. | definition l.20 |
| 53 | 8573a3c |  | S22; L26 | Each level produces one document | The document defines documents and decisions separately, so records don't conflict with one document per level. |  |
| 53 | 8573a3c |  | R4; S8; S9; S10; S20 |  | R4 has no own scenario, but S8, S9, S10, S20 each fail an early document; structure is for a later level. | definition l.29 |
| 54 | 8573a3c | 2 | L26 | where anything lives | The decisions.md path doesn't change what the user gets; the classification itself is a later-level definition. | SKILL L18; definition L20 |
| 54 | 8573a3c |  | L28 | Acceptance tests fail before the work and pass after it; no check relies only on tests written by the work being judged | This is a property of a verification and its pass bar, which the definition allows. | definition L16, L18 |
| 54 | 8573a3c | 6 | R2; R17; S6; S7 | your decisions are made before code starts | R2 has no absolute term and R17 reads as fallback; doesn't change what gets built. | definition L38; SKILL L18 |
| 54 | 8573a3c | 6 | R10; R11; S21 | A fact the work found appears only in a level that allows it | Whether a project term is a 'fact' needs a definition owned by a later level. | definition L20; SKILL L17 |
| 54 | 8573a3c |  | S22; R15; R11 | each level has produced exactly one document | What counts as a level's document is for a later level, and R15's allowance isn't R2's. | definition L20, L34 |
| 54 | 8573a3c | 5 | S10 | completed with what the work found | S10 doesn't check the fact is correct, but S16 and S17 already verify that. | definition L37 |
| 54 | 8573a3c | 5 | S10; R7; R4 | before the requirement and its verification are written | R4 requires the interview before the document is written, so the ordering is required, not merely allowed. | definition L34; SKILL L19 |
| 54 | 8573a3c | 5 | S4 | an earlier level of the second feature is approved, including your answer to a question | Levels a scenario starts from come with the scenario, so no reliance on the work. | definition L32; SKILL L19 |
| 54 | 8573a3c | 5 | S14; S17; R2; R10 | Its review reports ... as a finding | The review's findings are R2's and R10's stated result, not a self-report of success. | definition L33; SKILL L19 |
| 54 | 8573a3c |  | S2; S14 | reveal it only when asked | Scripted user possibly unable to answer is only a verification that could be built badly. | SKILL L19 |
| 54 | 8573a3c | 3 | S23 | codified | Undefined terms ('codified', 'level that allows found facts', 'treated as complete', 'the work') have clear intent; exact meanings are later. | definition L20; SKILL L17–L18 |
| 55 | 03a00aa |  | R4; S9 | written only after you confirm the playback | R4 checked only in S9, but S9 still fails if R4 isn't met; asking for more scenarios is a split request. | outcome.md L29; SKILL L19 |
| 55 | 03a00aa |  | S14; R2; L26 | a later review reports no findings | S14 doesn't check the defect is gone, but R2 and L26 make passing review the requirement itself. | outcome.md L30 |
| 55 | 03a00aa |  | S14; S17; R2; L26 | after it passes its review | Forbidding early approval requests isn't stricter since L26 makes approval come only after passing. | outcome.md L34 |
| 55 | 03a00aa |  | S15; R3 | in words other than yours | Wording that doesn't change what the user gets. | SKILL L18 |
| 55 | 03a00aa |  | R2; R17; S6 | your decisions are made before code starts | R2 states a purpose with no absolute term, and S6 sets up its gap itself. | outcome.md L32, L38 |
| 55 | 03a00aa |  | R7; R12; S10 | answered at that level, not earlier | R7 sets no timing, and S10's missing thing is needed at this level, so no contradiction. | outcome.md L38 |
| 55 | 03a00aa |  | L26 | Code starts | Definitions at L26 look like later-level points but don't change what gets built or judged. | outcome.md L20; SKILL L3, L18 |
| 55 | 03a00aa |  | L28 | Acceptance tests fail before the work and pass after it | Scripted-user behaviour and testing standard describe what comes with the scenario, which is permitted. | outcome.md L16, L18 |
| 55 | 03a00aa |  | S8; S15; R4 |  | These depend on the work asking questions, but R4 requires the interview, so it's behaviour under test. | outcome.md L32 |
| 55 | 03a00aa |  | S4 | an earlier level of the second feature is approved | It is listed in the starting state, which sets it up. | outcome.md L32 |
| 56 | 03a00aa |  | S10; R7 | before the requirement and its verification are written | R7 gives no express allowance to write first and ask later, so there's no allowance to fail. | def L29, L34 |
| 56 | 03a00aa |  | S23 | before the requirement is treated as complete | A transcript can show this behaviour; how a check tells it apart is how tests are built. | def L16; skill L19 |
| 56 | 03a00aa |  | S14 | only after a later review reports no findings | What counts as passing a review is left to a later level; the bar matches S17 and R10. | def L20 |
| 56 | 03a00aa |  | S2; S1 | It surfaces before code starts | S2 would pass if the work guessed, but S1 already checks that, and re-verification isn't needed. | def L37 |
| 56 | 03a00aa |  | S4 |  | Second feature's checks rest on approved levels the starting state supplies, so def L32 doesn't apply. | def L32 |
| 56 | 03a00aa |  | S1; L26 |  | How a judge tells user decisions from the work's comes from the classification, which comes with the scenario. | L26; decisions.md L25; def L16, L28 |
| 56 | 03a00aa |  | R2; R17; S6; S7 | so your decisions are made before code starts | R2 states a purpose with no absolute term; R17 covers only levels the scenarios set up as open. | def L38 |
| 56 | 03a00aa | 2 | L28 | Acceptance tests fail before the work and pass after it | Names the kind of check and what comes with each scenario, which the definition allows. | def L16, L18 |
| 56 | 03a00aa |  | R18 | The framework | 'The framework' versus 'the work' is wording that doesn't change what the user gets. | skill L18 |
| 57 | 03a00aa |  | S14; R2 | a later review reports no findings | Reading 'passes' as 'no findings' is natural; what counts as passing is for a later level. | outcome.md L20; skill L17, L19 |
| 57 | 03a00aa |  | S10 | before the requirement and its verification are written | The verification can't be written without the missing thing unless guessed, so it doesn't misjudge a correct run. | skill L19 |
| 57 | 03a00aa |  | S23; S4; R13 | treated as complete | How a verification tells these cases apart is how tests are built, a later-level matter. | outcome.md L16, L20; skill L17 |
| 57 | 03a00aa |  | S3; R12 | the work asks no question before its level | An early question answered by the scripted user would break R12, so S3 follows from R12. | skill L19 |
| 57 | 03a00aa |  | S1; S2; R17; R2 | before code starts | S1 and S2 verify R2; only the verified requirement's allowances count. | outcome.md L34 |
| 57 | 03a00aa |  | S6; R17; S5 | one of your decisions left unmade | Read against S5, the decision is one the feature needs, so it blocks. | skill L19 |
| 57 | 03a00aa |  | R16; R14 | Agreements carry over | Agreements carry over and apply within scope; no absolute is contradicted. | outcome.md L38 |
| 57 | 03a00aa |  | R5; R7; R10 |  | A verification can be written without stating the fact, and which levels allow found facts is later. | outcome.md L20; skill L19 |
| 57 | 03a00aa |  | R3; R4; S15 | acted on without that | S15's 'without a playback of its own' reconciles them; the difference is wording. | skill L18 |
| 57 | 03a00aa |  | S22; R11; R15; L26 | exactly one document | L26 lists decisions separately from documents; what counts as a level's document is later. | outcome.md L20 |
| 57 | 03a00aa |  | L28 | fail before the work and pass after it | Names what comes with a scenario and its pass bar, not how tests are built. | outcome.md L16 |
| 57 | 03a00aa |  |  | readable at a glance | These terms ('readable at a glance', 'stated scope', 'what that level needs') need definitions belonging to a later level. | outcome.md L20; skill L17 |
| 57 | 03a00aa |  | S15; R3 | in words other than yours | Wording that doesn't change what the user gets. | skill L18 |
| 61 | 22b52d3 (working tree before commit) | 6 | R14; R16; R13; S4; S19 | holds only within its stated scope | Agreements carry over within scope; S4 and S19 agree, so no contradiction shown. |  |
| 61 | 22b52d3 (working tree before commit) | 5 | S4 | an earlier level of the second feature is approved, including your answer | The starting state sets it up, and line 28 says starting levels come with the scenario. | lines 28, 32 |
| 61 | 22b52d3 (working tree before commit) | 5 | S5; R13; R17 | Nothing is asked after code starts | R13 and R17 allowances are ruled out by S5's starting state. |  |
| 61 | 22b52d3 (working tree before commit) |  | S3; R12 | the work asks no question before its level | Whether R12 allows asking early without answering isn't shown by the text. |  |
| 61 | 22b52d3 (working tree before commit) |  | S13 | a point the work must settle | Whether the scripted user can answer is only something that could be built badly. | review skill line 19 |
| 61 | 22b52d3 (working tree before commit) |  | S23; R14 | treated as complete | These terms need a definition or rule a later level supplies. | outcome.md line 20 |
| 61 | 22b52d3 (working tree before commit) | 2 | L26; S7; S20 | a conflict ... are yours to settle | It functions as requirement content verified by S7 and S20; its placement is wording. |  |
| 61 | 22b52d3 (working tree before commit) | 2 | L28 | Acceptance tests fail before the work and pass after it | A normal testing standard that doesn't change what the user gets. | outcome.md line 18 |
| 62 | 8e70a8c |  | S14; S17; L26 | you aren't asked to approve … while | Not a check against allowed behaviour because L26 places approval after passing. | outcome.md L34 |
| 62 | 8e70a8c |  | S15; R4 | a question the work asks | The question arises during the run from R4's interview, not something produced before the event. | outcome.md L32 |
| 62 | 8e70a8c |  | S16 | a requirement … needs | The starting state sets the requirement as part of the feature, so no reliance on the work. | outcome.md L32 |
| 62 | 8e70a8c |  | R16; R14 | Agreements carry over to later features | Carrying over within scope is not an exception to R14. | outcome.md L38 |
| 62 | 8e70a8c |  | R13; S19; R14 | Nothing already agreed … is asked again | A case outside the agreement's scope isn't already agreed, and R14 states its own exception. | outcome.md L38 |
| 62 | 8e70a8c |  | R2; R17; S6 | your decisions are made before code starts | R2 has no absolute term, and S6 starts from levels with a decision unmade. | outcome.md L38 |
| 62 | 8e70a8c |  | R5; R7; R10 |  | Text doesn't show a requirement must be complete at its own level when the missing piece is findable. | review skill L19 |
| 62 | 8e70a8c |  | L26 |  | Link only points to where the definition lives and doesn't change what the user gets. | review skill L18 |
| 62 | 8e70a8c |  | L28 | Acceptance tests fail before the work and pass after it | A pass bar applying to every scenario, stated once, not how tests are built. | outcome.md L11, L16 |
| 62 | 8e70a8c |  | S15; R3 | in words other than yours | Wording only. | review skill L18 |
| 62 | 8e70a8c |  | S17; R10 | Its review reports the wrong fact as a finding | The finding is R10's required result, not a self-report of success. | outcome.md L33 |
| 62 | 8e70a8c |  | S23 | treated as complete | Pinning these phrases down needs a definition belonging to a later level. | outcome.md L20; review skill L17 |
| 62 | 8e70a8c |  | S12 | the readability rules | Rules a judge applies come with the scenario; defining them is a later level's job. | outcome.md L16, L20 |
| 62 | 8e70a8c |  | S9; S21 |  | Text doesn't show a project term is a fact. | review skill L19 |
| 62 | 8e70a8c |  | S6; S7 |  | Acceptance tests depend on the answer, so not stating it blocks could only be built badly. | review skill L19 |
| 63 | 9fa0d81 |  | R2; R17; S1 | so your decisions are made before code starts | R17 applies only when something still blocks, so both hold; not a contradiction. | outcome.md 38; SKILL 19 |
| 63 | 9fa0d81 |  | R16; R14; S4; S19 | Agreements carry over to later features | Read together as carry over within scope; scope of unscoped decisions is a later-level rule. | outcome.md 20, 38 |
| 63 | 9fa0d81 |  | R7; R10; R5; R12; S10; S23 |  | R7 only says when a requirement is complete; R10 and R12 send the fact to a level allowing it. | outcome.md 20, 38; SKILL 19 |
| 63 | 9fa0d81 |  | S11 | A level passes its review | Can be read as setup like S5–S7; text doesn't show reliance on the work. | outcome.md 32; SKILL 19 |
| 63 | 9fa0d81 |  | S4 |  | The approved earlier level is a starting condition, and line 28 says starting levels come with it. | outcome.md 32 |
| 63 | 9fa0d81 |  | S2 | acceptance tests show the code follows it | Implies the invariant matters; at worst it could be built badly. | SKILL 19 |
| 63 | 9fa0d81 |  | S10 | something the sample project already shows | Built faithfully it is a fact; at worst it could be built badly. | SKILL 19 |
| 63 | 9fa0d81 |  | S10; R7; R4 | before the requirement and its verification are written | R4 already requires the interview before the document, so S10 doesn't fail allowed behaviour. | outcome.md 34 |
| 63 | 9fa0d81 |  | S18 |  | A weak reason would be a bad build since the scenario sets the expected choice beforehand. | outcome.md 35; SKILL 19 |
| 63 | 9fa0d81 |  | S15; R3 | in words other than yours | Wording only; doesn't change what the user gets. | SKILL 18 |
| 63 | 9fa0d81 |  | S17; R10 |  | R10 requires the review to report the wrong fact and S17 also checks the approval gate; not implementation testing. | outcome.md 33 |
| 63 | 9fa0d81 |  | S23 | treated as complete | These and 'several times' need a definition or threshold belonging to a later level. | outcome.md 20; SKILL 17 |
| 63 | 9fa0d81 |  | S12; R2; S22 | a document meant for someone other than you | What counts as a level's document is a later-level definition. | outcome.md 20; SKILL 17 |
| 63 | 9fa0d81 |  | L28 | Acceptance tests fail before the work and pass after it | Names what comes with a scenario and its pass bar; normal standards permitted by line 16. | outcome.md 16, 18; SKILL 18 |
| 63 | 9fa0d81 |  | R18 | the same way | Could mean same mechanism, but the user-facing results reading applies and the shared pass bar checks it. | outcome.md 33; SKILL 18 |
| 63 | 9fa0d81 |  | S12 | Readable at a glance | Needs readability rules that come with the scenario; defining them is for a later level. | outcome.md 20 |
| 64 | 9fa0d81 |  | S6; S7; R17 | and only then | Starting states don't say the decision blocks, but acceptance tests show it is needed; no misjudgement shown. | SKILL L19 |
| 64 | 9fa0d81 |  | S1; R17 | made by you before code starts | S1 checks R2; R17's allowance belongs to a different requirement. | outcome L34 |
| 64 | 9fa0d81 |  | R2; R17; S6 | your decisions are made before code starts | Only a contradiction if R2 were absolute, and it uses no absolute term. | outcome L38 |
| 64 | 9fa0d81 |  | R13; R14; S19 | Nothing already agreed … is asked again | R14 limits agreements to their scope, so out-of-scope cases aren't already agreed. | outcome L38 |
| 64 | 9fa0d81 |  | R9; R3; R12 | No statement … can be read two ways | The work can leave a later level's point openly to that level; no exception forced. | outcome L20, L38 |
| 64 | 9fa0d81 |  | L28 |  | Scripted-user and fail-before/pass-after sentences name what comes with the scenario and testing standards. | outcome L16, L18; SKILL L18 |
| 64 | 9fa0d81 |  | S23; S15 | readable at a glance | These terms ('readability rules', 'treated as complete', 'words other than yours') are left to a later level. | outcome L20; SKILL L17 |
| 64 | 9fa0d81 |  | S17; R10 |  | R10 makes the review's finding the result, and the second clause checks observed behaviour. | outcome L33 |
| 64 | 9fa0d81 |  | S10 |  | A playback mentioning the found fact taken as asking would only happen if built badly. | SKILL L19 |
| 64 | 9fa0d81 |  | S16 |  | The scripted user saying the fact earlier isn't brought about by the starting state; that would be a bad script. | SKILL L19 |
| 64 | 9fa0d81 |  | S22; R11; R15; R2 | exactly one document | Records can sit in the level's document, so R2 holds and no contradiction. | outcome L34, L38 |
| 64 | 9fa0d81 |  | Measure L67 | found facts … that are wrong | When 'wrong' is judged is left to a later level. | outcome L20 |
| 64 | 9fa0d81 |  | S8 | at every level | Whether Build is included depends on which levels exist, a later-level matter. | outcome L20 |
| 64 | 9fa0d81 |  | S3; S15; S22; R3 |  | Dependence on the work's progress or asking a question is part of each scenario's own event. | outcome L32 |
| 64 | 9fa0d81 |  | S4 | follows all three | A faithful build tests what is agreed; quoted text shows no misjudgement. | SKILL L19 |
| 65 | 9fa0d81 | 5 | S15 | you give a plain answer to a question the work asks | Needs the work to ask first, but if none comes the clause goes untested without misjudging, so not a finding. | O l.30, l.32; S l.19 |
| 65 | 9fa0d81 | 5 | S17; R10; R2 | Its review reports the wrong fact as a finding | R10 makes the review finding the required result and the second clause checks observed behaviour. | O l.33; S l.19 |
| 65 | 9fa0d81 | 5 | S15; R3 | in words other than yours | Wording that doesn't change what the user gets. | S l.18 |
| 65 | 9fa0d81 | 5 | S18; R14 | preferred default | The scenario sets both the reason and expected choice, so it's faithful to R14. | O l.34, l.35 |
| 65 | 9fa0d81 | 5 | S1; L26 | yours | Which decisions are the user's comes from the classification; how verifications tell cases apart is later. | O l.16, l.20, l.35; S l.17 |
| 65 | 9fa0d81 | 6 | R9; R12; R3 | No statement in it can be read two ways | Leaving a later-level point out resolves it, so no contradiction. | O l.38 |
| 65 | 9fa0d81 | 6 | R7; R10; R5; R12 |  | A findable fact at a non-allowing level is left to the later level that allows it. | O l.20, l.38; S l.17 |
| 65 | 9fa0d81 | 6 | R14; R16; S4; S19 | holds only within its stated scope | Consistent when agreements carry over within scope, as S4 and S19 show. | O l.38 |
| 65 | 9fa0d81 | 6 | R16; S7 | everything agreed | A replacing decision becomes the current agreement, so no conflict. | O l.38; decisions.md l.26 |
| 65 | 9fa0d81 | 2 | L28; L26 | Acceptance tests fail before the work and pass after it… | States the testing standard and what comes with the scenario; the link points to a definition. | O l.14, l.16, l.18; S l.18 |
| 65 | 9fa0d81 | 3 | S23 | readable at a glance | Exact definitions or thresholds for these terms are for a later level. | O l.20; S l.17 |
| 66 | 9fa0d81 |  | R2; R17; S6; S7 | your decisions are made before code starts | R2 has no absolute term, and after-code cases come only from starting states the scenarios set. | outcome.md L38, SKILL L19 |
| 66 | 9fa0d81 |  | R17; R3; S5 | and only then | Waiting for confirmation is itself something only the user can settle that blocks the action. | L38 |
| 66 | 9fa0d81 |  | S17; R10 | Its review reports the wrong fact as a finding | It checks exactly what R10 requires; when the review runs is for a later level. | L33, L20 |
| 66 | 9fa0d81 |  | S3; S22 |  | Producing passing levels is the behaviour these scenarios verify, unlike S11 where it's a precondition. |  |
| 66 | 9fa0d81 |  | S16 | a requirement of a level allowing found facts needs | The scenario's script can make the requirement certain; no reliance shown. | L19 |
| 66 | 9fa0d81 |  | S23 | treated as complete | What counts as complete and when the check runs need a later-level definition. | outcome.md L20, SKILL L17 |
| 66 | 9fa0d81 |  | S10; R5; R7; R4 | asked nothing for that thing | Only verified requirements' allowances count, and R4's playback isn't among them. | L34 |
| 66 | 9fa0d81 | 2 | L28 | Acceptance tests fail before the work and pass after it | A testing standard and pass bar that doesn't change what the user gets. | L16, L18; SKILL L18 |
| 66 | 9fa0d81 |  | L26 | where anything lives | The link references a definition and doesn't change what the user gets. | SKILL L18 |
| 66 | 9fa0d81 | 2 | R10; R2 | its review checks each found fact | The review is part of the user's R2 gate; text doesn't show it unobservable. |  |
| 66 | 9fa0d81 |  | R14; R16 |  | Whether an unscoped decision carries over needs a rule for a later level. | L20 |
| 66 | 9fa0d81 |  | M3 | Readings … taken without asking you | What counts as a reading needs a later-level definition. | L20 |
| 66 | 9fa0d81 |  | M12 |  | No requirement allows misreading the user, so nothing required or allowed gets counted. | L34 |
| 66 | 9fa0d81 |  | R5; R10; R12 |  | R12 sends the need to a later level that allows found facts; no contradiction shown. |  |
| 66 | 9fa0d81 |  | R18 | enforces itself the same way | Mechanism reading is wording; the shared pass bar checks results under both. |  |
| 67 | 4dbd3de |  | S14; S17; R8 | You aren't asked to approve the level while its document fails/holds one | Seemed stricter than R8, but line 26 orders approval after the pass. | outcome.md line 34 |
| 67 | 4dbd3de |  | R23; R9; R19 | and only then | An unconfirmed instruction or unclear agreement is itself something only the user can settle that blocks. | outcome.md line 38 |
| 67 | 4dbd3de |  | R8; S6; S7 | your decisions are made before code starts | R8 has no absolute term, and R23 is a fallback for unmade decisions. | outcome.md line 38 |
| 67 | 4dbd3de |  | R9; R10 | acted on without a playback of its own | 'Of its own' separates the plain-answer and level-playback cases; no contradiction. | outcome.md line 38 |
| 67 | 4dbd3de |  | S17; R16; R8 | Its review reports the wrong fact as a finding | R16 names the review finding as the result, and the review is a visible step. | outcome.md line 33 |
| 67 | 4dbd3de |  | S21 |  | Text doesn't show a term is a fact; what counts as one is later. | outcome.md line 20; SKILL.md line 19 |
| 67 | 4dbd3de |  | S1 | recorded where you can see it | decisions.md makes code the record for Build decisions; whether that counts is a later definition. | outcome.md line 20; decisions.md line 17 |
| 67 | 4dbd3de |  | S3; S11; S14 | moves to the next level | What counts as moving on is a later definition, and S3 catches early interviewing. | outcome.md lines 20, 29 |
| 67 | 4dbd3de |  | S6 |  | Acceptance tests show the unmade decision matters; could only be built badly. | SKILL.md line 19 |
| 67 | 4dbd3de |  | S4 |  | Ambiguity about when the earlier level was approved is wording that doesn't change the result. | SKILL.md line 18 |
| 67 | 4dbd3de |  | line 28 |  | The scripted-user sentence names what comes with the scenario, which is allowed. | outcome.md line 16; SKILL.md line 18 |
| 68 | 45c5bdd |  | S17; R10 | Its review reports the wrong fact as a finding | R10 itself requires the review to flag the wrong fact, so checking it checks the requirement. | outcome.md L33 |
| 68 | 45c5bdd |  | S4 |  | L28 says the levels a scenario starts from come with the scenario. | outcome.md L32 |
| 68 | 45c5bdd |  | L28 | Acceptance tests fail before the work and pass after it | Naming what comes with the scenario and normal standards is allowed and doesn't change the result. | outcome.md L16, L18, L27; SKILL.md L18 |
| 68 | 45c5bdd | 6 | R2; R17 | your decisions are made before code starts | R2 has no absolute term and R17 covers a case still left open. | outcome.md L38 |
| 68 | 45c5bdd |  | R17; R3 | and only then | An unconfirmed instruction blocks and only the user can settle it, so no conflict. |  |
| 68 | 45c5bdd |  | R7; R10 | found out by the work if it can be | The fact can go to a level allowing found facts; which level is later. | outcome.md L20 |
| 68 | 45c5bdd |  | S10; R7 | before the requirement and its verification are written | R7 states no allowance to write first, and only stated allowances count. | outcome.md L34 |
| 68 | 45c5bdd |  | S14; S11; S22 |  | Passing if the work stalls is covered by S22; how verifications split isn't a finding. | outcome.md L29, L37 |
| 68 | 45c5bdd |  | S23 | the verification runs once you supply it | How it is run is later, and a possibly badly built verification isn't a finding. | outcome.md L20; SKILL.md L19 |
| 68 | 45c5bdd |  | Measure L60; R3; R6 | Readings of your words ... taken without asking you | The measure verifies R6, which has no allowance. | outcome.md L34 |
| 68 | 45c5bdd |  | S3 | the work asks no question before its level | In context it means a later-level question; wording only. | SKILL.md L18 |
| 68 | 45c5bdd |  |  | Readable at a glance | Undefined terms ('where you can see them', 'codified') need definitions belonging to a later level. | outcome.md L20; SKILL.md L17 |
| 70 | 68ad628 |  | S14; S17; L26 | you aren't asked to approve the level while ... | L26 orders approval after the pass, and these checks test that order. | SKILL.md L19 |
| 70 | 68ad628 |  | S18 |  | Misjudges only if the set reason isn't compelling; could only be built badly. | SKILL.md L19 |
| 70 | 68ad628 |  | S23 | treated as complete | What counts as treated as complete is for a later level. | outcome.md L20 |
| 70 | 68ad628 |  | S17; R10 | Its review reports the wrong fact as a finding | R10 states the result in terms of the review, so not testing implementation. | outcome.md L33 |
| 70 | 68ad628 |  | R9; R3; R12 | no statement ... read two ways | A statement can stay general and leave the later point open; no contradiction shown. | SKILL.md L19 |
| 70 | 68ad628 |  | R5; R9; R10 |  | Which levels allow facts and what they need is for a later level. | outcome.md L20 |
| 70 | 68ad628 |  | Measure L60 | readings of your words ... taken without asking | What counts as a reading is a later-level definition. | outcome.md L20 |
| 70 | 68ad628 |  | L28 | Several times | The unspecified number of runs is a threshold for a later level. | outcome.md L20 |
| 70 | 68ad628 |  | L28 | Acceptance tests fail before the work and pass after it | These name what comes with the scenario and the pass bar, not scripting. | outcome.md L16 |
| 70 | 68ad628 |  | S1; S13 |  | They apply rules that come with the scenario; how verifications tell cases apart is how tests are built. | outcome.md L35, L16 |
| 70 | 68ad628 |  | S3; S14 | approve each level only after it passes its review | S3 doesn't verify the review pass; S14 does. | outcome.md L29, L37 |
| 70 | 68ad628 |  |  | Codified | What exactly counts as codified is for a later level. | outcome.md L20 |
| 71 | 5deb96f |  | S10; R7; R4 | before the requirement and its verification are written | R4 already requires the interview before the document is written. | outcome.md L34; SKILL L19 |
| 71 | 5deb96f |  | S23 | treated as complete | What counts as complete and how the verification runs are for a later level. | outcome.md L20; SKILL L17 |
| 71 | 5deb96f |  | S15 | the project changes only after you confirm | The clause is scoped to 'either instruction' and the confirmed reading, so it doesn't misjudge. | SKILL L19 |
| 71 | 5deb96f |  | S17; R10 |  | R10 requires the review to report the wrong fact; not the system reporting its own success. | outcome.md L33 |
| 71 | 5deb96f |  | L28 | The scripted user answers questions… | These state what comes with the scenario and normal standards and don't change what the user gets. | outcome.md L16, L18; SKILL L18 |
| 71 | 5deb96f |  | R2; R17; S6 | your decisions are made before code starts | R2 has no absolute term and R17 is explicitly the fallback. | outcome.md L38; SKILL L12 |
| 71 | 5deb96f |  | R17; R3; R13 | only then | Confirming an instruction blocks and only the user can settle it; R13 permits rather than requires asking. | outcome.md L38 |
| 71 | 5deb96f |  | R6; R17 | anything … is put to you | A point that blocks nothing isn't one the work must settle; no contradiction shown. | outcome.md L38; SKILL L19 |
| 71 | 5deb96f |  | R14; R16 | holds only within its stated scope | R14's 'unless an agreement … covers the case' reconciles them; scope is a later matter. | outcome.md L20, L38 |
| 71 | 5deb96f |  | R5; R10 |  | Which levels allow found facts is a later-level definition. | outcome.md L20; SKILL L17 |
| 71 | 5deb96f |  | S5; R2; S3; S22 | Nothing is asked after code starts | Whether Build is a level: R2, S3 and S22 put every level before code starts. | SKILL L19 |
| 71 | 5deb96f |  |  | Readable at a glance | The rules a judge applies come with the scenario. | doc L28; outcome.md L16, L20 |
| 71 | 5deb96f |  | S3 | the work asks no question before its level | How the judge knows each question's level is how a verification is built. | outcome.md L16, L20 |
| 72 | c144812 |  | R16; R14 | agreements carry over | Dropped: agreements carry over only where their scope covers the case, so the two are consistent. | outcome.md L38; review skill L19 |
| 72 | c144812 |  | S4 | those answers apply to | Dropped: 'apply to' reads as within scope; what counts as stated scope is for a later level. | outcome.md L20; review skill L17 |
| 72 | c144812 |  | R17 | and only then | Dropped: a playback after code starts waits on something only the user can settle, so it falls within R17's condition. | outcome.md L38 |
| 72 | c144812 |  | R11; R3 | without a playback of its own | Dropped: the clash is named in the level's playback, not a playback of the answer's own. | outcome.md L38 |
| 72 | c144812 |  | R10; R11; S21 | only | Dropped: using a project term is not stating a found fact and the clash record location is unstated; no conflict shown. | review skill L19 |
| 72 | c144812 |  | S17 | Its review reports the wrong fact as a finding | Dropped as implementation-testing concern: the review is a user-facing step, R10 requires the finding, and the user-facing half is also checked. | outcome.md L33; review skill L19 |
| 72 | c144812 |  | S23 | before the requirement is treated as complete | Dropped: exactly when this happens is left to a later level. | outcome.md L20; review skill L17 |
| 72 | c144812 |  | S2 | reveal it only when asked | Dropped: what counts as being asked is a scripting detail for a later level. | outcome.md L16, L20 |
| 72 | c144812 |  | S14 | while its document fails that standard | Dropped: how failure is detected after fixes is how tests are built. | outcome.md L16 |
| 72 | c144812 |  | L28 | The scripted user ... as its script says; Acceptance tests fail before the work and pass after it | Dropped as test-building detail concern: these describe what comes with the scenario, which is allowed. | outcome.md L16 |
| 72 | c144812 |  | S10 | exactly that thing | Dropped: possible over-strictness is wording that doesn't change what the user gets. | review skill L18 |
| 72 | c144812 |  | R2; R17 | decisions made before code starts | Dropped: R17 is a fallback for levels approved with something missing; S1's starting state doesn't set that up, so no contradiction. | outcome.md L38 |
| 74 | df3dcc1 |  | S14 |  | Dropped: S14 only sets up a failed standard; which failure is set up is test-building, and no gap is shown. | outcome.md l.16, l.29; SKILL.md l.19 |
| 74 | df3dcc1 |  | R4; S8; S9 |  | Dropped: S8 and S9 together cover R4's playback; wanting a scenario per level asks for a different structure. | outcome.md l.29 |
| 74 | df3dcc1 |  | S15 | the project changes only after you confirm | Dropped: the sentence is scoped to 'either instruction'; reading it as covering the plain answer would be a bad build. | SKILL.md l.19 |
| 74 | df3dcc1 |  | S23 | before the requirement is treated as complete | Dropped: exact timing is left to a later level. | outcome.md l.20; SKILL.md l.17 |
| 74 | df3dcc1 |  | R2; R17 | your decisions are made before code starts | Dropped: R2 is a purpose clause with no absolute term and S6 sets up the exception; no contradiction. | outcome.md l.38 |
| 74 | df3dcc1 |  | R13; R14; S19 | nothing agreed is asked again | Dropped: R14 limits agreements to their scope, so a case outside it is not already agreed. | outcome.md l.38 |
| 74 | df3dcc1 |  | R14; R16 | agreements carry over | Dropped: agreements carry over within their scope; S4 and S19 take each side consistently. | outcome.md l.38 |
| 74 | df3dcc1 |  | L28 | answers questions … as its script says | Dropped: possibly describes scripting, but removing it wouldn't change what the user gets. | outcome.md l.16; SKILL.md l.18 |
| 74 | df3dcc1 |  | L26 definitions |  | Dropped: the link to decisions.md points to a reference and doesn't say where anything in the product lives. | outcome.md l.14; SKILL.md l.18 |
| 74 | df3dcc1 |  | S12; R2 | document meant for someone other than you | Dropped: that document is not a level document, so nothing contradicts 'one document per level'. | outcome.md l.38 |
| 74 | df3dcc1 |  | S2 | it surfaces | Dropped: where it surfaces is left to how the verification is built. | outcome.md l.20 |
| 74 | df3dcc1 |  | S8; R3 | as a choice | Dropped: S8 not checking the choice form is wording and doesn't change what the user gets. | SKILL.md l.18 |
| 75 | c74f108 |  | S15 | the project changes only after you confirm | Dropped: in context it follows 'on either instruction', so it is wording only. | skill line 18 |
| 75 | c74f108 |  | S13; L15 | against … what is agreed or codified | Dropped: the pass condition matches L15; the judge's reference set doesn't change what passes. | skill line 19 |
| 75 | c74f108 |  | L23; L9 | you're asked, and only then | Dropped: confirming what the user meant is something only they can settle that blocks the action; no contradiction. |  |
| 75 | c74f108 |  | L8; L23; S1 | your decisions are made before code starts | Dropped: L8 has no absolute term and the L23 exception belongs to a different requirement. | outcome.md line 38, line 34 |
| 75 | c74f108 |  | L12; L23 | only then | Dropped: a point that blocks nothing need not be settled, so nothing is guessed. |  |
| 75 | c74f108 |  | pass bar | Several times | Dropped: a threshold, which belongs to a later level. | outcome.md line 20 |
| 75 | c74f108 |  | L28 | Acceptance tests fail before the work and pass after it | Dropped as extra content concern: the scripted-user sentence and test rule describe what comes with the scenario, which is allowed. | outcome.md line 16 |
| 75 | c74f108 |  | S23 | before the requirement is treated as complete | Dropped: observable when built faithfully; that it could be built badly is not a finding. | skill line 19 |
| 75 | c74f108 |  | S18 | nothing you agreed or codified covers it | Dropped: an agreed requirement ruling out one choice doesn't decide the point; the expected result is clear. |  |
| 75 | c74f108 |  | S14; S17; L7; L22 |  | Dropped: passing a run that stalls and never asks for approval is fine since L7 and L22 are covered by other scenarios. | outcome.md line 37 |
| 75 | c74f108 |  | L60; L9 | Readings … taken without asking you | Dropped: 'reading' means choosing between interpretations, which L9 puts to the user anyway. |  |
| 75 | c74f108 |  | S12; L8 | a document meant for someone other than you | Dropped: S22 doesn't set up that need and nothing quoted shows a conflict with one document per level. |  |
| 76 | 6a08a16 | 5 | S15; R3 | the project changes only after you confirm | Dropped: the cell is scoped to 'either instruction', so no misjudged run is shown. | review SKILL.md L19; outcome.md L34 |
| 76 | 6a08a16 | 3 | S8; R3 | after the playback | Dropped: which playback is meant is a when-exactly question left to a later level. | outcome.md L20; SKILL.md L17 |
| 76 | 6a08a16 | 3/5 | S23 | treated as complete; the verification runs | Dropped: meanings are left to a later level; built faithfully the check runs the verification itself. | outcome.md L20, L30; SKILL.md L17, L19 |
| 76 | 6a08a16 | 5 | S17; S14 |  | Dropped: a run never asking for approval would pass, but R2/R10 only forbid early asking and S22 catches never asking. | outcome.md L34, L37; SKILL.md L19 |
| 76 | 6a08a16 | 6/5 | R2; S1; R17 |  | Dropped: R2 uses no absolute term; only the verified requirement's allowances count and S1's starting state leaves nothing blocking. | outcome.md L38, L34 |
| 76 | 6a08a16 | 6 | R16; R14 | Agreements carry over; holds only within its stated scope | Dropped: carrying over doesn't extend an agreement past its scope, so no exception. | outcome.md L38 |
| 76 | 6a08a16 | 6 | R13; S19; R14 | Nothing already agreed … is asked again | Dropped: outside its scope the earlier answer isn't agreed for that case. | outcome.md L38 |
| 76 | 6a08a16 | 3 | R14 | The next feature | Dropped: 'next' versus 'a later' feature is wording that doesn't change what the user gets. | SKILL.md L18 |
| 76 | 6a08a16 | 3 | S22 | exactly one document | Dropped: whether clash or decision records count as a level's document is a definition for a later level. | outcome.md L20 |
| 76 | 6a08a16 | 2 | L28 | Acceptance tests fail before the work and pass after it | Dropped: scripted-user description and test rule describe what comes with the scenario and don't change what the user gets. | outcome.md L16, L18; SKILL.md L18 |
| 76 | 6a08a16 | 2 | S12 |  | Dropped: listing the readability rules names what is checked, not how the judge tells cases apart. | outcome.md L16 |
| 76 | 6a08a16 | 5 | S8; R4 |  | Dropped: S8 needing a question at every level is fine since R4 requires an interview at every level. | outcome.md L32 |
| 77 | 6a08a16 |  | S5 | nothing the decision classification leaves unassigned arises | Dropped: ensuring no unclear point arises is how the scenario is scripted, a later level. | outcome.md L16, L20; SKILL.md L17 |
| 77 | 6a08a16 |  | S17; S14 |  | Dropped: they pass trivially if approval is never asked, but progress is verified by S3, S11, S22. | outcome.md L37 |
| 77 | 6a08a16 |  | S23 | before the requirement is treated as complete | Dropped: no observable event, but exact timing is for a later level. | outcome.md L20; SKILL.md L17 |
| 77 | 6a08a16 |  | S1 | each of your decisions | Dropped: the classification decides which are the user's; telling cases apart is test-building. | outcome.md L16; SKILL.md L17 |
| 77 | 6a08a16 |  | R2; R17; S6; S7 |  | Dropped: R2 uses no absolute term and S6/S7 starting states create the gap; no contradiction. | outcome.md L38; SKILL.md L19 |
| 77 | 6a08a16 |  | R13; R17 | for clarity; only then | Dropped: R13's exception limits only its own rule and doesn't override R17. | outcome.md L38; SKILL.md L19 |
| 77 | 6a08a16 |  | R13; R14; R16 |  | Dropped: read with scope, approval, carry-over and scope are consistent, as S4 and S19 show. | outcome.md L38 |
| 77 | 6a08a16 |  | L26; L16 | a wrong fact is a finding | Dropped: whether a wrong fact fails a level's standards depends on standards set at a later level. | outcome.md L20; SKILL.md L17 |
| 77 | 6a08a16 |  | S18 | nothing you agreed ... covers it | Dropped: ruling out one option doesn't settle the decision; no contradiction. | SKILL.md L19 |
| 77 | 6a08a16 |  | L28; R7 | Acceptance tests fail before the work and pass after it | Dropped: these state verification standards and results, not test-building or behaviour rules. | outcome.md L14, L16, L18 |
| 77 | 6a08a16 |  | R5; R10 |  | Dropped: at levels disallowing found facts there's no way to supply a needed fact; that point belongs to a later level. | outcome.md L20; SKILL.md L17 |
| 77 | 6a08a16 |  | L72 | The work's decisions that aren't recorded | Dropped: how measures are counted is a procedure for a later level. | outcome.md L20 |
| 78 | 6a08a16 |  | R2; R17; S1 |  | Dropped: R17 is a fallback with no absolute term and no explicit exception to R2; S1 checks R2 only. | outcome.md L34, L38 |
| 78 | 6a08a16 |  | R14; R16 | holds only within its stated scope; Agreements carry over to later features | Dropped: both can hold at once since agreements carry over within scope. | L38 |
| 78 | 6a08a16 |  | S23 | before the requirement is treated as complete; the verification runs once you settle it | Dropped: which observable event counts and timing are for a later level. | outcome.md L20 |
| 78 | 6a08a16 |  | S1 |  | Dropped: which decisions are 'yours' isn't listed, but the classification sets that; telling cases apart is test-building. | outcome.md L16 |
| 78 | 6a08a16 |  | S3; S8; S9; S12 | You approve each level only after it passes its review | Dropped: how the scripted user is scripted is for a later level; R4 guarantees interview questions. | L16, L20 |
| 78 | 6a08a16 |  | S14; S17 |  | Dropped: passing a stalled run is fine since other scenarios check progress; could-be-built-badly isn't a finding. | L37; skill L19 |
| 78 | 6a08a16 |  | L28 | scripted user answers... as its script says; Acceptance tests fail before... pass after | Dropped: they name what comes with the scenario and the testing standard, not test construction. | L16, L18; skill L18 |
| 78 | 6a08a16 |  | M3 (L60) | Readings of your words... taken without asking you | Dropped: 'reading' consistently means a choice between senses, so wording only. | skill L18 |
| 78 | 6a08a16 |  | S15; S12 |  | Dropped: a run can do playback, confirmation, then the choice, so no contradiction with one-question-at-a-time. |  |
| 78 | 6a08a16 |  | R8; R15; R10; R14 | Readable at a glance; where you can see them; a level that allows found facts; stated scope | Dropped: each needs a definition that a later level supplies. | L20 |
| 79 | 91babdc |  | R11; R10; S21 |  | Dropped: whether a project term counts as a found fact is a what-exactly-counts question for a later level. | outcome.md l.20; review skill l.17 |
| 79 | 91babdc |  | S23 | before the requirement is treated as complete | Dropped: pinning the observable event is how the verification is built, a later level. | outcome.md l.16, l.20 |
| 79 | 91babdc |  | S10; R7; R4 | before the level's document is written | Dropped: the scenario also verifies R4, which requires asking before the document is written. | outcome.md l.30, l.34 |
| 79 | 91babdc |  | S9 | uses the project's word only for the project's meaning | Dropped: recording the clash mentions the word without using it; a faithful judge tells them apart. | review skill l.19; outcome.md l.30 |
| 79 | 91babdc |  | S14; S17 |  | Dropped: passing a stalled run is fine; progress belongs to R1, covered by S1 and S22. | outcome.md l.37 |
| 79 | 91babdc |  | R17; R3 | only then | Dropped: a pending confirmation is itself something only the user can settle that blocks acting. | outcome.md l.38 |
| 79 | 91babdc |  | R13; R14; S19 | nothing already agreed... asked again | Dropped: R14 limits agreement to stated scope and S19 sets up a part outside it. | outcome.md l.38, l.29 |
| 79 | 91babdc |  | R16; R14 | agreements carry over; only within its stated scope | Dropped: R16 has no absolute term and scope reconciles them. | outcome.md l.38 |
| 79 | 91babdc |  | R2; S6; S7 | decisions are made before code starts | Dropped: S6/S7 set up approved levels missing a decision or with conflict, covered by R17. | outcome.md l.32, l.38 |
| 79 | 91babdc |  | R10; R7 |  | Dropped: whether a verification can be written without the fact at a no-found-facts level is for a later level. | outcome.md l.20 |
| 80 | 91babdc |  | S23 | before the requirement is treated as complete | Dropped: what counts as 'treated as complete' is a definition for a later level. | outcome.md L20; SKILL.md L17 |
| 80 | 91babdc |  | S23 | the verification runs once you settle it | Dropped: who runs it and when is how tests are built. | outcome.md L16, L20 |
| 80 | 91babdc |  | S18 | nothing you agreed or codified covers it | Dropped: ruling one choice out doesn't settle the decision; no contradiction. | SKILL.md L19; outcome.md L38 |
| 80 | 91babdc |  | S1; R17; R2 | Each of your decisions ... made by you before code starts | Dropped: R2 has no absolute term and R17's exception doesn't belong to S1's requirements. | outcome.md L34, L38 |
| 80 | 91babdc |  | M (L60); R3; R6 | Readings of your words ... taken without asking you | Dropped: whether a plain answer counts as a reading is for a later level; the measure verifies R6. | outcome.md L20, L34 |
| 80 | 91babdc |  | S17; L26 |  | Dropped: whether a finding means the review hasn't passed is a definition for a later level. | outcome.md L20; SKILL.md L17 |
| 80 | 91babdc |  | S14; S17 |  | Dropped: passing a stalled run is fine since progress is verified by S1, S3, S22. | outcome.md L37 |
| 80 | 91babdc |  | S7; L28 | fail before the work | Dropped: existing code passing tests is set by the scenario; could-be-built-badly isn't a finding. | SKILL.md L19 |
| 80 | 91babdc |  | S8; S9; S10; S23 |  | Dropped: if the work doesn't interview, R4 is broken and the scenario correctly fails. | outcome.md L32, L31 |
| 80 | 91babdc |  | S10 |  | Dropped: the shown thing possibly being an agreed decision rather than a fact is about scenario scripting. | outcome.md L16; SKILL.md L19 |
| 80 | 91babdc |  | S4 |  | Dropped: the second feature's approved earlier level is set up by the starting state. | outcome.md L32 |
| 80 | 91babdc |  | S22 | exactly one document | Dropped: decisions.md puts planning records in the level's document, so no conflict; exact definitions for later. | outcome.md L20 |
| 80 | 91babdc |  | L26; L28 | Acceptance tests fail before the work and pass after it | Dropped: a reference link and shared pass bar, not location or test-building content. | outcome.md L11, L16; SKILL.md L18 |
| 80 | 91babdc |  | S21; S13 |  | Dropped: the project's term used in place of the user's words is a wording question. | SKILL.md L18 |
| 80 | 91babdc |  | S3 | its level | Dropped: the script sets which level it is. | outcome.md L16 |
| 81 | 91babdc |  | S10; S20; R7; R6; R4 | before the level's document is written | Dropped: R7/R6 set no timing but R4 does, so the behaviour is ruled out. | outcome.md L34; review skill L19 |
| 81 | 91babdc |  | S17; L26 |  | Dropped: 'A wrong fact is a finding' reads plainly as the review not passing; no gap. | review skill L19 |
| 81 | 91babdc |  | S23 | before the requirement is treated as complete | Dropped as implementation check: observable signs exist; telling cases apart is test-building. | outcome.md L16, L20, L33; review skill L19 |
| 81 | 91babdc |  | S23 | the verification runs once you settle it | Dropped: can be built faithfully with the harness running it. | review skill L19 |
| 81 | 91babdc |  | S4 | an earlier level of the second feature is approved, including your answer to a question | Dropped: it is among the starting-state conditions, so the starting state sets it up. | outcome.md L32 |
| 81 | 91babdc |  | S3; R3 | no ... playback ... of a level | Dropped: catching an R3 playback of a later-level question would only be a bad build. | review skill L19 |
| 81 | 91babdc |  | S8; R3 | after the playback | Dropped: which playback is meant is a when-exactly question for a later level. | outcome.md L20; review skill L17 |
| 81 | 91babdc |  | S12; R5 | no question is sent before you answer the one before it | Dropped: whether a playback counts as a question is a definition for a later level. | outcome.md L20, L34 |
| 81 | 91babdc |  | R2; R17 | your decisions are made before code starts | Dropped: R2 has no absolute term and R17 is a fallback; only R2's allowances count for S1. | outcome.md L34, L38 |
| 81 | 91babdc |  | R9; R3; R12 | No statement ... can be read two ways | Dropped: a document can state a point as left open, so no contradiction. | outcome.md L38 |
| 81 | 91babdc |  | R16; R14 | Agreements carry over; holds only within its stated scope | Dropped: they reconcile as carrying over within scope; no absolute term. | outcome.md L38 |
| 81 | 91babdc |  | R3 | anything from you | Dropped: the plain-answer exception is in the same requirement, not another. | outcome.md L38 |
| 81 | 91babdc |  | S18 | nothing you agreed ... covers it | Dropped: ruling out one option doesn't settle the decision; starting state is consistent. | outcome.md L38; review skill L19 |
| 81 | 91babdc |  | S13; R9 | against ... what is agreed or codified | Dropped: the verification's own list matches R9; judge material doesn't widen what passes. | outcome.md L30 |
| 81 | 91babdc |  | L26 | ../../skills/references/decisions.md | Dropped: the link is wording and a reference that doesn't change what the user gets. | review skill L18 |
| 81 | 91babdc |  | L28; S12 |  | Dropped: describing the scripted user, kinds of check and judge rules names what comes with a scenario, which is allowed. | outcome.md L16 |
| 81 | 91babdc | 2 | R13; R14; R7 |  | Dropped as behaviour rules (criterion 2): they state observable results and removing them would change what's built. | outcome.md L14, L27 |
| 81 | 91babdc |  | S14; S17 |  | Dropped: passing a stalled run is fine since R1 is verified elsewhere. | outcome.md L37 |
| 82 | 3948a73 |  | R39 |  | Dropped: no Verifies column names R39, but the shared pass bar covers it; grouping is for a later level. | outcome.md 36 |
| 82 | 3948a73 |  | R37; R2; R38 | proceeds with everything it needs | Dropped: R38 is a fallback for states only S6/S7 set up; either reading builds the same thing. | skill 18 |
| 82 | 3948a73 |  | R21 |  | Dropped: R21 describing the review's mechanism still gives an observable result. |  |
| 82 | 3948a73 |  | R33; M15 |  | Dropped: each stating two things on one line doesn't change what the user gets. | skill 18 |
| 82 | 3948a73 |  | glossary | Complete verification; Decision classification | Dropped: unused glossary term and link to a file path don't change what gets built. | skill 18 |
| 82 | 3948a73 |  | preamble |  | Dropped: describing the scripted user is needed so no verification needs a person. | outcome.md 15, 23 |
| 82 | 3948a73 |  | S23 | before the requirement is treated as complete | Dropped: what counts as treated as complete is for a later level. | outcome.md 23, 27 |
| 82 | 3948a73 |  | S18 | nothing agreed covers it | Dropped: even if the requirement covers the decision, the pass condition still judges correctly. |  |
| 82 | 3948a73 |  | S12; M4 | readability rules | Dropped: the rules a judge applies come with the scenario. | outcome.md line 62 of the spec |
| 82 | 3948a73 |  | M3; R7 | readings … taken without asking | Dropped: in context it means readings the work guessed, not every act of understanding. |  |
| 82 | 3948a73 |  | M1; S19 |  | Dropped: under R30 the decision for the new part isn't already agreed. |  |
| 82 | 3948a73 |  | R35; R30 | agreements carry over | Dropped: reading 'carry over' as within scope makes them consistent. |  |
| 82 | 3948a73 |  | S22; S5 |  | Dropped: whether Build counts as a level is unstated, so left to a later level. | skill 17 |
| 82 | 3948a73 |  | S10; R10 | asked nothing for it | Dropped: a playback is not asking for the fact. |  |
| 82 | 3948a73 |  | R22; S21 | uses the project's terms | Dropped: it plainly requires naming the concept with the project's term. |  |
| 83 | 4bc74af |  | R39 |  | Dropped: not in any Verifies column, but covered by the shared pass bar. | outcome.md lines 15, 36 |
| 83 | 4bc74af |  | S11; S22; S2; R1; R9 |  | Dropped: labels listing unchecked requirements don't change anything; R1 and R9 are covered elsewhere. | SKILL.md line 18; outcome.md line 36 |
| 83 | 4bc74af |  | R2; R15; R33; R38 |  | Dropped: lines stating more than one thing; splitting wouldn't change what's built. | SKILL.md lines 3, 18 |
| 83 | 4bc74af |  | glossary |  | Dropped: the decisions.md link points to a definition, not where parts of the feature live. | SKILL.md line 19 |
| 83 | 4bc74af |  | S12; M4 | Framework; level; codified; the readability rules | Dropped: undefined terms; what exactly counts is for a later level. | outcome.md line 27; SKILL.md line 17 |
| 83 | 4bc74af |  | R7; R8 |  | Dropped: which playback the choice follows is a when-exactly question for a later level. | outcome.md line 27 |
| 83 | 4bc74af |  | R2; R38; S6; S7 | decisions are made before code starts | Dropped: R2 uses no absolute term and S1 judges only against R2's allowances. | outcome.md lines 41, 45 |
| 83 | 4bc74af |  | S18; R31 | its choice is the first feature's; preferred default | Dropped: the starting state rules out reasons in the second feature and no other reason is shown. | SKILL.md line 19; outcome.md line 41 |
| 83 | 4bc74af |  | S14; S17; R4; R21 |  | Dropped: they fail whenever R4/R21 break in their own case; sampling cases isn't a finding. | SKILL.md line 19 |
| 83 | 4bc74af |  | S3; S13 | only after it passes its review; says nothing about a point | Dropped: how the user is scripted is for a later level. | outcome.md lines 23, 27 |
| 83 | 4bc74af |  | S21; R22 | uses the project's terms | Dropped: the natural reading requires the term, so no misjudgement shown. | SKILL.md line 19 |
| 83 | 4bc74af |  | R25; R20; S12; R3 |  | Dropped: the clash record location and which level produces extra documents aren't stated, so no conflict shown. | SKILL.md line 19 |
| 83 | 4bc74af |  | M10 |  | Dropped: timing of whether a fact counts as wrong is how the measure is computed, a later level. | outcome.md line 27 |
| 84 | 757428e |  | R39 |  | Dropped: not in any Verifies column but covered by the shared pass bar. | outcome.md line 36 |
| 84 | 757428e |  | R1; S11; S22 |  | Dropped: a wrong label doesn't change what the user gets; S1 and S5 cover R1. |  |
| 84 | 757428e |  | R10; S8; S9 |  | Dropped: how full a playback must be is a threshold for a later level. | outcome.md line 27 |
| 84 | 757428e |  | R8; R7 | after the playback | Dropped: which playback precedes the choice is a when-exactly question for a later level. |  |
| 84 | 757428e |  | R37; R38; S5; S7 | Something only the user can settle; the user's to settle | Dropped: used the same way, so wording only. |  |
| 84 | 757428e |  | R15 |  | Dropped: several things on one line, each covered elsewhere; doesn't change what the user gets. |  |
| 84 | 757428e |  | glossary |  | Dropped: the decisions.md link defines a term, not where anything built lives. |  |
| 84 | 757428e |  | glossary; R16; S10; S23 | Complete requirement; Complete verification | Dropped: defined but unused terms are wording only. |  |
| 84 | 757428e |  | M4 | codified; readability rules | Dropped: undefined terms, found-fact levels and standards are definitions for later levels. | outcome.md line 27 |
| 84 | 757428e |  | scenario intro |  | Dropped: the scripted-user sentence states what comes with the scenario. | outcome.md line 23 |
| 84 | 757428e |  | S2; S3 | no question … of a level | Dropped: both are only ways a verification could be built badly. | SKILL.md line 19 |
| 84 | 757428e |  | S20; S21 |  | Dropped: no explicit event, but the event is the level being worked; wording only. |  |
| 84 | 757428e |  | R2; R38 |  | Dropped: R38 applies only once R2 has failed; no absolute term excepted. |  |
| 84 | 757428e |  | R38; R6 | only then | Dropped: confirming what the user meant is itself something only they can settle. |  |
| 85 | e763ee9 (working tree before commit) |  | R39 |  | Dropped: no scenario row, but the shared pass bar covers it. | outcome.md line 36; SKILL.md line 19 |
| 85 | e763ee9 (working tree before commit) |  | S14; S17; R4; R21 | the user is asked to approve it | Dropped: never asking for approval breaks R1 under a scripted user, so it's ruled out. | outcome.md line 41 |
| 85 | e763ee9 (working tree before commit) |  | S8; R10 |  | Dropped: S8 doesn't test playback content, but completeness needs a later-level definition. | outcome.md line 27; SKILL.md line 17 |
| 85 | e763ee9 (working tree before commit) |  | R3; R25; R33; S12 | document meant for someone else | Dropped: what counts as a document is for a later level; no conflict shown. | outcome.md line 27; SKILL.md line 17 |
| 85 | e763ee9 (working tree before commit) |  | R15; R33 |  | Dropped: several parts on one line is wording only. | SKILL.md line 18 |
| 85 | e763ee9 (working tree before commit) |  | glossary | Complete requirement; Complete verification | Dropped: unused glossary entries are wording only. | SKILL.md line 18 |
| 85 | e763ee9 (working tree before commit) |  | R37; R38; S5 | Only the user can settle; the user's to settle | Dropped: plain reading is clear and changes nothing built. | SKILL.md line 18 |
| 85 | e763ee9 (working tree before commit) |  | R38; R6; R8 | only then | Dropped: confirming how the user is read is the user's to settle and blocks acting; no conflict. | SKILL.md line 19 |
| 85 | e763ee9 (working tree before commit) |  | S16; R12 |  | Dropped: S16 not checking R12 is fine since S10 covers it. | outcome.md line 44 |
| 85 | e763ee9 (working tree before commit) |  | S23 | the verification runs once the user settles it | Dropped: how that verification is built and run belongs to a later level. | outcome.md lines 23, 27 |
| 86 | 6e9d907 |  | S2; R2; R9 | It surfaces before code starts | Dropped: the invariant isn't shown to fall outside what a level needs, so no misjudged run. | SKILL.md line 19; outcome.md line 41 |
| 86 | 6e9d907 |  | R39 |  | Dropped: no Verifies entry, but covered by the shared pass bar. | outcome.md line 36 |
| 86 | 6e9d907 |  | S14; S17 | once it meets the standard / no longer does, the user is asked to approve it | Dropped: read as 'eventually asked', a correct run passes. | SKILL.md line 19 |
| 86 | 6e9d907 |  | S16 | no level that doesn't allow found facts holds it | Dropped: which levels allow found facts is left to a later level. | SKILL.md line 17; outcome.md line 27 |
| 86 | 6e9d907 |  | R15; R33 |  | Dropped: more than one result on a line; splitting doesn't change what the user gets. | SKILL.md line 18 |
| 86 | 6e9d907 |  | glossary | Complete requirement; Complete verification | Dropped: defined but unused terms are wording only. | SKILL.md line 18 |
| 86 | 6e9d907 |  | R2; R37; R38; S5 | something only the user can settle | Dropped: plain in context; any finer definition belongs to a later level. | outcome.md line 27 |
| 86 | 6e9d907 |  | R30 | stated scope | Dropped: resolving a missing stated scope needs a rule from a later level. | outcome.md line 27 |
| 86 | 6e9d907 |  | line 62 | Acceptance tests fail before the work and pass after it | Dropped: they establish no verification needs a person and name what comes with each scenario. | outcome.md lines 15, 23 |
| 86 | 6e9d907 |  | glossary |  | Dropped: the decisions.md link defines a term; removing it changes nothing for the user. | SKILL.md line 18 |
| 86 | 6e9d907 |  | S12; R3 | document meant for someone else | Dropped: no text shows a level produces that document, so no contradiction. | SKILL.md line 19 |
| 86 | 6e9d907 |  | M3 | Readings ... taken without asking | Dropped: read in the sense of 'Nothing is guessed', so it doesn't count unambiguous words. | SKILL.md line 19 |
| 86 | 6e9d907 |  | R7; R8; R10 | after the playback | Dropped: R8's playback is the level playback, so R7 and R8 don't contradict. | outcome.md line 45 |
| 87 | ea5e697 |  | R39 |  | Dropped: no Verifies row, but the shared pass bar covers it. | outcome.md line 36 |
| 87 | ea5e697 |  | S11; S22; R1 |  | Dropped: they list R1 without checking code, but S1 and S5 cover R1. | SKILL.md line 18 |
| 87 | ea5e697 |  | S16; R12 |  | Dropped: S1 and S10 cover R12. | outcome.md line 44 |
| 87 | ea5e697 |  | R2; S1; S5; R9; R16 | something only the user can settle that still blocks the work after code starts | Dropped: starting states rule out the broad reading and R9/R16 force asking; nothing built changes. |  |
| 87 | ea5e697 |  | R2; R37; R38 | Only the user can settle; the user's to settle | Dropped: S6, S7 and decisions.md put the same cases with the user; wording only. | decisions.md lines 25, 28 |
| 87 | ea5e697 |  | R20 | allow found facts | Dropped: which levels allow found facts belongs to a later level. | outcome.md line 27 |
| 87 | ea5e697 |  | S12; M4 | Readable at a glance; several times; readability rules | Dropped: thresholds and judge rules belong to a later level or come with the scenario. | outcome.md lines 23, 27 |
| 87 | ea5e697 |  | glossary | skills/references/decisions.md | Dropped: the link defines a term and doesn't change what the user gets. |  |
| 87 | ea5e697 |  | R18; S13 | agreed or codified | Dropped: codified rules need the user, so they read as agreed; nothing built changes. | decisions.md line 10 |
| 87 | ea5e697 |  | R22; S21 | uses the project's terms | Dropped: natural reading is adopting the terms; S9 and S21 agree. |  |
| 87 | ea5e697 |  | R15; R20; R33 | each line states one requirement | Dropped: multiple clauses per line is wording only. | SKILL.md line 18 |
| 87 | ea5e697 |  | preamble | acceptance tests fail before the work and pass after it | Dropped: naming check kind, pass bar and scenario contents is allowed. | outcome.md lines 23, 25 |
| 87 | ea5e697 |  | S14; S17 | once it meets the standard … the user is asked to approve it | Dropped: possible clash with other review failures is only a bad-build concern. | SKILL.md line 19 |
| 87 | ea5e697 |  | S6 |  | Dropped: approved levels with an unmade decision are set up by the starting state itself. | outcome.md line 39 |

## Appendix B: instruction files as each run read them


## skills/review-outcome/SKILL.md @ blob 7cab4de

```
---
name: review-outcome
description: Review a feature's Outcome document on its own and report findings that would change what gets built. Use at the Outcome gate, given only the Outcome document.
---

# Review an Outcome

Read [the Outcome definition](../references/outcome.md). Review the Outcome document you are given against it, on its own. Do not judge whether it matches any discussion or context that produced it.

## Method

Before judging, list for yourself every claim, scenario and measure, and map each claim to the scenarios that would fail without it. Then judge the document against each of the definition's six criteria.

## Findings

- A finding names the criterion it fails and quotes the document.
- A point the definition leaves to a later level is not a finding.
- Wording that doesn't change what the user gets is not a finding.
- Drop anything the quoted text doesn't show: perfection is the enemy of done. For criteria 4 and 5, the text shows a finding when a claim has no scenario, or when a check's own words would misjudge the result. A way the work could game a check, or a check built badly, is not shown by the text.
- Impact is high if the user might not get the intended result, and medium if only a check or measure is affected.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Output

- Trace map: each claim to its scenarios, one line each.
- Criteria 1-6: PASS or FINDINGS for each.
- Findings: id, criterion, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
```

## skills/references/outcome.md @ blob 42a5119

```
# Outcome

An Outcome states what the user gets and how success is judged. It is the first planning level of a feature.

## Contents

An Outcome contains:

- Who the feature is for.
- What it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated check and a pass bar. No check needs a person.
- How success is measured on real use, each measure with a target.

An Outcome does not contain non-goals, behaviour rules, edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

A scenario states its starting state, what happens and what passes, as results you can observe. How the scenario is scripted, and how a check tells one case from another, is how tests are built.

An Outcome leaves room for interpretation; later levels narrow it. A point that needs a definition, rule, threshold or procedure to resolve (what exactly counts as X, when exactly Y happens, how much work stops, how a scenario is scripted or a check is built) belongs to a later level.

## Criteria

A sound Outcome meets all six.

1. Complete. Every required element is present.
2. Nothing extra. Nothing is present that the Outcome isn't responsible for.
3. Clear. For every statement, a reader knows what result the user is meant to get.
4. Traceable. Every part of every claim has a scenario whose check fails if that part is broken. Every scenario and measure checks a claim. An allowance, something a claim permits but does not require, needs no scenario of its own.
5. Sound checks. Taking each check as built faithfully at a later level, and judged against the claims it traces to, no check or measure:
   - passes when the user doesn't get the result;
   - passes because the scenario never brings about what the claim is about;
   - fails or counts against behaviour a claim requires or allows. Each allowance or exception a scenario touches is either ruled out by its starting state or carried into its whole check, and each one a measure touches is carried into it;
   - can be satisfied by the work being judged;
   - compares against an expected result that the scenario doesn't set before the run;
   - leaves its starting state to the work being judged instead of setting it.

   A scenario need not re-check a claim that another scenario covers.
6. Consistent. No claims, scenarios, measures or definitions contradict each other.
```

## skills/references/outcome.md @ blob 16aa743

```
# Outcome

An Outcome states what the user gets and how success is judged. It is the first planning level of a feature.

## Contents

An Outcome contains:

- Who the feature is for.
- What it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated check and a pass bar. No check needs a person. A pass bar that applies to every scenario, such as how many runs must pass, is stated once.
- How success is measured on real use, each measure with a target.

An Outcome does not contain non-goals, behaviour rules, edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

A scenario states its starting state, what happens and what passes, as results you can observe. How the scenario is scripted, and how a check tells one case from another, is how tests are built.

An Outcome leaves room for interpretation; later levels narrow it. A point that needs a definition, rule, threshold or procedure to resolve (what exactly counts as X, when exactly Y happens, how much work stops, how a scenario is scripted or a check is built) belongs to a later level.

## Criteria

A sound Outcome meets all six.

1. Complete. Every required element is present.
2. Nothing extra. Nothing is present that the Outcome isn't responsible for.
3. Clear. For every statement, a reader knows what result the user is meant to get.
4. Traceable. Every part of every claim has a scenario whose check fails if that part is broken. Every scenario and measure checks a claim. An allowance, something a claim permits but does not require, needs no scenario of its own.
5. Sound checks. Taking each check as built faithfully at a later level, and judged against the claims it traces to, no check or measure:
   - passes when the user doesn't get the result;
   - passes because the scenario never brings about what the claim is about;
   - fails or counts against behaviour a claim requires or allows. Each allowance or exception a scenario touches is either ruled out by its starting state or carried into its whole check, and each one a measure touches is carried into it;
   - can be satisfied by the work being judged;
   - compares against an expected result that the scenario doesn't set before the run;
   - leaves its starting state to the work being judged instead of setting it.

   A scenario need not re-check a claim that another scenario covers.
6. Consistent. No claims, scenarios, measures or definitions contradict each other.
```

## skills/review-outcome/SKILL.md @ blob 611f58f

```
---
name: review-outcome
description: Review a feature's Outcome document on its own and report findings that would change what gets built. Use at the Outcome gate, given only the Outcome document.
---

# Review an Outcome

Read [the Outcome definition](../references/outcome.md). Review the Outcome document you are given against it, on its own. Do not judge whether it matches any discussion or context that produced it.

## Method

Before judging, list for yourself every requirement, scenario and measure, and map each requirement to the scenarios whose verification would fail without it. Then judge the document against each of the definition's six criteria.

## Findings

- A finding names the criterion it fails and quotes the document.
- A point the definition leaves to a later level is not a finding.
- Wording that doesn't change what the user gets is not a finding.
- Drop anything the quoted text doesn't show: perfection is the enemy of done. For criteria 4 and 5, the text shows a finding when a requirement has no scenario, or when a verification's own words, built faithfully, would misjudge the result. A verification that tests implementation instead of the behaviour the user observes is a finding. A verification that could be built badly is not.
- Impact is high if the user might not get the intended result, and medium if only a verification or measure is affected.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Output

- Trace map: each requirement to its scenarios, one line each.
- Criteria 1-6: PASS or FINDINGS for each.
- Findings: id, criterion, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
```

## skills/references/outcome.md @ blob ec1968e

```
# Outcome

An Outcome states what the user gets and how success is judged. It is the first planning level of a feature.

## Contents

An Outcome contains:

- Who the feature is for.
- Its requirements: what it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated verification and a pass bar. No verification needs a person. A pass bar that applies to every scenario, such as how many runs must pass, is stated once.
- How success is measured on real use, each measure with a target.

An Outcome does not contain non-goals, behaviour rules, edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

A scenario states its starting state, what happens and what passes, as results you can observe. How the scenario is scripted, and how a verification tells one case from another, is how tests are built. Naming a verification's kind, its pass bar, and what comes with the scenario is not.

Verifications are automated tests held to normal testing standards. Each tests the behaviour the user observes, not how it is implemented, and passes or fails on its own, independent of every other verification.

An Outcome leaves room for interpretation; later levels narrow it. A point that needs a definition, rule, threshold or procedure to resolve (what exactly counts as X, when exactly Y happens, how much work stops, how a scenario is scripted or a verification is built) belongs to a later level.

## Criteria

A sound Outcome meets all six.

1. Complete. Every required element is present.
2. Nothing extra. Nothing is present that the Outcome isn't responsible for.
3. Clear. For every statement, a reader knows what result the user is meant to get.
4. Traceable. Every part of every requirement has a scenario whose verification fails if that part is broken. A requirement that holds across levels, people or features needs one verification, unless the requirement itself says the cases differ; asking for a copy per case is not a finding. Every scenario and measure verifies a requirement. An allowance, something a requirement permits but does not require, needs no scenario of its own.
5. Sound verifications. Each verification is judged by its own words against the requirement it verifies, taken as built faithfully at a later level. No verification or measure:
   - passes when the user doesn't get the result;
   - relies on the work to produce anything it needs before its event, such as a failing draft, a defect, a decision or an earlier feature;
   - tests how the result is implemented instead of the behaviour the user observes, for example by reading the system's own log or report that it succeeded;
   - fails or counts against behaviour the requirement it verifies requires or allows. Only that requirement's allowances and exceptions count, and each one the starting state could bring about is either ruled out by the starting state or carried into the verification;
   - compares against an expected result that the scenario doesn't set before the run.

   A scenario need not re-verify a requirement that another scenario covers.
6. Consistent. No requirements, scenarios, measures or definitions contradict each other. An absolute term (every, never, only, always, all, none) means no exceptions, so an absolute requirement that another requirement makes an exception to is a contradiction.
```

## skills/review-outcome/SKILL.md @ blob 2792413

```
---
name: review-outcome
description: Review a feature's Outcome document on its own and report findings that would change what gets built. Use at the Outcome gate, given only the Outcome document.
---

# Review an Outcome

Read [the Outcome definition](../references/outcome.md). Review the Outcome document you are given against it, on its own. Do not judge whether it matches any discussion or context that produced it.

## Method

Before judging, list for yourself every requirement, scenario and measure, and map each requirement to the scenarios whose verification would fail without it. Then judge the document against each of the definition's six criteria.

## Findings

- A finding names the criterion it fails and quotes the document.
- A point the definition leaves to a later level is not a finding.
- Wording that doesn't change what the user gets is not a finding.
- Drop anything the quoted text doesn't show: perfection is the enemy of done. For criteria 4 and 5, the text shows a finding when a requirement has no verification that fails if it isn't met, or when a verification's own words, built faithfully, would misjudge the result. A verification that tests implementation instead of the behaviour the user observes is a finding. A verification that could be built badly is not.
- Impact is high if the user might not get the intended result, and medium if only a verification or measure is affected.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Output

- Trace map: each requirement to its scenarios, one line each.
- Criteria 1-6: PASS or FINDINGS for each.
- Findings: id, criterion, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
```

## skills/references/outcome.md @ blob 545e7b8

```
# Outcome

An Outcome states what the user gets and how success is judged. It is the first planning level of a feature.

## Contents

An Outcome contains:

- Who the feature is for.
- Its requirements: what it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated verification and a pass bar. No verification needs a person. A pass bar that applies to every scenario, such as how many runs must pass, is stated once.
- How success is measured on real use, each measure with a target.

An Outcome does not contain non-goals, behaviour rules, edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

A scenario states its starting state, what happens and what passes, as results you can observe. How the scenario is scripted, and how a verification tells one case from another, is how tests are built. Naming a verification's kind, its pass bar, and what comes with the scenario is not.

Verifications are automated tests held to normal testing standards. Each tests the behaviour the user observes, not how it is implemented, and passes or fails on its own, independent of every other verification.

An Outcome leaves room for interpretation; later levels narrow it. A point that needs a definition, rule, threshold or procedure to resolve (what exactly counts as X, when exactly Y happens, how much work stops, how a scenario is scripted or a verification is built) belongs to a later level.

## Criteria

A sound Outcome meets all six.

1. Complete. Every required element is present.
2. Nothing extra. Nothing is present that the Outcome isn't responsible for.
3. Clear. For every statement, a reader knows what result the user is meant to get.
4. Traceable. Every requirement is covered by a verification that fails if the requirement isn't met. How verifications are split, grouped or structured, such as one per listed item or one per level, person or feature, is for a later level; asking for a different structure is not a finding. Every scenario and measure verifies a requirement. An allowance, something a requirement permits but does not require, needs no scenario of its own.
5. Sound verifications. Each verification is judged by its own words against the requirement it verifies, taken as built faithfully at a later level. No verification or measure:
   - passes when the user doesn't get the result;
   - relies on the work to have produced anything it needs before its event, such as a failing draft, a defect, a decision or an earlier feature. A starting state that sets these up itself is not a finding;
   - tests how the result is implemented instead of the behaviour the user observes, for example by reading the system's own log or report that it succeeded;
   - fails or counts against behaviour the requirement it verifies requires or allows. Only that requirement's allowances and exceptions count, and each one the starting state could bring about is either ruled out by the starting state or carried into the verification;
   - compares against an expected result that the scenario doesn't set before the run.

   A scenario need not re-verify a requirement that another scenario covers.
6. Consistent. No requirements, scenarios, measures or definitions contradict each other. An absolute term (every, never, only, always, all, none) means no exceptions, so an absolute requirement that another requirement makes an exception to is a contradiction.
```

## skills/references/outcome.md @ blob 00d00e2

```
# Outcome

An Outcome states what the user gets and how success is judged. It is the first planning level of a feature.

## Contents

An Outcome contains:

- Who the feature is for.
- Its requirements: what it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated verification and a pass bar. No verification needs a person. A pass bar that applies to every scenario, such as how many runs must pass, is stated once.
- How success is measured on real use, each measure with a target.

An Outcome does not contain non-goals, behaviour rules, edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

A scenario states its starting state, what happens and what passes, as results you can observe. How the scenario is scripted, and how a verification tells one case from another, is how tests are built. Naming a verification's kind, its pass bar, and what comes with the scenario is not.

Verifications are automated tests held to normal testing standards. Each tests the behaviour the user observes, not how it is implemented, and passes or fails on its own, independent of every other verification.

An Outcome leaves room for interpretation; later levels narrow it. A point that needs a definition, rule, threshold or procedure to resolve (what exactly counts as X, when exactly Y happens, how much work stops, how a scenario is scripted or a verification is built) belongs to a later level.

## Criteria

A sound Outcome meets all six.

1. Complete. Every required element is present.
2. Nothing extra. Nothing is present that the Outcome isn't responsible for.
3. Clear. For every statement, a reader knows what result the user is meant to get.
4. Traceable. Every requirement is covered by a verification that fails if the requirement isn't met. How verifications are split, grouped or structured, such as one per listed item or one per level, person or feature, is for a later level; asking for a different structure is not a finding. Every scenario and measure verifies a requirement. An allowance, something a requirement permits but does not require, needs no scenario of its own.
5. Sound verifications. Each verification is judged by its own words against the requirement it verifies, taken as built faithfully at a later level. No verification or measure:
   - passes when the user doesn't get the result;
   - relies on the work to have produced anything it needs before its event, such as a failing draft, a defect, a decision or an earlier feature. A starting state that sets these up itself is not a finding;
   - tests how the result is implemented instead of the behaviour the user observes, for example by reading the system's own log or report that it succeeded;
   - fails or counts against behaviour the requirement it verifies requires or allows. Only that requirement's allowances and exceptions count, and each one the starting state could bring about is either ruled out by the starting state or carried into the verification;
   - compares against an expected result that the scenario doesn't set before the run.

   A scenario need not re-verify a requirement that another scenario covers.
6. Consistent. No requirements, scenarios, measures or definitions contradict each other. An absolute term, such as every, never, only, always, all, none, any or anything, means no exceptions, so an absolute requirement that another requirement makes an exception to is a contradiction.
```

## skills/review-outcome/SKILL.md @ blob 5ac0393

```
---
name: review-outcome
description: Review a feature's Outcome document on its own and report findings that would change what gets built. Use at the Outcome gate, given only the Outcome document.
---

# Review an Outcome

Read [the Outcome definition](../references/outcome.md). Review the Outcome document you are given against it, on its own. Do not judge whether it matches any discussion or context that produced it.

## Method

Before judging, list for yourself every requirement, scenario and measure, and map each requirement to the scenarios whose verification would fail without it. List every absolute term in every sentence of every requirement and definition, and check each against every other requirement for an exception. Then judge the document against each of the definition's six criteria.

## Findings

- A finding names the criterion it fails and quotes the document.
- A point the definition leaves to a later level is not a finding.
- Wording that doesn't change what the user gets is not a finding.
- Drop anything the quoted text doesn't show: perfection is the enemy of done. For criteria 4 and 5, the text shows a finding when a requirement has no verification that fails if it isn't met, or when a verification's own words, built faithfully, would misjudge the result. A verification that tests implementation instead of the behaviour the user observes is a finding. A verification that could be built badly is not.
- Impact is high if the user might not get the intended result, and medium if only a verification or measure is affected.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Output

- Trace map: each requirement to its scenarios, one line each.
- Criteria 1-6: PASS or FINDINGS for each.
- Findings: id, criterion, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
```

## skills/review-outcome/SKILL.md @ blob 808b23d

```
---
name: review-outcome
description: Review a feature's Outcome document on its own and report findings that would change what gets built. Use at the Outcome gate, given only the Outcome document.
---

# Review an Outcome

Read [the Outcome definition](../references/outcome.md). Review the Outcome document you are given against it, on its own. Do not judge whether it matches any discussion or context that produced it.

## Method

Before judging, list for yourself every requirement, scenario and measure, and map each requirement to the scenarios whose verification would fail without it. List every absolute term in every sentence of every requirement and definition, and check each against every other requirement for an exception. For each check in a scenario or measure, find the requirement words that rule out what it fails; a requirement allows whatever its words don't rule out. Then judge the document against each of the definition's six criteria.

## Findings

- A finding names the criterion it fails and quotes the document.
- A point the definition leaves to a later level is not a finding.
- Wording that doesn't change what the user gets is not a finding.
- Drop anything the quoted text doesn't show: perfection is the enemy of done. For criteria 4 and 5, the text shows a finding when a requirement has no verification that fails if it isn't met, or when a verification's own words, built faithfully, would misjudge the result. A verification that tests implementation instead of the behaviour the user observes is a finding. A verification that could be built badly is not.
- Impact is high if the user might not get the intended result, and medium if only a verification or measure is affected.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Output

- Trace map: each requirement to its scenarios, one line each.
- Criteria 1-6: PASS or FINDINGS for each.
- Findings: id, criterion, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
```

## skills/references/outcome.md @ blob a1155df

```
# Outcome

An Outcome states what the user gets and how success is judged. It is the first planning level of a feature.

## Contents

An Outcome contains:

- Who the feature is for.
- Its requirements: what it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated verification and a pass bar. No verification needs a person. A pass bar that applies to every scenario, such as how many runs must pass, is stated once.
- How success is measured on real use, each measure with a target.

An Outcome does not contain non-goals, behaviour rules, edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

A scenario states its starting state, what happens and what passes, as results you can observe. How the scenario is scripted, and how a verification tells one case from another, is how tests are built. Naming a verification's kind, its pass bar, and what comes with the scenario is not.

Verifications are automated tests held to normal testing standards. Each tests the behaviour the user observes, not how it is implemented, and passes or fails on its own, independent of every other verification.

An Outcome leaves room for interpretation; later levels narrow it. A point that needs a definition, rule, threshold or procedure to resolve (what exactly counts as X, when exactly Y happens, how much work stops, how a scenario is scripted or a verification is built) belongs to a later level.

## Criteria

A sound Outcome meets all six.

1. Complete. Every required element is present.
2. Nothing extra. Nothing is present that the Outcome isn't responsible for.
3. Clear. For every statement, a reader knows what result the user is meant to get.
4. Traceable. Every requirement is covered by a verification that fails if the requirement isn't met. How verifications are split, grouped or structured, such as one per listed item or one per level, person or feature, is for a later level; asking for a different structure is not a finding. Every scenario and measure verifies a requirement. An allowance, something a requirement permits but does not require, needs no scenario of its own. A requirement allows whatever its words don't rule out.
5. Sound verifications. Each verification is judged by its own words against the requirement it verifies, taken as built faithfully at a later level. No verification or measure:
   - passes when the user doesn't get the result;
   - relies on the work to have produced anything it needs before its event, such as a failing draft, a defect, a decision or an earlier feature. A starting state that sets these up itself is not a finding;
   - tests how the result is implemented instead of the behaviour the user observes, for example by reading the system's own log or report that it succeeded;
   - fails or counts against behaviour the requirement it verifies requires or allows. Only that requirement's allowances and exceptions count, and each one the starting state could bring about is either ruled out by the starting state or carried into the verification;
   - compares against an expected result that the scenario doesn't set before the run.

   A scenario need not re-verify a requirement that another scenario covers.
6. Consistent. No requirements, scenarios, measures or definitions contradict each other. An absolute term, such as every, never, only, always, all, none, any or anything, means no exceptions, so an absolute requirement that another requirement makes an exception to is a contradiction.
```

## skills/review-outcome/SKILL.md @ blob 421336d

```
---
name: review-outcome
description: Review a feature's Outcome document on its own and report findings that would change what gets built. Use at the Outcome gate, given only the Outcome document.
---

# Review an Outcome

Read [the Outcome definition](../references/outcome.md). Review the Outcome document you are given against it, on its own. Do not judge whether it matches any discussion or context that produced it.

## Method

Before judging, list for yourself every requirement, scenario and measure, and map each requirement to the scenarios whose verification would fail without it. List every absolute term in every sentence of every requirement and definition, and check each against every other requirement for an exception. For each check in a scenario or measure, quote the requirement words that rule out what it fails, and confirm that a run doing the failed behaviour would break them. Words on the same subject that don't forbid it are not enough; a requirement allows whatever its words don't rule out. Then judge the document against each of the definition's six criteria.

## Findings

- A finding names the criterion it fails and quotes the document.
- A point the definition leaves to a later level is not a finding.
- Wording that doesn't change what the user gets is not a finding.
- Drop anything the quoted text doesn't show: perfection is the enemy of done. For criteria 4 and 5, the text shows a finding when a requirement has no verification that fails if it isn't met, or when a verification's own words, built faithfully, would misjudge the result. A verification that tests implementation instead of the behaviour the user observes is a finding. A verification that could be built badly is not.
- Impact is high if the user might not get the intended result, and medium if only a verification or measure is affected.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Rounds

A round starts with one run of this review. When it reports no findings, two more run independently, and the round passes when all three report none. When the first run reports findings, the round ends there and the findings are fixed before the next round.

## Output

- Trace map: each requirement to its scenarios, one line each.
- Criteria 1-6: PASS or FINDINGS for each.
- Findings: id, criterion, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
```

## skills/review-outcome/SKILL.md @ blob cc8b1d0

```
---
name: review-outcome
description: Review a feature's Outcome document on its own and report findings that would change what gets built. Use at the Outcome gate, given only the Outcome document.
---

# Review an Outcome

Read [the Outcome definition](../references/outcome.md). Review the Outcome document you are given against it, on its own. Do not judge whether it matches any discussion or context that produced it.

## Method

Before judging, list for yourself every requirement, scenario and measure, and map each requirement to the scenarios whose verification would fail without it. Then judge the document against each of the definition's six criteria.

## Findings

- A finding names the criterion it fails and quotes the document.
- A point the definition leaves to a later level is not a finding.
- Wording that doesn't change what the user gets is not a finding.
- Drop anything the quoted text doesn't show: perfection is the enemy of done. For criteria 4 and 5, the text shows a finding when a requirement has no verification that fails if it isn't met, or when a verification's own words, built faithfully, would misjudge the result. A verification that tests implementation instead of the behaviour the user observes is a finding. A verification that could be built badly is not.
- Impact is high if the user might not get the intended result, and medium if only a verification or measure is affected.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Rounds

A round starts with one run of this review. When it reports no findings, two more run independently, and the round passes when all three report none. When the first run reports findings, the round ends there and the findings are fixed before the next round.

## Output

- Trace map: each requirement to its scenarios, one line each.
- Criteria 1-6: PASS or FINDINGS for each.
- Findings: id, criterion, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
```

## skills/references/outcome.md @ blob e407f70

```
# Outcome

An Outcome states what the user gets and how success is judged. It is the first planning level of a feature.

## Contents

An Outcome contains:

- Who the feature is for.
- Its requirements: what it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated verification and a pass bar. No verification needs a person. A pass bar that applies to every scenario, such as how many runs must pass, is stated once.
- How success is measured on real use, each measure with a target.

An Outcome does not contain non-goals, behaviour rules, edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

A scenario states its starting state, what happens and what passes, as results you can observe. How the scenario is scripted, and how a verification tells one case from another, is how tests are built. Naming a verification's kind, its pass bar, and what comes with the scenario is not.

Verifications are automated tests held to normal testing standards. Each tests the behaviour the user observes, not how it is implemented, and passes or fails on its own, independent of every other verification.

An Outcome leaves room for interpretation; later levels narrow it. A point that needs a definition, rule, threshold or procedure to resolve (what exactly counts as X, when exactly Y happens, how much work stops, how a scenario is scripted or a verification is built) belongs to a later level.

## Criteria

A sound Outcome meets all six.

1. Complete. Every required element is present.
2. Nothing extra. Nothing is present that the Outcome isn't responsible for.
3. Clear. For every statement, a reader knows what result the user is meant to get.
4. Traceable. Every requirement is covered by a verification that fails if the requirement isn't met. How verifications are split, grouped or structured, such as one per listed item or one per level, person or feature, is for a later level; asking for a different structure is not a finding. Every scenario and measure verifies a requirement. An allowance, something a requirement permits but does not require, needs no scenario of its own. A requirement allows whatever its words don't rule out.
5. Sound verifications. Each verification is judged by its own words against the requirement it verifies, taken as built faithfully at a later level. No verification or measure:
   - passes when the user doesn't get the result;
   - relies on the work to have produced anything it needs before its event, such as a failing draft, a defect, a decision or an earlier feature. A starting state that sets these up itself is not a finding;
   - tests how the result is implemented instead of the behaviour the user observes, for example by reading the system's own log or report that it succeeded;
   - fails or counts against behaviour the requirement it verifies requires or allows. A behaviour is ruled out only by requirement words that a run doing it would break; words on the same subject that don't forbid it don't rule it out. Only that requirement's allowances and exceptions count, and each one the starting state could bring about is either ruled out by the starting state or carried into the verification;
   - compares against an expected result that the scenario doesn't set before the run.

   A scenario need not re-verify a requirement that another scenario covers.
6. Consistent. No requirements, scenarios, measures or definitions contradict each other. An absolute term, such as every, never, only, always, all, none, any or anything, means no exceptions, so an absolute requirement that another requirement makes an exception to is a contradiction.
```

## skills/review-outcome/SKILL.md @ blob 2b1bf0b

```
---
name: review-outcome
description: Review a feature's Outcome document on its own and report findings that would change what gets built. Use at the Outcome gate, given only the Outcome document.
---

# Review an Outcome

Read [the Outcome definition](../references/outcome.md). Review the Outcome document you are given against it, on its own, as the reader the definition names would read it. Do not judge whether it matches any discussion or context that produced it.

## Method

Before judging, list for yourself every requirement, scenario and measure, and map each requirement to the scenarios whose verification would fail without it. Then judge the document against each of the definition's six criteria.

## Findings

- A finding names the criterion it fails and quotes the document.
- A point the definition leaves to a later level is not a finding.
- Wording that doesn't change what the user gets is not a finding.
- Drop anything the quoted text doesn't show: perfection is the enemy of done. For criteria 4 and 5, the text shows a finding when a requirement has no verification that fails if it isn't met, or when a verification's own words, built faithfully, would misjudge the result. A verification that tests implementation instead of the behaviour the user observes is a finding. A verification that could be built badly is not.
- Impact is high if the user might not get the intended result, and medium if only a verification or measure is affected.

Do not propose answers, rewrite the document, comment on wording or style, or list open questions.

## Rounds

A round starts with one run of this review. When it reports no findings, two more run independently, and the round passes when all three report none. When the first run reports findings, the round ends there and the findings are fixed before the next round.

## Output

- Trace map: each requirement to its scenarios, one line each.
- Criteria 1-6: PASS or FINDINGS for each.
- Findings: id, criterion, quoted evidence, what it changes, impact.
- Dropped: one line each, with the reason.
```

## skills/references/outcome.md @ blob c834139

```
# Outcome

An Outcome states what the user gets and how success is judged. It is the first planning level of a feature.

## Reader

An Outcome is written for those who build from it: the agents doing later levels, whoever turns its scenarios into tests, and maintainers. The user approves that same document. It is written in a neutral voice, naming "the user", not "you".

## Contents

An Outcome contains:

- Who the feature is for.
- Its requirements: what it achieves, as results the user can observe.
- End-to-end scenarios, each with an automated verification and a pass bar. No verification needs a person. A pass bar that applies to every scenario, such as how many runs must pass, is stated once.
- How success is measured on real use, each measure with a target.
- A glossary of the terms it defines.

Every requirement, scenario and measure carries a visible ID (R1, S1, M1), stable once approved. Each line states one requirement.

An Outcome does not contain non-goals, behaviour rules, edge cases, design decisions, implementation, a slicing plan, where anything lives, or how tests are built.

A scenario states its starting state, what happens and what passes, as results you can observe. How the scenario is scripted, and how a verification tells one case from another, is how tests are built. Naming a verification's kind, its pass bar, and what comes with the scenario is not.

Verifications are automated tests held to normal testing standards. Each tests the behaviour the user observes, not how it is implemented, and passes or fails on its own, independent of every other verification.

An Outcome leaves room for interpretation; later levels narrow it. A point that needs a definition, rule, threshold or procedure to resolve (what exactly counts as X, when exactly Y happens, how much work stops, how a scenario is scripted or a verification is built) belongs to a later level.

## Criteria

A sound Outcome meets all six.

1. Complete. Every required element is present, in the form the contents set.
2. Nothing extra. Nothing is present that the Outcome isn't responsible for.
3. Clear. For every statement, a reader knows what result the user is meant to get.
4. Traceable. Every requirement is covered by a verification that fails if the requirement isn't met. How verifications are split, grouped or structured, such as one per listed item or one per level, person or feature, is for a later level; asking for a different structure is not a finding. Every scenario and measure verifies a requirement. An allowance, something a requirement permits but does not require, needs no scenario of its own. A requirement allows whatever its words don't rule out.
5. Sound verifications. Each verification is judged by its own words against the requirement it verifies, taken as built faithfully at a later level. No verification or measure:
   - passes when the user doesn't get the result;
   - relies on the work to have produced anything it needs before its event, such as a failing draft, a defect, a decision or an earlier feature. A starting state that sets these up itself is not a finding;
   - tests how the result is implemented instead of the behaviour the user observes, for example by reading the system's own log or report that it succeeded;
   - fails or counts against behaviour the requirement it verifies requires or allows. A behaviour is ruled out only by requirement words that a run doing it would break; words on the same subject that don't forbid it don't rule it out. Only that requirement's allowances and exceptions count, and each one the starting state could bring about is either ruled out by the starting state or carried into the verification;
   - compares against an expected result that the scenario doesn't set before the run.

   A scenario need not re-verify a requirement that another scenario covers.
6. Consistent. No requirements, scenarios, measures or definitions contradict each other. An absolute term, such as every, never, only, always, all, none, any or anything, means no exceptions, so an absolute requirement that another requirement makes an exception to is a contradiction.
```


## Appendix C: commits in the period

- 80788cd 2026-11-02T23:18:07+00:00 Carry the level 1 changes over from level-2-behaviour
- 4605655 2026-11-02T23:26:43+00:00 Outcome: interview, playback and approval at every level
- e4a4d92 2026-11-02T23:32:47+00:00 Fix Outcome review round 1 findings
- a36bf1f 2026-11-02T23:39:16+00:00 Fix Outcome review round 2 findings
- 847802b 2026-11-02T23:47:12+00:00 Leave the number of scenario runs to Design; 0027 covers found facts
- 9c62834 2026-11-02T23:53:16+00:00 Scenario 14 checks that a level's review passes before approval
- 0c662c6 2026-11-03T17:30:20+00:00 One question at a time; the next waits for the answer
- dd487b5 2026-11-03T20:29:39+00:00 Outcome: write in the level 1 interview and confirmed playback
- b563f13 2026-11-03T20:35:26+00:00 Fix Outcome review round 6 findings
- 2cb2dcb 2026-11-03T20:42:34+00:00 Fix Outcome review round 7 findings
- c53db24 2026-11-03T20:54:33+00:00 Four review rounds per approved version; all decisions need approval
- 0b304f0 2026-11-03T21:58:54+00:00 Open question for Design: a hook enforcing one question at a time
- 32d8b5e 2026-11-03T22:45:13+00:00 Candidates: decision categories, invariants apply in full, run policy defaults
- 39a0f70 2026-11-03T22:49:45+00:00 Outcome: write in Craig's level 1 decisions
- 877b935 2026-11-03T22:58:03+00:00 Fix Outcome review round 1 findings
- dd7b7d0 2026-11-03T23:07:01+00:00 Fix Outcome review round 2 findings
- ec102df 2026-11-04T16:27:50+00:00 Fix Outcome review round 3 finding
- 3e512e3 2026-11-04T16:54:45+00:00 Align with decisions 0023 and 0033 after review round 4
- 0cb5b9e 2026-11-04T17:48:41+00:00 Scenario 14 requires the planted defect to be reported before approval
- d514d01 2026-11-04T18:04:22+00:00 Move decisions into one append-only log, docs/decisions.md
- fa027db 2026-11-04T18:13:22+00:00 Hooks load an agent prompt, not a human doc
- a7ab315 2026-11-04T18:13:35+00:00 Point CLAUDE.md and README at the goals prompt
- cf5f70b 2026-11-04T18:13:44+00:00 Mark D13 replaced by D44
- c2764af 2026-11-04T18:24:01+00:00 Stop check as a command hook, wired for Claude Code and Codex
- bd73aa3 2026-11-04T18:24:30+00:00 Outcome: the same results under Claude Code and Codex
- 1d7d23a 2026-11-04T18:28:20+00:00 Align Outcome scenarios 4, 5, 10, 13 and 23 with existing decisions
- 89876c0 2026-11-04T18:32:48+00:00 Narrow the both-hosts requirement to the framework's own enforcement
- 9b2f71a 2026-11-04T18:36:48+00:00 Align the Outcome with D42 and D29 after review
- 2cb26bc 2026-11-04T21:04:07+00:00 Align the Outcome with D29, D31, D34 and D42 after review
- 0a15cfb 2026-11-04T21:05:20+00:00 Align the classification, the Outcome and CLAUDE.md with D40, D30, D33 and D47
- 2ce9279 2026-11-04T21:10:55+00:00 Clarify the Outcome definition's check-soundness and test-building lines
- c7d8cc4 2026-11-04T21:27:50+00:00 Verifications test behaviour and pass independently (D48)
- 86abb78 2026-11-04T21:30:29+00:00 One verification for a requirement that holds across cases (D49)
- a52ab6f 2026-11-04T21:33:18+00:00 Absolute terms have no exceptions (D50)
- a81dcfe 2026-11-04T21:39:03+00:00 Align scenarios 5, 14, 15 and 16 and clarify criterion 5's starting-state line
- b7b609f 2026-11-04T21:39:36+00:00 Scenario 7: the existing code is something no one decided (D42)
- 8573a3c 2026-11-04T22:36:54+00:00 Every requirement covered; how verifications are structured is a later level's (D51)
- 03a00aa 2026-11-04T22:45:45+00:00 Scope R3 to the current level, align S10 to R10, absolute terms as examples
- 2f2d6d8 2026-11-04T22:53:09+00:00 Align R3, S15 and S18 to what was agreed
- 22b52d3 2026-11-04T22:58:54+00:00 R3: drop the clause that repeated R4
- 363af74 2026-11-04T22:59:12+00:00 R3: a plain answer is acted on without a playback of its own (FF-14)
- 8e70a8c 2026-11-04T23:02:47+00:00 What a level's review checks (D52); S14 aligned to it
- 9fa0d81 2026-11-04T23:09:54+00:00 S10, S23 scoped to the level; S18 tests re-deciding
- 4dbd3de 2026-11-04T23:22:54+00:00 Scenario starting states set up what they need (criterion 5)
- 45c5bdd 2026-11-04T23:28:03+00:00 R7: what's missing is settled at the level it belongs to
- e72a1d0 2026-11-04T23:31:56+00:00 S18: the decision is the work's in the second feature too
- f1e405e 2026-11-04T23:35:46+00:00 Revert "R7: what's missing is settled at the level it belongs to"
- 257d738 2026-11-04T23:37:29+00:00 S19: the decision is yours in the second feature
- 062a367 2026-11-04T23:38:44+00:00 Pre-commit hook: a level document needs a full self-check table (D53)
- 68ad628 2026-11-04T23:39:57+00:00 R7 scoped to what is yours at this level (FF-44 A, D50); S10, S23 aligned
- 5deb96f 2026-11-04T23:47:17+00:00 Self-check runs each criterion as its own step; R7 scoped in full
- c144812 2026-11-04T23:54:11+00:00 A requirement allows whatever its words don't rule out (D48); R2 approval timing (FF-4)
- fc2430d 2026-11-04T23:55:17+00:00 A review round is one run, then two more if it's clean (D54, replaces D12)
- 8741933 2026-11-04T23:59:09+00:00 Self-check confirms the quoted words forbid what a check fails; S8, S18 aligned
- df3dcc1 2026-11-05T00:02:00+00:00 Review judges against the standard, not the writer's steps (D52)
- c74f108 2026-11-05T00:05:46+00:00 S17 checks what you observe; self-check considers every way a run reaches the result
- 6a08a16 2026-11-05T00:09:39+00:00 Gate scenarios catch any move to the next level; self-check lists every way a requirement breaks
- 91babdc 2026-11-05T00:19:19+00:00 S15 scopes its "only after you confirm" to the instructions; self-check finds absolutes in scenarios and measures
- a716c11 2026-11-06T19:07:38+00:00 Self-check enforced by agent hooks on both hosts, not a git hook (D55, replaces D53)
- 3948a73 2026-11-06T20:45:26+00:00 Level documents are written for those who build from them (D56, FF-47 A)
- 4bc74af 2026-11-06T20:51:38+00:00 R15 lists the work's own decisions among the ways a point is settled (D50)
- 757428e 2026-11-06T20:57:46+00:00 R37 and R35 carry their exceptions on their own line (D50); S23 checks an observable point
- 763eca1 2026-11-06T20:59:22+00:00 Absolute terms are listed by a script; wiring test for both hosts' hooks
- e763ee9 2026-11-06T21:04:01+00:00 S14, S17 fail a run that stalls; S4 sets up the second feature's level; self-check looks for runs that pass without the result
- 6e9d907 2026-11-06T21:08:47+00:00 R2 carries R38's exception on its own line (D50)
- ea5e697 2026-11-06T21:14:15+00:00 S1 rules out R2's after-code case in its starting state
- 3b17c96 2026-11-06T21:22:02+00:00 Restore the completeness requirement (R40), scope R8's playback (R7), and tighten the instructions
- 6d31c23 2026-11-06T21:37:45+00:00 Align hooks and skills with the current Claude Code, Codex and skill docs
- 6540052 2026-11-06T21:39:01+00:00 D57 replaces D46: nested stop check with hooks off; SessionStart on every source; null last message
- 6e82d4d 2026-11-06T21:40:21+00:00 Only an absolute term rules out exceptions (D58, FF-48 B); drop R2's carve-out
- a58c557 2026-11-06T21:40:54+00:00 Project terms aren't found facts (D59, FF-49 A)

