def solution(n, left, right):
    return [max(i//n+1,i%n+1) for i in range(left,right+1)]

print(f'test1 = {solution(3,2,5)}')
print(f'test2 = {solution(4,7,14)}')