def solution(num, total):
    count = max(num, total)
    
    while True:
        temp = [count-i for i in range(num-1,-1,-1)]
        if sum(temp) == total:
            return temp
        count -= 1
        
print(f'test1 = {solution(3,12)}')
print(f'test2 = {solution(5,15)}')
print(f'test3 = {solution(4,14)}')
print(f'test4 = {solution(5,5)}')