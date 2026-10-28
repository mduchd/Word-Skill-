---
name: anti-ai-writer
description: >-
  Use this skill when the user wants to write content that sounds natural and
  human-like, avoiding AI-generated patterns and banned AI characters/symbols.
  Also use when the user asks to make text "less AI", "more natural",
  "sound like a real person", "remove AI symbols/emojis", or "avoid AI detection".
  Enforces strict input sanctity (never change user titles or rewrite out of scope).
  Apply when writing essays, reports, blog posts, academic work, or any text that
  must not be identifiable as AI-written.
---

# Anti-AI Writer

A skill for producing text that reads as naturally human-written, avoiding
the telltale patterns, transition words, and signature symbols that AI detection tools look for.

## ⚠️ NGUYÊN TẮC BẤT KHẢ XÂM PHẠM: KHÔNG SỬA LINH TINH (INPUT SANCTITY)

1. **TIÊU ĐỀ & ĐỀ MỤC LÀ BẤT BIẾN (100% READ-ONLY):**
   - Giữ nguyên 100% từng chữ của tiêu đề báo cáo, tên đề tài, tên dự án và tiêu đề các mục do người dùng cung cấp.
   - Nghiêm cấm Agent tự ý "sáng tạo" hay đổi tiêu đề sang cụm từ khác trừ khi người dùng nói rõ: *"Hãy đặt lại tiêu đề giúp tôi"*.
2. **SỬA ĐÚNG TRỌNG TÂM - PHẪU THUẬT CHÍNH XÁC (SURGICAL EDITING):**
   - Chỉ can thiệp vào đúng các câu/đoạn có dấu vết AI (từ nối máy móc, câu quá phẳng, dính ký tự cấm).
   - Tuyệt đối không "xóa đi viết lại bừa bãi" (wholesale rewriting) làm biến dạng ý tưởng gốc hoặc xáo trộn trật tự đoạn văn của người dùng.
3. **BẢO LƯU NGUYÊN VẸN SỰ THẬT & THUẬT NGỮ:**
   - Số liệu thống kê, tên riêng người/cơ quan, ngày tháng, thông số kỹ thuật và thuật ngữ chuyên ngành phải được giữ nguyên vẹn 100%.

---

## The Core Problem: Why AI Text Gets Detected

AI models default to predictable patterns and visual telltales:
- Random inline bolding (**key phrases**) like social media posts
- Emojis in formal text (🚀, 💡, 📌, ✅)
- Overuse of em dashes (—) borrowed from English syntax
- Transition words used mechanically (Furthermore, Bên cạnh đó, Hơn nữa...)
- Arrow symbols (→, =>) instead of actual written sentences
- Lists and bullet points for everything ("bullet-point-itis")
- Uniform sentence lengths and paragraph sizes

---

## Workflow

### Step 1 – Understand the Context, Scope & Tone
Before writing, confirm:
- **Scope Limit**: Exactly which section/paragraph is the user asking to edit? (Do NOT touch anything outside this scope).
- **Preserve Title & Headings**: Lock the exact user's title and headings into memory.
- **Register**: Formal (academic/government) or Semi-formal/casual?
- **Tone Cloning**: Check if user provided sample text or if `./references/my_sample_style.md` exists. If so, follow `./references/tone-cloning.md`.

### Step 2 – Surgical Drafting with Human Patterns
Apply rules from `./references/humanizing-techniques.md` ONLY to sentences that need improvement:

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

**D. Structural Imperfection & Real-world Trade-offs**
- Occasionally start a sentence with "Nhưng", "Và", "Vì thế"
- Acknowledge real-world friction/trade-offs (costs, training, human habits) instead of proposing unrealistic ideal solutions

**E. Avoid Perfect Parallel Structure**
- Bad: "Thứ nhất... Thứ hai... Thứ ba... Cuối cùng..."
- Good: Vary how you introduce new points organically

### Step 3 – Apply the Banned Patterns Checklist
Reference `./references/common-ai-patterns.md` and verify:
- [ ] User's title and headings are strictly untouched
- [ ] No banned symbols used (no emojis, no inline bolding, no arrows)
- [ ] No banned transition words used
- [ ] No "AI vocabulary" words used
- [ ] Core facts, metrics, and terminology preserved

### Step 4 – Final Review
Before outputting, do a mental pass:
- Did I stay strictly within the user's requested scope?
- Did I accidentally alter any factual meaning or user's title?
- Does it read as natural human writing without drifting into chaos?
