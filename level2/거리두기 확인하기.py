def solution(places):
    result = []
    
    for i in range(5):
        flag = 1
        for j in range(5):
            for k in range(5):
                temp = []
                seat = places[i][j][k]
                if seat == 'P':
                    for nx,ny in [(j-1,k),(j,k-1),(j+1,k),(j,k+1)]:
                        if 0<=nx<5 and 0<=ny<5:
                            temp.append(places[i][nx][ny])
                    if temp.count('P') > 0:
                        flag = 0
                elif seat == 'O':
                    for nx,ny in [(j-1,k),(j,k-1),(j+1,k),(j,k+1)]:
                        if 0<=nx<5 and 0<=ny<5:
                            temp.append(places[i][nx][ny])
                    if temp.count('P') > 1:
                        flag = 0
        
        result.append(flag)
            
    return result

print(f'test1 = {solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])}')