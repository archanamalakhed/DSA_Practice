def rotate_array(arr,k):
    rotated_array= arr[-k:]+ arr[:-k]
    return rotated_array
arr = [1,2,3,4,5,6,7]
print(rotate_array(arr,3))


def rotate(nums, k):
    n = len(nums)
    k = k % n  # handle k > n

    # Helper function to reverse a segment in-place
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(0, n-1)

    # Step 2: Reverse first k elements
    reverse(0, k-1)

    # Step 3: Reverse remaining n-k elements
    reverse(k, n-1)

# Example usage
nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)  # Output: [5,6,7,1,2,3,4]
