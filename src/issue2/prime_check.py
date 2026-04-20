from typing import Any, Tuple, Union

from .parsers import try_parse_int


def is_prime(n_input: Any) -> Tuple[bool, Union[bool, str]]:
    """Check prime with TryParse and integer constraints."""
    ok_n, n = try_parse_int(n_input)
    if not ok_n or n is None:
        return False, "n must be an integer"

    if n < 2:
        return True, False
    if n == 2:
        return True, True
    if n % 2 == 0:
        return True, False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return True, False
        i += 2
    return True, True
