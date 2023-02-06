def solution(n):
    consume = 1
    
    while n!=1:
        if n%2!=0:
            consume += 1
        n = n//2
        
    return consume

print(f'test1 = {solution(5)}')
print(f'test2 = {solution(6)}')
print(f'test3 = {solution(5000)}')