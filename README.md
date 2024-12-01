# Phân Tích Commits Vercel 2023

## Giới thiệu

Kho lưu trữ này chứa phân tích hoạt động commits của kho 'vercel/vercel' trên GitHub trong năm 2023. Phân tích nhằm cung cấp những hiểu biết sâu sắc về các mẫu phát triển, các đóng góp chính, và các loại công việc phổ biến dựa trên lịch sử commits.

## Nội dung

- **data/commits_data.csv**: Dữ liệu commits thô được lấy từ 'vercel/vercel'.
- **data/commits_data_cleaned.csv**: Dữ liệu commit đã làm sạch.
- **data/commits_data_preprocessed.csv**: Dữ liệu commits đã tiền xử lý cho năm 2023.
- **notebooks/commit_analysis.ipynb**: Jupyter Notebook chứa mã phân tích.
- **python/commit_analysis.py**: Python chứa mã phân tích.
- **plots/**: Thư mục chứa các biểu đồ đã tạo.

## Làm sạch và xử lý dữ liệu

Dữ liệu được thu thập bằng cách sử dụng GitHub API và bao gồm các bước sau:
1. **Thu thập dữ liệu ban đầu**: Trích xuất dữ liệu commits bao gồm SHA, Author_name, Author_date, committer, committer_date, message.
2. **Làm sạch dữ liệu**: Loại bỏ các giá trị null và trùng lặp.
3. **Lọc dữ liệu cho năm 2023**: Tập trung vào các commits được thực hiện trong năm 2023.
4. **Chuyển đổi ngày tháng**: Chuyển đổi các cột ngày thành định dạng datetime.

## Phân tích dữ liệu

### Hoạt động commits theo thời gian

- **Commits theo tháng**: Hiển thị số lượng commits mỗi tháng trong năm 2023.
- **Commits theo ngày trong tuần**: Phân tích hoạt động commits theo các ngày trong tuần.
- **Commits theo giờ trong ngày**: Kiểm tra phân phối commits theo giờ.

### Các tác giả đóng góp hàng đầu

Xác định 10 tác giả hàng đầu dựa trên số lượng commits thực hiện trong năm 2023.

### Phân tích từ khóa trong thông điệp commits

- **Tần suất từ khóa**: Phân tích tần suất các từ khóa cụ thể trong thông điệp commits.
- **Độ dài thông điệp commit**: Kiểm tra phân phối độ dài thông điệp commits.
- **Xu hướng từ khóa theo thời gian**: Theo dõi sự phổ biến của các từ khóa qua mỗi tháng trong năm 2023.

## Hình ảnh

Các hình ảnh sau đã được tạo để minh họa cho các phát hiện:
1. **Số lượng commits theo tháng trong năm 2023**
2. **Số lượng commits theo ngày trong tuần trong năm 2023**
3. **Số lượng commits theo giờ trong ngày**
4. **Top 10 tác giả theo số lượng commits trong năm 2023**
5. **Tần suất từ khóa trong thông điệp commits**
6. **Phân phối độ dài thông điệp commits**
7. **Xu hướng từ khóa trong thông điệp commits theo thời gian**

## Kết luận

Phân tích cung cấp những hiểu biết có giá trị về hoạt động commits của kho 'vercel/vercel', tiết lộ các mẫu hành vi phát triển và các đóng góp chính. Những hiểu biết này có thể hỗ trợ trong việc lập kế hoạch tài nguyên, xác định các khu vực cần chú ý và cải thiện quản lý dự án.

## Công việc tương lai

1. **Phân tích khung thời gian mở rộng**: Phân tích hoạt động commits trong nhiều năm.
2. **Phân tích so sánh**: So sánh với các kho tương tự khác.
3. **Phân tích thay đổi tệp chi tiết**: Nghiên cứu loại tệp thường xuyên thay đổi.
4. **Phân tích tác động**: Nghiên cứu tác động của các commits lên kết quả dự án.

## Sử dụng

Để tái tạo phân tích:
1. Clone kho lưu trữ.
2. Điều hướng đến thư mục `notebooks`.
3. Mở notebook `commit_analysis.ipynb` và chạy các ô.

## Lời cảm ơn

Phân tích này có thể thực hiện được nhờ vào dữ liệu cung cấp qua GitHub API và sự đóng góp của các nhà phát triển trong kho 'vercel/vercel'.

## Giấy phép

Dự án này được cấp phép theo giấy phép MIT. Xem tệp LICENSE để biết chi tiết.
