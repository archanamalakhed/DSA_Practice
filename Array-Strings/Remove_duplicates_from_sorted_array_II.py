def removeDuplicates(nums):
    nums.sort() 
    if len(nums) <= 2:
        return len(nums)
    
    j = 2 #   start writing valid elements from index 2 as first two elements are valid 
    for i in range(2, len(nums)):
        if nums[i] != nums[j - 2]:
            nums[j] = nums[i]
            j += 1
    return j
nums = [1,5, 2,1, 2, 3]
print(removeDuplicates(nums))   # Output: 5
