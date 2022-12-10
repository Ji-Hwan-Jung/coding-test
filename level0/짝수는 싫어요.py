def solution(n):
    return [i for i in range(1, n+1, 2)]

test1 = solution(10)
test2 = solution(15)

print(f'test1 = {test1}')
print(f'test2 = {test2}')