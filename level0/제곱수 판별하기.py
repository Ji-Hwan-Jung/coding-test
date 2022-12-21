def solution(n):
    return 1 if int(n**0.5)**2 == n else 2

print(f'test1 = {solution(144)}')
print(f'test2 = {solution(976)}')