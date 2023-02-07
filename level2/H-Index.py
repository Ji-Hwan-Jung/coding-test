def solution(citations):
    for i in range(len(citations),0,-1):
        arr1 = list(filter(lambda x: x>=i,citations))
        arr2 = list(filter(lambda x: x<i,citations))
        if len(arr1) >= i and len(arr1)+len(arr2) == len(citations):
            return i
    return 0

print(f'test1 = {solution([3,0,6,1,5])}')