from typing import Any, Tuple, Union

from .parsers import try_parse_int


def is_leap_year(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def days_in_month(month_input: Any, year_input: Any) -> Tuple[bool, Union[int, str]]:
    """Compute number of days with TryParse and leap year rule."""
    ok_month, month = try_parse_int(month_input)
    ok_year, year = try_parse_int(year_input)

    if not ok_month or not ok_year:
        return False, "month and year must be integers"
    if month is None or year is None:
        return False, "month and year must be integers"
    if year <= 0:
        return False, "year must be > 0"
    if month < 1 or month > 12:
        return False, "month must be in [1, 12]"

    if month in (1, 3, 5, 7, 8, 10, 12):
        return True, 31
    if month in (4, 6, 9, 11):
        return True, 30
    return True, 29 if is_leap_year(year) else 28
