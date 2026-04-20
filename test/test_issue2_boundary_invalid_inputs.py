import sys
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from issue2.alternating_sum import alternating_sum
from issue2.days_in_month import days_in_month
from issue2.factorial_sum import factorial_sum
from issue2.gcd_calculator import gcd
from issue2.prime_check import is_prime
from issue2.quadratic_solver import solve_quadratic
from issue2.rectangle_area import rectangle_area
from issue2.rectangle_perimeter import rectangle_perimeter


class TestIssue2BoundaryAndInvalidInputs(unittest.TestCase):
    def test_rectangle_perimeter_boundary_and_invalid(self):
        self.assertEqual(rectangle_perimeter(1, 1), (True, 4.0))
        self.assertEqual(rectangle_perimeter(0, 5), (False, "length and width must be > 0"))
        self.assertEqual(rectangle_perimeter("abc", 5), (False, "length and width must be numbers"))

    def test_rectangle_area_boundary_and_invalid(self):
        self.assertEqual(rectangle_area(1, 1), (True, 1.0))
        self.assertEqual(rectangle_area(-1, 2), (False, "length and width must be > 0"))
        self.assertEqual(rectangle_area(None, 2), (False, "length and width must be numbers"))

    def test_quadratic_important_branches_and_invalid(self):
        self.assertEqual(solve_quadratic(0, 2, -4), (True, ("linear_solution", 2.0)))
        self.assertEqual(solve_quadratic(1, -3, 2), (True, ("two_roots", 2.0, 1.0)))
        self.assertEqual(solve_quadratic(1, -2, 1), (True, ("double_root", 1.0)))
        self.assertEqual(solve_quadratic(1, 2, 5), (True, ("no_real_root",)))
        self.assertEqual(solve_quadratic("x", 2, 3), (False, "a, b, c must be numbers"))

    def test_days_in_month_leap_rule_boundary_and_invalid(self):
        self.assertEqual(days_in_month(2, 2000), (True, 29))
        self.assertEqual(days_in_month(2, 1900), (True, 28))
        self.assertEqual(days_in_month(2, 2024), (True, 29))
        self.assertEqual(days_in_month(0, 2024), (False, "month must be in [1, 12]"))
        self.assertEqual(days_in_month("thang2", 2024), (False, "month and year must be integers"))

    def test_prime_check_boundary_and_invalid(self):
        self.assertEqual(is_prime(2), (True, True))
        self.assertEqual(is_prime(1), (True, False))
        self.assertEqual(is_prime("x"), (False, "n must be an integer"))

    def test_alternating_sum_n_less_than_1_and_invalid(self):
        self.assertEqual(alternating_sum(1), (True, 1))
        self.assertEqual(alternating_sum(0), (False, "n must be >= 1"))
        self.assertEqual(alternating_sum("abc"), (False, "n must be an integer"))

    def test_gcd_boundary_and_invalid(self):
        self.assertEqual(gcd(0, 15), (True, 15))
        self.assertEqual(gcd(0, 0), (False, "at least one value must be non-zero"))
        self.assertEqual(gcd("a", 12), (False, "a and b must be integers"))

    def test_factorial_sum_n_less_than_1_and_invalid(self):
        self.assertEqual(factorial_sum(1), (True, 1))
        self.assertEqual(factorial_sum(0), (False, "n must be >= 1"))
        self.assertEqual(factorial_sum("n"), (False, "n must be an integer"))


if __name__ == "__main__":
    unittest.main()
