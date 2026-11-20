# Prose (fiction, essay, scene)

Use for short stories, essays, descriptions and narration.

## Overrides to the core rules

- Sentences may be longer (see profile), but **at least one third of sentences must be short** to set the rhythm.
- At least one sensory detail per paragraph (sight, sound, smell, touch, taste).
- At most one simile or metaphor per 200 words.
- Zero sentences that explain an emotion after the action already showed it.

## Principles

1. **Show, do not tell.** Do not write "she was sad". Write what she does when she is sad.
2. **Specific, uncommon details.** "A bowl of cold rice" beats "sorrow".
3. **Do not explain the meaning.** Do not close a paragraph with "he realized that...". Let the reader realize it.
4. **Vary the rhythm.** Long sentences describe, short sentences land.
5. **Dialogue does not explain.** Characters say what they would say, not what the author needs the reader to know.
6. **One point of view** per scene. Do not jump into another head.
7. **Avoid clichés.** See the cliché list in `languages/<lang>/banned.txt` (sections `[prose]`) and in the examples.

## Brief the AI needs

1. Scene, characters, what happens (3 to 5 lines).
2. Point of view (first or third person) and tone (cold, warm, ironic).
3. Target length.
4. One passage you like.
5. What must not happen or must not be said.

## Checklist

- [ ] No sentence names a character's feeling without an action next to it.
- [ ] No cliché from the list.
- [ ] No paragraph ends with a sentence that explains the meaning.
- [ ] Short sentences are mixed in.
- [ ] Every paragraph has a sensory detail.
- [ ] `python3 scripts/check_style.py story.md --lang <lang> --type prose`
