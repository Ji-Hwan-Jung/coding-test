def solution(chiken):
    service = 0
    
    while chiken >= 10:
        service += chiken//10
        chiken = chiken//10 + chiken%10
    
    return service

print(f'test1 = {solution(100)}')
print(f'test2 = {solution(1081)}')