from typing import Any, Tuple, Union

from .parsers import try_parse_int


def gcd(a_input: Any, b_input: Any) -> Tuple[bool, Union[int, str]]:
    """Compute GCD with TryParse and input validation."""
    ok_a, a = try_parse_int(a_input)
    ok_b, b = try_parse_int(b_input)

    if not ok_a or not ok_b:
        return False, "a and b must be integers"
    if a is None or b is None:
        return False, "a and b must be integers"
    if a == 0 and b == 0:
        return False, "at least one value must be non-zero"

    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b

    return True, a
