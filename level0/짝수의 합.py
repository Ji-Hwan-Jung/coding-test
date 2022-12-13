def solution(n):
    return sum([i for i in range(2,n+1,2)])

print(f'test1 = {solution(10)}')
print(f'test2 = {solution(4)}')