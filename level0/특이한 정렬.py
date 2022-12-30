def solution(numlist, n):
    return sorted(numlist,key=lambda x: (abs(x-n),n-x))

print(f'test1 = {solution([1,2,3,4,5,6],4)}')
print(f'test2 = {solution([10000,20,36,47,40,6,10,7000],30)}')