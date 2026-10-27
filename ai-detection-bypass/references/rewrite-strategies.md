# Chiến Lược Rewrite Theo Mức Độ Rủi Ro

## Chiến Lược 1: POLISH (Rủi ro thấp < 30%)

Chỉ chỉnh nhỏ, không viết lại hoàn toàn.

### Việc cần làm:
- [ ] Tìm 3–5 câu có transition word điển hình → thay bằng cách diễn đạt khác
- [ ] Chọn đoạn dài nhất → chèn 1 câu ngắn (<8 từ) vào giữa
- [ ] Thay 2–3 từ "AI vocabulary" bằng từ cụ thể hơn
- [ ] Thêm 1 chi tiết cụ thể (số, tên, thời gian) vào đoạn mà hiện tại chung chung nhất

---

## Chiến Lược 2: SECTION REWRITE (Rủi ro trung bình 30–60%)

Viết lại các đoạn có điểm cao nhất.

### Cách xác định đoạn nguy hiểm nhất:
- Đoạn nào có ≥ 2 transition word
- Đoạn nào toàn câu cùng độ dài
- Đoạn nào bắt đầu và kết thúc bằng câu "template"

### Quy trình rewrite từng đoạn:
1. Đọc đoạn gốc, ghi ra **ý chính** (không nhìn vào text gốc)
2. Viết lại đoạn đó từ đầu dựa trên ý chính vừa ghi
3. So sánh — nếu vẫn còn câu nào giống gốc quá, paraphrase thêm

---

## Chiến Lược 3: FULL PARAPHRASE (Rủi ro cao 60–80%)

Viết lại toàn bộ, chỉ giữ thông tin/số liệu.

### Bước 1 — Trích xuất Data Points
Liệt kê tất cả thông tin quan trọng cần giữ:
- Số liệu, tỷ lệ phần trăm
- Tên người/tổ chức/địa điểm
- Kết quả, kết luận chính

### Bước 2 — Viết lại từ đầu
Dùng data points đó làm nguyên liệu. Không nhìn vào bản gốc.
Apply toàn bộ kỹ thuật từ `../anti-ai-writer/references/humanizing-techniques.md`.

### Bước 3 — Kiểm tra không overlap
Đọc lại bản mới so với bản gốc — không được có chuỗi >6 từ giống nhau.

---

## Chiến Lược 4: RECONSTRUCT (Rủi ro rất cao > 80%)

Chỉ lấy facts, viết lại hoàn toàn với cấu trúc khác.

### Cho phép thay đổi:
- Thứ tự trình bày các ý
- Cách mở đầu và kết thúc
- Văn phong (chuyển từ liệt kê sang tường thuật)
- Góc nhìn (chuyển từ "khách quan" sang có quan điểm rõ ràng)

---

## Bảng Thay Thế Từ Nhanh

### Tiếng Việt

| ❌ Gốc | ✅ Thay thế 1 | ✅ Thay thế 2 |
|---|---|---|
| "quan trọng" | "then chốt" | "có ý nghĩa lớn" |
| "bên cạnh đó" | "ngoài ra" | "cũng cần nói thêm" |
| "tuy nhiên" | "nhưng" | "thế nhưng" |
| "cho thấy rằng" | "phản ánh" | "chứng tỏ" |
| "cần phải" | "nên" | "buộc phải" |
| "nhìn chung" | "xét toàn cảnh" | "tổng mà nói" |
| "đóng vai trò" | "góp phần" | "là yếu tố" |
| "ngày càng" | "dần dần" | "theo thời gian" |
| "hiệu quả" | "thiết thực" | "có kết quả rõ ràng" |
| "phát triển bền vững" | [mô tả cụ thể] | [mô tả cụ thể] |

### Tiếng Anh

| ❌ Gốc | ✅ Thay thế 1 | ✅ Thay thế 2 |
|---|---|---|
| "Furthermore," | "On top of that," | "And—" |
| "It is important to" | [delete, just say it] | "Worth noting:" |
| "In conclusion," | "So," | "All in all," |
| "delve into" | "look at" | "explore" |
| "robust" | "solid" | "reliable" |
| "utilize" | "use" | "apply" |
| "leverage" | "use" | "draw on" |
| "comprehensive" | "thorough" | "full" |
| "navigate" | "handle" | "deal with" |
| "showcase" | "show" | "highlight" |

---

## Kỹ Thuật Tăng Perplexity (Gây Bất Ngờ Cho Detector)

Các detector đo **perplexity** — mức độ bất ngờ của từ tiếp theo.
AI chọn từ an toàn nhất → perplexity thấp → bị detect.

Cách tăng perplexity:
1. **Dùng ẩn dụ bất ngờ**: "Dữ liệu như một tấm gương vỡ — mỗi mảnh đúng, nhưng ghép lại thì lệch"
2. **Đặt câu hỏi giữa đoạn phân tích**: Phá nhịp kỳ vọng của detector
3. **Dùng từ địa phương / thông tục 1 lần**: "cũng được thôi", "thật ra mà nói"
4. **Viết câu không hoàn chỉnh có chủ đích**: "Một bài toán cũ. Một câu trả lời mới."
