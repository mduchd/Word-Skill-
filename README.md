# Word-Skill- (Bộ Skill Soạn Báo Cáo & Tránh AI Cho Google Antigravity)

Bộ 3 skill chuyên biệt dành cho Google Antigravity / Gemini CLI nhằm hỗ trợ soạn thảo văn bản Word, báo cáo hành chính - học thuật theo quy chuẩn Việt Nam, kết hợp kỹ thuật nhân hóa văn phong và tối ưu điểm AI detector.

---

## 📦 Danh Sách Skill

### 1. `word-report-pro`
- **Mục đích:** Soạn thảo, chuẩn hóa cấu trúc báo cáo, văn bản hành chính theo chuẩn Nghị định 30/2020/NĐ-CP (Times New Roman 13pt, lề 2-2-3-2 cm, đánh số phân cấp khoa học).
- **Tài nguyên kèm theo:**
  - `resources/formatting-guide.md`: Bảng quy chuẩn lề, font, ngắt dòng, đánh số mục.
  - `resources/templates/`: Các mẫu tài liệu chuẩn:
    - `bao-cao-tong-hop.md`: Báo cáo tổng kết / định kỳ.
    - `bien-ban-hop.md`: Biên bản họp cơ quan / dự án.
    - `thuyet-minh-du-an.md`: Thuyết minh đề tài / dự án đầu tư.
  - `scripts/generate_docx.py`: Script tự động render Markdown thành file `.docx` đúng chuẩn.

### 2. `anti-ai-writer`
- **Mục đích:** Viết nội dung mang văn phong người thật, loại bỏ "AI fingerprint" (dấu vân tay AI) ngay từ khâu sinh văn bản.
- **Tài nguyên kèm theo:**
  - `references/humanizing-techniques.md`: Quy tắc 30-50-20 về nhịp điệu câu, cách ngắt nhịp tự nhiên, chèn ý kiến chủ quan có kiểm soát.
  - `references/common-ai-patterns.md`: Blacklist các từ ngữ sáo rỗng AI hay dùng (*furthermore, delve, bên cạnh đó, trong bối cảnh hiện nay...*).
  - `examples/before-after-formal.md`: Các case study đối chiếu trực tiếp trước & sau khi nhân hóa văn phong.

### 3. `ai-detection-bypass`
- **Mục đích:** Rà soát, chấm điểm nguy cơ bị nhận diện bởi các công cụ AI detector (GPTZero, Turnitin, Copyleaks, ZeroGPT) và thực hiện chiến lược rewrite tương ứng.
- **Tài nguyên kèm theo:**
  - `references/rewrite-strategies.md`: 4 cấp độ xử lý: *Polish* (<30%), *Section Rewrite* (30-60%), *Full Paraphrase* (60-80%), *Reconstruct* (>80%).
  - `scripts/checklist.md`: Checklist tự kiểm định 18 tiêu chí an toàn trước khi xuất bản.

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

## 💡 Cách Sử Dụng Trong Chat

- **Làm báo cáo:** *"Soạn cho tôi báo cáo tổng kết quý 1 về tình hình triển khai dự án X theo chuẩn Word..."*
- **Nhân hóa văn bản:** *"Viết lại đoạn này sao cho tự nhiên, nghe như người thật viết, tránh giọng AI..."*
- **Kiểm tra & bypass:** *"Kiểm tra đoạn văn này xem có bị detector bắt không và sửa lại giúp tôi..."*
