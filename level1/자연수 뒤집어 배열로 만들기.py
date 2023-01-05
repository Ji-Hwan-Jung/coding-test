def solution(n):
    return [int(s) for s in str(n)][::-1]

print(f'test1 = {solution(12345)}')
