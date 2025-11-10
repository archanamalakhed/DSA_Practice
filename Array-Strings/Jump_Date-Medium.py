def canJump(nums):
    max_reach = 0  # farthest index we can reach
    for i in range(len(nums)):
        if i > max_reach:
            return False  # we can’t move further
        max_reach = max(max_reach, i + nums[i])
    return True
nums = [2,3,1,1,4]
print(canJump(nums))