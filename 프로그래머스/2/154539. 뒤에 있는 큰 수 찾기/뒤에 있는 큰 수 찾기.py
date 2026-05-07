def solution(numbers):
    answer = []
    stack = []
    stack.append(numbers[len(numbers)-1])
    answer.append(-1)
    
    for i in range(len(numbers)-2, -1, -1):
        while len(stack) != 0 and numbers[i] >= stack[-1]:
            stack.pop()
        
        answer.append(stack[-1] if len(stack) != 0 else -1)
        
        stack.append(numbers[i])
        
    answer.reverse()
        
    return answer