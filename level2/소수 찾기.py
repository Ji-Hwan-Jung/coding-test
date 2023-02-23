from itertools import permutations as pm

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = set()
    for i in range(1,len(numbers)+1):
        nums.update(set(filter(lambda x: x not in (0,1),map(lambda x: int(''.join(x)),pm(numbers,i)))))
        
    for n in nums:
        if isPrime(n):
            answer += 1
            
    return answer

print(f'test1 = {solution("17")}')
print(f'test2 = {solution("011")}')