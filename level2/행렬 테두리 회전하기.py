def solution(rows, columns, queries):
    matrix = [[(r-1)*columns+c for c in range(1,columns+1)] for r in range(1,rows+1)]
    types = {'L': (0,-1), 'R': (0,1), 'D': (1,0), 'U': (-1,0)}
    result = []
    
    for x1,y1,x2,y2 in queries:
        mode = 'R'
        w,h = x2-x1+1, y2-y1+1
        cnt = w*h-((w-2)*(h-2))
        x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
        cur = (x1,y1)
        rotation = [matrix[x1][y1]]
        for _ in range(cnt):
            x,y = cur
            if y+types[mode][1] > y2:
                mode = 'D'
            elif x+types[mode][0] > x2:
                mode = 'L'
            elif y+types[mode][1] < y1:
                mode = 'U'

            nx,ny = x+types[mode][0], y+types[mode][1]
            cur = (nx,ny)
            rotation.append(matrix[nx][ny])
            temp, matrix[nx][ny] = matrix[nx][ny], rotation[-2]
        
        result.append(min(rotation))
        
    return result

print(f'test1 = {solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])}')
print(f'test2 = {solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])}')
print(f'test3 = {solution(100,97,[[1,1,100,97]])}')