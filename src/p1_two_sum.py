def two_sum_1(nums, target): # 1
    """Brute force solution - O(n²) time, O(1) space"""
    n = len(nums)
    for i in range(n):
        r = target - nums[i]
        for j in range(i+1, n):
            if r == nums[j]:
                return [i, j]
    return []


def two_sum(nums, target): # 2
    """Hash table solution - O(n) time, O(n) space"""
    d = {}  # map value to index
    for i, num in enumerate(nums):
        r = target - num
        if r in d:
            return [d[r], i]
        d[num] = i
    return []    
