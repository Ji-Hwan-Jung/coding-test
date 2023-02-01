def solution(s):
    temp = list(map(int,s.split()))
    return f'{str(min(temp))} {str(max(temp))}'

print(f'test1 = {solution("1 2 3 4")}')
print(f'test2 = {solution("-1 -2 -3 -4")}')
print(f'test3 = {solution("-1 -1")}')