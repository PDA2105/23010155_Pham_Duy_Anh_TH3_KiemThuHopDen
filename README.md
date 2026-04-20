# BÀI THỰC HÀNH 03 - KIỂM THỬ HỘP ĐEN (PYTHON)

Repository gồm 8 bài toán và bộ test theo hướng kiểm thử hộp đen.

## Danh sách bài toán

1. Tính chu vi hình chữ nhật
2. Tính diện tích hình chữ nhật
3. Giải phương trình bậc 2
4. Tính số ngày của một tháng
5. Kiểm tra n có là số nguyên tố hay không
6. Tính tổng S = 1 - 2 + 3 - 4 + ... + n
7. Tìm UCLN của a và b
8. Tính tổng S = 1! + 2! + 3! + ... + n!

## Cấu trúc dự án

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
|       |-- __init__.py
|       |-- parsers.py
|       |-- rectangle_perimeter.py
|       |-- rectangle_area.py
|       |-- quadratic_solver.py
|       |-- days_in_month.py
|       |-- prime_check.py
|       |-- alternating_sum.py
|       |-- gcd_calculator.py
|       `-- factorial_sum.py
`-- test/
	|-- issue1_valid_testcases.md
	|-- issue2_valid_testcases.md
	|-- test_issue1_valid_inputs.py
	`-- test_issue2_boundary_invalid_inputs.py
```

## Mô tả thư mục

- `src/issue1/`: Logic chính cho 8 bài toán với dữ liệu hợp lệ
- `src/issue2/`: Logic kiểm tra dữ liệu biên/không hợp lệ (TryParse + ràng buộc điều kiện)
- `test/issue1_valid_testcases.md`: Test case hợp lệ cho Issue 1
- `test/issue2_valid_testcases.md`: Test case biên và không hợp lệ cho Issue 2
- `test/test_issue1_valid_inputs.py`: Unit test cho Issue 1
- `test/test_issue2_boundary_invalid_inputs.py`: Unit test cho Issue 2

## Cách chạy test

Chạy từng bộ test:

```bash
python -m unittest test/test_issue1_valid_inputs.py
python -m unittest test/test_issue2_boundary_invalid_inputs.py
```

Hoặc chạy toàn bộ test trong thư mục `test`:

```bash
python -m unittest discover -s test -p "test_*.py"
```

## Trạng thái

- Issue 1: Đã hoàn thành
- Issue 2: Đã hoàn thành