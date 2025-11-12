def first_occurance(haystack,needle):
    """
    This function takes two strings as input: 'haystack' and 'needle'.
    It returns the index of the first occurrence of 'needle' in 'haystack'.
    If 'needle' is not found, it returns -1.
    """
  
    # Step 1: check if needle is substring of haystack
    if needle in haystack:
        # Step 2: find the starting index of needle in haystack
        index = haystack.index(needle)
        return index
    else:
        return -1
       

print(first_occurance("sadbutsad", "sad"))  # Output: 0
print(first_occurance("leetcode", "leeto")) # Output: -1
    
    