from math import gcd

def solution(a,b):
    denominator = b//gcd(a,b)
    
    while denominator != 1:
        if denominator%2 == 0:
            denominator //= 2
        elif denominator%5 == 0:
            denominator //= 5
        else:
            break
        
    return 2 if denominator != 1 else 1

print(f'test1 = {solution(7, 20)}')
print(f'test2 = {solution(11,22)}')
print(f'test3 = {solution(12,21)}')