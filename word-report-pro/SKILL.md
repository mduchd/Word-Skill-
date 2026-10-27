---
name: word-report-pro
description: >-
  Use this skill when the user asks to write, draft, format, or generate a
  Word document, official report, administrative document, meeting minutes,
  project proposal, or any structured Vietnamese professional document.
  Also use when the user needs help with document structure, formatting
  standards, or converting text into a properly formatted report.
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
- **Báo cáo tổng hợp** (Summary Report) → use `templates/bao-cao-tong-hop.md`
- **Biên bản họp** (Meeting Minutes) → use `templates/bien-ban-hop.md`
- **Thuyết minh dự án** (Project Proposal) → use `templates/thuyet-minh-du-an.md`
- **Công văn** (Official Letter) → use `templates/cong-van.md`
- **Tiểu luận / Luận văn** (Essay / Thesis) → use `templates/tieu-luan.md`

### Step 2 – Gather Content
Collect from the user:
- Document title, issuing unit/author, date
- Main content sections and key points
- Any data, figures, or tables to include

### Step 3 – Draft with Template
Load the appropriate template from `./resources/templates/`.
Fill in all placeholder fields marked with `[[ ]]`.
Follow the structure strictly — do NOT skip sections.

### Step 4 – Apply Formatting Rules
- Use `./resources/formatting-guide.md` for detailed rules
- Number all sections (1., 1.1., 1.1.1.)
- Tables must have headers and borders
- Figures/images must have captions below them
- Page numbers in footer (right-aligned)

### Step 5 – Generate Output
- Default: Output as **formatted Markdown** that mirrors Word layout
- If user has Python + python-docx: run `./scripts/generate_docx.py`
- Always end with a summary of what was created

## Key Rules
- ALWAYS write in Vietnamese unless user requests otherwise
- NEVER use bullet points for formal sections — use numbered headings
- ALWAYS include: cover page info, table of contents placeholder, conclusion
- Date format: ngày DD tháng MM năm YYYY
- Signature block goes bottom-right, name centered below the title
