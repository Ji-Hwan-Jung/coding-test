def solution(a, b, n):
    answer = 0
    
    while n>=a:
        answer += (n//a)*b
        n = n-(n//a*a)+(n//a*b)
        
    return answer

print(f'test1 = {solution(2,1,20)}')
print(f'test2 = {solution(3,1,20)}')