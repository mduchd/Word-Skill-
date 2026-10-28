# Nguyên Tắc Bảo Toàn Đầu Vào & Giới Hạn Can Thiệp Của Agent (Input Sanctity & Scope Boundaries)

> [!IMPORTANT]
> Đây là nguyên tắc cốt lõi ngăn chặn tình trạng Agent "sửa linh tinh", "sáng tạo quá đà", làm biến dạng tiêu đề hoặc xáo trộn văn bản của người dùng.

---

## 🔒 1. DANH MỤC BẤT KHẢ XÂM PHẠM (IMMUTABLES LIST)

Những thành phần sau đây do người dùng nhập vào được coi là **"BẤT BIẾN" (Read-Only)**, Agent **TUYỆT ĐỐI KHÔNG ĐƯỢC TỰ Ý THAY ĐỔI**:

1. **Tiêu đề tài liệu / Tên báo cáo / Tên đề tài:**
   - *Ví dụ:* Người dùng nhập `"Báo cáo tiến độ triển khai dự án DSS Quý 3"`.
   - ❌ **CẤM:** Không được tự ý đổi thành `"Báo cáo Toàn diện về Nghiên cứu Hệ thống Hỗ trợ Ra quyết định trong Chuyển đổi số"`.
   - ✅ **ĐÚNG:** Giữ nguyên 100% từng chữ của tiêu đề gốc.
   - *Ngoại lệ duy nhất:* Chỉ khi người dùng nói rõ: *"Hãy đặt lại tiêu đề giúp tôi"* hoặc *"Gợi ý tiêu đề hay hơn"*.
2. **Tiêu đề các mục con & Đề mục (Headings):**
   - Giữ nguyên tên và thứ tự các mục người dùng đã lập, không tự ý gộp, tách hoặc đổi tên đề mục.
3. **Thực thể thực tế (Entities):**
   - Tên cơ quan, trường học, công ty, phòng ban.
   - Họ và tên người thực hiện, chức vụ, chức danh.
   - Tên phần mềm, mã hiệu thiết bị, thuật ngữ chuyên ngành.
   - Ngày tháng, mốc thời gian cụ thể.
4. **Dữ liệu & Số liệu (Facts & Metrics):**
   - Mọi con số, bảng biểu, tỷ lệ phần trăm người dùng cung cấp phải được giữ nguyên vẹn 100%, không được tự ý "làm tròn" hay suy diễn con số khác.

---

## 🎯 2. NGUYÊN TẮC PHẪU THUẬT CHÍNH XÁC (SURGICAL EDITING)

Thay vì xóa đi viết lại toàn bộ một cách hỗn loạn, Agent phải tuân thủ nguyên tắc can thiệp tối thiểu nhưng hiệu quả tối đa:

### Quy tắc 3 "Đúng":
1. **Đúng phạm vi (In-Scope Only):**
   - Người dùng bảo: *"Sửa giúp tôi phần Thực trạng"* $\rightarrow$ CHỈ đọc và sửa đúng phần Thực trạng. Tuyệt đối không chạm vào phần Mở đầu hay Kết luận.
   - Người dùng hỏi: *"Đoạn này có bị dính AI không?"* $\rightarrow$ CHỈ phân tích và chỉnh sửa đoạn đó, không sinh thêm các đoạn mới ngoài yêu cầu.
2. **Đúng bệnh (Symptom-Specific):**
   - Nếu câu bị lỗi từ nối AI (*"Bên cạnh đó"*, *"Hơn nữa"*) $\rightarrow$ Chỉ thay từ nối và chỉnh lại nhịp câu.
   - Nếu câu bị lỗi ký tự cấm (emoji, mũi tên) $\rightarrow$ Chỉ xóa emoji và viết lại câu xuôi.
   - **Không viết lại cả đoạn khi chỉ có 1 câu cần sửa!**
3. **Đúng ý đồ tác giả (Intent Preservation):**
   - Câu văn sau khi sửa phải truyền tải **chính xác 100% luận điểm** của câu gốc, không được lái sang ý khác hay chèn thêm quan điểm lạ hoắc vào bài.

---

## 🚫 3. NHỮNG HÀNH VI "SỬA LOẠN XẠ" BỊ CẤM TUYỆT ĐỐI

| Hành vi sai trái của Agent | Hậu quả gây phiền hà | Quy tắc bắt buộc |
|---|---|---|
| Tự ý viết lại tiêu đề cho "kêu" hơn | Làm sai tên đề tài chính thức được giao | **Giữ nguyên 100% tiêu đề người dùng đưa vào.** |
| Tự ý đảo lộn thứ tự các đoạn văn | Phá vỡ logic trình bày của người viết | **Giữ đúng mạch văn và thứ tự của văn bản gốc.** |
| Tự ý bịa thêm mục mới không ai yêu cầu | Làm bài dài dòng, loãng nội dung | **Chỉ triển khai đúng các mục trong dàn ý.** |
| Thay đổi thuật ngữ chuyên ngành | Làm sai lệch bản chất kỹ thuật | **Nếu gặp thuật ngữ chuyên sâu, giữ nguyên từ đó.** |
| "Phun" ra một văn bản hoàn toàn xa lạ | Người dùng không nhận ra bài của mình | **Sửa bám sát từng câu từng đoạn gốc.** |

---

## ✅ 4. CHECKLIST BẢO TOÀN TRƯỚC KHI TRẢ VỀ CHO NGƯỜI DÙNG

Trước khi bấm gửi câu trả lời, Agent phải tự rà soát:
- [ ] Tiêu đề báo cáo có bị đổi một chữ nào không? (Phải = Gốc)
- [ ] Các đề mục lớn/nhỏ có bị đảo lộn hoặc đổi tên không? (Phải = Gốc)
- [ ] Số liệu, ngày tháng, tên riêng có còn nguyên vẹn không? (Phải = Gốc)
- [ ] Mình có sửa vượt quá phạm vi người dùng yêu cầu không? (Nếu có $\rightarrow$ cắt bỏ phần thừa ngay).
