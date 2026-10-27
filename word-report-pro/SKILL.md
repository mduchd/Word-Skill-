---
name: word-report-pro
description: >-
  Use this skill when the user asks to write, draft, format, or generate a
  Word document, official report, thesis, administrative proposal, meeting minutes,
  project proposal, or any structured Vietnamese professional document.
  Also use when the user needs help with document structure, formatting
  standards, structural & redundancy auditing (MECE check), citation rules,
  or converting Markdown into a properly formatted .docx file.
---

# Word Report Pro

Skill for creating professional Vietnamese Word documents and reports following
Vietnamese administrative and academic formatting standards.

## Core Formatting Standards (Vietnamese)

Based on Nghị định 30/2020/NĐ-CP:

| Property | Value |
|---|---|
| Font | Times New Roman |
| Body size | 13pt |
| Heading 1 | 14pt, Bold, ALL CAPS |
| Heading 2 | 13pt, Bold |
| Heading 3 | 13pt, Bold, Italic |
| Line spacing | 1.3 – 1.5 |
| Margin Top | 2.0 cm |
| Margin Bottom | 2.0 cm |
| Margin Left | 3.0 cm |
| Margin Right | 2.0 cm |
| Page size | A4 |
| Paragraph indent | 1.27 cm (first line) |

## Workflow

### Step 1 – Identify Document Type
Ask the user which type they need if not specified:
- **Khóa luận tốt nghiệp / Đề tài NCKH** → use `templates/khoa-luan-tot-nghiep.md`
- **Tờ trình hành chính (Chủ trương / Kinh phí)** → use `templates/to-trinh.md`
- **Báo cáo tổng hợp** (Summary Report) → use `templates/bao-cao-tong-hop.md`
- **Biên bản họp** (Meeting Minutes) → use `templates/bien-ban-hop.md`
- **Thuyết minh dự án** (Project Proposal) → use `templates/thuyet-minh-du-an.md`

### Step 2 – Gather Content & Verify Citations
Collect from the user:
- Document title, issuing unit/author, date
- Main content sections and key points
- Data, figures, or tables to include
- Check `resources/citation-guide.md`: NEVER hallucinate fake author citations or fabricated statistics. Use explicit placeholders if sources are unknown.

### Step 3 – Draft with Template
Load the appropriate template from `./resources/templates/`.
Fill in all placeholder fields marked with `[[ ]]`.
Follow the structure strictly — do NOT skip sections.

### Step 4 – Structural & Redundancy Audit (MECE Principle)
Before finalizing the document, run the structural audit from `./resources/structural-audit.md`:
1. **Scope Boundary Check:** Ensure sections do not bleed into each other (e.g., Introduction must not reveal detailed conclusions; Solutions must not re-explain the problem).
2. **De-duplicate Semantic Overlaps:** Check if adjacent sub-sections or chapters repeat the same core argument with different wording. Merge or refer back instead of re-stating.
3. **Volume Balance:** Ensure ~10-15% Intro, ~35-40% Findings/Body, ~35-40% Analysis/Solutions, ~10% Conclusion.
4. **No Conclusion Echoing:** The conclusion must provide synthesis and forward-looking decisions, NOT a copy-paste of the introduction.

### Step 5 – Apply Formatting Rules
- Use `./resources/formatting-guide.md` for detailed rules
- Number all sections (1., 1.1., 1.1.1.)
- Tables must have headers and borders (cantSplit, tblHeader)
- Figures/images must have captions below them
- Page numbers start on page 2, placed at top-center per Nghị định 30/2020

### Step 6 – Generate Output
- Default: Output as **formatted Markdown** that mirrors Word layout
- If user has Python + python-docx: run `./scripts/generate_docx.py`
- Always end with a summary of what was created
