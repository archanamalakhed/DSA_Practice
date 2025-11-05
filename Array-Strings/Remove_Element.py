def remove_element(nums,val):
    j = 0
    for i in range(len(nums)):
        if nums[i]!=val:
         nums[j] = nums[i]
         j+=1
    return j
nums = [3,2,2,4,3,5]
val = 3
print(remove_element(nums,val))