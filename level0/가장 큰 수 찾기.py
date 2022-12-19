def solution(array):
    return [max(array), array.index(max(array))]

print(f'test1 = {solution([1,8,3])}')
print(f'test2 = {solution([9,10,11,8])}')