def solution(t, p):
    result = 0
    
    for i in range(len(t)-len(p)+1):
        if t[i:i+len(p)] <= p:
            result += 1
    
    return result

print(f'test1 = {solution("3141592","271")}')
print(f'test2 = {solution("500220839878","7")}')
print(f'test3 = {solution("10203","15")}')