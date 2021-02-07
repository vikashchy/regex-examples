import re

"""Find the matches where the string starts with Bat and ends with this following."""
text = "In this sentence we will find Batman or BatMobile or Batbat"
regex_expression = re.compile(r'Bat(man|copter|mobile|bat)')
match_object = regex_expression.search(text)
print(match_object.group())
print(match_object.groups()) # return the tuple of groups which were found

