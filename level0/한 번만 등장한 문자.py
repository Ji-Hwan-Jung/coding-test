def solution(s):
    return ''.join(sorted([c for c in set(s) if s.count(c)==1]))

print(f'test1 = {solution("abcabcadc")}')
print(f'test2 = {solution("abdc")}')
print(f'test3 = {solution("hello")}')