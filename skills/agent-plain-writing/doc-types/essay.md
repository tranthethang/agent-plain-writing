# Essay (personal, reflective)

Use for personal essays, reflections, and short narrative pieces for general readers.

## Purpose and reader

- Reader: general readers who do not need specialized background.
- Length: open (`length` in `profile.json` is `null`). Stop when the piece lands; do not pad to hit a word count.

## Overrides to the core rules

- Sentences may be longer (`sentence` in `profile.json`), but **at least one third of sentences must be short** to set the rhythm.
- Paragraphs follow `paragraph` in `profile.json`.
- At least one sensory detail per paragraph (sight, sound, smell, touch, taste).
- Zero sentences that explain an emotion after the action already showed it.
- Evaluative adjectives are allowed only when paired with a visible detail.

## Voice

- First person. Speak directly, without preaching.
- Keep natural narrative flow (context, tension, shift, landing). Do not restate the brief as a flat report.
- Admit mistakes or doubts when the brief has them. An honest flaw carries more weight than a neat success.
- **Show, do not tell.** Do not write "I was sad". Write what you did or saw.
- **Specific, uncommon details.** "A bowl of cold rice" beats "loneliness".
- **Do not explain the meaning.** Do not close a paragraph with "I realized that...". Let the reader realize it.
- **Vary the rhythm.** Long sentences describe; short sentences land.
- No emoji. No greeting to the audience. No chains of rhetorical questions.
- No meta-report openings (a sentence about why you write the essay) and no label closings (a closing line that starts with a label such as a lesson or a note). The phrases for each language are in `banned.txt`, section `[essay]`.

## Structure

- **Title**: concrete and specific. Not "Reflections on X".
- **No fixed headings**: write continuous prose with natural paragraph breaks.
- **Opening** (at most 2 sentences): start in a scene, a moment, or a concrete detail.
- **Closing** (1 or 2 sentences): close on one image or one action, not a lesson or summary.

## Brief the AI needs

1. Event, memory, or question at the center (3 to 5 lines).
2. Tone (warm, quiet, ironic, sharp).
3. One or two passages you like, marked "imitate this rhythm and word choice".
4. What must not happen or must not be said.

## Checklist

- [ ] No sentence names a feeling without an action or detail next to it.
- [ ] Every paragraph has at least one sensory detail.
- [ ] Short sentences are mixed in to vary the rhythm.
- [ ] No paragraph ends with a sentence that explains the meaning.
- [ ] No meta-report opening, no label closing, and no banned phrase from `[all]` or `[essay]`.
- [ ] No fixed section headings; the closing is one image or one action, not a lesson.
- [ ] `python3 scripts/check_style.py essay.md --lang <lang> --type essay`
