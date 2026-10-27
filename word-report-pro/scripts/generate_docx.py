"""
generate_docx.py (Bản nâng cấp Pro)
───────────────────────────────────
Chuyển đổi file báo cáo Markdown sang .docx chuẩn thể thức Việt Nam:
- Chuẩn Nghị định 30/2020/NĐ-CP (Khổ A4, lề 2-2-3-2cm, Times New Roman 13pt).
- Bảng biểu nâng cao: Tự lặp tiêu đề trang mới (tblHeader), chống gãy dòng (cantSplit),
  tự động căn phải cột số, căn trái cột chữ.
- Chân trang chữ ký 2 bên dùng bảng ẩn viền (borderless) chống xô lệch trên các máy.
- Đánh số trang tự động: Bắt đầu từ trang 2, đặt ở canh giữa lề trên (chuẩn NĐ 30).
- Nhúng trường mục lục tự động (TOC - Table of Contents).

Yêu cầu:
    pip install python-docx

Cách dùng:
    python generate_docx.py baocao.md baocao.docx
"""

import sys
import re
from pathlib import Path

try:
    from docx import Document
    from docx.shared import Pt, Cm, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
    from docx.oxml.ns import qn, nsdecls
    from docx.oxml import OxmlElement, parse_xml
except ImportError:
    print("LỖI: Chưa cài đặt thư viện python-docx.")
    print("Vui lòng chạy lệnh: pip install python-docx")
    sys.exit(1)


# ── Thông số quy chuẩn thể thức Việt Nam (Nghị định 30/2020/NĐ-CP) ────────────
FONT_NAME    = "Times New Roman"
FONT_BODY    = 13
FONT_H1      = 14
FONT_H2      = 13
FONT_H3      = 13
MARGIN_TOP   = Cm(2.0)
MARGIN_BOT   = Cm(2.0)
MARGIN_LEFT  = Cm(3.0)
MARGIN_RIGHT = Cm(2.0)


def setup_document() -> Document:
    doc = Document()
    section = doc.sections[0]
    section.top_margin    = MARGIN_TOP
    section.bottom_margin = MARGIN_BOT
    section.left_margin   = MARGIN_LEFT
    section.right_margin  = MARGIN_RIGHT
    section.different_first_page_header_footer = True

    # Định dạng Style Normal
    style = doc.styles["Normal"]
    font  = style.font
    font.name = FONT_NAME
    font.size = Pt(FONT_BODY)
    font.color.rgb = RGBColor(0x22, 0x22, 0x22)

    pf = style.paragraph_format
    pf.line_spacing      = Pt(FONT_BODY * 1.35)
    pf.space_before      = Pt(4)
    pf.space_after       = Pt(4)
    pf.first_line_indent = Cm(1.27)
    return doc


def add_heading(doc: Document, text: str, level: int):
    """Thêm tiêu đề theo chuẩn cấp mục."""
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0)
    
    run = p.add_run(text.upper() if level == 1 else text)
    run.font.name = FONT_NAME
    run.font.bold = True
    run.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

    if level == 1:
        run.font.size = Pt(FONT_H1)
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after  = Pt(6)
    elif level == 2:
        run.font.size = Pt(FONT_H2)
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after  = Pt(4)
    else:
        run.font.size = Pt(FONT_H3)
        run.font.italic = True
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after  = Pt(3)


def add_page_number_to_header(section):
    """Đánh số trang từ trang 2, đặt ở canh giữa lề trên (Nghị định 30/2020)."""
    header = section.header
    p = header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.first_line_indent = Cm(0)

    run = p.add_run()
    run.font.name = FONT_NAME
    run.font.size = Pt(13)

    fldChar1 = OxmlElement("w:fldChar")
    fldChar1.set(qn("w:fldCharType"), "begin")
    instrText = OxmlElement("w:instrText")
    instrText.set(qn("xml:space"), "preserve")
    instrText.text = "PAGE"
    fldChar2 = OxmlElement("w:fldChar")
    fldChar2.set(qn("w:fldCharType"), "end")

    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)


def add_toc_field(doc: Document):
    """Chèn mã trường Mục Lục tự động (TOC)."""
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_after = Pt(12)
    run = p.add_run("MỤC LỤC TỰ ĐỘNG (Bấm chuột phải chọn Update Field để cập nhật số trang)")
    run.font.italic = True
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    fldSimple = OxmlElement("w:fldSimple")
    fldSimple.set(qn("w:instr"), 'TOC \\o "1-3" \\h \\z \\u')
    p._p.append(fldSimple)


def format_table_pro(table):
    """Định dạng bảng nâng cao: cantSplit, tblHeader, padding, viền."""
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Lặp lại tiêu đề khi sang trang
    header_tr = table.rows[0]._tr.get_or_add_trPr()
    header_tr.append(OxmlElement("w:tblHeader"))

    # Áp dụng cho từng dòng
    for row_idx, row in enumerate(table.rows):
        trPr = row._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))  # Ngăn gãy dòng

        for cell_idx, cell in enumerate(row.cells):
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after  = Pt(3)

            # Tiêu đề cột
            if row_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in p.runs:
                    run.font.bold = True
                    run.font.size = Pt(12)
                # Đổ màu nền xám nhẹ cho header
                shading = parse_xml(r'<w:shd {} w:fill="F2F2F2"/>'.format(nsdecls('w')))
                cell._tc.get_or_add_tcPr().append(shading)
            else:
                for run in p.runs:
                    run.font.size = Pt(12)
                # Tự động căn lề số hoặc chữ
                text = cell.text.strip()
                if re.match(r"^[\d.,%+\-–\/VNĐ$]+$", text) and not text.isalpha():
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                elif len(text) <= 5 and text.isdigit():
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT


def add_signature_block(doc: Document, left_title: str, right_title: str, left_name: str = "", right_name: str = ""):
    """Tạo khối chữ ký 2 cột ẩn viền (borderless) chống xô lệch vị trí."""
    table = doc.add_table(rows=3, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Ẩn viền bảng
    tblPr = table._tbl.tblPr
    borders = parse_xml(r'''
        <w:tblBorders {} >
            <w:top w:val="none"/>
            <w:left w:val="none"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
            <w:insideH w:val="none"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    '''.format(nsdecls('w')))
    tblPr.append(borders)

    # Dòng 1: Chức vụ / Đại diện
    cell_l1 = table.cell(0, 0).paragraphs[0]
    cell_l1.paragraph_format.first_line_indent = Cm(0)
    cell_l1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = cell_l1.add_run(left_title.upper())
    r1.font.bold = True

    cell_r1 = table.cell(0, 1).paragraphs[0]
    cell_r1.paragraph_format.first_line_indent = Cm(0)
    cell_r1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = cell_r1.add_run(right_title.upper())
    r2.font.bold = True

    # Dòng 2: Khoảng trống để ký
    cell_l2 = table.cell(1, 0).paragraphs[0]
    cell_l2.paragraph_format.first_line_indent = Cm(0)
    cell_l2.paragraph_format.space_before = Pt(45)
    cell_l2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cell_l2.add_run("(Ký và ghi rõ họ tên)").font.italic = True

    cell_r2 = table.cell(1, 1).paragraphs[0]
    cell_r2.paragraph_format.first_line_indent = Cm(0)
    cell_r2.paragraph_format.space_before = Pt(45)
    cell_r2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cell_r2.add_run("(Ký và ghi rõ họ tên)").font.italic = True

    # Dòng 3: Họ và tên
    if left_name:
        cell_l3 = table.cell(2, 0).paragraphs[0]
        cell_l3.paragraph_format.first_line_indent = Cm(0)
        cell_l3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = cell_l3.add_run(left_name)
        r.font.bold = True

    if right_name:
        cell_r3 = table.cell(2, 1).paragraphs[0]
        cell_r3.paragraph_format.first_line_indent = Cm(0)
        cell_r3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = cell_r3.add_run(right_name)
        r.font.bold = True


def parse_markdown_to_docx(md_text: str, doc: Document):
    """Phân tích nội dung Markdown và xuất ra văn bản Word hoàn chỉnh."""
    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        # Mục lục tự động
        if "MỤC LỤC" in line.upper() and ("(TỰ ĐỘNG" in line.upper() or "TABLE OF CONTENTS" in line.upper()):
            add_heading(doc, "MỤC LỤC", 1)
            add_toc_field(doc)
            i += 1
            continue

        # Tiêu đề các cấp
        if line.startswith("### "):
            add_heading(doc, line[4:], 3)
        elif line.startswith("## "):
            add_heading(doc, line[3:], 2)
        elif line.startswith("# "):
            add_heading(doc, line[2:], 1)
        # Đường kẻ ngang hoặc ngắt trang
        elif line.startswith("---") or line.startswith("***"):
            p = doc.add_paragraph()
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after  = Pt(6)
            run = p.add_run("─" * 55)
            run.font.color.rgb = RGBColor(0xBB, 0xBB, 0xBB)
        # Chú thích bảng hoặc hình ảnh
        elif line.startswith("*Bảng") or line.startswith("*Hình"):
            p = doc.add_paragraph()
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after  = Pt(4)
            if line.startswith("*Hình"):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(line.strip("*"))
            run.font.italic = True
            run.font.size = Pt(11)
        # Bảng biểu Markdown
        elif line.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            i -= 1  # Lùi lại 1 bước vì while vượt quá

            rows_data = []
            for t_line in table_lines:
                cells = [c.strip() for c in t_line.strip("|").split("|")]
                if all(set(c) <= set("-: ") for c in cells):
                    continue  # Bỏ qua dòng phân cách |---|---|
                rows_data.append(cells)

            if rows_data:
                col_count = len(rows_data[0])
                table = doc.add_table(rows=len(rows_data), cols=col_count)
                table.style = "Table Grid"
                for r_idx, r_data in enumerate(rows_data):
                    for c_idx, cell_text in enumerate(r_data):
                        if c_idx < col_count:
                            table.cell(r_idx, c_idx).text = cell_text
                format_table_pro(table)
        # Khối chữ ký đối xứng
        elif ("**CHỦ TỌA**" in line and "**THƯ KÝ**" in line) or ("**ĐƠN VỊ PHÊ DUYỆT**" in line and "**CHỦ NHIỆM DỰ ÁN**" in line):
            left_t = "CHỦ TRÌ / PHÊ DUYỆT"
            right_t = "NGƯỜI LẬP / THƯ KÝ"
            if "CHỦ TỌA" in line:
                left_t, right_t = "CHỦ TỌA", "THƯ KÝ"
            elif "ĐƠN VỊ PHÊ DUYỆT" in line:
                left_t, right_t = "ĐƠN VỊ PHÊ DUYỆT", "CHỦ NHIỆM DỰ ÁN"
            add_signature_block(doc, left_t, right_t)
        # Đoạn văn thường
        else:
            p = doc.add_paragraph()
            # Bỏ thụt đầu dòng nếu là căn giữa hoặc dòng trích yếu
            if line.startswith("**") and line.endswith("**") and len(line) < 100:
                p.paragraph_format.first_line_indent = Cm(0)
                p.add_run(line.replace("**", "")).font.bold = True
            else:
                p.paragraph_format.first_line_indent = Cm(1.27)
                p.add_run(line)

        i += 1


def main():
    if len(sys.argv) < 2:
        print("Sử dụng: python generate_docx.py <input.md> [output.docx]")
        sys.exit(1)

    input_path  = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_suffix(".docx")

    if not input_path.exists():
        print(f"LỖI: Không tìm thấy file nguồn {input_path}")
        sys.exit(1)

    md_text = input_path.read_text(encoding="utf-8")
    doc = setup_document()
    parse_markdown_to_docx(md_text, doc)
    add_page_number_to_header(doc.sections[0])
    doc.save(output_path)
    print(f"✅ Đã tạo file Word chuẩn: {output_path}")


if __name__ == "__main__":
    main()
