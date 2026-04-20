def gcd(a: int, b: int) -> int:
    """Return greatest common divisor of two integers."""
    if a == 0 and b == 0:
        raise ValueError("at least one value must be non-zero")

    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a
