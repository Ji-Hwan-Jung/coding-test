def solution(s):
    if len(s)%2 == 0:
        return s[len(s)//2-1:len(s)//2+1]
    else:
        return s[len(s)//2]
    
print(f'test1 = {solution("abcde")}')
print(f'test2 = {solution("qwer")}')