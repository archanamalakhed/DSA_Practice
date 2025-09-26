def remove_duplicates(nums):
    if not nums:
        return 0
    
    # Pointer for the position of the next unique element
    i = 0
    
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    
    return i + 1


# Example usage:
arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
arr1 = [2,2,2]
new_length = remove_duplicates(arr)
new_length1 = remove_duplicates(arr1)
print("New length:", new_length)
print("Array after removing duplicates:", arr[:new_length])
print("New length1:", new_length1)
print("Array after removing duplicates:", arr1[:new_length1])
