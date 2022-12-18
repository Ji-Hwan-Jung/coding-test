def solution(n):
    return [i for i in range(1,n+1) if n%i==0]

print(f'test1 = {solution(24)}')
print(f'test2 = {solution(29)}')