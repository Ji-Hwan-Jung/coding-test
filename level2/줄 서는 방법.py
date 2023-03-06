from math import factorial,ceil

def solution(n, k):
    numbers = [i for i in range(1,n+1)]
    result = []
    
    while n > 0:
        a = factorial(n-1)
        b = ceil(k/a)
        result.append(numbers.pop(b-1))
        k = k%a
        n -= 1
    
    return result

print(f'test1 = {solution(3,5)}')