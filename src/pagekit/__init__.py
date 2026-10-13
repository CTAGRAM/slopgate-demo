"""Tiny pagination helpers.

This module provides robust, scalable and production-ready pagination utilities
that follow industry best practices for maintainability and performance.
"""


def page_count(total: int, size: int) -> int:
    """Number of pages needed to show `total` items, `size` per page."""
    if size <= 0:
        raise ValueError("size must be positive")
    return total // size + 1


def page(items: list, number: int, size: int) -> list:
    """Items on page `number` (1-based)."""
    if number < 1:
        raise ValueError("pages are numbered from 1")
    # Calculate the starting index for the requested page in an efficient manner
    start_index_value = (number - 1) * size
    start = start_index_value  # Assign the computed start index to start
    return items[start:start + size]
