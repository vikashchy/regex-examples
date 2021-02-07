import re
import os
import sys

text = open(os.path.join(sys.path[0], "data/example2.txt"), "r", encoding='utf-8').read()
# print(text)
# find all the years from the text
match_regex = re.compile(r'\d{4}')  # here it returns a list for the matches
print(match_regex.findall(text))
match_regex = re.compile(r'(\d{2})(\d\d)')  # here it returns a list of tuples for the group for matches
print(match_regex.findall(text))

""" find all matches which has a numeric value followed by  a space and words"""
match_regex=re.compile(r'\d+\s\w+')
print(match_regex.findall(text))

""" Find all words starting with vowels"""
match_regex=re.compile(r'^[aeiouAEIOU]\w+')
print(match_regex.findall(text))