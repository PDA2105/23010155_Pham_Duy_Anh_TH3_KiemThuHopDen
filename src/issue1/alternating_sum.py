def alternating_sum(n: int) -> int:
    """Return S = 1 - 2 + 3 - 4 + ... + n for n >= 1."""
    if n < 1:
        raise ValueError("n must be >= 1")
    if n % 2 == 0:
        return -(n // 2)
    return (n + 1) // 2
