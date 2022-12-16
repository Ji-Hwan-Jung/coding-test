def solution(n):
    seed = 1
    for i in range(1,12):
        seed *= i
        if seed > n:
            return i-1
        
print(f'test1 = {solution(3628800)}')
print(f'test1 = {solution(7)}')