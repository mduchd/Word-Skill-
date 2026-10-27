---
name: ai-detection-bypass
description: >-
  Use this skill when the user wants to check if text looks AI-generated,
  or wants to rewrite/edit existing text to reduce AI detection scores.
  Activate when the user says "tránh AI", "bypass AI detector", "kiểm tra
  AI", "chỉnh văn bản tránh bị phát hiện", or wants to pass tools like
  GPTZero, Turnitin AI, Copyleaks, or ZeroGPT. Works on both Vietnamese
  and English text.
---

# AI Detection Bypass

Skill for analyzing text for AI-detection signals and systematically
rewriting it to read as naturally human-written.

## How AI Detectors Work (Brief)

Most detectors (GPTZero, Turnitin, ZeroGPT, Copyleaks) measure:

1. **Perplexity** — how "surprising" the word choices are. AI picks
   the statistically safest word; humans pick unexpected ones.
2. **Burstiness** — variation in sentence length. AI is flat; humans burst.
3. **Pattern matching** — known AI phrases, sentence structures, transitions.
4. **Coherence uniformity** — AI paragraphs are eerily consistent in quality.

## Workflow

### Step 1 — Analyze the Text

Read the submitted text and mentally score it on:

| Signal | What to look for | Risk |
|---|---|---|
| Transition words | Furthermore, Additionally, Moreover, Bên cạnh đó... | 🔴 High |
| Sentence length variance | All similar length = AI | 🔴 High |
| Parallel structure | "Thứ nhất... Thứ hai... Thứ ba..." | 🔴 High |
| Generic vocabulary | "important", "significant", "comprehensive" | 🟡 Medium |
| Missing specifics | No names, dates, real numbers | 🟡 Medium |
| Passive voice overuse | "It was found that...", "Được xác định là..." | 🟡 Medium |
| Zero subjectivity | No opinion, no uncertainty expressed | 🟡 Medium |
| Perfect paragraph structure | Topic → Body → Conclusion every time | 🟢 Low-Med |

Report estimated risk level: **Low / Medium / High / Very High**

### Step 2 — Choose Rewrite Strategy

Based on risk level, apply the matching strategy from
`./references/rewrite-strategies.md`:

| Risk Level | Strategy |
|---|---|
| Low (<30%) | **Polish** — swap key phrases, vary 2–3 sentences |
| Medium (30–60%) | **Section Rewrite** — rewrite highest-risk paragraphs |
| High (60–80%) | **Full Paraphrase** — rewrite all paragraphs, preserve only facts |
| Very High (>80%) | **Reconstruct** — keep only data/facts, rewrite everything |

### Step 3 — Apply Rewrite

While rewriting, apply these transformations:

**Lexical Changes:**
- Replace banned words (see `./references/rewrite-strategies.md`)
- Introduce one unexpected/colloquial word per paragraph
- Replace round numbers with specific ones where plausible

**Syntactic Changes:**
- Break long sentences into shorter ones (and vice versa — vary it)
- Change passive constructions to active voice
- Start some sentences with non-subject elements:
  - "Từ góc nhìn đó,..."
  - "Điều đáng chú ý là..."
  - "Năm 2024, khi..."

**Structural Changes:**
- Merge two short paragraphs or split one long one
- Reorder supporting points within a paragraph
- Replace a bulleted list with flowing prose (or vice versa — one only)

### Step 4 — Run Self-Checklist

Use `./scripts/checklist.md` to verify before outputting.

### Step 5 — Output

Present the rewritten text clearly. If significant changes were made,
briefly note what was changed and why (1–2 sentences max).

## Important Constraints

- **NEVER change factual content** — only change how facts are expressed
- **NEVER introduce false information** to seem more "human"
- **Preserve the user's intended meaning** at all times
- If the user provides citations/sources, keep them exactly as-is
