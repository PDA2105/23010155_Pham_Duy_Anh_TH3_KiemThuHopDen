def is_leap_year(year: int) -> bool:
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def days_in_month(month: int, year: int) -> int:
    """Return number of days in the given month/year."""
    if year <= 0:
        raise ValueError("year must be positive")
    if month < 1 or month > 12:
        raise ValueError("month must be in [1, 12]")

    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month in (4, 6, 9, 11):
        return 30
    return 29 if is_leap_year(year) else 28
