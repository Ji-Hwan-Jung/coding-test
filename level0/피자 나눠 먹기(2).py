import math

# math 모듈 사용
def solution1(n):
    return (n*6)//math.gcd(n,6)//6

# 모듈 사용 X
def solution2(n):
    gcd = 0
    for i in range(6,0,-1):
        if n%i == 0 and 6%i == 0:
            gcd = i
            break
    
    return (n*6)//gcd//6

print(f'test1 = {solution1(10)}')
print(f'test2 = {solution2(4)}')