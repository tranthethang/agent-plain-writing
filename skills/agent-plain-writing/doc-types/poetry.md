# Poetry

Use for free verse and for fixed forms (each language has its own forms, see `languages/<lang>/examples/poetry.md`).

## Overrides to the core rules

- Sentence and paragraph limits do not apply. The script only checks cliché words.
- At least half of the lines carry a concrete image.
- At most one simile per 4 lines.
- At most one abstract word per poem ("longing", "soul", "life").
- The last line does not state a lesson.

## Principles

1. **Image first, emotion second.** Put an object in the line. Do not name the feeling.
2. **Do not explain.** The poem stops at the image. The reader connects it.
3. **Choose the form before writing.** Ask the user if they have not said. Default: free verse.
4. **Break lines for a reason.** Break where the reader needs to breathe.
5. **Avoid stock words.** See the cliché list in the language's `banned.txt` (section `[poetry]`).
6. **Write two variants** with different central images, so the user can choose.
7. **Do not explain the poem** after writing it, unless the user asks.

## Process

1. Ask for the form, or choose free verse if you cannot ask.
2. Write two variants.
3. Check clichés. Cut the last line if it explains.
4. For fixed forms, check the rules by hand. The script does not check meter or rhyme.
5. Send the two variants with no long commentary.

## Brief the AI needs

1. The subject or moment (one sentence).
2. The form (free verse or a fixed form).
3. Tone: warm, cold, funny, grave.
4. Length (number of lines or stanzas).
5. A poem you like, and what you like about it (rhythm, image, tone).
