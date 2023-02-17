import copy

def del_block(m, n, board):
    board = list(map(list,board))
    block = set()
    for i in range(1,m-1):
        for j in range(1,n-1):
            if board[i-1][j-1] == board[i][j] and board[i-1][j] == board[i][j] and board[i][j-1] == board[i][j]:
                block.add((i,j))
                block.add((i-1,j-1))
                block.add((i-1,j))
                block.add((i,j-1))
            if board[i-1][j] == board[i][j] and board[i-1][j+1] == board[i][j] and board[i][j+1] == board[i][j]:
                block.add((i,j))
                block.add((i-1,j))
                block.add((i-1,j+1))
                block.add((i,j+1))
            if board[i][j-1] == board[i][j] and board[i+1][j-1] == board[i][j] and board[i+1][j] == board[i][j]:
                block.add((i,j))
                block.add((i,j-1))
                block.add((i+1,j-1))
                block.add((i+1,j))
            if board[i][j+1] == board[i][j] and board[i+1][j+1] == board[i][j] and board[i+1][j] == board[i][j]:
                block.add((i,j))
                block.add((i,j+1))
                block.add((i+1,j+1))
                block.add((i+1,j))

    for e in block:
        board[e[0]][e[1]] = "0"
        
    board = [[board[i][j] for i in range(m) if board[i][j] != "0"] for j in range(n)]
    
    for i,v in enumerate(board):
        board[i] = ["0"]*(m-len(v)) + v
        
    board = [[board[i][j] for i in range(n)] for j in range(m)]
        
    return list(map(lambda x: ''.join(x),board))
            
def solution(m, n, board):
    board_cp = copy.deepcopy(board)
    
    while True:
        temp = del_block(m,n,board_cp)
        if board_cp == temp:
            break
        else:
            board_cp = temp
    
    answer = list(map(lambda x: x.count('0'), board_cp))
    
    return sum(answer)

print(f'test1 = {solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])}')
print(f'test2 = {solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])}')