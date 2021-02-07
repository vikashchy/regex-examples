import re

text = "he said hahaha"
regex_expression = re.compile(r'(ha){3}')
match = regex_expression.search(text)
print(match.group())

regex_expression = re.compile(r'(ha){3,}')  # 3 or more
match = regex_expression.search(text)
print(match.group())

regex_expression = re.compile(r'(ha){3,5}')  # 3 or 5 occurrence of ha
match = regex_expression.search(text)
print(match.group())

""" By default regex in python does a greedy match i.e. it will try finding as 
long as possible but if the requirement is to have non greedy match ? should be specified"""
text = '123456789'
regex_expression = re.compile(r'(\d){3,5}')  # 3 or 5 occurrence of ha
match = regex_expression.search(text)
print(match.group())
print(match)  # this has the biggest string possible after match

regex_expression = re.compile(r'(\d){3,5}?')  # 3 or 5 occurrence of ha
match = regex_expression.search(text)
print(match.group())
print(match)  # this has the shortest possible match


