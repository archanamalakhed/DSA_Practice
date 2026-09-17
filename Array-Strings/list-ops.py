a = [1,2,4,6]
b = a
a.remove(6)
print(b)
c = [1,2,4]
d = ["a","b","c"]

pairs = [[number, letter] for number, letter in zip(c, d)]
print(pairs)
