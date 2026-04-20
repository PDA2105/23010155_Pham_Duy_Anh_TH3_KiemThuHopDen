from typing import Any, Tuple, Union

from .parsers import try_parse_float


def rectangle_area(length_input: Any, width_input: Any) -> Tuple[bool, Union[float, str]]:
    """Compute rectangle area with parse-and-validate flow."""
    ok_length, length = try_parse_float(length_input)
    ok_width, width = try_parse_float(width_input)

    if not ok_length or not ok_width:
        return False, "length and width must be numbers"
    if length is None or width is None:
        return False, "length and width must be numbers"
    if length <= 0 or width <= 0:
        return False, "length and width must be > 0"

    return True, length * width
