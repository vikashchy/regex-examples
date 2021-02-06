import re

teststr = '6234597890'
regresult = re.findall(r'\b^[789]\d{9}\b', teststr)
print(regresult)

teststr = "This is generated on 01/5-11. Executed on 05-05-2018. My phone no :963 222.4597"
regresult = re.findall(r'\d{1,2}-\d{1,2}-\d{1,2}', teststr)
print(regresult)
regresult = re.findall(r'\d{1,2}[-,/]\d{1,2}[-,/]\d{2,4}', teststr)
print(regresult)

regresult = re.findall(r'\d{3}[-/. ]\d{3}[-/. ]\d{4}', teststr)
for result in regresult:
    phone = re.sub(r'[., ]', '-', result)
    print(phone)
