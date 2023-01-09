def solution(a, b):
    if a==b:
        return a
    
    x = max(a,b)
    y = min(a,b)-1
    
    return x*(x+1)//2 - y*(y+1)//2
    

print(f'test1 = {solution(3,5)}')
print(f'test2 = {solution(3,3)}')
print(f'test3 = {solution(5,3)}')