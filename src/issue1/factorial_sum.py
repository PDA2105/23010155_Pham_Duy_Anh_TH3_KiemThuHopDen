def factorial_sum(n: int) -> int:
    """Return S = 1! + 2! + 3! + ... + n! for n >= 1."""
    if n < 1:
        raise ValueError("n must be >= 1")

    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total += fact
    return total
