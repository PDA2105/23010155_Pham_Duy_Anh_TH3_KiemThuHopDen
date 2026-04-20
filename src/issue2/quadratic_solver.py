import math
from typing import Any, Tuple, Union

from .parsers import try_parse_float


ResultType = Union[Tuple[str], Tuple[str, float], Tuple[str, float, float], str]


def solve_quadratic(a_input: Any, b_input: Any, c_input: Any) -> Tuple[bool, ResultType]:
    """Solve equation with full important branches, including a = 0."""
    ok_a, a = try_parse_float(a_input)
    ok_b, b = try_parse_float(b_input)
    ok_c, c = try_parse_float(c_input)

    if not ok_a or not ok_b or not ok_c:
        return False, "a, b, c must be numbers"
    if a is None or b is None or c is None:
        return False, "a, b, c must be numbers"

    # Branch 1: a = 0 -> linear equation bx + c = 0
    if a == 0:
        if b == 0:
            if c == 0:
                return True, ("infinitely_many_solutions",)
            return True, ("no_solution",)
        return True, ("linear_solution", -c / b)

    # Branch 2-4: delta > 0, delta = 0, delta < 0
    delta = b * b - 4 * a * c
    if delta > 0:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        return True, ("two_roots", x1, x2)

    if delta == 0:
        x = -b / (2 * a)
        return True, ("double_root", x)

    return True, ("no_real_root",)
