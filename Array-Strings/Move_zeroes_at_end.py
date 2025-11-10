def moveZeroes(nums):
    j = 0  # position for next non-zero element

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums
nums = [1,20,0,0,0,3,4,5]
print(moveZeroes(nums))