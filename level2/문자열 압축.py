def solution(s):
    result = []
    
    if len(s) == 1:
        return 1
    
    for i in range(1,len(s)//2+1):
        comp = []
        for j in range(0,len(s),i):
            if not comp:
                comp.append(1)
                comp.append(s[j:j+i])
            elif comp[-1] == s[j:j+i]:
                comp[-2] += 1
            else:
                comp.append(1)
                comp.append(s[j:j+i])
        
        result.append(''.join(list(map(lambda x: str(x),filter(lambda x: x != 1,comp)))))
        
    return min(list(map(lambda x: len(x),result)))

print(f'test1 = {solution("aabbaccc")}')
print(f'test2 = {solution("ababcdcdababcdcd")}')
print(f'test3 = {solution("abcabcdede")}')
print(f'test4 = {solution("abcabcabcabcdededededede")}')
print(f'test5 = {solution("xababcdcdababcdcd")}')