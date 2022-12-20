def solution(num, k):
    num, k = str(num), str(k)
    
    if num.count(k):
        return num.index(k)+1
    
    return -1

print(f'test1 = {solution(29183, 1)}')
print(f'test2 = {solution(232443, 4)}')
print(f'test3 = {solution(123456, 7)}')