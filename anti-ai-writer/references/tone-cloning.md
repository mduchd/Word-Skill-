# Hướng Dẫn Clone Văn Phong Cá Nhân (Personal Tone Cloning)

Kỹ thuật này giúp agent phân tích và "bắt chước" chính xác giọng văn tự nhiên của người dùng, biến bài viết thành 100% phong cách của chính bạn.

---

## 1. Cách Cung Cấp Mẫu Văn Phong

Người dùng có thể đưa 1 đến 2 đoạn văn/bài viết cũ do chính mình viết vào chat với lệnh:
> *"Đây là văn phong mẫu của tôi, hãy học phong cách này để viết báo cáo tiếp theo: [Dán bài viết mẫu]"*

---

## 2. 5 Chiều Không Gian Agent Cần Trích Xuất Từ Mẫu (Extraction Vector)

Khi nhận bài mẫu của người dùng, agent phải phân tích 5 đặc tính sau:

1. **Độ dài câu và nhịp thở (Pacing):**
   - Người viết chuộng câu cộc, gãy gọn hay câu dài nhiều vế?
   - Có hay dùng dấu gạch ngang (—), dấu ngoặc đơn `()` hoặc dấu hai chấm `:` không?
2. **Cách xưng hô và Đại từ nhân xưng:**
   - Xưng là *tôi*, *chúng tôi*, *tác giả*, *người viết*, hay dùng câu khuyết chủ ngữ?
3. **Từ ngữ "cửa miệng" (Idiolect / Favorite phrases):**
   - Hay dùng từ nào để chuyển ý: *thật ra, rõ ràng, nói cách khác, nhìn chung, vấn đề là...*
4. **Mức độ cảm xúc & Phản biện (Subjectivity level):**
   - Văn phong hoàn toàn khách quan lạnh lùng, hay có chút hóm hỉnh, hoài nghi, nhấn mạnh quan điểm cá nhân?
5. **Thói quen dùng thuật ngữ:**
   - Thích dùng từ Hán-Việt trang trọng (*tiến hành, triển khai, sở hữu*) hay thích dùng từ thuần Việt giản dị (*làm, mở rộng, nắm giữ*)?

---

## 3. Ma Trận Chuyển Đổi (Mapping Matrix)

Sau khi phân tích xong, agent lập bảng chuyển đổi ngầm để sinh văn bản mới:

| Đặc tính văn phong | Phong cách AI mặc định | Phong cách người dùng (Đã học) |
|---|---|---|
| **Mở đầu đoạn** | *Bên cạnh đó, Ngoài ra, Hơn nữa...* | Áp dụng cách chuyển ý theo mẫu của người dùng |
| **Kết luận vấn đề** | *Tóm lại, có thể thấy rằng...* | Đặt câu hỏi mở hoặc kết luận thực dụng theo gu người dùng |
| **Nhịp điệu** | Đồng đều, mượt mà hoàn hảo | Tái hiện đúng độ gồ ghề, nhịp ngắt tự nhiên của mẫu |

---

## 4. Tệp Cấu Hình Cá Nhân Hóa (Tùy Chọn Lưu Trữ)

Người dùng có thể lưu trực tiếp mẫu văn phong của mình vào file:
`D:\Antigravity\skills\anti-ai-writer\references\my_sample_style.md`

Khi file này có nội dung, agent sẽ **tự động ưu tiên mô phỏng theo mẫu này** trong mọi lần sinh nội dung tiếp theo mà không cần nhắc lại!
