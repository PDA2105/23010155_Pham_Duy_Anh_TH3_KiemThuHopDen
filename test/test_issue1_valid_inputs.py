import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from issue1.alternating_sum import alternating_sum
from issue1.days_in_month import days_in_month
from issue1.factorial_sum import factorial_sum
from issue1.gcd_calculator import gcd
from issue1.prime_check import is_prime
from issue1.quadratic_solver import solve_quadratic
from issue1.rectangle_area import rectangle_area
from issue1.rectangle_perimeter import rectangle_perimeter


class TestIssue1ValidInputs(unittest.TestCase):
    def test_rectangle_perimeter_valid(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)
        self.assertEqual(rectangle_perimeter(2.5, 4), 13.0)
        self.assertEqual(rectangle_perimeter(1, 1), 4)

    def test_rectangle_area_valid(self):
        self.assertEqual(rectangle_area(5, 3), 15)
        self.assertEqual(rectangle_area(2.5, 4), 10.0)
        self.assertEqual(rectangle_area(1, 1), 1)

    def test_quadratic_solver_valid(self):
        self.assertEqual(solve_quadratic(1, -3, 2), ("two_roots", 2.0, 1.0))
        self.assertEqual(solve_quadratic(1, -2, 1), ("double_root", 1.0))
        self.assertEqual(solve_quadratic(1, 2, 5), ("no_real_root",))

    def test_days_in_month_valid(self):
        self.assertEqual(days_in_month(2, 2024), 29)
        self.assertEqual(days_in_month(2, 2023), 28)
        self.assertEqual(days_in_month(4, 2025), 30)
        self.assertEqual(days_in_month(1, 2025), 31)

    def test_prime_check_valid(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(49))

    def test_alternating_sum_valid(self):
        self.assertEqual(alternating_sum(1), 1)
        self.assertEqual(alternating_sum(5), 3)
        self.assertEqual(alternating_sum(6), -3)

    def test_gcd_valid(self):
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(13, 17), 1)
        self.assertEqual(gcd(0, 15), 15)

    def test_factorial_sum_valid(self):
        self.assertEqual(factorial_sum(1), 1)
        self.assertEqual(factorial_sum(4), 33)
        self.assertEqual(factorial_sum(5), 153)


if __name__ == "__main__":
    unittest.main()
