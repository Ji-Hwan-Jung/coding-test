def solution(s: str):
    s = s.lower()
    return s.count('p') == s.count('y')

print(f'test1 = {solution("pPoooyY")}')
print(f'test2 = {solution("Pyy")}')