def solution(n):
    return (n**0.5+1)**2 if (n**0.5)**2==n else -1

print(f'test1 = {solution(121)}')
print(f'test2 = {solution(3)}')