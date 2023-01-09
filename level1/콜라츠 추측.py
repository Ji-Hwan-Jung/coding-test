def solution(num):
    cnt = 0
    
    while num != 1:
        if cnt >= 500:
            return -1
        else:
            num = num//2 if num%2 == 0 else num*3 + 1
            cnt += 1
    
    return cnt

print(f'test1 = {solution(6)}')
print(f'test2 = {solution(16)}')
print(f'test3 = {solution(626331)}')