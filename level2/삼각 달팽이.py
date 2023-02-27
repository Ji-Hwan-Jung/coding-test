def cnt(n):
    a = 0
    for i in range(1,n+1):
        a += i
    return a

def solution(n):
    arr = [[0]*n for i in range(n)]
    result = []
    d = {"U": (-1,-1), "D": (1,0), "R": (0,1)}
    cur = (0,0)
    mode = "D"

    for i in range(1,cnt(n)+1):
        x,y = cur
        arr[x][y] = i
        dx,dy = x+d[mode][0],y+d[mode][1]
        if mode == "D":
            if n in (dx,dy):
                mode = "R"
            elif arr[dx][dy] != 0:
                mode = "R"
        elif mode == "R":
            if n in (dx,dy):
                mode = "U"
            elif arr[dx][dy] != 0:
                mode = "U"
        elif mode == "U":
            if n in (dx,dy):
                mode = "D"
            elif arr[dx][dy] != 0:
                mode = "D"
        cur = (x+d[mode][0],y+d[mode][1])

    for i in arr:
        for j in i:
            if j != 0:
                result.append(j)

    return result

print(f'test1 = {solution(4)}')
print(f'test2 = {solution(5)}')
print(f'test3 = {solution(6)}')