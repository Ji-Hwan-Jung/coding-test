def solution(dirs):
    c = (0,0)
    d = {"U": (0,1), "D": (0,-1), "L": (-1,0), "R": (1,0)}
    square = 5
    route = []
    
    for i in dirs:
        dx = c[0]+d[i][0]
        dy = c[1]+d[i][1]
        
        if abs(dx) > square or abs(dy) > square:
            continue
        else:
            temp = (dx,dy)
            r = [c]
            r.append(temp)
            r.sort()
            c = temp
            route.append(tuple(r))
        
    return len(set(route))

print(f'test1 = {solution("ULURRDLLU")}')
print(f'test2 = {solution("LULLLLLLU")}')