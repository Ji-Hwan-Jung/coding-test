def solution(s):
    arr = sorted(s[2:len(s)-2].split('},{'),key=lambda x: len(x))
    arr = list(map(set,map(lambda x: x.split(','),arr)))
    temp = set()
    result = list()
    
    for i in arr:
        result.append(int(*(i-temp)))
        temp = i
    
    return result
    
print(f'test1 = {solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")}')
print(f'test2 = {solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")}')
print(f'test3 = {solution("{{20,111},{111}}")}')
print(f'test4 = {solution("{{123}}")}')
print(f'test5 = {solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")}')