def solution(array, commands):
    return [sorted(array[a-1:b])[c-1] for a,b,c in commands]

print(f'test1 = {solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]])}')