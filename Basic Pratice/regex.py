import re
text = "User123 logged in at 10:45am"
print(re.findall(r'\d+',text))

string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""
            
regex = r'\d+'
match = re.findall(regex, string)
print(match)




text1 = "User123 logged in at 10:45am and 10:45am logged out at 07:30 PM."

pattern = r'\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)'
matches = re.findall(pattern, text1)
print(matches)

txt = "Order IDs are 123, 456 and 7890."
match = r'\d+' # extract all numbers
print(re.findall(match,txt))

txt_2 = "Hello Archana, welcome to Bosch!"
match = r'\w+'
print(re.findall(match,txt_2))

txt_3="Archana met Akarsh and went to bosch."
match = r'\b[A-Z][a-z]*\b'
print(re.findall(match,txt_3))

