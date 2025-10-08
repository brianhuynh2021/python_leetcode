📌 Định lý CAP là gì?

📌 What is the CAP Theorem?

Định lý CAP phát biểu rằng:
A distributed system cannot simultaneously guarantee all three of the following:
	1.	Consistency (Tính nhất quán)
→ Tất cả các nút trong hệ thống đều thấy dữ liệu giống nhau tại cùng một thời điểm.
→ All nodes in the system see the same data at the same time.
✅ Ví dụ: Ghi dữ liệu ở một nơi thì nơi khác phải đọc được dữ liệu mới nhất.
✅ Example: Once data is written, all reads reflect the latest write.
	2.	Availability (Tính sẵn sàng)
→ Hệ thống luôn phản hồi mọi yêu cầu, không bị treo hoặc báo lỗi.
→ Every request gets a (non-error) response, even without the most recent data.
	3.	Partition Tolerance (Chịu lỗi phân vùng)
→ Hệ thống vẫn hoạt động bình thường ngay cả khi có sự cố mạng giữa các máy chủ.
→ The system continues to operate even when network partitions (communication failures) occur.

⸻

⚠️ Vì sao không thể có cả 3?

⚠️ Why can’t we have all three?

Khi xảy ra lỗi mạng (partition), bạn buộc phải chọn giữa:
→ Consistency hoặc Availability

When a network partition happens, you must choose between:
→ Consistency or Availability

⸻

🔒 C + P: Tính nhất quán + Chịu phân vùng (hy sinh sẵn sàng)

🔒 C + P: Consistency + Partition Tolerance (sacrifice availability)

✅ Chính xác, nhưng có thể không phản hồi được
✅ Accurate but may deny requests or delay
🧾 Ví dụ: Hệ thống ngân hàng
🧾 Example: Banking systems

⸻

⚡ A + P: Tính sẵn sàng + Chịu phân vùng (hy sinh nhất quán)

⚡ A + P: Availability + Partition Tolerance (sacrifice consistency)

✅ Luôn phản hồi, nhưng dữ liệu có thể chưa cập nhật
✅ Always responds, but data might be stale
📱 Ví dụ: Mạng xã hội, hệ thống cache
📱 Example: Social networks, caching systems

⸻

❌ C + A (Tính nhất quán + sẵn sàng) KHÔNG khả thi nếu có lỗi mạng

❌ C + A (Consistency + Availability) is NOT achievable under network failures

⸻

🎯 Tóm tắt / Summary
	•	Partition là điều bắt buộc phải chấp nhận.
→ Partition tolerance is a must in distributed systems.
	•	Nên bạn phải chọn giữa Consistency và Availability.
→ So you must choose either Consistency or Availability.

⸻

Nếu bạn cần thêm ví dụ thực tế hoặc bài tập về CAP, mình có thể chuẩn bị tiếp nhé!

✅ 1. CP (Consistency + Partition Tolerance)

⛔ Hy sinh Availability (hệ thống có thể tạm thời không phản hồi)

📌 Ví dụ 1: Hệ thống ngân hàng
	•	Khi bạn chuyển khoản, hệ thống phải chắc chắn số dư được cập nhật đúng trước khi cho phép giao dịch tiếp theo.
	•	Nếu mạng giữa 2 server bị lỗi (partition), hệ thống sẽ từ chối xử lý để đảm bảo không ghi sai dữ liệu.

📌 Ví dụ 2: Hệ thống quản lý đơn hàng
	•	Đơn hàng chỉ được tạo khi có hàng trong kho.
	•	Nếu server kiểm kho không phản hồi do lỗi mạng, hệ thống sẽ tạm dừng xử lý thay vì tạo đơn sai.

⸻

✅ 2. AP (Availability + Partition Tolerance)

⛔ Hy sinh Consistency (có thể đọc dữ liệu cũ)

📌 Ví dụ 1: Hệ thống mạng xã hội (Facebook, Twitter)
	•	Khi bạn đăng một bài viết, bạn có thể ngay lập tức thấy bài viết đó, nhưng người khác có thể chưa thấy vì nó chưa được đồng bộ hoàn toàn.
	•	Miễn là hệ thống vẫn phản hồi, nó chấp nhận một chút không nhất quán tạm thời.

📌 Ví dụ 2: Hệ thống DNS (Domain Name System)
	•	Luôn phản hồi để phân giải tên miền, dù có thể cập nhật IP chưa được đồng bộ hết giữa các server DNS.

📌 Ví dụ 3: Hệ thống cache (Redis, Memcached)
	•	Nếu dữ liệu trong cache khác với dữ liệu gốc (database), hệ thống vẫn phản hồi nhanh.
	•	Ưu tiên tốc độ và khả năng truy cập liên tục.

⸻

❌ 3. CA (Consistency + Availability)

⚠️ KHÔNG thể đạt được nếu có lỗi mạng (không partition-tolerant)

📌 Ví dụ lý thuyết: Hệ thống chạy trên 1 máy chủ đơn (single-node)
	•	Nếu không có phân vùng mạng, bạn có thể đảm bảo cả tính nhất quán và sẵn sàng.
	•	Nhưng khi scale ra nhiều máy chủ, partition là không thể tránh, nên CA không còn khả thi.
