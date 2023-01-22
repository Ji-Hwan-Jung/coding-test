def solution(numbers):
    result = []
    l = 0
    r = len(numbers)-1
    
    while l != len(numbers)-1:
        if l == r:
            l += 1
            r = len(numbers)-1
        else:
            a,b = numbers[l],numbers[r]
            if a+b not in result:
                result.append(a+b)
            r -= 1
    
    return sorted(result)

print(f'test1 = {solution([2,1,3,4,1])}')
print(f'test2 = {solution([5,0,2,7])}')