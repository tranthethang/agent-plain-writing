# Banned phrases and what to use instead (English)

The machine-readable list is `banned.txt` in this folder. This file explains the replacements. When you add a phrase in one place, add it in the other.

## "AI voice" phrases (all types)

| Phrase | Use instead | Example |
|---|---|---|
| in order to | to | "in order to speed up" → "to speed up" |
| delve into | look at | |
| it is important to note that, it's important to note, it is worth noting | (delete), or bold "Note:" | |
| in today's fast-paced world | (delete). Open with a concrete event | |
| seamless, robust, comprehensive, cutting-edge, state-of-the-art, game-changer, revolutionize, unlock the, empower | say what it does, with a number | "robust tool" → "tool that handles 10,000 rows a second" |
| not only … but also *(warn)* | two sentences | "Not only fast but cheap" → "It is fast. It is also cheap." |
| plays a crucial role, plays a vital role | say the role | "Caching plays a crucial role" → "Caching keeps page loads under 1 second" |
| a wide range of | name them, or "many" | |
| in the realm of | in | "in the realm of security" → "in security" |
| at the end of the day, needless to say, as we all know | (delete) | |
| furthermore, moreover *(warn)* | (delete), or use a heading | |
| very, really | (delete), or give a number | |

## Vague words in API design

| Word | Use instead |
|---|---|
| appropriate | the exact condition |
| as needed, if necessary | the exact condition, or `TBD` |
| etc. | list everything, or point to an appendix |
| quickly, easily | a number (ms, number of steps) |
| flexible | what can be configured, and how |
| efficient, secure | a measurable criterion |
| user-friendly | the concrete property (one button per screen) |

## Words common in user guides

| Word | Use instead |
|---|---|
| carry out, perform the, perform a | a concrete verb: click, select, enter. "perform the validation" → "validate" |
| configure | set up, change the settings |

## Phrases of tech-blog and essay

| Phrase | Use instead |
|---|---|
| i am writing this blog to, i'm writing this blog to | open with the event or conclusion directly |
| lesson learned:, lesson:, key takeaway: | weave the point into the narrative, no label |
| utilize, leverage | use |
| in conclusion, to sum up | (delete). Do not recap |

## Report labels (first or last 3 lines)

| Label | Use instead |
|---|---|
| result:, guesses:, assumptions: | (delete from the document). Put the report outside it, or leave it out when there is no other place |

## General rules

- A banned phrase may stay when it is a **direct quote** or a proper name.
- Banning a phrase does not ban the idea. "The system is fast" is still needed, with a number.
- If you catch yourself repeating a phrase three times, replace two of them.
