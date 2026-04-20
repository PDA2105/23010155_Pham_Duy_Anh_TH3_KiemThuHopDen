import math


def solve_quadratic(a: float, b: float, c: float):
    """Solve ax^2 + bx + c = 0 over R.

    Returns:
        ("two_roots", x1, x2)
        ("double_root", x)
        ("no_real_root",)
    """
    if a == 0:
        raise ValueError("a must be non-zero for a quadratic equation")

    delta = b * b - 4 * a * c
    if delta > 0:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        return ("two_roots", x1, x2)

    if delta == 0:
        x = -b / (2 * a)
        return ("double_root", x)

    return ("no_real_root",)
