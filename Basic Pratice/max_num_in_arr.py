def max_num_in_array(arr):
    max_arr = arr[0]
    for num in arr:
        if num > max_arr:
            max_arr = num
    return max_arr
arr = [12,44,51,1,2,81]
print(max_num_in_array(arr))

def reverse_string(s):
    rev_str = ''
    for char in s:
        rev_str = char+rev_str
    if s == rev_str:
        return "Yes, it is palindrome"
    else:
        return 'No'
s = input("Enter a string to check palindrome: ")
print(reverse_string(s))