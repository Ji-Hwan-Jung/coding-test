def solution(hp):
    return hp//5 + (hp%5)//3 + (hp%5%3)

print(f'test1 = {solution(23)}')
print(f'test2 = {solution(24)}')