# Play back before acting; interview before drafting

Before the work acts on anything from the user that could change the project:

- It plays back, in its own words, what it understood, and waits for the user to confirm. This covers a level, an instruction, a decision or a correction, whether or not it looks clear. The project is its code, tests, documents, decisions, settings, branches and pull requests.
- A plain answer to the work's own question is a reading the user chose, and is acted on without another playback. Something that changes nothing needs no playback.
- Anything that could be read more than one way is put to the user as a choice between readings, in a message of its own after the playback, one at a time.
- A correction gets a fresh playback of the corrected parts.

Before a level's document is written, at every level before code:

- The work interviews the user one question at a time and waits for the answer. The next question is chosen from what the answer settles. Each question carries the work's recommended answer, and the user can answer by letter. Asking several at once makes the exchange messy as soon as the user has a follow-up on any one of them.
- The work looks up facts itself and asks only for decisions.
- The work then plays back what it understood the user wants at that level. The document is written only after the user confirms the playback.
- The level's review also checks that every statement in the document is something the user said or agreed, or something marked as the work's; that every fact marked as the work's is true of the project; and that no statement can be read two ways that would change what gets built.

These techniques are adapted, with thanks, from the Superpowers brainstorming skill (obra/superpowers: a hard approval gate, and only what the user said goes in as theirs), Matt Pocock's grilling and to-spec skills (aihero.dev: each question with a recommendation, facts looked up and decisions asked, a confirmation gate, and "if the spec states something you never said, that is a defect"; its rounds of independent questions were considered and not taken, because a follow-up on one question in a round makes the exchange messy), and Cursor's pstack poteto-mode skill (a fact that can be observed is not the user's to answer). The framework carries its own copy of them and doesn't load those skills.
