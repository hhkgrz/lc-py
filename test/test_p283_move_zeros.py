"""
Test cases for p283_move_zeros.py
"""
import pytest
from src.p283_move_zeros import move_zeros


def test_move_zeros_basic():
    """Test basic case with zeros and non-zeros"""

    nums = [0, 1, 0, 3, 12]
    move_zeros(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_move_zeros_all_zeros():
    """Test case with all zeros"""

    nums = [0, 0, 0]
    move_zeros(nums)
    assert nums == [0, 0, 0]


def test_move_zeros_no_zeros():
    """Test case with no zeros"""

    nums = [1, 2, 3]
    move_zeros(nums)
    assert nums == [1, 2, 3]


def test_move_zeros_empty():
    """Test case with empty list"""

    nums = []
    move_zeros(nums)
    assert nums == []


def test_move_zeros_single_element():
    """Test case with single element"""

    # Single zero
    nums1 = [0]
    move_zeros(nums1)
    assert nums1 == [0]

    # Single non-zero
    nums2 = [5]
    move_zeros(nums2)
    assert nums2 == [5]


def test_move_zeros_zeros_at_end():
    """Test case with zeros already at the end"""

    nums = [1, 2, 3, 0, 0]
    move_zeros(nums)
    assert nums == [1, 2, 3, 0, 0]


def test_move_zeros_alternating():
    """Test case with alternating zeros and non-zeros"""

    nums = [0, 1, 0, 2, 0, 3]
    move_zeros(nums)
    assert nums == [1, 2, 3, 0, 0, 0]
