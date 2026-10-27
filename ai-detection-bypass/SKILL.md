---
name: ai-detection-bypass
description: >-
  Use this skill when the user wants to check if text looks AI-generated,
  measure perplexity/burstiness stats, or rewrite/edit existing text to reduce
  AI detection scores. Activate when the user says "tránh AI", "bypass AI detector",
  "kiểm tra AI", "chỉnh văn bản tránh bị phát hiện", or wants to pass tools like
  GPTZero, Turnitin AI, Copyleaks, or ZeroGPT. Works on both Vietnamese
  and English text.
---

# AI Detection Bypass

Skill for analyzing text for AI-detection signals, calculating quantitative
risk scores, and systematically rewriting it to read as naturally human-written.

## How AI Detectors Work (Brief)

Most detectors (GPTZero, Turnitin, ZeroGPT, Copyleaks) measure:

1. **Perplexity** — how "surprising" the word choices are. AI picks
   the statistically safest word; humans pick unexpected ones.
2. **Burstiness** — variation in sentence length. AI is flat; humans burst.
3. **Pattern matching** — known AI phrases, sentence structures, transitions.
4. **Coherence uniformity** — AI paragraphs are eerily consistent in quality.

## Workflow

### Step 1 — Analyze the Text (Quantitative & Qualitative)

Run quantitative analysis if Python script is available:
`python ./scripts/analyze_text.py <file>`
This measures:
- Sentence length standard deviation (Burstiness score)
- Ratio of short/medium/long sentences
- AI transition word density
- Calculated Risk Index (0 - 100%)

Or qualitatively inspect:
- Transition words: Furthermore, Additionally, Bên cạnh đó, Hơn nữa...
- Flat sentence lengths (all sentences 15-20 words)
- Parallel enumeration ("Thứ nhất... Thứ hai... Thứ ba...")
- Generic vocabulary without concrete figures/dates

Report estimated risk level: **Low (<30%) / Medium (30-60%) / High (60-80%) / Very High (>80%)**

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

Use `./scripts/checklist.md` (22 criteria) to verify before outputting.

### Step 5 — Output

Present the rewritten text clearly. If significant changes were made,
briefly note what was changed and why (1–2 sentences max).
