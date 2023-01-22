def solution(nums):
    return min(len(set(nums)), len(nums)//2)

print(f'test1 = {solution([3,1,2,3])}')
print(f'test2 = {solution([3,3,3,2,2,4])}')
print(f'test3 = {solution([3,3,3,2,2,2])}')