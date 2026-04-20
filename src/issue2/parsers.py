import math
from typing import Any, Optional, Tuple


def try_parse_int(value: Any) -> Tuple[bool, Optional[int]]:
    """Try parse input to int, similar to TryParse style."""
    if isinstance(value, bool):
        return False, None
    if isinstance(value, int):
        return True, value
    if value is None:
        return False, None

    try:
        if isinstance(value, str):
            value = value.strip()
            if value == "":
                return False, None
        parsed = int(value)
    except (TypeError, ValueError):
        return False, None

    return True, parsed


def try_parse_float(value: Any) -> Tuple[bool, Optional[float]]:
    """Try parse input to float, similar to TryParse style."""
    if isinstance(value, bool) or value is None:
        return False, None

    try:
        if isinstance(value, str):
            value = value.strip()
            if value == "":
                return False, None
        parsed = float(value)
    except (TypeError, ValueError):
        return False, None

    if math.isnan(parsed) or math.isinf(parsed):
        return False, None

    return True, parsed
