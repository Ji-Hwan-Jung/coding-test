def solution(array):
    while True:
        if len(array) == 0:
            return -1
        if len(array) == 1:
            return array[0]
        for i in set(array):
            array.remove(i)
            
test1 = solution([1,2,3,3,3,4])
test2 = solution([1,1,2,2])
test3 = solution([1])

print(f'test1 = {test1}')
print(f'test2 = {test2}')
print(f'test3 = {test3}')