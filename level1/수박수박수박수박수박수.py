def solution(n):
    return ''.join(['수' if not i%2 else '박' for i in range(n)])

print(f'test1 = {solution(3)}')
print(f'test2 = {solution(4)}')