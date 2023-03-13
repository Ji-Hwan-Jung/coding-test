def solution(maps):
    result = []
    lands = []
    queue = []
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                lands.append([i,j])
    
    if not lands:
        return [-1]
    
    for l,k in lands:
        provision = 0
        if not visited[l][k]:
            queue.append([l,k])
            provision += int(maps[l][k])
            visited[l][k] = True
            while queue:
                a,b = queue.pop(0)
                for nx,ny in [(a-1,b),(a,b-1),(a+1,b),(a,b+1)]:
                    if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
                        queue.append([nx,ny])
                        provision += int(maps[nx][ny])
                        visited[nx][ny] = True
        else:
            continue
            
        result.append(provision)

    return sorted(result)

print(f'test1 = {solution(["X591X","X1X5X","X231X", "1XXX1"])}')
print(f'test2 = {solution(["XXX","XXX","XXX"])}')