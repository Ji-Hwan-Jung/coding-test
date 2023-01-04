def solution(n):
    return sum(list(map(int,str(n))))

print(f'test1 = {solution(123)}')
print(f'test2 = {solution(987)}')