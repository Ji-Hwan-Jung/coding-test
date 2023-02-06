import math

def solution(n):
    total = 0
    for i,e in enumerate(range(n,(n-1)//2-1,-1)):
        total += math.comb(e,i)
        
    return total%1234567

print(f'test1 = {solution(4)}')
print(f'test2 = {solution(3)}')