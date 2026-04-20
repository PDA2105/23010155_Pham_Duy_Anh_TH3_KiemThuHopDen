def rectangle_area(length: float, width: float) -> float:
    """Return area of a rectangle with valid positive dimensions."""
    if length <= 0 or width <= 0:
        raise ValueError("length and width must be positive")
    return length * width
