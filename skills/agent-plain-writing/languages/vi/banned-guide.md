# Bảng từ cấm và cách thay

Danh sách máy đọc nằm ở `banned.txt` cùng thư mục. File này giải thích cách thay. Khi thêm cụm vào một nơi, thêm vào cả hai.

## Cụm "văn AI" (áp dụng mọi loại)

| Cụm | Thay bằng | Ví dụ |
|---|---|---|
| nhằm mục đích | để | "Nhằm mục đích tăng tốc" → "Để chạy nhanh hơn" |
| có thể nói rằng | (bỏ) | Nói thẳng điều đó |
| đóng vai trò quan trọng, đóng vai trò then chốt | nói vai trò cụ thể | "Cache đóng vai trò quan trọng" → "Cache giúp trang tải dưới 1 giây" |
| hãy cùng | (bỏ) | "Hãy cùng tìm hiểu" → vào thẳng nội dung |
| trong thế giới ngày nay, trong thời đại ... | (bỏ) | Mở bài bằng sự việc cụ thể |
| không chỉ ... mà còn *(warn)* | tách thành hai câu | "Không chỉ nhanh mà còn rẻ" → "Nó nhanh. Nó cũng rẻ." |
| toàn diện | nói cụ thể phủ những gì | "Báo cáo toàn diện" → "Báo cáo gồm doanh thu, chi phí, lợi nhuận" |
| tối ưu hóa | nói giảm hoặc tăng cái gì, từ đâu đến đâu | "Tối ưu hóa truy vấn" → "Truy vấn giảm từ 3 giây xuống 200 ms" |
| tiến hành, thực hiện việc | động từ trực tiếp | "Tiến hành kiểm tra" → "Kiểm tra" |
| một cách + tính từ *(warn)* | trạng từ trực tiếp hoặc bỏ | "Một cách nhanh chóng" → "nhanh" |
| cho phép người dùng có thể | người dùng có thể | |
| đảm bảo rằng | (bỏ) hoặc "để chắc là" | |
| điều quan trọng cần lưu ý là, cần lưu ý rằng | (bỏ) hoặc in đậm "Chú ý:" | |
| thông qua việc | bằng cách, bằng | |
| như chúng ta đã biết | (bỏ) | |
| bên cạnh đó, ngoài ra *(warn)* | (bỏ) hoặc dùng tiêu đề mục | Tránh mở đầu câu liên tục |
| hạng mục | việc, mục | |

## Từ mơ hồ trong detail design

| Từ | Thay bằng |
|---|---|
| phù hợp, thích hợp | điều kiện cụ thể |
| nếu cần | điều kiện cụ thể, hoặc `TBD` |
| v.v., và các thứ | liệt kê đủ, hoặc trỏ tới phụ lục |
| nhanh chóng, dễ dàng | con số (ms, số bước) |
| linh hoạt | nói cấu hình được gì, bằng cách nào |
| hiệu quả, an toàn | tiêu chí đo được |

## Từ hay gặp trong user guide

| Từ | Thay bằng |
|---|---|
| thực hiện, tiến hành | động từ cụ thể: bấm, chọn, nhập |
| cấu hình | cài đặt, thiết lập |

## Cụm của blog

| Cụm | Thay bằng |
|---|---|
| tôi viết blog này để | vào thẳng sự việc hoặc kết luận |
| bài học rút ra:, bài học: | lồng vào đoạn kết tự nhiên, không gắn nhãn |
| lưu ý: | viết thẳng vào mạch bài hoặc bỏ |
| vô cùng | (bỏ) hoặc số liệu |
| mạnh mẽ | số liệu hoặc việc nó làm được. "Công cụ mạnh mẽ" → "Công cụ xử lý 10.000 dòng mỗi giây" |
| tận dụng | dùng |
| trong quá trình | khi |
| nhìn chung, tóm lại | (bỏ). Đừng tóm tắt lại điều vừa nói |

## Cụm của prose

| Cụm | Thay bằng |
|---|---|
| trái tim loạn nhịp, thời gian như ngừng trôi, nước mắt lăn dài, một cảm giác khó tả, nỗi buồn bao trùm, ánh mắt sâu thẳm, tim như thắt lại | một hành động hoặc chi tiết nhìn thấy được |
| vô cùng | (bỏ) hoặc số liệu |
| mạnh mẽ | số liệu hoặc việc nó làm được |
| tận dụng | dùng |
| trong quá trình | khi |
| nhìn chung, tóm lại | (bỏ) |

## Cụm của poetry

| Cụm | Thay bằng |
|---|---|
| tràn về, lặng lẽ, mênh mang, nao nao, bồi hồi, thổn thức | một hình ảnh cụ thể: vật, tiếng động, cử chỉ |
| con tim, nỗi nhớ, tâm hồn, cuộc đời | tên vật hoặc việc làm gợi ra cảm xúc đó |

## Nhãn báo cáo (3 dòng đầu hoặc 3 dòng cuối)

| Nhãn | Thay bằng |
|---|---|
| kết quả:, giả định:, phỏng đoán: | (bỏ khỏi văn bản). Ghi báo cáo ngoài văn bản, hoặc bỏ nếu không có chỗ nào khác |

## Quy tắc chung

- Cụm bị cấm vẫn dùng được khi **trích nguyên văn** hoặc khi nó là tên riêng.
- Cấm cụm không có nghĩa là cấm ý. Ý "hệ thống nhanh" vẫn cần, chỉ là phải kèm con số.
- Thấy mình lặp một cụm từ ba lần trong bài, thay hai lần.
