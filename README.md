# Word-Skill- (Bộ Skill Soạn Báo Cáo & Tránh AI Cho Google Antigravity)

Bộ 3 skill chuyên biệt dành cho Google Antigravity / Gemini CLI nhằm hỗ trợ soạn thảo văn bản Word, báo cáo hành chính - học thuật theo quy chuẩn Việt Nam, kết hợp kỹ thuật nhân hóa văn phong và tối ưu điểm AI detector.

---

## 📦 Danh Sách & Cấu Trúc Chi Tiết Các Skill

### 1. `word-report-pro` (Soạn Báo Cáo & Xuất Word Chuẩn)
- **Mục đích:** Soạn thảo, chuẩn hóa cấu trúc báo cáo, văn bản hành chính theo chuẩn Nghị định 30/2020/NĐ-CP (Times New Roman 13pt, lề 2-2-3-2 cm, đánh số phân cấp khoa học).
- **Tài nguyên kèm theo:**
  - `resources/formatting-guide.md`: Bảng quy chuẩn lề, font, ngắt dòng, đánh số mục.
  - `resources/structural-audit.md`: Bộ quy tắc kiểm tra ranh giới nội dung và loại bỏ trùng lặp ý tưởng theo nguyên tắc MECE.
  - `resources/citation-guide.md`: Hướng dẫn trích dẫn chuẩn APA 7th, IEEE và quy tắc Citation Guard chống bịa nguồn.
  - `resources/templates/`: Các mẫu tài liệu chuẩn thực chiến:
    - `khoa-luan-tot-nghiep.md`: Khóa luận tốt nghiệp / Đề tài NCKH đầy đủ Lời cam đoan, Lời cảm ơn, Tóm tắt, Danh mục viết tắt, 5 chương nội dung.
    - `to-trinh.md`: Mẫu tờ trình hành chính xin phê duyệt chủ trương và dự toán kinh phí.
    - `bao-cao-tong-hop.md`: Báo cáo tổng kết / định kỳ công tác.
    - `bien-ban-hop.md`: Biên bản họp cơ quan / dự án.
    - `thuyet-minh-du-an.md`: Thuyết minh đề tài / dự án đầu tư.
  - `scripts/generate_docx.py`: Script Python nâng cao xuất file `.docx` chuyên nghiệp:
    - Bảng biểu chống ngắt dòng (`cantSplit`), tự lặp tiêu đề trang mới (`tblHeader`).
    - Cột số tự động căn phải, cột chữ căn trái.
    - Khối chữ ký 2 cột ẩn viền không bị xô lệch layout.
    - Đánh số trang tự động từ trang 2 đặt ở canh giữa lề trên (chuẩn NĐ 30/2020).
    - Nhúng mã trường mục lục tự động (TOC field code).

### 2. `anti-ai-writer` (Nhân Hóa Văn Phong Người Viết)
- **Mục đích:** Viết nội dung mang văn phong người thật, loại bỏ "AI fingerprint" (dấu vân tay AI) ngay từ khâu sinh văn bản.
- **Tài nguyên kèm theo:**
  - `references/humanizing-techniques.md`: Quy tắc 30-50-20 về nhịp điệu câu, cách ngắt nhịp tự nhiên, chèn ý kiến chủ quan có kiểm soát.
  - `references/common-ai-patterns.md`: Blacklist các từ ngữ sáo rỗng AI hay dùng (*furthermore, delve, bên cạnh đó, trong bối cảnh hiện nay...*).
  - `references/tone-cloning.md`: Kỹ thuật trích xuất và bắt chước văn phong cá nhân từ bài viết mẫu của người dùng.
  - `examples/before-after-formal.md`: Các case study đối chiếu trực tiếp trước & sau khi nhân hóa văn phong.

### 3. `ai-detection-bypass` (Đo Lường & Rewrite Bypass Detector)
- **Mục đích:** Rà soát, chấm điểm định lượng nguy cơ bị nhận diện bởi các công cụ AI detector (GPTZero, Turnitin, Copyleaks, ZeroGPT) và thực hiện chiến lược rewrite tương ứng.
- **Tài nguyên kèm theo:**
  - `scripts/analyze_text.py`: Công cụ Python đo lường chỉ số Burstiness (độ lệch chuẩn độ dài câu), tỷ lệ câu ngắn/dài, mật độ từ khóa AI và tính toán AI Risk Index (0 - 100%).
  - `references/rewrite-strategies.md`: 4 cấp độ xử lý: *Polish* (<30%), *Section Rewrite* (30-60%), *Full Paraphrase* (60-80%), *Reconstruct* (>80%).
  - `scripts/checklist.md`: Checklist tự kiểm định 22 tiêu chí an toàn trước khi xuất bản (bổ sung tiêu chí MECE rà soát trùng lặp).

---

## 🚀 Hướng Dẫn Kích Hoạt Trong Antigravity

Đăng ký đường dẫn các skill trong file cấu hình `~/.gemini/config/skills.json` (hoặc `C:\Users\<Tên_User>\.gemini\config\skills.json`):

```json
{
  "skills": [
    {
      "path": "D:/Antigravity/skills/word-report-pro"
    },
    {
      "path": "D:/Antigravity/skills/anti-ai-writer"
    },
    {
      "path": "D:/Antigravity/skills/ai-detection-bypass"
    }
  ]
}
```

---

## 💡 Ví Dụ Sử Dụng Trong Thực Tế

1. **Soạn Khóa Luận / Đồ Án:**
   > *"Dựa vào template khoa-luan-tot-nghiep, hãy lập khung đề cương chi tiết và viết chương 1 về đề tài X, áp dụng chuẩn trích dẫn APA 7th và quy tắc MECE chống trùng lặp ý."*

2. **Soạn Tờ Trình Hành Chính:**
   > *"Lập tờ trình xin phê duyệt chủ trương và kinh phí nâng cấp phòng máy tính cho trường theo đúng thể thức Nghị định 30."*

3. **Bắt Chước Văn Phong Cá Nhân:**
   > *"Đây là văn phong của tôi: [dán đoạn văn mẫu]. Hãy clone phong cách này để viết báo cáo tiến độ tuần."*

4. **Đo Lường & Khử Dấu Vết AI:**
   > *"Phân tích đoạn văn này bằng analyze_text.py và rewrite lại để đạt chỉ số an toàn cao nhất."*
