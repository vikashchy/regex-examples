import re

""" Get the area code from the phone number"""

text = "my phone number is: 963-221-1633"
phone_no_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # group the patterns inside parentheses
match_object = phone_no_regex.search(text)
print(match_object.group(0))   # this will return the whole string
print(match_object.group(1))   # this will return the first match
print(match_object.group(2))   # this will return the second match


text = "my phone number is: (963)-221-1633"
phone_no_regex = re.compile(r'\(\d\d\d\)-(\d\d\d-\d\d\d\d)')  # group the patterns inside parentheses
match_object = phone_no_regex.search(text)
print(match_object.group(0))   # this will return the whole string
print(match_object.group(1))   # this will return the first match
