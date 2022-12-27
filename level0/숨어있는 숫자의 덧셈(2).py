def solution(my_string):
    s = ''.join([i if i.isdigit() else ' ' for i in my_string]).split()
    return sum(map(int,s))
    
print(f'test1 = {solution("aAb1B2cC34oOp")}')
print(f'test2 = {solution("1a2b3c4d123Z")}')