"""
Tests for bubble_sort function.
Tests cover: empty lists, single elements, sorted arrays, reverse-sorted arrays, and duplicates.
"""

import pytest
from main import bubble_sort


def test_empty_list():
    """Test bubble_sort with an empty list."""
    result = bubble_sort([])
    assert result == []


def test_single_element():
    """Test bubble_sort with a single element."""
    result = bubble_sort([1])
    assert result == [1]


def test_already_sorted():
    """Test bubble_sort with an already sorted list (early exit optimization)."""
    result = bubble_sort([1, 2, 3])
    assert result == [1, 2, 3]


def test_reverse_sorted():
    """Test bubble_sort with a reverse-sorted list (worst case)."""
    result = bubble_sort([3, 2, 1])
    assert result == [1, 2, 3]


def test_with_duplicates():
    """Test bubble_sort with duplicate elements."""
    result = bubble_sort([2, 1, 2, 1])
    assert result == [1, 1, 2, 2]

