from itertools import combinations as cb

def solution(orders, course):
    orders = list(map(lambda x: ''.join(sorted(x)),orders))
    result = []
    
    for i in course:
        comb = filter(lambda z: len(z)!=0,map(lambda x: list(map(lambda y: ''.join(y),cb(x,i))),orders))
        temp = []
        
        for j in comb:
            temp.extend(j)
        
        combs = {t: temp.count(t) for t in set(temp)}
        
        if temp:
            m = max(combs.values())
            hottest = list(filter(lambda x: combs[x] == m and combs[x] > 1,combs.keys()))
            for h in hottest:
                result.append(h)
    
    return sorted(result)

print(f'test1 = {solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])}')
print(f'test2 = {solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5])}')
print(f'test3 = {solution(["XYZ", "XWY", "WXA"],[2,3,4])}')