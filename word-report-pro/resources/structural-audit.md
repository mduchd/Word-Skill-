# Quy Trình Rà Soát Bố Cục & Loại Bỏ Trùng Lặp Ý Tưởng (Structural & Redundancy Audit)

Quy trình này áp dụng nguyên tắc **MECE (Mutually Exclusive, Collectively Exhaustive)**: *Các phần phải tách bạch, không dẫm chân lên nhau nhưng tổng thể không được bỏ sót khía cạnh nào.*

---

## 1. Ma Trận Ranh Giới Nội Dung (Scope Boundary Matrix)

Trước khi duyệt báo cáo, kiểm tra xem từng phần có vượt rào sang phần khác không:

| Thành phần | ĐƯỢC PHÉP có | ❌ TUYỆT ĐỐI KHÔNG để lẫn |
|---|---|---|
| **I. Đặt vấn đề / Mở đầu** | Lý do chọn đề tài, mục tiêu, đối tượng, phạm vi nghiên cứu | Không đưa kết quả cụ thể, không phân tích sâu, không đưa kiến nghị |
| **II. Cơ sở lý thuyết / Thực trạng** | Số liệu khảo sát, hiện trạng thực tế, mô tả quy trình | Không đưa nhận xét chủ quan, không lấn sang giải pháp |
| **III. Phân tích & Đánh giá** | Điểm mạnh, điểm yếu, nguyên nhân gốc rễ, đối chiếu số liệu | Không lặp lại nguyên văn số liệu mô tả ở phần Thực trạng |
| **IV. Giải pháp / Kiến nghị** | Hành động cụ thể, lộ trình, dự toán, người thực hiện | Không diễn giải lại nguyên nhân, không tóm tắt lại thực trạng |
| **V. Kết luận** | Đánh giá mức độ hoàn thành mục tiêu, 2–3 bài học cốt lõi | Không dùng câu từ lặp lại phần Mở đầu, không đưa thêm thông tin mới |

---

## 2. Các Dạng Trùng Lặp Tiêu Biểu & Cách Xử Lý

### Dạng 1: "Bình mới rượu cũ" (Semantic Redundancy)
* **Dấu hiệu:** Hai đoạn văn ở hai mục khác nhau dùng từ ngữ khác nhau nhưng bản chất nói cùng 1 ý.
  - *Ví dụ Mục 1:* "Hệ thống hạ tầng mạng còn chậm, làm gián đoạn công việc."
  - *Ví dụ Mục 2:* "Tốc độ đường truyền Internet không ổn định gây cản trở năng suất nhân viên."
* **Cách sửa:** Gộp làm một điểm trọng tâm duy nhất tại mục *Nguyên nhân kỹ thuật*, loại bỏ câu thừa ở mục còn lại.

### Dạng 2: Kết luận sao chép Tóm tắt (Conclusion Echoing)
* **Dấu hiệu:** Phần Kết luận lấy lại nguyên văn các câu trong phần Tóm tắt/Mở đầu rồi thêm chữ "Tóm lại,...".
* **Cách sửa:** Kết luận phải trả lời câu hỏi: *Sau tất cả dữ liệu trên, quyết định tiếp theo là gì? Đâu là giới hạn cần nghiên cứu tiếp?*

### Dạng 3: Tiểu mục dẫm chân tiểu mục
* **Dấu hiệu:** Mục `2.1` và `2.2` cùng giải thích một nguyên nhân hoặc nêu giải pháp na ná nhau.
* **Cách sửa:** Xác lập tiêu chí phân chia rõ ràng trước khi viết:
  - Theo **Chủ thể**: Khách hàng vs Nội bộ
  - Theo **Thời gian**: Ngắn hạn vs Dài hạn
  - Theo **Bản chất**: Kỹ thuật vs Con người vs Tài chính

---

## 3. Quy Tắc Tỷ Lệ Vàng Về Dung Lượng (Structure Balance)

Báo cáo chuẩn không được để tình trạng mục chính cụt ngủn, mục phụ lê thê:

```
┌─────────────────────────────────────────────────────────┐
│ 1. Mở đầu / Bối cảnh          │ ~ 10% - 15% tổng bài    │
├─────────────────────────────────────────────────────────┤
│ 2. Nội dung / Thực trạng      │ ~ 35% - 40% tổng bài    │
├─────────────────────────────────────────────────────────┤
│ 3. Phân tích / Giải pháp      │ ~ 35% - 40% tổng bài    │
├─────────────────────────────────────────────────────────┤
│ 4. Kết luận & Kiến nghị       │ ~ 10% tổng bài          │
└─────────────────────────────────────────────────────────┘
```

---

## 4. Checklist 5 Bước Rà Soát Trùng Lặp Của Agent

Khi người dùng yêu cầu *Rà soát bố cục* hoặc *Soát lại bài*, thực hiện lần lượt:

- [ ] **Bước 1 - Lập bản đồ ý tưởng (Idea Mapping):** Rút ra mỗi mục con (1.1, 1.2...) đúng 1 câu luận điểm cốt lõi.
- [ ] **Bước 2 - Quét xung đột & chồng chéo:** So sánh các câu luận điểm trên: Có 2 câu nào mang cùng thông điệp không?
- [ ] **Bước 3 - Cắt gọt redundancy:** Nếu trùng, chỉ giữ lại ở mục đúng ngữ cảnh nhất, mục còn lại thay bằng dẫn chiếu ngắn (ví dụ: *"như đã phân tích tại mục 2.1"*).
- [ ] **Bước 4 - Kiểm tra ranh giới:** Kiểm tra phần Mở đầu có bị "nói trước kết quả" và phần Kết luận có bị "nhai lại" không.
- [ ] **Bước 5 - Cân đối độ dài:** Điều chỉnh độ dài giữa các phần theo tỷ lệ vàng ở Mục 3.
