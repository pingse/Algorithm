from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((0, 0, 1))
    
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        y, x, dist = queue.popleft()
        
        if y == n-1 and x == m-1:
            return dist
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            
            if maps[ny][nx] == 0 or visited[ny][nx]:
                continue
            
            visited[ny][nx] = True
            queue.append((ny, nx, dist+1))
    
    return -1