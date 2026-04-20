# BÀI THỰC HÀNH 03 - KIỂM THỬ HỘP ĐEN (PYTHON)

Repository này gồm 8 bài toán và bộ test theo hướng kiểm thử hộp đen.

## Danh sách bài toán

1. Tính chu vi hình chữ nhật
2. Tính diện tích hình chữ nhật
3. Giải phương trình bậc 2
4. Tính số ngày của một tháng
5. Kiểm tra n có là số nguyên tố hay không
6. Tính tổng S = 1 - 2 + 3 - 4 + ... + n
7. Tìm UCLN của a và b
8. Tính tổng S = 1! + 2! + 3! + ... + n!

## Cấu trúc dự án hiện tại

```text
.
|-- README.md
|-- src/
|   |-- issue1/
|   |   |-- __init__.py
|   |   |-- rectangle_perimeter.py
|   |   |-- rectangle_area.py
|   |   |-- quadratic_solver.py
|   |   |-- days_in_month.py
|   |   |-- prime_check.py
|   |   |-- alternating_sum.py
|   |   |-- gcd_calculator.py
|   |   `-- factorial_sum.py
|   `-- issue2/
`-- test/
	|-- issue1_valid_testcases.md
	`-- test_issue1_valid_inputs.py
```

## Mô tả nhanh

- `src/issue1/`: Logic chính cho 8 bài toán (mỗi file là 1 bài)
- `src/issue2/`: Chưa triển khai (dành cho test case không hợp lệ, biên, ngoại lệ)
- `test/issue1_valid_testcases.md`: Danh sách test case hợp lệ theo phân lớp tương đương
- `test/test_issue1_valid_inputs.py`: Unit test Python cho các test case hợp lệ

## Cách chạy test (Issue 1)

Từ thư mục gốc project, chạy:

```bash
python -m unittest test/test_issue1_valid_inputs.py
```

Nếu máy có nhiều phiên bản Python, dùng đúng đường dẫn Python bạn đang cấu hình (ví dụ `python3` hoặc đường dẫn tuyệt đối tới `python.exe`).

## Trạng thái hiện tại

- Issue 1: Đã có logic và test case hợp lệ cho 8 bài toán
- Issue 2: Chưa triển khai