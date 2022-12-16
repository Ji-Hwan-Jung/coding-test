def solution(my_string):
    return sorted([int(s) for s in my_string if s.isdecimal()])

print(f'test1 = {solution("hi12392")}')
print(f'test2 = {solution("p2o4i8gj2")}')
print(f'test3 = {solution("abcde0")}')