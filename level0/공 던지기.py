def solution(numbers, k):
    return numbers[2*(k-1)%len(numbers)]

print(f'test1 = {solution([1,2,3,4],2)}')
print(f'test2 = {solution([1,2,3],3)}')