# English examples: tech-blog

Details in the stories are made up to serve as models. In real work, use the author's own story.

## Bad → good pairs

### 1. Opening

**Bad:** In the ever-evolving world of web development, managing state in React applications plays a crucial role. Let's delve into this topic together!
**Good:** Last week, one button in my React app responded two seconds late. The cause: I had put everything in one global state.

### 2. Explaining a concept

**Bad:** A cache is a temporary storage mechanism designed to accelerate data retrieval by maintaining copies of frequently accessed data.
**Good:** A cache is a saved copy of data you use often. Next time you need it, the system takes the copy instead of computing it again.

### 3. Personal opinion

**Bad:** It can be said that the adoption of TypeScript brings a number of significant benefits throughout the software development lifecycle.
**Good:** Since I switched to TypeScript, my editor flags type mistakes as I type. I no longer wait until runtime to find out.

### 4. What you learned

**Bad:** Through this experience, we can draw many valuable lessons about the importance of planning.
**Good:** I lost a whole afternoon because I skipped a ten-minute plan before coding. I do not skip that step anymore.

### 5. Vague advice

**Bad:** We should always pay close attention to code quality to ensure the long-term sustainability of the project.
**Good:** Set one rule: no merge while a test is red. This rule saved me three times last month.

### 6. Admitting a limit

**Bad:** While this solution may have certain limitations, overall it provides relatively good results.
**Good:** This solution can't handle a network drop halfway through. I haven't found a simpler fix yet.

## Complete sample post (about 620 words)

```markdown
# I dropped global state after one lost afternoon

My "Save" button reacted two seconds late every time a user typed into the settings form. I spent half an afternoon blaming our backend server before realizing the bug lived in my own global store.

## Everything felt clean at first

Three months ago, the settings page held four fields: name, email, timezone, and language. I put all four into one global state to avoid passing props down three nested levels.

That shortcut worked well enough that I felt clever for choosing it. Each time product asked for a new option, I tossed another field into the same bucket. After all, the data belonged to the settings screen.

Nobody pushed back during code review because the page still felt fast on small test accounts. Local machines handled four fields in less than a millisecond. That early smoothness hid the cost for two full months.

By week eight, the page had grown to 40 fields, three date pickers, and a live preview panel. Still, nobody noticed until QA sent a screen recording where the text cursor froze on every keystroke. You typed a single letter and waited two seconds for it to appear.

## Two hours looking in the wrong place

My first instinct was to open the Network tab and hunt for a slow API call. Every request returned in under 80 ms, and not a single 500 error showed up. I even pinged our backend engineer to ask if the database had a new lock.

She checked the server logs and sent back a clean screenshot with zero slow queries. Even our heaviest lookup finished in 15 ms.

Next, I blamed browser memory and disabled every extension I had installed. The "Save" button stayed just as sluggish as before.

Around four o'clock, I finally opened React DevTools Profiler and recorded a single keystroke in the name box. The flame graph lit up bright red across all 40 inputs at once. Changing one letter in the name box forced the live preview and all three date pickers to recalculate from scratch.

## How I split the state back up

I closed my editor and sketched on paper which fields actually needed to talk to each other. Most groups on the page were completely independent. Only two permission toggles needed to read anything from the main account object.

Instead of one giant store, I moved each form's state down into its own component. Shared values—the signed-in user and the active language—stayed in the global store. The live preview subscribed only to the form currently open on screen.

The refactor took one morning, mostly deleting wiring hooks I should never have added. I kept every field name identical so unsaved drafts in browser storage still loaded cleanly after deploy. When I recorded the same keystroke in the Profiler afterward, render time dropped from 1,800 ms to 12 ms.

## What still feels clumsy

Splitting state fixed the lag, yet it is no silver bullet for every screen. When two tabs must cross-check each other before submit, I still write a small bridge in the parent.

That bridge feels manual, and I have not found a cleaner pattern that avoids dragging everything back upstairs. If you have 20 independent forms on one screen, local state is the straightest line. If your whole page works like one connected spreadsheet, global state still earns its keep.

## Ask who needs the data

My mistake had nothing to do with the state library we picked. I had asked "where is it convenient to dump this data" instead of asking "who actually needs to read it."

Try one thing today: open your current project and count the fields sitting in global state. If more than five belong to a single screen, start moving them down before your "Save" button pays the price.
```

## Your own samples

<!-- Paste a passage you wrote and like. Add Bad / Good pairs from posts the AI wrote badly. -->
