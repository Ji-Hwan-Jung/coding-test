def solution(n):
    a,b = 0,1
    
    for _ in range(0,n-1):
        a,b = b,a+b
        
    return b%1234567

print(f'test1 = {solution(3)}')
print(f'test2 = {solution(5)}')