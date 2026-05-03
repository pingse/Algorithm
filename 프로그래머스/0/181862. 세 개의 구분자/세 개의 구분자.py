import re

def solution(myStr):
    answer = []
    myStr = myStr.replace('a', ' ')
    myStr = myStr.replace('b', ' ')
    myStr = myStr.replace('c', ' ')
    
    myStr.strip()
    
    answer = myStr.split()
    
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer