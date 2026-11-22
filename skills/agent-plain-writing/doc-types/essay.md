# Essay (personal, reflective)

Use for personal essays, reflections, and short narrative pieces for general readers.

## Purpose and reader

- Reader: general readers who do not need specialized background.
- Length: open (`length` in `profile.json` is `null`). Stop when the piece lands; do not pad to hit a word count. A piece that only retells the brief summary has not landed yet: each main point needs its own scene (see Structure).

## Overrides to the core rules

- Sentences may be longer (`sentence` in `profile.json`), but **at least one third of sentences must be short** to set the rhythm.
- Paragraphs follow `paragraph` in `profile.json`.
- At least one sensory detail per paragraph (sight, sound, smell, touch, taste).
- Core rule 5 (No invention), essay reading. The facts stay fixed: do not add an event, a person, a place, a number or an outcome that is not in the brief. The texture may grow:
  - A small sensory detail that the scene already implies, for example the hum of a fan that the brief turns on, the light in a room the brief names, or the tape on a box the brief packs.
  - The narrator's inner voice. Use the thoughts, memories and doubts that the brief gives first. When the brief gives none, add at most two sentences of thought that the scene prompts. Write each as an open thought or a doubt (for example, "I still do not know if that was all he had to say."), never as a lesson or a conclusion. Report each added thought outside the text (Workflow step 7 in `SKILL.md`).
- Zero sentences that explain an emotion after the action already showed it. An open thought is not an explanation: it asks or remembers, and it does not conclude.
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
- No meta-report openings (a sentence about why you write the essay) and no label closings (a closing line that starts with a label such as a lesson or a note). The phrases for each language are in `banned.txt`, section `[tech-blog,essay]` (shared with `tech-blog`).

## Structure

- **Title**: concrete and specific. Not "Reflections on X".
- **No fixed headings**: write continuous prose with natural paragraph breaks.
- **Opening** (at most 2 sentences): start in a scene, a moment, or a concrete detail.
- **Body**: give each main point of the brief its own scene, with at least one action and one sensory detail. Do not compress a main point into one summary sentence. Before the shift, let the reader feel the tension through a brief fact (the empty days, the box not yet opened), not through a named feeling.
- **Closing** (1 or 2 sentences): close on one image or one action, not a lesson or summary. Do not restate the feeling that a main point names (for example, "the room felt like home"); show the action that makes the reader feel it.

## Brief the AI needs

1. Event, memory, or question at the center (3 to 5 lines).
2. Tone (warm, quiet, ironic, sharp).
3. One or two passages you like, marked "imitate this rhythm and word choice".
4. What must not happen or must not be said.
5. Inner material: what you thought, remembered or doubted at the time. Without it, the AI adds at most two open thoughts and reports them outside the text.

## Checklist

- [ ] No sentence names a feeling without an action or detail next to it.
- [ ] Every paragraph has at least one sensory detail.
- [ ] Each main point of the brief has its own scene with an action and a sensory detail, not one summary sentence.
- [ ] Every added sensory detail is one the scene implies; no new event, person, place, number or outcome.
- [ ] The closing does not restate the feeling a main point names.
- [ ] The narrator has an inner voice: the thoughts the brief gives, or at most two added open thoughts, each reported outside the text.
- [ ] No inner thought states a lesson or a conclusion.
- [ ] Short sentences are mixed in to vary the rhythm.
- [ ] No paragraph ends with a sentence that explains the meaning.
- [ ] No meta-report opening, no label closing, and no banned phrase from `[all]` or `[tech-blog,essay]`.
- [ ] No fixed section headings; the closing is one image or one action, not a lesson.
- [ ] `python3 <skill-dir>/scripts/check_style.py essay.md --lang <lang> --type essay`
