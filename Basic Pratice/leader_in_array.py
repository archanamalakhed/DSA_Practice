def get_leader_in_array(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] <arr[j]:
                break
        else:
                res.append(arr[i])
    return res
arr = [16, 17, 4, 3]
res = get_leader_in_array(arr)
print(" ".join(map(str,res)))
