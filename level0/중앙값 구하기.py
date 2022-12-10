def solution(array):
    return sorted(array)[len(array)//2]

test1 = solution([1,2,7,10,11])
test2 = solution([9,-1,0])

print(f'test1 = {test1}')
print(f'test2 = {test2}')