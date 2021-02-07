import re

"""Find a string where there is space character \b around the word, beginning with 7,8 or 9 followed by 9 digits"""
test_str = 'call me  at 8234597890 or 9780948489'
regex_pattern = re.compile(r'\b[789]\d{9}\b')
reg_result = regex_pattern.search(test_str)
print(reg_result.group() if reg_result else "No match found")    # this returns the first occurrence of the string
reg_result = re.findall(r'\b[789]\d{9}\b', test_str)  # returns a list of all occurrences
print(reg_result)

test_str = "This is generated on 01/5-11. Executed on 05-05-2018. My phone no :963 222.4597"
reg_result = re.findall(r'\d{1,2}-\d{1,2}-\d{1,2}', test_str)
print(reg_result)
reg_result = re.findall(r'\d{1,2}[-,/]\d{1,2}[-,/]\d{2,4}', test_str)
print(reg_result)

""" Find a pattern matching 3 digits followed by -,/or. then again 3 digits and last 4 digits and substitute 
it with a -"""
reg_result = re.findall(r'\d{3}[-/. ]\d{3}[-/. ]\d{4}', test_str)
for result in reg_result:
    phone = re.sub(r'[., ]', '-', result)
    print(phone)
