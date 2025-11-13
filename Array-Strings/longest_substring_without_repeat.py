def lengthoflongestsubstring(s):
    i = 0
    seen = set()
    max_length = 0

    for j in range(len(s)):
        while s[j] in seen:
            seen.remove(s[i]) #  if duplicate, shrink from left
            i +=1
        seen.add(s[j]) # add new unique char
        max_length = max(max_length,j-i+1)
    return max_length
s = "abcabccc"
print(lengthoflongestsubstring(s))