def solution(n):
    return sum(list(map(int,str(n))))

print(f'test1 = {solution(1234)}')
print(f'test2 = {solution(930211)}')