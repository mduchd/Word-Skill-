---
name: ai-detection-bypass
description: >-
  Use this skill when the user wants to check if text looks AI-generated,
  measure perplexity/burstiness stats, or rewrite/edit existing text to reduce
  AI detection scores. Activate when the user says "tránh AI", "bypass AI detector",
  "kiểm tra AI", "chỉnh văn bản tránh bị phát hiện", or wants to pass tools like
  GPTZero, Turnitin AI, Copyleaks, or ZeroGPT. Enforces strict input sanctity
  (never change user titles, headings, or scope). Works on Vietnamese and English.
---

# AI Detection Bypass

Skill for analyzing text for AI-detection signals, calculating quantitative
risk scores, and systematically rewriting it with surgical precision to read naturally.

## ⚠️ MANDATORY INPUT SANCTITY CONSTRAINTS (CHỐNG SỬA LINH TINH)

- **TIÊU ĐỀ & ĐỀ MỤC LÀ BẤT BIẾN:** Tuyệt đối KHÔNG tự ý đổi tiêu đề bài viết, tên đề tài, tên chương mục. Giữ nguyên 100% từng từ.
- **ĐÚNG PHẠM VI YÊU CẦU:** Chỉ sửa đúng đoạn/phần người dùng yêu cầu. Tuyệt đối không can thiệp lan man sang các đoạn khác.
- **BẢO TỒN NỘI DUNG GỐC:** Không thay đổi ý nghĩa, không đổi số liệu, ngày tháng, tên riêng và thuật ngữ chuyên ngành.
- **SỬA PHẪU THUẬT (Surgical Editing):** Chỉ sửa các câu có lỗi AI (từ nối máy móc, câu quá phẳng, ký tự cấm). Không viết lại bừa bãi toàn bộ bài viết.

---

## How AI Detectors Work (Brief)

Most detectors (GPTZero, Turnitin, ZeroGPT, Copyleaks) measure:

1. **Perplexity** — how "surprising" the word choices are. AI picks the safest words; humans pick unexpected ones.
2. **Burstiness** — variation in sentence length. AI is flat; humans burst.
3. **Pattern matching** — known AI phrases, PR buzzwords, transition markers, cliché openers.
4. **Coherence uniformity** — AI paragraphs are eerily uniform in tone and lack real-world friction/trade-offs.

---

## Workflow

### Step 1 — Analyze the Text (Quantitative & Qualitative)

Run quantitative analysis if Python script is available:
`python ./scripts/analyze_text.py <file>`
This measures:
- Sentence length standard deviation (Burstiness score)
- Ratio of short/medium/long sentences
- AI transition word density & PR buzzwords
- Detection of banned AI symbols (emojis, em dashes, arrows)
- Calculated Risk Index (0 - 100%)

Report estimated risk level: **Low (<30%) / Medium (30-60%) / High (60-80%) / Very High (>80%)**

### Step 2 — Choose Surgical Rewrite Strategy

Based on risk level, apply the matching strategy from
`./references/rewrite-strategies.md`:

| Risk Level | Strategy | Scope of Editing |
|---|---|---|
| Low (<30%) | **Polish** | Swap 2–3 transition words, insert 1 short sentence |
| Medium (30–60%) | **Surgical Rewrite** | Rewrite only sentences with high AI density |
| High (60–80%) | **Deep Rephrasing** | Rephrase sentence structures, preserve all facts |
| Very High (>80%) | **Total Reconstruction** | Rewrite prose completely, but LOCK title, headings & facts |

### Step 3 — Apply Rewrite (Strict Scope)

While rewriting, apply these transformations:

**Lexical Changes:**
- Remove banned words and PR buzzwords (*"bước tiến vượt bậc", "vô cùng tuyệt vời"*)
- Introduce one unexpected/colloquial word per paragraph
- Replace banned symbols (remove emojis, replace arrows with words)

**Syntactic Changes:**
- Break long sentences into shorter ones (and vice versa)
- Vary sentence openers (avoid always starting with Subject)
- Introduce real-world friction/trade-offs to ground the analysis

**Structural Boundaries:**
- **DO NOT** re-order sections or change headings
- **DO NOT** delete user arguments or invent unrequested points

### Step 4 — Run Self-Checklist

Use `./scripts/checklist.md` to verify before outputting:
- [ ] User's title and headings are strictly 100% untouched
- [ ] No factual data was altered
- [ ] Only requested sections were modified

### Step 5 — Output

Present the rewritten text clearly. Note what specific sentences were improved and why (1–2 sentences max).
