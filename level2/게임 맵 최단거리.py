def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    queue = [(0,0)]
    d = {(0,0): 1}
    
    while len(queue) > 0:
        x,y = queue.pop(0)
        if x==n-1 and y==m-1:
            return d[(x,y)]
        for i,j in [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]:
            if 0<=i<n and 0<=j<m and visited[i][j] == False and maps[i][j] == 1:
                queue.append((i,j))
                d[(i,j)] = d[(x,y)] + 1
                visited[i][j] = True
        
    return -1

print(f'test1 = {solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])}')
print(f'test2 = {solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])}')