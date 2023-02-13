def solution(k, tangerine):
    cot = {x: 0 for x in set(tangerine)}
    answer = []
    temp = 0
    
    for i in tangerine:
        cot[i] += 1
        
    for n,m in sorted(cot.items(),key=lambda x: x[1],reverse=True):
        temp += m
        answer.append(n)
        if temp>=k:
            return len(answer)
        
print(f'test1 = {solution(6,[1,3,2,5,4,5,2,3])}')
print(f'test2 = {solution(4,[1,3,2,5,4,5,2,3])}')
print(f'test1 = {solution(2,[1,1,1,1,2,2,2,3])}')