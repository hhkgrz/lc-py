def move_zeros(nums): # 1
    n = len(nums)
    left = 0
    for right in range(n):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
