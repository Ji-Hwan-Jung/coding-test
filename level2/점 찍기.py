def solution(k, d):
    result = 0
    for x in range(0,d+1,k):
        y = int((d**2 - x**2)**0.5)
        result += y//k + 1
            
    return result

print(f'test1 = {solution(2,4)}')
print(f'test2 = {solution(1,5)}')