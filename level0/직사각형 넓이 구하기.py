def solution(dots):
    w,h,p = 0,0,dots.pop()
    
    for dot in dots:
        if dot[0] == p[0]:
            w = abs(dot[1]-p[1])
        if dot[1] == p[1]:
            h = abs(dot[0]-p[0])

    return w*h

print(f'test1 = {solution([[1, 1], [2, 1], [2, 2], [1, 2]])}')
print(f'test2 = {solution([[-1, -1], [1, 1], [1, -1], [-1, 1]])}')