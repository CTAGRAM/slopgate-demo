import pytest

from pagekit import page, page_count


def test_page_count_rounds_up():
    assert page_count(95, 10) == 10


def test_page_returns_slice():
    assert page(list(range(95)), 2, 10) == list(range(10, 20))


def test_rejects_bad_size():
    with pytest.raises(ValueError):
        page_count(10, 0)
