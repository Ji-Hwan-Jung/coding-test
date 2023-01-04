def solution(n):
    return n+1+sum([i for i in range(2,n) if n%i == 0])

print(f'test1 = {solution(12)}')
print(f'test2 = {solution(5)}')