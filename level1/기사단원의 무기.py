def get_divisors(n):
    result = {1,n}
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            result.add(i)
            result.add(n//i)
    return len(result)

def solution(number, limit, power):
    divisors = list(map(get_divisors,range(1,number+1)))
    return sum([i if i<=limit else power for i in divisors])
    
print(f'test1 = {solution(5,3,2)}')
print(f'test2 = {solution(10,3,2)}')