# Test cases hop le - Issue 1

## 1) Tinh chu vi hinh chu nhat

| TC | Input (dai, rong) | Expected |
|---|---|---|
| P1 | (5, 3) | 16 |
| P2 | (2.5, 4) | 13.0 |
| P3 | (1, 1) | 4 |

## 2) Tinh dien tich hinh chu nhat

| TC | Input (dai, rong) | Expected |
|---|---|---|
| A1 | (5, 3) | 15 |
| A2 | (2.5, 4) | 10.0 |
| A3 | (1, 1) | 1 |

## 3) Giai phuong trinh bac 2

| TC | Input (a, b, c) | Expected |
|---|---|---|
| Q1 | (1, -3, 2) | ("two_roots", 2.0, 1.0) |
| Q2 | (1, -2, 1) | ("double_root", 1.0) |
| Q3 | (1, 2, 5) | ("no_real_root",) |

## 4) Tinh so ngay cua mot thang

| TC | Input (thang, nam) | Expected |
|---|---|---|
| D1 | (2, 2024) | 29 |
| D2 | (2, 2023) | 28 |
| D3 | (4, 2025) | 30 |
| D4 | (1, 2025) | 31 |

## 5) Kiem tra so nguyen to

| TC | Input (n) | Expected |
|---|---|---|
| PR1 | 2 | True |
| PR2 | 17 | True |
| PR3 | 49 | False |

## 6) Tinh tong S = 1 - 2 + 3 - 4 + ... + n

| TC | Input (n) | Expected |
|---|---|---|
| S1 | 1 | 1 |
| S2 | 5 | 3 |
| S3 | 6 | -3 |

## 7) Tim UCLN cua a va b

| TC | Input (a, b) | Expected |
|---|---|---|
| G1 | (54, 24) | 6 |
| G2 | (13, 17) | 1 |
| G3 | (0, 15) | 15 |

## 8) Tinh tong S = 1! + 2! + ... + n!

| TC | Input (n) | Expected |
|---|---|---|
| F1 | 1 | 1 |
| F2 | 4 | 33 |
| F3 | 5 | 153 |
