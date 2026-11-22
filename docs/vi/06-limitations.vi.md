# Hạn chế

- **Script chỉ kiểm tra cơ học.** Script không đánh giá giọng văn.
- **Các giới hạn số chỉ là ước lượng ban đầu.** Chưa ai kiểm chứng chúng như tiêu chuẩn. Hãy chạy script trên văn bản thật của nhóm bạn rồi chỉnh `profile.json`.
- **Ví dụ chỉ để minh họa.** Câu chuyện và con số trong `examples/` không phải sự thật. Khi làm việc thật, dùng dữ kiện của tác giả hoặc ghi `TBD`.
- **Chưa có bằng chứng về hiệu quả.** Xem [05-evals](05-evals.vi.md). Bộ eval nhỏ. Bằng chứng hiện có là một lần chạy cho mỗi phiên bản, xem [evidence/](../../evidence/README.md).
- **Test tự động còn ít.** Test phủ thống kê `TBD-n` trong `evals/score.py`, bộ loại tài liệu, loại mặc định của checker, các phép kiểm tra ô bảng, nhãn báo cáo và `--short-brief` của checker, và các bảng Units (`python3 -m unittest discover -s tests`). `AGENTS.md` liệt kê các bước kiểm tra thủ công cho phần còn lại.
- **Các loại ngoài phạm vi.** `prose`, `poetry` và `screen-design` hiện nằm ngoài phạm vi.

## Đóng góp

Đọc `AGENTS.md` trước. File đó giữ ba thư mục ngôn ngữ song song và nói rõ file nào sở hữu thông tin nào.

## Giấy phép

GNU GPL v3. Xem `LICENSE`.
