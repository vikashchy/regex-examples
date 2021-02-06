import re
sent = "We give coders a try . We are hero!"
def solution(S):
    # write your code in Python 3.6
    senlist = re.split("\\.|\\!\\?",S)
    maxlen = 0
    lenh = []
    for sen in senlist:
        lenght= sen.strip().split(' ')
        print(lenght)
        a = len(lenght)
        print(a)

solution(sent)