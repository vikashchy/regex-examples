# search pattern , split, substitute etc

# \d -> Single character 0-9
# \D -> Non digic characer
# s  -> White space
# S  -> Non white space
# w  -> Any alphanumeric characet a-z
# W  -> Non alphanumeric word
# b  -> Space around words
# \A -> Match at the start of the string
# \Z -> Match at the end of the string.

# Quantifiers-> Multiple characters matching

# +     -> One or more repetition
# *     -> Zero or more
# ?     -> 0 or 1
# {m}   -> exactly m no of regular expression
# {m,n} -> minimum no of occurrences, n is the max no occurrences


import re
'''   Searching in a string'''
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	    Returns a list where the string has been split at each match
# sub	    Replaces one or many matches with a string


# search	Returns a Match object if there is a match anywhere in the string
test_str = "Take one idea. One at a time"
reg_result = re.search(r'[O]\w', test_str)
print(reg_result.group())   # group function fails if none is returned

# findall	Returns a list containing all matches
reg_result = re.findall(r'o\w', test_str)
print(reg_result)

reg_result = re.match(r'T\w', test_str)
print(reg_result)

test_str = "Take one1  idea3. One at4 a time"
reg_result = re.findall(r'O\w+', test_str)
print(reg_result)

reg_result = re.findall(r'O\w*', test_str)
print(reg_result)

reg_result = re.findall(r'O\w?', test_str)
print(reg_result)

reg_result = re.findall(r'O\w{2}', test_str)
print(reg_result)

''' Splitting a string '''
# split	    Returns a list where the string has been split at each match
test_str = "Take one1  idea3. One at4 a time"
reg_result = re.split(r'\d+', test_str)
print(reg_result)

'''Substituting a string'''
# sub	    Replaces one or many matches with a string
test_str = "Take one1  idea3. One at4 a time"
reg_result = re.sub(r'[o,O]ne', 'Two', test_str)
print(reg_result)



