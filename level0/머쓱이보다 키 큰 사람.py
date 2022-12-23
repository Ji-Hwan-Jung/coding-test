def solution(array, height):
    return len([i for i in array if i>height])

print(f'test1 = {solution([149,180,192,170],167)}')
print(f'test2 = {solution([180,120,140],190)}')