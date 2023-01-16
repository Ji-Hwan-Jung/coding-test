def solution(price, money, count):
    result = sum([price*i for i in range(1,count+1)]) - money
    return max(0,result)

print(f'test1 = {solution(3,20,4)}')