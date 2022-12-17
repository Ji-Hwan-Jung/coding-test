def solution(sides):
    sides.sort()
    
    if sides[2] < sides[0]+sides[1]:
        return 1
    else:
        return 2
    
print(f'test1 = {solution([1,2,3])}')
print(f'test2 = {solution([3,6,2])}')
print(f'test3 = {solution([199,72,222])}')