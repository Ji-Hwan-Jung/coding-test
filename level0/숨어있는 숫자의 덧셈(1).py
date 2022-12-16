def solution(my_string):
    return sum([int(s) for s in my_string if s.isdecimal()])

print(f'test1 = {solution("aAb1B2cC34oOp")}')
print(f'test2 = {solution("1a2b3c4d123")}')