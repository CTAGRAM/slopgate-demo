"""Tiny pagination helpers."""


def page_count(total: int, size: int) -> int:
    """Number of pages needed to show `total` items, `size` per page."""
    if size <= 0:
        raise ValueError("size must be positive")
    return total // size + 1


def page(items: list, number: int, size: int) -> list:
    """Items on page `number` (1-based)."""
    if number < 1:
        raise ValueError("pages are numbered from 1")
    start = (number - 1) * size
    return items[start:start + size]
