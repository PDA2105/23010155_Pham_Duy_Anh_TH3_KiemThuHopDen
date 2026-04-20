def rectangle_perimeter(length: float, width: float) -> float:
    """Return perimeter of a rectangle with valid positive dimensions."""
    if length <= 0 or width <= 0:
        raise ValueError("length and width must be positive")
    return 2 * (length + width)
