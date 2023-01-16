def solution(arr1, arr2):
    return [[a+b for a,b in zip(x,y)] for x,y in zip(arr1, arr2)]

print(f'test1 = {solution([[1,2],[2,3]],[[3,4],[5,6]])}')
print(f'test2 = {solution([[1],[2]],[[3],[4]])}')