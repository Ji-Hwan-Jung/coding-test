def solution(common):
    if common[-1]-common[-2] == common[1]-common[0]:
        return common[-1] + (common[1]-common[0])
    else:
        return common[-1] * (common[1]//common[0])
    
print(f'test1 = {solution([1,2,3,4])}')
print(f'test2 = {solution([2,4,8])}')