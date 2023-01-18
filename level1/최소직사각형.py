def solution(sizes):
    elements = list(map(sorted, sizes))
    elements = list(zip(*elements))
    return max(elements[0]) * max(elements[1])

print(f'test1 = {solution([[60, 50], [30, 70], [60, 30], [80, 40]])}')
print(f'test2 = {solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	)}')
print(f'test3 = {solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	)}')