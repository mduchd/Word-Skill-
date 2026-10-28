---
name: word-report-pro
description: >-
  Use this skill when the user asks to write, draft, format, or generate a
  Word document, official report, thesis, administrative proposal, meeting minutes,
  project proposal, or any structured Vietnamese professional document.
  Also use when the user needs help with document structure, formatting
  standards, structural & redundancy auditing (MECE check), citation rules,
  strict 100% Times New Roman font enforcement, table styling rules,
  or strict input sanctity preservation (never change user titles or scope).
---

# Word Report Pro

Skill for creating professional Vietnamese Word documents and reports following
Vietnamese administrative (Nghị định 30/2020/NĐ-CP) and academic formatting standards.

## ⚠️ NON-NEGOTIABLE CORE RULES (QUY TẮC BẮT BUỘC)

1. **BẢO VỆ NGUYÊN VẸN TIÊU ĐỀ & ĐẦU VÀO CỦA NGƯỜI DÙNG (INPUT SANCTITY):**
   - **TIÊU ĐỀ BÁO CÁO LÀ BẤT BIẾN:** Tuyệt đối KHÔNG tự ý đổi tiêu đề, tên đề tài, tên dự án của người dùng. Giữ nguyên 100% từng chữ trừ khi người dùng yêu cầu *"hãy sửa/đặt lại tiêu đề"*.
   - **SỬA ĐÚNG TRỌNG TÂM (Surgical Precision):** Người dùng yêu cầu sửa phần nào, CHỈ sửa đúng phần đó. Không tự ý xáo trộn các đoạn khác hoặc viết lại cả bài.
   - **BẢO TỒN THỰC THỂ & SỐ LIỆU:** Tên riêng, cơ quan, ngày tháng, thông số kỹ thuật, số liệu đo đạc phải giữ nguyên vẹn 100%. Xem chi tiết tại `./resources/input-sanctity.md`.

2. **100% Phông Chữ Times New Roman Cho Toàn Bộ Tài Liệu:**
   - Mọi thành phần: Trang bìa, Tiêu đề (H1, H2, H3), Thân bài, Bảng biểu, Chú thích hình/bảng, Đầu trang, Chân trang, Số trang, Chữ ký... **100% bắt buộc là Times New Roman**.
   - Tuyệt đối không để sót phông chữ mặc định của Word (Calibri, Aptos, Arial).

3. **Quy Tắc Bảng Biểu (Strict Table Rules):**
   - **NỀN TRẮNG 100% (No Shading):** Tuyệt đối KHÔNG tô màu xám, xanh, vàng hay bất kỳ màu nền nào trong bảng để tránh bị đen kịt hoặc mờ chữ khi in ấn/photo/ký số.
   - **KHÔNG IN ĐẬM NỘI DUNG TRONG BẢNG:**
     - Hàng tiêu đề cột: In đậm, căn giữa.
     - Các hàng dữ liệu bên trong: **Chữ thường đứng, KHÔNG in đậm**.
     - Ngoại lệ duy nhất: Hàng **TỔNG CỘNG** hoặc **TỔNG SỐ** ở cuối bảng được phép in đậm.
   - Cỡ chữ trong bảng: **11pt – 12pt** (nhỏ hơn thân bài 1-2 cỡ để bảng gọn gàng).
   - Căn lề trong bảng: Cột số căn phải, cột chữ căn trái, cột STT căn giữa.

4. **Căn Lề Đoạn Văn:** Thân bài luôn căn đều 2 bên (**Justified**), thụt đầu dòng **1.0 cm** (hoặc 1.27 cm), giãn dòng **1.5 lines**, Spacing Before/After 6pt.

---

## Workflow

### Step 1 – Identify Document Type & Preserve Title
Ask the user which type they need if not specified:
- **Khóa luận tốt nghiệp / Đề tài NCKH** → use `templates/khoa-luan-tot-nghiep.md`
- **Tờ trình hành chính (Chủ trương / Kinh phí)** → use `templates/to-trinh.md`
- **Báo cáo tổng hợp** (Summary Report) → use `templates/bao-cao-tong-hop.md`
- **Biên bản họp** (Meeting Minutes) → use `templates/bien-ban-hop.md`
- **Thuyết minh dự án** (Project Proposal) → use `templates/thuyet-minh-du-an.md`
*LƯU Ý: Khóa chặt tiêu đề người dùng cung cấp vào template, không tự ý chỉnh sửa.*

### Step 2 – Gather Content & Verify Citations
Collect from the user:
- Document title (exact match), issuing unit/author, date
- Main content sections and key points
- Data, figures, or tables to include
- Check `resources/citation-guide.md`: NEVER hallucinate fake author citations or fabricated statistics. Use explicit placeholders if sources are unknown.

### Step 3 – Draft with Template (Strict Scope)
Load the appropriate template from `./resources/templates/`.
Fill in all placeholder fields marked with `[[ ]]`.
Follow the structure strictly — do NOT skip sections and do NOT invent arbitrary unrequested sections.

### Step 4 – Structural & Redundancy Audit (MECE Principle)
Before finalizing the document, run the structural audit from `./resources/structural-audit.md`:
1. **Scope Boundary Check:** Ensure sections do not bleed into each other.
2. **De-duplicate Semantic Overlaps:** Merge or refer back instead of re-stating duplicate arguments.
3. **Volume Balance:** Ensure ~10-15% Intro, ~35-40% Findings/Body, ~35-40% Analysis/Solutions, ~10% Conclusion.
4. **No Conclusion Echoing:** The conclusion must provide synthesis and forward-looking decisions, NOT a copy-paste of the introduction.

### Step 5 – Apply Formatting Rules
- Follow `./resources/formatting-guide.md` strictly:
  - 100% Times New Roman.
  - Table: No background colors, no bold body text, 11pt.
  - Headings: H1 (14pt, Bold, ALL CAPS), H2 (13pt, Bold), H3 (13pt, Bold Italic).
  - Page numbers start on page 2, placed at top-center per Nghị định 30/2020.

### Step 6 – Generate Output
- Default: Output as **formatted Markdown** that mirrors Word layout
- If user has Python + python-docx: run `./scripts/generate_docx.py`
- Always end with a summary of what was created, confirming that the user's title and core facts were strictly preserved.
