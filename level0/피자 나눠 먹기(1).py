import math

def solution1(n):
    return math.ceil(n/7)

def solution2(n):
    return (n-1)//7 + 1

print(f'test1 = {solution1(7)}')
print(f'test2 = {solution2(15)}')