def isParallel(a,b,c,d):
    gN = (a[1]-b[1])/(a[0]-b[0])
    gM = (c[1]-d[1])/(c[0]-d[0])
    
    if a[0]==b[0]:
        gN = 1
    elif a[1]==b[1]:
        gN = 0
    
    if c[0]==d[0]:
        gM = 1
    elif c[1]==d[1]:
        gM = 0
    
    return gN == gM

def solution(dots):
    a,b,c,d = dots
    return int(isParallel(a,b,c,d) or isParallel(a,c,b,d) or isParallel(a,d,b,c))

print(f'test1 = {solution([[1, 4], [9, 2], [3, 8], [11, 6]])}')
print(f'test2 = {solution([[3, 5], [4, 1], [2, 4], [5, 10]])}')