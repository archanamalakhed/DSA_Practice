def getalternative(arr):
    n = len(arr)
    res = []
    for i in range(0, n, 2):
        res.append(arr[i])
    return res
arr = [10,20,30,40,50]
print(getalternative(arr))
