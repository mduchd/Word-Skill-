---
name: anti-ai-writer
description: >-
  Use this skill when the user wants to write content that sounds natural and
  human-like, avoiding AI-generated patterns and banned AI characters/symbols.
  Also use when the user asks to make text "less AI", "more natural",
  "sound like a real person", "remove AI symbols/emojis", or "avoid AI detection".
  Apply when writing essays, reports, blog posts, academic work, or any text that
  must not be identifiable as AI-written.
---

# Anti-AI Writer

A skill for producing text that reads as naturally human-written, avoiding
the telltale patterns, transition words, and signature symbols that AI detection tools look for.

## The Core Problem: Why AI Text Gets Detected

AI models default to predictable patterns and visual telltales:
- Random inline bolding (**key phrases**) like social media posts
- Emojis in formal text (🚀, 💡, 📌, ✅)
- Overuse of em dashes (—) borrowed from English syntax
- Transition words used mechanically (Furthermore, Bên cạnh đó, Hơn nữa...)
- Arrow symbols (→, =>) instead of actual written sentences
- Lists and bullet points for everything ("bullet-point-itis")
- Uniform sentence lengths and paragraph sizes

## Workflow

### Step 1 – Understand the Context & Tone
Before writing, ask:
- **Register**: Formal (academic/government) or Semi-formal/casual?
- **Topic**: What is the subject matter?
- **Voice**: First person (tôi), collective (chúng tôi), or impersonal?
- **Tone Cloning**: Check if user provided sample text or if `./references/my_sample_style.md` exists. If so, follow `./references/tone-cloning.md` to replicate the user's authentic style.

### Step 2 – Draft with Human Patterns
Apply ALL rules from `./references/humanizing-techniques.md`.

Key principles to apply actively:

**A. Sentence Rhythm Variation (Burstiness)**
- Mix sentence lengths deliberately: short → medium → long → short
- Target ratio: ~30% short (<10 words), 50% medium, 20% long
- Avoid 3+ consecutive sentences of similar length

**B. Strict Character & Symbol Prohibition (AI Telltales)**
- **ABSOLUTELY NO EMOJIS:** Zero emojis in formal/academic reports.
- **NO RANDOM INLINE BOLDING:** Do NOT bold random words inside body paragraphs (`**...**`). Only Headings and table total rows are bolded.
- **NO ARROWS OR AMPERSANDS:** Do NOT use `→`, `=>`, `->`, or `&`. Always write complete words: *"dẫn đến"*, *"và"*.
- **AVOID EM DASHES (`—`):** Do not overuse em dashes between clauses. Native Vietnamese writers use commas `,` or parentheses `(...)`.
- **CURE BULLET-POINT-ITIS:** Write flowing narrative paragraphs instead of turning every thought into a bulleted list.

**C. Vocabulary Humanization**
- Swap formal synonyms for colloquial alternatives where appropriate
- Use Vietnamese-native expressions, NOT translated English phrases
- See `./references/common-ai-patterns.md` for the full banned word list

**D. Structural Imperfection**
- Occasionally start a sentence with "Nhưng", "Và", "Vì thế" (informal connectors)
- Add one genuine subjective comment or personal stance per section
- Include one specific concrete detail (a number, a name, a date) per paragraph

**E. Avoid Perfect Parallel Structure**
- Bad: "Thứ nhất... Thứ hai... Thứ ba... Cuối cùng..."
- Good: Vary how you introduce new points organically

### Step 3 – Apply the Banned Patterns Checklist
Reference `./references/common-ai-patterns.md` and verify:
- [ ] No banned symbols used (no emojis, no inline bolding, no arrows)
- [ ] No banned transition words used
- [ ] No "AI vocabulary" words used
- [ ] Sentence lengths are varied
- [ ] At least one subjective/opinionated statement included
- [ ] Flowing prose used instead of excessive bullets

### Step 4 – Final Review
Before outputting, do a mental pass:
- Read aloud (mentally) — does it flow naturally?
- Would a Vietnamese person actually write this?
- Is there any section that sounds "too perfect" or "robotic"? Break it up.
