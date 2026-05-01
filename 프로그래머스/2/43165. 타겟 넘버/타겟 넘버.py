answer = 0

def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer

def dfs(start, num, numbers, target):
    global answer
    
    if len(numbers) == start:
        if num == target:
            answer+=1
        return
    
    dfs(start+1, num + numbers[start], numbers, target)
    dfs(start+1, num - numbers[start], numbers, target)
            