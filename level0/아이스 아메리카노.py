def solution(money):
    return [money//5500, money%5500]

print(f'test1 = {solution(5500)}')
print(f'test2 = {solution(15000)}')