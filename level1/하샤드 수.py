def solution(x):
    return x%sum(list(map(int,str(x)))) == 0

print(f'test1 = {solution(10)}')
print(f'test2 = {solution(12)}')
print(f'test3 = {solution(11)}')
print(f'test4 = {solution(13)}')