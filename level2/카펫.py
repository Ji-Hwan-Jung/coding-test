def solution(brown, yellow):
    total = brown+yellow
    for i in range(int(total**0.5)+1,2,-1):
        if total%i == 0 and (i-2)*((total//i)-2) == yellow:
            return [max(i, total//i), min(i, total//i)]
        
print(f'test1 = {solution(10,2)}')
print(f'test2 = {solution(8,1)}')
print(f'test3 = {solution(24,24)}')