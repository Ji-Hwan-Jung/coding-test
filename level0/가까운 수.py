def solution(array, n):
    array.sort(key = lambda x: (abs(x-n), x-n))
    return array[0]

print(f'test1 = {solution([3,10,28],20)}')
print(f'test1 = {solution([10,11,12],13)}')