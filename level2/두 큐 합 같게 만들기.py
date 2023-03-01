def solution(queue1, queue2):
    arr = queue1 + queue2
    result = 0
    l, r = 0, len(queue1)
    total = sum(arr)//2
    sum1 = sum(queue1)
    
    while sum1 != total:
        if sum1 < total:
            sum1 += arr[r]
            r += 1
            result += 1
        else:
            sum1 -= arr[l]
            l += 1
            result += 1
        if r == len(arr):
            return -1
        
    return result

print(f'test1 = {solution([3,2,7,2],[4,6,5,1])}')
print(f'test2 = {solution([1,2,1,2],[1,10,1,2])}')
print(f'test3 = {solution([1,1],[1,5])}')