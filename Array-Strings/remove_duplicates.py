lst = [2,4,5,6,7,2]
print(list(dict.fromkeys(lst)))


lst1 = [10,10,22,2]
result = []
for num in lst1:
    if num not in result:
        result.append(num)
print(result)

