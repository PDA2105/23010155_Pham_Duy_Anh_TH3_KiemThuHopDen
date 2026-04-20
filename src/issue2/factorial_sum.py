from typing import Any, Tuple, Union

from .parsers import try_parse_int


def factorial_sum(n_input: Any) -> Tuple[bool, Union[int, str]]:
    """Compute S = 1! + 2! + ... + n! with n >= 1 constraint."""
    ok_n, n = try_parse_int(n_input)
    if not ok_n or n is None:
        return False, "n must be an integer"
    if n < 1:
        return False, "n must be >= 1"

    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total += fact

    return True, total
