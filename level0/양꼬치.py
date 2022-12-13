def solution(n, k):
    return (6*n+k-n//10)*2000

print(f'test1 = {solution(10, 3)}')
print(f'test2 = {solution(64, 6)}')