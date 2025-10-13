# Lộ Trình Xây Dựng Trợ Lý Xổ Số AI (AI Lottery Assistant)

Dự án này được xây dựng với mục tiêu sau cùng là phục vụ cho toàn bộ hệ sinh thái xổ số tại Việt Nam, từ người bán lẻ đến các công ty phát hành. Lộ trình được chia thành các giai đoạn để tập trung vào từng nhóm đối tượng cụ thể.

## Đối Tượng Mục Tiêu & Lộ Trình Phát Triển

-   **Giai đoạn 1: Tập trung vào Người Bán Vé Số & Người Chơi:**
    -   **Mục tiêu:** Cung cấp công cụ tiện lợi, nhanh chóng để dò số, quản lý vé cá nhân và phát hiện vé giả ở mức độ cơ bản.
    -   **Sản phẩm:** Ứng dụng di động với các tính năng cốt lõi.
    -   **Tương ứng:** Phase 1 & 2 trong lộ trình kỹ thuật bên dưới.

-   **Giai đoạn 2: Mở rộng cho Đại Lý Vé Số:**
    -   **Mục tiêu:** Xây dựng các tính năng nâng cao để quản lý kho vé số lượng lớn, thống kê doanh thu, quản lý công nợ và khách hàng.
    -   **Sản phẩm:** Thêm một giao diện web (Dashboard) cho đại lý, tích hợp với ứng dụng di động.
    -   **Tương ứng:** Phase 3 và các tính năng mở rộng (sẽ được định nghĩa sau).

-   **Giai đoạn 3: Hướng tới Công Ty Xổ Số (B2B):**
    -   **Mục tiêu:** Cung cấp một nền tảng phân tích dữ liệu (Data Analytics Platform) về xu hướng thị trường, các điểm bán hiệu quả, và một hệ thống chống gian lận tinh vi.
    -   **Sản phẩm:** Nền tảng SaaS (Software-as-a-Service) với các API và báo cáo chuyên sâu.
    -   **Tương ứng:** Tầm nhìn dài hạn của dự án.

---

## PHASE 1 (Tuần 1-4): "Máy Dò Số Tự Động" - Nền Tảng Cho Người Bán Lẻ

---

## 🎯 Tổng Quan Dự Án

### Elevator Pitch
"Xuất thân từ việc bán vé số, em hiểu rõ những khó khăn hàng ngày: quản lý hàng trăm cùi vé, dò số thủ công tốn thời gian và nỗi lo vé giả. Vì vậy, em đã xây dựng một ứng dụng AI trên điện thoại để giải quyết chính xác những vấn đề đó. Ứng dụng của em có thể: 1) Quét và lưu trữ hàng loạt vé số chỉ trong vài giây bằng camera. 2) Tự động dò kết quả và thông báo ngay khi có kết quả. 3) Sử dụng Computer Vision để cảnh báo các dấu hiệu bất thường của vé giả, giúp người bán tự bảo vệ mình."

### Thành Phẩm Cuối Cùng
- **Ứng dụng di động (cross-platform):** Cho phép người dùng quét, quản lý và dò vé số.
- **Backend System:** Tự động thu thập kết quả, xử lý dò số và gửi thông báo.
- **3 AI Models:**
    1.  **OCR Model:** Đọc số và ngày trên vé.
    2.  **Object Detection Model:** Nhận diện nhiều cùi vé trong một ảnh.
    3.  **Anomaly Detection Model:** Phát hiện dấu hiệu vé giả.
- **API Documentation:** Cho các dịch vụ backend.
- **GitHub Repository:** Với code được tổ chức tốt và README chi tiết.

---

## 🛠️ Tech Stack Đề Xuất

### Mobile App (Frontend)
- **React Native / Flutter:** Để xây dựng ứng dụng cho cả iOS và Android từ một codebase.
- **Expo (cho React Native):** Giúp đơn giản hóa quá trình build và deploy.
- **Camera API:** Để truy cập camera của thiết bị.
- **SQLite:** Lưu trữ dữ liệu vé số local trên điện thoại.

### Backend
- **Python 3.10+**
- **FastAPI:** Xây dựng API hiệu năng cao.
- **PostgreSQL:** Lưu trữ kết quả xổ số, thông tin người dùng.
- **Celery & RabbitMQ/Redis:** Xử lý các tác vụ bất đồng bộ (dò số hàng loạt, gửi thông báo).
- **Beautiful Soup / Scrapy:** Thu thập kết quả xổ số từ các trang web.

### AI/ML
- **PyTorch / TensorFlow:** Framework chính để train model.
- **OpenCV:** Xử lý hình ảnh (cắt, xoay, tăng cường chất lượng).
- **Tesseract / EasyOCR:** Thư viện OCR ban đầu.
- **YOLOv5 / YOLOv8:** Train mô hình object detection.
- **EfficientNet / Vision Transformer (ViT):** Train mô hình phân loại/phát hiện bất thường.
- **ONNX / TensorFlow Lite:** Tối ưu hóa model để chạy trên thiết bị di động.

### DevOps
- **Docker:** Đóng gói backend services.
- **GitHub Actions:** Tự động hóa testing và build.
- **Nginx:** Reverse proxy.
- **Firebase Cloud Messaging (FCM):** Gửi push notification.
- **Cloud Provider (AWS/GCP/Azure):** Để deploy backend.

---

## 🗓️ GIAI ĐOẠN 1: MÁY DÒ SỐ TỰ ĐỘNG (Tuần 1-4)
*Mục tiêu: Xây dựng tính năng cốt lõi, giải quyết vấn đề dò số thủ công.*

---

### **TUẦN 1: Setup & Giao Diện Cơ Bản**

#### Nhiệm vụ:
- [ ] **Project Setup:**
    - [ ] Khởi tạo Git repository với cấu trúc thư mục rõ ràng (`mobile-app`, `backend`, `ml-models`).
    - [ ] Setup môi trường phát triển cho React Native/Flutter.
    - [ ] Setup môi trường Python cho backend với `Poetry` hoặc `venv`.
- [ ] **Mobile App UI (Mockup):**
    - [ ] Thiết kế giao diện chính với 3 tab: "Quét Vé", "Vé Của Tôi", "Kết Quả".
    - [ ] Tạo màn hình "Quét Vé" với một nút bấm lớn để mở camera.
    - [ ] Tạo màn hình "Vé Của Tôi" hiển thị danh sách các vé đã lưu (dữ liệu giả).
    - [ ] Tạo màn hình "Kết Quả" hiển thị kết quả xổ số (dữ liệu giả).
- [ ] **Backend API Cơ Bản:**
    - [ ] Dựng một server `FastAPI` đơn giản.
    - [ ] Tạo endpoint `/health` để kiểm tra server có hoạt động không.

#### Deliverables:
- [ ] Git repo được khởi tạo.
- [ ] Ứng dụng di động có thể build và chạy trên máy ảo/thiết bị thật với giao diện giả.
- [ ] Server FastAPI cơ bản có thể khởi chạy.

---

### **TUẦN 2: Tích Hợp OCR & Quét Vé Đơn Lẻ**

#### Nhiệm vụ:
- [ ] **Nghiên cứu OCR:**
    - [ ] Thử nghiệm `Tesseract`, `EasyOCR` và các API OCR (Google Vision) với ảnh chụp vé số thật.
    - [ ] Đánh giá độ chính xác, tốc độ và sự phức tạp khi tích hợp.
    - [ ] **Quyết định:** Chọn một giải pháp OCR cho phiên bản đầu tiên.
- [ ] **Tích hợp Camera & OCR:**
    - [ ] Trong ứng dụng di động, implement chức năng mở camera.
    - [ ] Sau khi chụp ảnh, gửi ảnh đến một service (có thể chạy local trên điện thoại hoặc qua API backend) để xử lý OCR.
    - [ ] Nhận dạng dãy số và ngày tháng từ ảnh.
- [ ] **Lưu Trữ Local:**
    - [ ] Hiển thị số vừa quét cho người dùng xác nhận.
    - [ ] Sau khi xác nhận, lưu dãy số, ngày xổ và ảnh gốc vào database SQLite trên điện thoại.
    - [ ] Cập nhật màn hình "Vé Của Tôi" để hiển thị các vé đã lưu thật.

#### Deliverables:
- [ ] Chức năng quét một cùi vé và nhận dạng số hoạt động.
- [ ] Vé được quét được lưu thành công vào bộ nhớ local của điện thoại.
- [ ] Màn hình "Vé Của Tôi" hiển thị chính xác các vé đã quét.

---

### **TUẦN 3: Backend Dò Số & Lấy Kết Quả**

#### Nhiệm vụ:
- [ ] **Thiết Kế Database Backend:**
    - [ ] Thiết kế schema cho bảng `LotteryResults` trong PostgreSQL để lưu kết quả theo ngày và theo đài.
- [ ] **Xây Dựng Scraper:**
    - [ ] Viết một script Python dùng `Beautiful Soup` hoặc `Scrapy` để tự động lấy kết quả xổ số từ 1-2 trang web uy tín.
    - [ ] Script cần lấy được kết quả của tất cả các đài trong ngày.
    - [ ] Lưu kết quả vào database PostgreSQL.
- [ ] **Tạo API Dò Số:**
    - [ ] Xây dựng endpoint `POST /api/v1/check-tickets`.
    - [ ] Endpoint này nhận một danh sách các số và ngày, so sánh với kết quả trong database và trả về kết quả trúng thưởng cho từng số.
- [ ] **Tích hợp API vào Mobile App:**
    - [ ] Tạo một nút "Dò số" trên màn hình "Vé Của Tôi".
    - [ ] Khi bấm nút, gọi API `/check-tickets` và hiển thị kết quả trúng thưởng (ví dụ: highlight các vé trúng).

#### Deliverables:
- [ ] Script lấy kết quả xổ số hoạt động ổn định.
- [ ] Database backend chứa dữ liệu kết quả xổ số của ít nhất 1 tuần.
- [ ] API dò số hoạt động chính xác.
- [ ] Ứng dụng di động có thể dò số thành công.

---

### **TUẦN 4: Hoàn Thiện & Kiểm Thử V1.0**

#### Nhiệm vụ:
- [ ] **Xử lý ảnh cơ bản:**
    - [ ] Trước khi đưa vào OCR, thêm các bước xử lý ảnh để tăng độ chính xác: chuyển ảnh xám, tăng độ tương phản, tự động xoay ảnh cho thẳng.
- [ ] **Cải thiện UX:**
    - [ ] Thêm màn hình loading khi đang xử lý OCR hoặc gọi API.
    - [ ] Thêm thông báo lỗi rõ ràng (ví dụ: "Không đọc được số, vui lòng chụp lại rõ hơn").
    - [ ] Cho phép người dùng sửa lại số nếu OCR nhận dạng sai.
- [ ] **Kiểm thử End-to-End:**
    - [ ] Test toàn bộ luồng: Quét -> Lưu -> Dò -> Xem kết quả.
    - [ ] Thử với nhiều loại vé, điều kiện ánh sáng khác nhau.
    - [ ] Ghi nhận các trường hợp OCR sai và lên kế hoạch cải thiện.

#### Deliverables:
- [ ] **Phiên bản 1.0 hoàn chỉnh:** Một ứng dụng cho phép người dùng quét, lưu và dò vé số một cách thủ công.
- [ ] Độ chính xác OCR đạt >95% trong điều kiện đủ sáng.
- [ ] Video demo sản phẩm V1.0.

---

## 🗓️ GIAI ĐOẠN 2: QUẢN LÝ VÉ HÀNG LOẠT (Tuần 5-8)
*Mục tiêu: Tăng tốc độ nhập liệu, tự động hóa hoàn toàn.*

---

### **TUẦN 5: Train Mô Hình Object Detection**

#### Nhiệm vụ:
- [ ] **Thu thập dữ liệu:**
    - [ ] Chụp khoảng 200-300 ảnh, mỗi ảnh chứa nhiều cùi vé được xếp trên một mặt phẳng.
    - [ ] Dùng một công cụ gán nhãn (như `LabelImg` hoặc `Roboflow`) để vẽ các bounding box quanh từng cùi vé.
- [ ] **Train Mô Hình YOLO:**
    - [ ] Chọn một phiên bản YOLO (ví dụ: `YOLOv8n` cho tốc độ nhanh trên mobile).
    - [ ] Fine-tune mô hình trên bộ dữ liệu đã gán nhãn.
    - [ ] Mục tiêu: Mô hình có thể nhận diện chính xác vị trí của từng cùi vé trong ảnh.
- [ ] **Tối ưu hóa Model:**
    - [ ] Chuyển đổi mô hình đã train sang định dạng `ONNX` hoặc `TFLite` để chuẩn bị tích hợp vào app di động.

#### Deliverables:
- [ ] Bộ dữ liệu gán nhãn cho object detection.
- [ ] Mô hình YOLO đã được train với độ chính xác (mAP) > 0.9.
- [ ] File model đã được tối ưu hóa.

---

### **TUẦN 6: Tích Hợp Quét Hàng Loạt**

#### Nhiệm vụ:
- [ ] **Tích hợp Model vào App:**
    - [ ] Tìm hiểu cách chạy mô hình TFLite/ONNX trên React Native/Flutter.
    - [ ] Khi người dùng chụp ảnh, chạy mô hình YOLO để lấy tọa độ của từng cùi vé.
- [ ] **Xử lý Logic Quét Hàng Loạt:**
    - [ ] Dựa vào tọa độ từ YOLO, dùng `OpenCV` (hoặc thư viện tương đương) để cắt từng ảnh cùi vé ra.
    - [ ] Gửi lần lượt từng ảnh đã cắt vào mô hình OCR từ V1.0.
    - [ ] Hiển thị danh sách các số vừa quét được trên một màn hình xác nhận.
- [ ] **Lưu Hàng Loạt:**
    - [ ] Cho phép người dùng xác nhận và lưu tất cả các vé vừa quét vào SQLite.

#### Deliverables:
- [ ] Chức năng quét hàng loạt hoạt động: Chụp 1 ảnh -> Nhận diện được nhiều số.
- [ ] Tốc độ xử lý một ảnh chứa 10 cùi vé < 10 giây.

---

### **TUẦN 7: Tự Động Hóa & Thông Báo Đẩy**

#### Nhiệm vụ:
- [ ] **Setup Tác Vụ Tự Động (Backend):**
    - [ ] Tạo một tác vụ `Celery` định kỳ để chạy script lấy kết quả xổ số mỗi ngày lúc 16h15.
    - [ ] Tạo một tác vụ `Celery` khác để tự động dò tất cả các vé "chưa xổ" trong hệ thống vào lúc 16h35.
- [ ] **Tích hợp Push Notification:**
    - [ ] Setup `Firebase Cloud Messaging (FCM)`.
    - [ ] Khi người dùng đăng ký tài khoản, lưu FCM token của họ.
    - [ ] Sau khi tác vụ dò số tự động hoàn tất, gửi thông báo đẩy đến người dùng có vé trúng.
- [ ] **Cải thiện Mobile App:**
    - [ ] Thêm chức năng đăng ký/đăng nhập.
    - [ ] Đồng bộ hóa vé đã quét từ local SQLite lên database backend (PostgreSQL) khi người dùng đăng nhập.

#### Deliverables:
- [ ] Hệ thống tự động lấy kết quả và dò số mỗi ngày.
- [ ] Người dùng nhận được push notification khi có vé trúng.
- [ ] Dữ liệu vé được đồng bộ giữa điện thoại và server.

---

### **TUẦN 8: Tối Ưu Hóa & Hoàn Thiện V2.0**

#### Nhiệm vụ:
- [ ] **Tối ưu OCR:**
    - [ ] Phân tích các trường hợp OCR sai và tìm cách cải thiện (ví dụ: train một mô hình OCR tùy chỉnh nếu cần).
- [ ] **Tối ưu Hiệu Năng:**
    - [ ] Giảm thời gian xử lý quét hàng loạt.
    - [ ] Tối ưu hóa việc chạy model trên mobile để tiết kiệm pin.
- [ ] **Kiểm thử Toàn Diện:**
    - [ ] Test luồng quét hàng loạt, đồng bộ, và nhận thông báo tự động.
    - [ ] Mời 5-10 người bán vé số dùng thử và xin phản hồi.

#### Deliverables:
- [ ] **Phiên bản 2.0 hoàn chỉnh:** Ứng dụng có khả năng quét hàng loạt và tự động dò số, thông báo kết quả.
- [ ] Phản hồi từ người dùng thực tế được ghi nhận.
- [ ] Video demo sản phẩm V2.0.

---

## 🗓️ GIAI ĐOẠN 3: CHUYÊN GIA CHỐNG VÉ GIẢ (Tuần 9-14)
*Mục tiêu: Xây dựng tính năng "deep tech", tạo sự khác biệt lớn.*

---

### **TUẦN 9-10: Thu Thập & Phân Tích Dữ Liệu Vé Giả**

#### Nhiệm vụ:
- [ ] **Nghiên cứu Đặc Điểm Vé Giả:**
    - [ ] Tìm hiểu các kỹ thuật làm vé giả phổ biến (in phun, scan màu, dán số...).
    - [ ] Phỏng vấn người bán vé số để biết kinh nghiệm nhận biết của họ.
    - [ ] Liệt kê các đặc điểm cần phân tích: chất lượng hoa văn, độ sắc nét của số, chất liệu giấy, các ký hiệu bảo an...
- [ ] **Thu Thập Dữ Liệu:**
    - [ ] Chụp ít nhất 500 ảnh vé thật dưới nhiều điều kiện ánh sáng, góc độ khác nhau, dùng chế độ macro để lấy chi tiết.
    - [ ] Tạo ra các mẫu vé "bất thường":
        - Dùng máy scan để scan vé thật rồi in màu ra giấy thường.
        - Chụp ảnh vé thật qua màn hình máy tính.
        - Nếu có thể, tìm các mẫu vé giả thật.
    - [ ] Gán nhãn cho bộ dữ liệu: "real" và "anomaly".

#### Deliverables:
- [ ] Một tài liệu phân tích chi tiết về các đặc điểm của vé giả.
- [ ] Bộ dữ liệu hình ảnh gồm ít nhất 500 ảnh vé thật và 200 ảnh vé "bất thường".

---

### **TUẦN 11-12: Train Mô Hình Phát Hiện Bất Thường**

#### Nhiệm vụ:
- [ ] **Chọn Phương Pháp:**
    - [ ] **Cách 1 (Classification):** Train một mô hình (ví dụ: `EfficientNet`) để phân loại ảnh là "real" hay "fake".
    - [ ] **Cách 2 (Anomaly Detection):** Chỉ train mô hình với vé thật (dùng Autoencoder hoặc One-Class SVM). Khi có ảnh mới, mô hình sẽ tính "điểm bất thường" (reconstruction error). Cách này linh hoạt hơn vì không cần nhiều mẫu vé giả.
    - [ ] **Quyết định:** Chọn một phương pháp để bắt đầu.
- [ ] **Tiền xử lý ảnh:**
    - [ ] Viết script để tự động crop vùng chứa các chi tiết quan trọng (hoa văn, ký hiệu bảo an) từ ảnh vé.
- [ ] **Train và Đánh giá:**
    - [ ] Train mô hình đã chọn.
    - [ ] Đánh giá độ chính xác, tỉ lệ bỏ sót (false negative) và báo động nhầm (false positive).
    - [ ] Tinh chỉnh mô hình để đạt hiệu quả tốt nhất.

#### Deliverables:
- [ ] Mô hình phát hiện bất thường đã được train.
- [ ] Báo cáo đánh giá hiệu năng của mô hình.
- [ ] Model được tối ưu hóa để chạy trên mobile.

---

### **TUẦN 13: Tích Hợp & Hoàn Thiện Giao Diện**

#### Nhiệm vụ:
- [ ] **Tích hợp Model vào App:**
    - [ ] Thêm chức năng chạy mô hình phát hiện bất thường sau khi người dùng quét vé.
- [ ] **Thiết kế Giao Diện Cảnh Báo:**
    - [ ] Khi phát hiện điểm bất thường cao, hiển thị một cảnh báo rõ ràng (ví dụ: màn hình đỏ với thông báo "Cảnh báo: Vé có dấu hiệu bất thường!").
    - [ ] Hiển thị các vùng "bất thường" trên ảnh để người dùng tự kiểm tra (nếu có thể).
- [ ] **Thu thập Phản hồi:**
    - [ ] Cho phép người dùng gửi phản hồi ("Đây là vé thật" / "Đây là vé giả") để cải thiện mô hình trong tương lai (Active Learning).

#### Deliverables:
- [ ] Chức năng chống vé giả được tích hợp vào ứng dụng.
- [ ] Giao diện cảnh báo hoạt động.
- [ ] Hệ thống thu thập phản hồi sẵn sàng.

---

### **TUẦN 14: Kiểm Thử Cuối Cùng & Chuẩn Bị Demo**

#### Nhiệm vụ:
- [ ] **Kiểm thử với người dùng cuối:**
    - [ ] Đưa ứng dụng cho 5-10 người bán vé số dùng thử trong 1 tuần.
    - [ ] Ghi nhận tất cả các phản hồi, đặc biệt là về tính năng chống vé giả.
- [ ] **Hoàn thiện sản phẩm:**
    - [ ] Sửa các lỗi cuối cùng.
    - [ ] Viết một trang giới thiệu đơn giản về ứng dụng.
    - [ ] Cập nhật file `README.md` trên GitHub với mô tả chi tiết dự án, kiến trúc và cách cài đặt.
- [ ] **Chuẩn bị Demo:**
    - [ ] Quay một video demo 2-3 phút, trình bày tất cả các tính năng từ V1.0 đến V3.0.
    - [ ] Chuẩn bị slide để trình bày dự án khi phỏng vấn.

#### Deliverables:
- [ ] **Sản phẩm hoàn chỉnh:** Sẵn sàng để demo hoặc thậm chí phát hành beta.
- [ ] GitHub repo chuyên nghiệp.
- [ ] Video và slide demo.

---

## ✅ Checklist Hoàn Thành

- [ ] **V1.0:** Ứng dụng quét và dò được vé đơn lẻ.
- [ ] **V2.0:** Ứng dụng quét được hàng loạt, tự động dò và gửi thông báo.
- [ ] **V3.0:** Ứng dụng có khả năng cảnh báo vé giả.
- [ ] **Backend:** Hoạt động ổn định, tự động lấy kết quả.
- [ ] **Testing:** Unit test và End-to-end test được viết đầy đủ.
- [ ] **Documentation:** `README.md` chi tiết, có video demo.

Chúc bạn thành công với dự án đầy ý nghĩa và ấn tượng này! 🚀