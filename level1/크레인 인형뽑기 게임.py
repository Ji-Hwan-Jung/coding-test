def solution(board, moves):
    result = []
    cnt = 0
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if len(result) > 0 and result[-1] == board[j][i-1]:
                    result.pop()
                    cnt += 1
                else:
                    result.append(board[j][i-1])
                board[j][i-1] = 0
                break
                    
    return cnt*2

print(f'test1 = {solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])}')