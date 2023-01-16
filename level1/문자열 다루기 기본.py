def solution(s):
    return len(s) in (4,6) and s.isdigit()

print(f'test1 = {solution("a234")}')
print(f'test2 = {solution("1234")}')