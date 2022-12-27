def solution(board):
    danger_pos = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    danger = set()
    safe = set()
    mine = set()
    
    for i in range(len(board)):
        for j in range(len(board)):
            mine.add((i,j)) if board[i][j] == 1 else safe.add((i,j))
            
    for nx,ny in mine:
        for mx,my in danger_pos:
            danger.add((nx+mx, ny+my))
    
    return len(safe-danger-mine)

print(f'test1 = {solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])}')
print(f'test2 = {solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]])}')
print(f'test3 = {solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])}')