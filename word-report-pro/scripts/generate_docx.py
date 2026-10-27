"""
generate_docx.py (Bản Chuẩn Thể Thức Nhà Nước & Luận Văn Tốt Nghiệp)
───────────────────────────────────────────────────────────────────
Cập nhật theo chuẩn Nghị định 30/2020/NĐ-CP & Quy chuẩn Luận văn (ĐH Thái Nguyên / ĐHQG / Blog Dạy Tin Học):
- CĂN LỀ: Trái 3.0 cm, Phải 1.5 cm, Trên 2.0 cm, Dưới 2.0 cm (Khổ A4 đứng).
- ĐOẠN VĂN: Căn đều 2 bên (Justified), Giãn dòng 1.5 lines, Spacing Before/After 6pt,
  Thụt đầu dòng chuẩn 1.0 cm.
- NGẮT TRANG ĐẦU CHƯƠNG: Tự động ngắt trang trước mỗi Tiêu đề cấp 1 (# CHƯƠNG, # KẾT LUẬN).
- CHỐNG TIÊU ĐỀ MỒ CÔI: Bật keep_with_next cho toàn bộ Heading 1, 2, 3.
- MỤC LỤC TỰ ĐỘNG: Nhúng mã trường TOC cho Nội dung, Danh mục Bảng biểu ({TOC \c "Bảng"}),
  Danh mục Hình ảnh ({TOC \c "Hình"}).
- BẢNG BIỂU:
  + NỀN TRẮNG 100% (KHÔNG tô màu xám/xanh).
  + KHÔNG in đậm dữ liệu (chỉ in đậm tiêu đề hoặc dòng Tổng cộng).
  + Cỡ chữ bảng: 11 - 12pt.
  + Chống gãy dòng khi sang trang (cantSplit), tự lặp tiêu đề (tblHeader).
- 100% TOÀN BỘ VĂN BẢN LÀ PHÔNG CHỮ "TIMES NEW ROMAN" (thiết lập sâu XML w:rFonts).
- ĐÁNH SỐ TRANG: Tự động từ trang 2, đặt ở canh giữa lề trên.

Yêu cầu:
    pip install python-docx

Cách dùng:
    python generate_docx.py input.md output.docx
"""

import sys
import re
from pathlib import Path

# Đảm bảo console Windows không bị lỗi Unicode
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

try:
    from docx import Document
    from docx.shared import Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
    from docx.oxml.ns import qn, nsdecls
    from docx.oxml import OxmlElement, parse_xml
except ImportError:
    print("LỖI: Chưa cài đặt python-docx. Hãy chạy: pip install python-docx")
    sys.exit(1)


# ── Quy chuẩn thể thức (NĐ 30/2020 & Quy chuẩn ĐH Thái Nguyên) ───────────────
FONT_NAME    = "Times New Roman"
FONT_BODY    = 13
FONT_H1      = 14
FONT_H2      = 13
FONT_H3      = 13
FONT_TABLE   = 11
MARGIN_TOP   = Cm(2.0)
MARGIN_BOT   = Cm(2.0)
MARGIN_LEFT  = Cm(3.0)   # Đóng gáy luận văn
MARGIN_RIGHT = Cm(1.5)   # Chuẩn ĐH Thái Nguyên (1.5cm giúp trang thoáng rộng)


def force_times_new_roman(run, size=None, bold=None, italic=None, color=None):
    """
    Ép buộc phông chữ Times New Roman sâu vào thuộc tính XML (w:rFonts).
    Đảm bảo 100% không bao giờ bị Word tự chuyển sang Calibri / Aptos.
    """
    run.font.name = FONT_NAME
    rPr = run._r.get_or_add_rPr()
    rFonts = parse_xml(
        f'<w:rFonts {nsdecls("w")} w:ascii="{FONT_NAME}" w:hAnsi="{FONT_NAME}"'
        f' w:cs="{FONT_NAME}" w:eastAsia="{FONT_NAME}"/>'
    )
    rPr.append(rFonts)

    if size is not None:
        run.font.size = Pt(size)
    if bold is not None:
        run.font.bold = bold
    if italic is not None:
        run.font.italic = italic
    if color is not None:
        run.font.color.rgb = color


def setup_document() -> Document:
    doc = Document()
    section = doc.sections[0]
    section.top_margin    = MARGIN_TOP
    section.bottom_margin = MARGIN_BOT
    section.left_margin   = MARGIN_LEFT
    section.right_margin  = MARGIN_RIGHT
    section.different_first_page_header_footer = True

    # Cấu hình Style mặc định toàn tài liệu là Times New Roman
    style = doc.styles["Normal"]
    style.font.name = FONT_NAME
    style.font.size = Pt(FONT_BODY)
    style.font.color.rgb = RGBColor(0x11, 0x11, 0x11)

    pf = style.paragraph_format
    pf.line_spacing      = Pt(FONT_BODY * 1.5)  # Chuẩn 1.5 lines
    pf.space_before      = Pt(6)                # Chuẩn Spacing Before 6pt
    pf.space_after       = Pt(6)                # Chuẩn Spacing After 6pt
    pf.alignment         = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf.first_line_indent = Cm(1.0)              # Chuẩn First line 1.0 cm
    return doc


def add_heading(doc: Document, text: str, level: int, is_first_heading: bool = False):
    """
    Thêm tiêu đề chuẩn Times New Roman theo cấp bậc:
    - Bật keep_with_next để chống tiêu đề mồ côi ở cuối trang.
    - Cấp 1 (# CHƯƠNG): Bật page_break_before để tự động mở đầu trang mới.
    """
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.keep_with_next = True    # Chống mồ côi dòng tiêu đề
    
    run = p.add_run(text.upper() if level == 1 else text)
    if level == 1:
        force_times_new_roman(run, size=FONT_H1, bold=True)
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after  = Pt(6)
        # Tự động ngắt sang trang mới trước mỗi chương (ngoại trừ tiêu đề bìa đầu tiên)
        if not is_first_heading and len(doc.paragraphs) > 2:
            p.paragraph_format.page_break_before = True
    elif level == 2:
        force_times_new_roman(run, size=FONT_H2, bold=True)
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after  = Pt(4)
    else:
        force_times_new_roman(run, size=FONT_H3, bold=True, italic=True)
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after  = Pt(3)


def add_page_number_to_header(section):
    """Đánh số trang từ trang 2, đặt ở canh giữa lề trên (chuẩn Nghị định 30/2020)."""
    header = section.header
    p = header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.first_line_indent = Cm(0)

    run = p.add_run()
    force_times_new_roman(run, size=13)

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
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(12)
    run = p.add_run("MỤC LỤC TỰ ĐỘNG (Bấm chuột phải chọn Update Field để cập nhật số trang)")
    force_times_new_roman(run, size=11, italic=True, color=RGBColor(0x66, 0x66, 0x66))

    fldSimple = OxmlElement("w:fldSimple")
    fldSimple.set(qn("w:instr"), 'TOC \\o "1-3" \\h \\z \\u')
    p._p.append(fldSimple)


def add_tof_field(doc: Document, label: str):
    """Chèn mã trường Danh mục Bảng biểu hoặc Hình ảnh tự động (Table of Figures)."""
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_after = Pt(12)
    run = p.add_run(f"DANH MỤC {label.upper()} TỰ ĐỘNG (Bấm chuột phải chọn Update Field để cập nhật số trang)")
    force_times_new_roman(run, size=11, italic=True, color=RGBColor(0x66, 0x66, 0x66))

    fldSimple = OxmlElement("w:fldSimple")
    fldSimple.set(qn("w:instr"), f'TOC \\c "{label}" \\h \\z \\u')
    p._p.append(fldSimple)


def format_table_strict(table):
    """
    Định dạng bảng nghiêm ngặt:
    - NỀN TRẮNG 100% (TUYỆT ĐỐI KHÔNG TÔ MÀU NỀN).
    - KHÔNG IN ĐẬM dữ liệu (chỉ in đậm tiêu đề hoặc dòng Tổng cộng).
    - 100% Phông chữ Times New Roman cỡ 11pt.
    - Chống gãy dòng (cantSplit), lặp tiêu đề trang (tblHeader).
    """
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Lặp lại dòng tiêu đề khi sang trang mới
    header_tr = table.rows[0]._tr.get_or_add_trPr()
    header_tr.append(OxmlElement("w:tblHeader"))

    for row_idx, row in enumerate(table.rows):
        trPr = row._tr.get_or_add_trPr()
        trPr.append(OxmlElement("w:cantSplit"))  # Ngăn gãy dòng giữa 2 trang

        # Kiểm tra xem dòng này có phải dòng TỔNG CỘNG / TỔNG SỐ không
        is_total_row = any("TỔNG" in cell.text.upper() for cell in row.cells)

        for cell_idx, cell in enumerate(row.cells):
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after  = Pt(2)

            cell_text = cell.text.strip()

            # Dòng tiêu đề cột (Row 0)
            if row_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.text = cell_text
                if p.runs:
                    force_times_new_roman(p.runs[0], size=FONT_TABLE, bold=True)
            # Dòng Tổng cộng
            elif is_total_row:
                p.text = cell_text
                if p.runs:
                    force_times_new_roman(p.runs[0], size=FONT_TABLE, bold=True)
                if re.match(r"^[\d.,%+\-–\/VNĐ$]+$", cell_text) and not cell_text.isalpha():
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            # Các dòng dữ liệu thông thường: TUYỆT ĐỐI KHÔNG IN ĐẬM
            else:
                p.text = cell_text
                if p.runs:
                    force_times_new_roman(p.runs[0], size=FONT_TABLE, bold=False)

                # Quy tắc căn lề thông minh
                if re.match(r"^[\d.,%+\-–\/VNĐ$]+$", cell_text) and not cell_text.isalpha():
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT  # Cột số căn phải
                elif len(cell_text) <= 5 and cell_text.isdigit():
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER  # STT căn giữa
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT    # Văn bản căn trái


def add_signature_block(doc: Document, left_title: str, right_title: str, left_name: str = "", right_name: str = ""):
    """Tạo khối chữ ký 2 cột ẩn viền, chuẩn Times New Roman."""
    table = doc.add_table(rows=3, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

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

    # Dòng 1: Chức vụ
    cell_l1 = table.cell(0, 0).paragraphs[0]
    cell_l1.paragraph_format.first_line_indent = Cm(0)
    cell_l1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = cell_l1.add_run(left_title.upper())
    force_times_new_roman(r1, size=FONT_BODY, bold=True)

    cell_r1 = table.cell(0, 1).paragraphs[0]
    cell_r1.paragraph_format.first_line_indent = Cm(0)
    cell_r1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = cell_r1.add_run(right_title.upper())
    force_times_new_roman(r2, size=FONT_BODY, bold=True)

    # Dòng 2: Khoảng trống để ký
    cell_l2 = table.cell(1, 0).paragraphs[0]
    cell_l2.paragraph_format.first_line_indent = Cm(0)
    cell_l2.paragraph_format.space_before = Pt(45)
    cell_l2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r3 = cell_l2.add_run("(Ký và ghi rõ họ tên)")
    force_times_new_roman(r3, size=11, italic=True)

    cell_r2 = table.cell(1, 1).paragraphs[0]
    cell_r2.paragraph_format.first_line_indent = Cm(0)
    cell_r2.paragraph_format.space_before = Pt(45)
    cell_r2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r4 = cell_r2.add_run("(Ký và ghi rõ họ tên)")
    force_times_new_roman(r4, size=11, italic=True)

    # Dòng 3: Họ và tên
    if left_name:
        cell_l3 = table.cell(2, 0).paragraphs[0]
        cell_l3.paragraph_format.first_line_indent = Cm(0)
        cell_l3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r5 = cell_l3.add_run(left_name)
        force_times_new_roman(r5, size=FONT_BODY, bold=True)

    if right_name:
        cell_r3 = table.cell(2, 1).paragraphs[0]
        cell_r3.paragraph_format.first_line_indent = Cm(0)
        cell_r3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r6 = cell_r3.add_run(right_name)
        force_times_new_roman(r6, size=FONT_BODY, bold=True)


def parse_markdown_to_docx(md_text: str, doc: Document):
    """Phân tích nội dung Markdown và xuất ra Word chuẩn 100% Times New Roman."""
    lines = md_text.splitlines()
    i = 0
    first_h1_passed = False

    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        # Mục lục nội dung tự động
        if "MỤC LỤC" in line.upper() and ("(TỰ ĐỘNG" in line.upper() or "TABLE OF CONTENTS" in line.upper() or line.strip("# ") == "MỤC LỤC"):
            add_heading(doc, "MỤC LỤC", 1, is_first_heading=(not first_h1_passed))
            first_h1_passed = True
            add_toc_field(doc)
            i += 1
            continue

        # Danh mục Bảng biểu tự động ({TOC \c "Bảng"})
        if "DANH MỤC" in line.upper() and "BẢNG" in line.upper():
            title = line.strip("#* ")
            add_heading(doc, title, 1, is_first_heading=(not first_h1_passed))
            first_h1_passed = True
            add_tof_field(doc, label="Bảng")
            i += 1
            continue

        # Danh mục Hình ảnh tự động ({TOC \c "Hình"})
        if "DANH MỤC" in line.upper() and ("HÌNH" in line.upper() or "BIỂU ĐỒ" in line.upper()):
            title = line.strip("#* ")
            add_heading(doc, title, 1, is_first_heading=(not first_h1_passed))
            first_h1_passed = True
            add_tof_field(doc, label="Hình")
            i += 1
            continue

        # Tiêu đề các cấp
        if line.startswith("### "):
            add_heading(doc, line[4:], 3)
        elif line.startswith("## "):
            add_heading(doc, line[3:], 2)
        elif line.startswith("# "):
            add_heading(doc, line[2:], 1, is_first_heading=(not first_h1_passed))
            first_h1_passed = True
        # Đường kẻ ngang
        elif line.startswith("---") or line.startswith("***"):
            p = doc.add_paragraph()
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after  = Pt(4)
            r = p.add_run("─" * 50)
            force_times_new_roman(r, size=11, color=RGBColor(0xCC, 0xCC, 0xCC))
        # Chú thích bảng hoặc hình ảnh (Times New Roman 11pt, nghiêng)
        elif line.startswith("*Bảng") or line.startswith("*Hình"):
            p = doc.add_paragraph()
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after  = Pt(4)
            if line.startswith("*Hình"):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(line.strip("*"))
            force_times_new_roman(r, size=11, italic=True)
        # Bảng biểu Markdown
        elif line.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            i -= 1

            rows_data = []
            for t_line in table_lines:
                cells = [c.strip() for c in t_line.strip("|").split("|")]
                if all(set(c) <= set("-: ") for c in cells):
                    continue
                rows_data.append(cells)

            if rows_data:
                col_count = len(rows_data[0])
                table = doc.add_table(rows=len(rows_data), cols=col_count)
                table.style = "Table Grid"
                for r_idx, r_data in enumerate(rows_data):
                    for c_idx, cell_text in enumerate(r_data):
                        if c_idx < col_count:
                            table.cell(r_idx, c_idx).text = cell_text
                format_table_strict(table)
        # Khối chữ ký đối xứng
        elif ("**CHỦ TỌA**" in line and "**THƯ KÝ**" in line) or ("**ĐƠN VỊ PHÊ DUYỆT**" in line and "**CHỦ NHIỆM DỰ ÁN**" in line) or ("**LÃNH ĐẠO ĐƠN VỊ" in line):
            left_t = "CHỦ TRÌ / PHÊ DUYỆT"
            right_t = "NGƯỜI LẬP / THỦ TRƯỞNG"
            if "CHỦ TỌA" in line:
                left_t, right_t = "CHỦ TỌA", "THƯ KÝ"
            elif "ĐƠN VỊ PHÊ DUYỆT" in line:
                left_t, right_t = "ĐƠN VỊ PHÊ DUYỆT", "CHỦ NHIỆM DỰ ÁN"
            elif "LÃNH ĐẠO ĐƠN VỊ" in line:
                left_t, right_t = "LÃNH ĐẠO PHỤ TRÁCH", "THỦ TRƯỞNG ĐƠN VỊ"
            add_signature_block(doc, left_t, right_t)
        # Đoạn văn thường
        else:
            p = doc.add_paragraph()
            # Tiêu đề hoặc dòng căn giữa
            if line.startswith("**") and line.endswith("**") and len(line) < 100:
                p.paragraph_format.first_line_indent = Cm(0)
                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = p.add_run(line.replace("**", ""))
                force_times_new_roman(r, size=FONT_BODY, bold=True)
            else:
                p.paragraph_format.first_line_indent = Cm(1.0)  # Chuẩn First line 1.0 cm
                p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                r = p.add_run(line)
                force_times_new_roman(r, size=FONT_BODY, bold=False)

        i += 1


def main():
    if len(sys.argv) < 2:
        print("Sử dụng: python generate_docx.py <input.md> [output.docx]")
        sys.exit(1)

    input_path  = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.with_suffix(".docx")

    if not input_path.exists():
        print(f"LỖI: Không tìm thấy file {input_path}")
        sys.exit(1)

    md_text = input_path.read_text(encoding="utf-8")
    doc = setup_document()
    parse_markdown_to_docx(md_text, doc)
    add_page_number_to_header(doc.sections[0])
    doc.save(output_path)
    print(f"✅ Đã tạo file Word chuẩn 100% Times New Roman & ĐH Thái Nguyên: {output_path}")


if __name__ == "__main__":
    main()
