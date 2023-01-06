def solution(n):
    return int(''.join(sorted(str(n),reverse=True)))

print(f'test1 = {solution(118372)}')