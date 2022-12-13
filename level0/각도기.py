def solution(angle):
    if 0<angle<90:
        return 1
    elif angle==90:
        return 2
    elif 90<angle<180:
        return 3
    else:
        return 4
    
print(f'test1 = {solution(70)}')
print(f'test2 = {solution(91)}')
print(f'test3 = {solution(180)}')