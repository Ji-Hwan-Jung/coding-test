def solution(my_string):
    return ''.join(sorted(my_string.lower()))

print(f'test1 = {solution("Bcad")}')
print(f'test2 = {solution("heLLo")}')
print(f'test3 = {solution("Python")}')