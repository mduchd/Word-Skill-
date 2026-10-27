---
name: anti-ai-writer
description: >-
  Use this skill when the user wants to write content that sounds natural and
  human-like, avoiding AI-generated patterns. Also use when the user asks to
  make text "less AI", "more natural", "sound like a real person", "clone personal tone",
  or "avoid AI detection". Apply when writing essays, reports, blog posts,
  academic work, or any text that must not be identifiable as AI-written.
---

# Anti-AI Writer

A skill for producing text that reads as naturally human-written, avoiding
the telltale patterns that AI detection tools look for.

## The Core Problem: Why AI Text Gets Detected

AI models (including this one) default to predictable patterns:
- Overly structured, perfectly balanced sentences
- Transition words used mechanically (Furthermore, Bên cạnh đó, Hơn nữa...)
- No genuine opinion, digression, or personality
- Vocabulary that is "safe" and never colloquial
- Every paragraph roughly the same length
- Lists and bullet points for everything

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

**B. Structural Imperfection**
- Occasionally start a sentence with "Nhưng", "Và", "Vì thế" (informal connectors)
- Add one genuine subjective comment or personal stance per section
- Include one specific concrete detail (a number, a name, a date) per paragraph
- Allow one mild "digression" or aside per major section

**C. Vocabulary Humanization**
- Swap formal synonyms for colloquial alternatives where appropriate
- Use Vietnamese-native expressions, NOT translated English phrases
- See `./references/common-ai-patterns.md` for the full banned word list

**D. Avoid Perfect Parallel Structure**
- Bad: "Thứ nhất... Thứ hai... Thứ ba... Cuối cùng..."
- Good: Vary how you introduce new points organically

### Step 3 – Apply the Banned Patterns Checklist
Reference `./references/common-ai-patterns.md` and verify:
- [ ] No banned transition words used
- [ ] No "AI vocabulary" words used
- [ ] Sentence lengths are varied
- [ ] At least one subjective/opinionated statement included
- [ ] No more than 2 consecutive bullet points

### Step 4 – Register-Specific Adjustments

**For Formal/Academic Vietnamese:**
- Keep formal register but vary sentence openings
- Add hedging phrases: "Theo quan điểm của người viết...", "Có thể thấy rằng..."
- Include one limitation or counterargument to show balanced thinking

**For Semi-formal/Blog:**
- Allow contractions and casual connectors
- Use rhetorical questions: "Vậy thực sự điều gì đang xảy ra ở đây?"
- First-person observations are encouraged

### Step 5 – Final Review
Before outputting, do a mental pass:
- Read aloud (mentally) — does it flow naturally?
- Would a Vietnamese person actually write this?
- Is there any section that sounds "too perfect"? Break it up.
