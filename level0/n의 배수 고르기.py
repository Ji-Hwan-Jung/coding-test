def solution(n, numlist):
    return [i for i in numlist if i%n==0]

print(f'test1 = {solution(3, [4,5,6,7,8,9,10,11,12])}')
print(f'test2 = {solution(5, [1,9,3,10,13,5])}')