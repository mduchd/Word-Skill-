"""
generate_docx.py
────────────────
Convert a Markdown report file into a properly formatted .docx
following Vietnamese administrative standards (Nghi dinh 30/2020).

Requirements:
    pip install python-docx markdown

Usage:
    python generate_docx.py input.md output.docx
    python generate_docx.py input.md           # saves as input.docx
"""

import sys
import re
from pathlib import Path

try:
    from docx import Document
    from docx.shared import Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
except ImportError:
    print("ERROR: python-docx not installed. Run: pip install python-docx")
    sys.exit(1)


# ── Vietnamese formatting constants ─────────────────────────────────────────
FONT_NAME   = "Times New Roman"
FONT_BODY   = 13
FONT_H1     = 14
FONT_H2     = 13
FONT_H3     = 13
MARGIN_TOP  = Cm(2.0)
MARGIN_BOT  = Cm(2.0)
MARGIN_LEFT = Cm(3.0)
MARGIN_RIGHT= Cm(2.0)


def setup_document() -> Document:
    doc = Document()
    section = doc.sections[0]
    section.top_margin    = MARGIN_TOP
    section.bottom_margin = MARGIN_BOT
    section.left_margin   = MARGIN_LEFT
    section.right_margin  = MARGIN_RIGHT

    # Default paragraph style
    style = doc.styles["Normal"]
    font  = style.font
    font.name = FONT_NAME
    font.size = Pt(FONT_BODY)

    pf = style.paragraph_format
    pf.line_spacing   = Pt(FONT_BODY * 1.4)
    pf.space_before   = Pt(6)
    pf.space_after    = Pt(6)
    pf.first_line_indent = Cm(1.27)
    return doc


def add_heading(doc: Document, text: str, level: int):
    """Add a heading with correct Vietnamese formatting."""
    p = doc.add_paragraph()
    run = p.add_run(text.upper() if level == 1 else text)
    run.font.name = FONT_NAME
    run.font.bold = True
    run.font.italic = (level == 3)
    run.font.size = Pt(FONT_H1 if level == 1 else FONT_H2)
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after  = Pt(6)


def add_body(doc: Document, text: str):
    p = doc.add_paragraph(text)
    p.paragraph_format.first_line_indent = Cm(1.27)


def add_footer_page_numbers(doc: Document):
    """Add right-aligned page numbers to footer."""
    section = doc.sections[0]
    footer  = section.footer
    p       = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run()
    fldChar1 = OxmlElement("w:fldChar")
    fldChar1.set(qn("w:fldCharType"), "begin")
    instrText = OxmlElement("w:instrText")
    instrText.text = "PAGE"
    fldChar2 = OxmlElement("w:fldChar")
    fldChar2.set(qn("w:fldCharType"), "end")
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)


def parse_markdown_to_docx(md_text: str, doc: Document):
    lines = md_text.splitlines()
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # Headings
        if stripped.startswith("### "):
            add_heading(doc, stripped[4:], 3)
        elif stripped.startswith("## "):
            add_heading(doc, stripped[3:], 2)
        elif stripped.startswith("# "):
            add_heading(doc, stripped[2:], 1)
        # Horizontal rule
        elif stripped.startswith("---"):
            doc.add_paragraph("─" * 60).paragraph_format.first_line_indent = Cm(0)
        # Table row (basic)
        elif stripped.startswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue  # separator row
            table = doc.add_table(rows=1, cols=len(cells))
            table.style = "Table Grid"
            row = table.rows[0]
            for i, cell_text in enumerate(cells):
                row.cells[i].text = cell_text
        # Normal paragraph
        else:
            add_body(doc, stripped)


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_docx.py <input.md> [output.docx]")
        sys.exit(1)

    input_path  = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_suffix(".docx")

    if not input_path.exists():
        print(f"ERROR: File not found: {input_path}")
        sys.exit(1)

    md_text = input_path.read_text(encoding="utf-8")
    doc = setup_document()
    parse_markdown_to_docx(md_text, doc)
    add_footer_page_numbers(doc)
    doc.save(output_path)
    print(f"✅ Saved: {output_path}")


if __name__ == "__main__":
    main()
