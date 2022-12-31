def solution(i, j, k):
    return sum([str(n).count(str(k)) for n in range(i,j+1)])

print(f'test1 = {solution(1,13,1)}')
print(f'test2 = {solution(10,50,5)}')
print(f'test3 = {solution(3,10,2)}')