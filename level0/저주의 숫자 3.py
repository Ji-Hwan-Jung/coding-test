def solution(n):
    safe_numbers = []
    cnt = 1
    
    while len(safe_numbers) < n:
        if cnt%3 and '3' not in str(cnt):
            safe_numbers.append(cnt)
        cnt += 1
        
    return safe_numbers[-1]

print(f'test1 = {solution(15)}')
print(f'test2 = {solution(40)}')