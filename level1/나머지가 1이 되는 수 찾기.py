def solution(n):
    for x in range(2,n):
        if n%x == 1:
            return x
        
print(f'test1 = {solution(10)}')
print(f'test2 = {solution(12)}')