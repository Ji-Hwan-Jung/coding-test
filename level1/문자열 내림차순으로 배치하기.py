def solution(s):
    return ''.join(sorted(s, reverse=True))

print(f'test1 = {solution("Zbcdefg")}')