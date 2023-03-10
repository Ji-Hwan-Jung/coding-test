def solution(board):
    dp = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]
    result = 0
    
    for i in range(1, len(board)+1):
        for j in range(1, len(board[0])+1):
            if board[i-1][j-1]:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                if dp[i][j] > result:
                    result = dp[i][j]
                    
    return result**2

print(f'test1 = {solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])}')
print(f'test2 = {solution([[0,0,1,1],[1,1,1,1]])}')