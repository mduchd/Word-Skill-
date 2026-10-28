# Chiến Lược Rewrite Đúng Trọng Tâm & Bảo Toàn Đầu Vào (Surgical Rewriting)

> [!CAUTION]
> **QUY TẮC BẢO TOÀN ĐẦU VÀO (IMMUTABLES RULE):**
> Trong MỌI chiến lược rewrite từ thấp đến cao:
> 1. **TIÊU ĐỀ & ĐỀ MỤC LÀ BẤT BIẾN:** Giữ nguyên 100% từng chữ của tiêu đề báo cáo và các đề mục của người dùng. Tuyệt đối không tự ý đổi tiêu đề.
> 2. **SỰ THẬT & SỐ LIỆU LÀ BẤT BIẾN:** Không thay đổi số liệu, ngày tháng, tên riêng, thuật ngữ kỹ thuật.
> 3. **ĐÚNG PHẠM VI:** Chỉ can thiệp vào câu hoặc đoạn văn cần sửa, không xáo trộn cấu trúc hoặc viết lại lan man sang phần khác.

---

## Chiến Lược 1: POLISH (Rủi ro thấp < 30%)

Chỉ chỉnh sửa cục bộ tại các điểm có vấn đề, không động chạm vào phần văn bản đã ổn định.

### Việc cần làm:
- [ ] Giữ nguyên 100% tiêu đề, đề mục và mạch bài gốc.
- [ ] Tìm các từ nối AI điển hình (*"Bên cạnh đó"*, *"Hơn nữa"*) $\rightarrow$ thay bằng cách diễn đạt tự nhiên hoặc bỏ hẳn từ nối.
- [ ] Chèn 1 câu ngắn (<8 từ) vào giữa đoạn dài nhất để tạo nhịp thở.
- [ ] Xóa bỏ toàn bộ emoji, dấu mũi tên, hoặc in đậm lắt nhắt nếu có.

---

## Chiến Lược 2: SURGICAL REWRITE (Rủi ro trung bình 30–60%)

Viết lại cục bộ các đoạn bị chấm điểm AI cao nhất, giữ nguyên khung sườn bài viết.

### Cách xác định câu/đoạn cần phẫu thuật:
- Câu nào có mật độ từ nối AI dày đặc.
- Đoạn nào toàn câu cùng một độ dài (thiếu Burstiness).
- Đoạn nào bắt đầu bằng câu mở đầu rập khuôn (*"Bạn đã bao giờ..."*).

### Quy trình sửa:
1. Đọc câu gốc để nắm chính xác ý đồ của người viết.
2. Viết lại cấu trúc câu đó (chuyển câu bị động sang chủ động, ngắt câu dài thành 2 câu ngắn).
3. Đặt lại vào đúng vị trí cũ trong đoạn văn, đảm bảo tính liên kết mạch lạc với câu trước và câu sau.

---

## Chiến Lược 3: DEEP REPHRASING (Rủi ro cao 60–80%)

Tái cấu trúc cách diễn đạt của toàn đoạn văn nhưng **khóa chặt toàn bộ thông tin cốt lõi**.

### Các bước thực hiện:
1. **Khóa thông tin bất biến:** Đánh dấu toàn bộ số liệu, tên riêng, thuật ngữ chuyên ngành và luận điểm chính.
2. **Thay đổi cấu trúc cú pháp:**
   - Thay đổi thứ tự các vế câu (đưa vế phụ hoặc điều kiện lên trước).
   - Đan xen nhịp điệu 30-50-20 (câu ngắn xen câu trung bình/dài).
   - Bổ sung ít nhất một sự đánh đổi thực tế (Trade-off / chi phí / con người) để tăng tính người thật.
3. **Giữ nguyên trật tự logic:** Không được tự tiện đảo đoạn 1 xuống đoạn 3, không xóa bỏ ý của tác giả.

---

## Chiến Lược 4: TOTAL RECONSTRUCTION (Rủi ro rất cao > 80%)

Khi văn bản gốc bị dính mẫu câu chatbot quá nặng (100% giọng máy), viết lại toàn diện nhưng **tuân thủ nghiêm ngặt ranh giới**:

### Ranh giới bắt buộc:
- **Tiêu đề báo cáo:** Giữ nguyên 100%.
- **Các đề mục (Headings):** Giữ nguyên 100%.
- **Thông tin & Số liệu:** Giữ nguyên 100%.
- **Trình tự luận điểm:** Bám sát dàn ý của người dùng, không được tự ý bịa thêm mục mới hay bỏ sót nội dung gốc.
- **Thực hiện:** Viết lại toàn bộ câu văn bằng văn phong tự nhiên, điềm tĩnh, triệt tiêu mọi từ ngữ PR và cấu trúc liệt kê máy móc.

---

## Bảng Thay Thế Từ Nhanh Chuẩn Xác

### Tiếng Việt

| ❌ Từ máy móc | ✅ Thay thế tự nhiên 1 | ✅ Thay thế tự nhiên 2 |
|---|---|---|
| "đóng vai trò quan trọng" | "ảnh hưởng lớn đến" | "là yếu tố then chốt" |
| "bên cạnh đó" | "ngoài ra" | "cũng cần xét đến" |
| "tuy nhiên" | "nhưng" | "thế nhưng" |
| "điều này cho thấy rằng" | "kết quả đó phản ánh" | "số liệu chứng tỏ" |
| "cần phải" | "nên" | "cần" |
| "nhìn chung" | "tổng thể mà nói" | "xét toàn diện" |
| "hướng đến phát triển bền vững" | "hướng tới hiệu quả lâu dài" | [nêu mục tiêu cụ thể] |
| "giải pháp toàn diện" | [chỉ rõ tên giải pháp] | [chỉ rõ hành động] |

### Tiếng Anh

| ❌ Từ máy móc | ✅ Thay thế tự nhiên 1 | ✅ Thay thế tự nhiên 2 |
|---|---|---|
| "Furthermore," | "Also," | "And—" |
| "It is important to" | [xóa, nói trực tiếp] | "We should note that" |
| "In conclusion," | "To wrap up," | "All in all," |
| "delve into" | "look at" | "examine" |
| "robust" | "solid" | "reliable" |
| "utilize" | "use" | "apply" |
| "leverage" | "use" | "take advantage of" |
| "comprehensive" | "thorough" | "detailed" |
| "streamline" | "simplify" | "speed up" |
