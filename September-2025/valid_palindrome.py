def valid_palindrome(str):
   
    cleaned_str = ''.join(char for char in str if char.isalnum())
    cleaned_str = cleaned_str.lower()
    if cleaned_str == cleaned_str[::-1]:
        return True
    else:
        return False
    
print(valid_palindrome("ARE  ,  ! era"))
print(valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(valid_palindrome("race a car"))                       # False
print(valid_palindrome(" "))  