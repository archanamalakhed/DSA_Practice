def majority_element(arr):
    count_map = {} ## dictionary to store counts
    n = len(arr)//2  
    for i in arr:
        # increase count each time we see the number
        count_map[i] =count_map.get(0,i)+1
         # if count crosses half the length, it's majority
        if count_map[i] > n // 2:
            return i
nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]

print(majority_element(nums1))  # Output: 3
print(majority_element(nums2))  # Output: 2

#Optimal — Boyer-Moore Voting Algorithm
#---------------------------------------------------------------------
#We keep a count and a candidate:
#When count = 0 → choose a new candidate.
#When element = candidate → increase count.
#Else → decrease count.
#__________________________________________________________________________

def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
nums1 = [3, 2, 3]
nums2 = [2, 2, 1, 1, 1, 2, 2]
print("From Boyer and Moore")
print(majorityElement(nums1))
print(majorityElement(nums2))

