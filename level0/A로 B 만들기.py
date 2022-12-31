def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0

print(f'test1 = {solution("olleh", "hello")}')
print(f'test2 = {solution("allpe", "apple")}')