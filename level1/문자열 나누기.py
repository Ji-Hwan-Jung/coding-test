def solution(s):
    first = ''
    first_cnt = 0
    another_cnt = 0
    result = 0
    
    for i in s:
        if first_cnt == 0:
            first = i
            
        if first == i: first_cnt += 1
        else: another_cnt += 1
        
        if first_cnt == another_cnt:
            result += 1
            first_cnt = 0
            another_cnt = 0
    return result if first_cnt == 0 else result+1

print(f'test1 = {solution("banana")}')
print(f'test2 = {solution("abracadabra")}')
print(f'test3 = {solution("aaabbaccccabba")}')