def solution(str1, str2):
    str1,str2 = str1.lower(),str2.lower()
    
    list1 = list(filter(lambda x: x.isalpha(),[str1[i:i+2] for i in range(len(str1)-1)]))
    list2 = list(filter(lambda x: x.isalpha(),[str2[i:i+2] for i in range(len(str2)-1)]))
    
    dict1 = {i: 0 for i in set(list1)}
    dict2 = {i: 0 for i in set(list2)}
    
    for i in list1:
        dict1[i] += 1
    for i in list2:
        dict2[i] += 1
            
    temp = set(list1)&set(list2)
    
    intersection = {i: min(dict1[i],dict2[i]) for i in temp}
    union = {i: max(dict1[i],dict2[i]) for i in temp}
    
    for k,v in dict1.items():
        if k not in union.keys():
            union[k] = v
    for k,v in dict2.items():
        if k not in union.keys():
            union[k] = v
            
    s1 = sum(intersection.values())
    s2 = sum(union.values())
    j = 1 if s1 == 0 or s2 == 0 else s1/s2
    
    return int(j*65536)

print(f'test1 = {solution("FRANCE","french")}')
print(f'test2 = {solution("handshake","shake hands")}')
print(f'test3 = {solution("aa1+aa2","AAAA12")}')
print(f'test4 = {solution("E=M*C^2","e=m*c^2")}')