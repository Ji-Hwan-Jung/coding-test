def solution(x, n):
    return [x*i for i in range(1,n+1)]

print(f'test1 = {solution(2,5)}')
print(f'test2 = {solution(4,3)}')
print(f'test3 = {solution(-4,2)}')