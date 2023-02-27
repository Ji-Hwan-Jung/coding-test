def solution(n):
    result = []
    
    while n >= 3:
        r = str(n%3) if n%3!=0 else '4'
        result.append(r)
        if n%3 == 0:
            n = n//3-1
        else:
            n = n//3
        
    if str(n) == '0':
        return ''.join(result[::-1])
    else:
        return str(n)+''.join(result[::-1])
    
print(f'test1 = {solution(1)}')
print(f'test2 = {solution(2)}')
print(f'test3 = {solution(3)}')
print(f'test4 = {solution(4)}')