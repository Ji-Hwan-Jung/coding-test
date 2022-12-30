def solution(score):
    s = sorted([sum(i) for i in score],reverse=True)
    return [s.index(sum(i))+1 for i in score]

print(f'test1 = {solution([[80, 70], [90, 50], [40, 70], [50, 80]])}')
print(f'test2 = {solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])}')