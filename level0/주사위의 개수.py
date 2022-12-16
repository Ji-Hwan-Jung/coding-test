def solution(box, n):
    return (box[0]//n)*(box[1]//n)*(box[2]//n)

print(f'test1 = {solution([1,1,1], 1)}')
print(f'test2 = {solution([10,8,6], 3)}')