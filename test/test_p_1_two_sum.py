"""
Test cases for LeetCode 1: Two Sum
"""
import pytest
from p_1_two_sum import two_sum


@pytest.mark.leetcode
def test_two_sum_case1():
    """Test case 1: normal case"""
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]


@pytest.mark.leetcode
def test_two_sum_case2():
    """Test case 2: different target"""
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]


@pytest.mark.leetcode
def test_two_sum_case3():
    """Test case 3: same elements"""
    assert sorted(two_sum([3, 3], 6)) == [0, 1]


@pytest.mark.leetcode
def test_two_sum_no_solution():
    """Test case: no valid solution"""
    assert two_sum([1, 2, 3], 7) == []
