from itertools import combinations as cb

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def solution(nums):
    s = [sum(i) for i in cb(nums,3) if isPrime(sum(i))]
    return len(s)

print(f'test1 = {solution([1,2,3,4])}')
print(f'test2 = {solution([1,2,7,6,4])}')