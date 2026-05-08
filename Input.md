# ĐỀ THI CUỐI KỲ

**Môn học:** Software Testing Foundations
**Học phần:** Kiểm thử phần mềm bằng Python
**Hình thức:** Tự luận + Lập trình

---

## CÂU 1: PHÂN TÍCH HỆ THỐNG (2.0 điểm)
Hệ thống Smart Travel / Explore California là một nền tảng hỗ trợ người dùng:
* Tìm kiếm chuyến bay, khách sạn, nhà hàng
* Lập kế hoạch du lịch cá nhân hóa
* Tích hợp API bên thứ ba (Airline, Hotel, Maps)
* Đảm bảo tốc độ tìm kiếm < 50ms

Trong quá trình kiểm thử Alpha, hệ thống phát hiện các lỗi sau:
* Không truy xuất được booking mới (< 7 ngày)
* Một số hãng hàng không không trả dữ liệu
* Tìm kiếm theo địa điểm bị timeout

**Yêu cầu:**
1. Xác định 3 loại lỗi tương ứng với các vấn đề trên
2. Phân tích nguyên nhân khả dĩ (Database / API/Performance / Logic)

---

## CÂU 2: THIẾT KẾ TEST CASE (3.0 điểm)
Xét 3 module chính của hệ thống:

**Module 1: Air**
Chức năng:
1. Xác nhận booking
2. Tìm hãng hàng không
3. Tìm chuyến theo địa điểm
4. Kiểm tra thời gian bay
5. Gửi nhắc check-in

**Module 2: Hotel**
Chức năng:
1. Tìm khách sạn
2. Đặt phòng
3. Hủy phòng
4. Kiểm tra giá
5. Đánh giá khách sạn

**Module 3: Search & Plan**
Chức năng:
1. Tìm kiếm toàn hệ thống
2. Lọc kết quả
3. Gợi ý cá nhân hóa
4. Lưu kế hoạch
5. Tối ưu lịch trình

**Yêu cầu:**
Lập bảng ít nhất 12 test cases theo format:
`# | Module | Action | Expected Result | Actual Result | Status | Type`

**Điều kiện bắt buộc:**
* Ít nhất:
    * 5 Functional test
    * 3 Negative test
    * 2 Boundary test
    * 2 Performance test
* Phải có cả PASS và FAIL

---

## CÂU 3: LẬP TRÌNH KIỂM THỬ PYTHON (4.0 điểm)
**Yêu cầu:**
1. **Xây dựng hệ thống giả lập**
   Viết 3 class:
   * `AirService`
   * `HotelService`
   * `SearchPlanService`
   Mỗi class phải có đầy đủ 5 chức năng như mô tả ở Câu 2.
   
2. **Viết chương trình kiểm thử**
   Sử dụng `unittest` hoặc `pytest` để:
   * Viết test cho từng module
   * Mỗi module tối thiểu 5 test functions
   * Bao gồm:
       * Functional test
       * Negative test
       * Boundary test
       * Performance test

**Yêu cầu kỹ thuật:**
* Code phải chạy được
* Có assert rõ ràng
* Có test PASS và FAIL

---

## CÂU 4: PHÂN TÍCH KẾT QUẢ KIỂM THỬ (1 điểm)
Trình bày ngắn gọn:
1. Tổng kết kết quả kiểm thử
2. Liệt kê ít nhất 3 lỗi tìm được
3. Phân loại mức độ lỗi:
   * Critical
   * Major
   * Minor
   * Trivial
