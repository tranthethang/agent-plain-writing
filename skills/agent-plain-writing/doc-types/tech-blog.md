# Tech blog

Use for sharing posts, field notes and technical write-ups for peers.

## Reader and length

- Reader: peers in the same field. Technical terms are allowed. Define a term once if it is new or rare.
- Outside readers: run the script with `--non-tech`.
- Length: the `length` range in `languages/<lang>/profile.json` applies only when the brief has enough material for it. When a brief is thin, write a shorter post that covers each point once. Do not pad, repeat points, or add a recap to reach the range.

## Voice

- First person. Speak to the reader directly ("you").
- Talk as if telling a colleague at the next desk. Direct, opinionated, no preaching.
- Vary sentence length and keep natural narrative flow (context, mistake, tension, fix, lesson). Do not restate the brief as a flat, bullet-like report.
- Write short paragraphs of flowing sentences, within the `paragraph` limit in `profile.json`.
- Admit mistakes. A story about your own error is more convincing than a success story.
- No emoji. No greeting to the audience. No chains of rhetorical questions.
- No meta-report openings (a sentence about why you write the post) and no label closings (a closing line that starts with a label such as a lesson or a note). Start directly in the event or conclusion. The phrases for each language are in `banned.txt`, section `[tech-blog]`.
- No throat-clearing lead-ins ("This is an important difference from the old approach:") and no references to the prompt ("The brief does not say..."). State what the system does in one concrete sentence instead of naming a pattern in one sentence and re-explaining it in the next. Keep one plain, consistent term for a mechanism.

## Structure

1. **Title**: states the takeaway or what you did. Not "Everything about X". Keep both the action and the cause accurate to the facts—do not claim you removed something you only changed or shortened.
2. **Opening** (at most 2 sentences): one concrete event or one conclusion.
3. **Body**: 3 to 5 sections, each with a short heading. Use *claim → example or story → lesson* when a section has its own example, not as a template that forces repeating the opening's incident or numbers. Move forward from the opening: state each fact or number once, explain each mechanism once, and keep a section to one short paragraph if it only has one point.
4. **Closing** (1 or 2 sentences): one concrete action or takeaway for the reader. Never recap earlier sections, summarize the incident, or restate the steps you just explained.

## Brief the AI needs

Give these five. Whatever is missing, the AI will guess.

1. Summary of the content (3 to 5 lines).
2. Main points to stress (at most 3).
3. Reader: who they are and what they know.
4. One or two paragraphs you wrote yourself, marked "imitate this rhythm and word choice".
5. Words to use and words to avoid.

## Checklist

- [ ] The opening is a concrete event or conclusion, not a greeting or meta-report.
- [ ] Sentence lengths vary naturally instead of reading like a telegram.
- [ ] One example or story per section, and a section is one main point.
- [ ] No repeated facts from the opening, no padded restatements, and no recap paragraph before the closing.
- [ ] At least one place where the author admits a limit or a mistake (if the brief has one).
- [ ] The closing is one action, not a summary.
- [ ] `python3 scripts/check_style.py post.md --lang <lang> --type tech-blog`
