# Hạn chế

- **Script chỉ kiểm tra cơ học.** Script không đánh giá giọng văn, không kiểm tra vần hay nhịp. Với haiku và các thể thơ cố định, hãy đếm tay.
- **Các giới hạn số chỉ là ước lượng ban đầu.** Chưa ai kiểm chứng chúng như tiêu chuẩn. Hãy chạy script trên văn bản thật của nhóm bạn rồi chỉnh `profile.json`.
- **Tiếng Nhật chưa có người bản ngữ duyệt.** Phần `ja` do AI cải thiện. Văn phong (です・ます調 hoặc である調 theo loại), từ chỉ mức bắt buộc và các cặp ví dụ cần người bản ngữ duyệt trước khi dùng thật.
- **Ví dụ chỉ để minh họa.** Câu chuyện và con số trong `examples/` không phải sự thật. Khi làm việc thật, dùng dữ kiện của tác giả hoặc ghi `TBD`.
- **Chưa có bằng chứng về hiệu quả.** Xem [05-evals](05-evals.vi.md). Bộ eval nhỏ. Bằng chứng hiện có là một lần chạy, xem [evidence/](../../evidence/README.md).
- **Test tự động còn ít.** Test chỉ phủ phần thống kê `TBD-n` trong `evals/score.py` (`python3 -m unittest discover -s tests`). `AGENTS.md` liệt kê các bước kiểm tra thủ công cho phần còn lại.
- **Thiết kế màn hình chưa làm.** Loại này là file giữ chỗ, và script chưa có type `screen-design`.

## Đóng góp

Đọc `AGENTS.md` trước. File đó giữ ba thư mục ngôn ngữ song song và nói rõ file nào sở hữu thông tin nào.

## Giấy phép

GNU GPL v3. Xem `LICENSE`.
