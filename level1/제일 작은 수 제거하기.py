def solution(arr):    
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr

print(f'test1 = {solution([4,3,2,1])}')
print(f'test2 = {solution([-10])}')