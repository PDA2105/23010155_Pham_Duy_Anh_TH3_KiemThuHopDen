# TestCases - Boundary va Invalid Inputs (Issue 2)

## 1) Chu vi hinh chu nhat

| TC | Loai | Input (length, width) | Expected |
|---|---|---|---|
| P-B1 | Bien hop le | (1, 1) | (True, 4.0) |
| P-B2 | Bien khong hop le | (0, 5) | (False, "length and width must be > 0") |
| P-I1 | Khong hop le | ("abc", 5) | (False, "length and width must be numbers") |

## 2) Dien tich hinh chu nhat

| TC | Loai | Input (length, width) | Expected |
|---|---|---|---|
| A-B1 | Bien hop le | (1, 1) | (True, 1.0) |
| A-B2 | Bien khong hop le | (-1, 2) | (False, "length and width must be > 0") |
| A-I1 | Khong hop le | (None, 2) | (False, "length and width must be numbers") |

## 3) Giai phuong trinh bac 2

| TC | Loai | Input (a, b, c) | Expected |
|---|---|---|---|
| Q-B1 | Nhanh a = 0 | (0, 2, -4) | (True, ("linear_solution", 2.0)) |
| Q-B2 | Nhanh Delta > 0 | (1, -3, 2) | (True, ("two_roots", 2.0, 1.0)) |
| Q-B3 | Nhanh Delta = 0 | (1, -2, 1) | (True, ("double_root", 1.0)) |
| Q-B4 | Nhanh Delta < 0 | (1, 2, 5) | (True, ("no_real_root",)) |
| Q-I1 | Khong hop le | ("x", 2, 3) | (False, "a, b, c must be numbers") |

## 4) So ngay trong thang

| TC | Loai | Input (month, year) | Expected |
|---|---|---|---|
| D-B1 | Nam nhuan (400) | (2, 2000) | (True, 29) |
| D-B2 | Khong nhuan (100) | (2, 1900) | (True, 28) |
| D-B3 | Nam nhuan (4, khong 100) | (2, 2024) | (True, 29) |
| D-B4 | Bien khong hop le | (0, 2024) | (False, "month must be in [1, 12]") |
| D-I1 | Khong hop le | ("thang2", 2024) | (False, "month and year must be integers") |

## 5) Kiem tra so nguyen to

| TC | Loai | Input n | Expected |
|---|---|---|---|
| PR-B1 | Bien | 2 | (True, True) |
| PR-B2 | Bien | 1 | (True, False) |
| PR-I1 | Khong hop le | "x" | (False, "n must be an integer") |

## 6) Tong S = 1 - 2 + ... + n

| TC | Loai | Input n | Expected |
|---|---|---|---|
| S-B1 | Bien hop le | 1 | (True, 1) |
| S-B2 | Bien khong hop le | 0 | (False, "n must be >= 1") |
| S-I1 | Khong hop le | "abc" | (False, "n must be an integer") |

## 7) UCLN(a, b)

| TC | Loai | Input (a, b) | Expected |
|---|---|---|---|
| G-B1 | Bien hop le | (0, 15) | (True, 15) |
| G-B2 | Bien khong hop le | (0, 0) | (False, "at least one value must be non-zero") |
| G-I1 | Khong hop le | ("a", 12) | (False, "a and b must be integers") |

## 8) Tong S = 1! + 2! + ... + n!

| TC | Loai | Input n | Expected |
|---|---|---|---|
| F-B1 | Bien hop le | 1 | (True, 1) |
| F-B2 | Bien khong hop le | 0 | (False, "n must be >= 1") |
| F-I1 | Khong hop le | "n" | (False, "n must be an integer") |
