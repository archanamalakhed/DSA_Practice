def remove_duplicate_from_sorted_arry(nums):
    if not nums:
        return 0
    j = 1 # pointer for new unique number
    for i in range(1,len(nums)):
        if nums[i] !=nums[i-1]:
            nums[j] = nums[i]
            j+=1
    return j
nums = [1,1,2,2,4,5,6,6]
print(remove_duplicate_from_sorted_arry(nums))