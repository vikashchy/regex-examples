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
teststr = "Take one idea. One at a time"
regresult = re.search(r'[O]\w', teststr)
print(regresult.group())   # group function fails if none is returned

# findall	Returns a list containing all matches
regresult = re.findall(r'o\w', teststr)
print(regresult)

regresult = re.match(r'T\w', teststr)
print(regresult)

teststr = "Take one1  idea3. One at4 a time"
regresult = re.findall(r'O\w+', teststr)
print(regresult)

regresult = re.findall(r'O\w*', teststr)
print(regresult)

regresult = re.findall(r'O\w?', teststr)
print(regresult)

regresult = re.findall(r'O\w{2}', teststr)
print(regresult)

''' Splitting a string '''
# split	    Returns a list where the string has been split at each match
teststr = "Take one1  idea3. One at4 a time"
regresult = re.split(r'\d+', teststr)
print(regresult)

'''Substituting a string'''
# sub	    Replaces one or many matches with a string
teststr = "Take one1  idea3. One at4 a time"
regresult = re.sub(r'[o,O]ne', 'Two', teststr)
print(regresult)



