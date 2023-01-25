def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

print(f'test1 = {solution(3,4,[1,2,3,1,2,3,1])}')
print(f'test2 = {solution(4,3,[4,1,2,2,4,4,4,4,1,2,4,2])}')