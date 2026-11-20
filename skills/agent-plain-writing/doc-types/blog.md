# Blog post (sharing experience)

Use for sharing posts, field notes and technical write-ups for peers.

## Reader and length

- Reader: peers in the same field. Technical terms are allowed. Define a term once if it is new or rare.
- Outside readers: run the script with `--non-tech`.
- Length: hit the target range in `languages/<lang>/profile.json` (`600–800` words for `en` and `vi`, `1500–2000` chars for `ja`). Do not cut a post down to a short summary.

## Voice

- First person. Speak to the reader directly ("you").
- Talk as if telling a colleague at the next desk. Direct, opinionated, no preaching.
- Vary sentence length and keep natural narrative flow (context, mistake, tension, fix, lesson). Do not restate the brief as a flat, bullet-like report.
- Write normal paragraphs of 2–3 flowing sentences—never split every sentence onto its own line with trailing spaces (`  \n`) like a social-media thread.
- Admit mistakes. A story about your own error is more convincing than a success story.
- No emoji. No "hey everyone". No chains of rhetorical questions.
- No meta-report openings ("I am writing this blog to...") or meta-report closings ("Lesson learned:", "Lesson:", "Note:"). Start directly in the event or conclusion.

## Structure

1. **Title**: states the takeaway or what you did. Not "Everything about X".
2. **Opening** (at most 2 sentences): one concrete event or one conclusion.
3. **Body**: 3 to 5 sections, each with a short heading. Each section runs *claim → example or story → lesson*.
4. **Closing** (1 or 2 sentences): one action the reader can take now. No recap.

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
- [ ] At least one place where the author admits a limit or a mistake (if the brief has one).
- [ ] The closing is one action, not a summary.
- [ ] `python3 scripts/check_style.py post.md --lang <lang> --type blog`
