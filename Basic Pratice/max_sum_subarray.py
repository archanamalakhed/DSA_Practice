def max_sum(arr,k):
    max_sum = current_sum = sum(arr[:k]) # sum of first window
    for i in range(k, len(arr)):
        current_sum +=arr[i]-arr[i-k]
        max_sum = max(max_sum,current_sum)
    return max_sum
arr = [1,2,3,4,5,6]
k = 3
print(max_sum(arr,k))


