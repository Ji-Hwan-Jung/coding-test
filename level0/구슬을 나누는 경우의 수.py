from math import comb

def solution(balls, share):
    return comb(balls,share)

print(f'test1 = {solution(3,2)}')
print(f'test2 = {solution(5,3)}')