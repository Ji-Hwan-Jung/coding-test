def solution(arr, divisor):
    arr = sorted(list(filter(lambda x: x%divisor == 0,arr)))
    return arr if len(arr) != 0 else [-1]

print(f'test1 = {solution([5,9,7,10],5)}')
print(f'test2 = {solution([2,36,1,3],1)}')
print(f'test3 = {solution([3,2,6],10)}')