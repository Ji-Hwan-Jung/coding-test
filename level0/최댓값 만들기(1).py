def solution(numbers):
    numbers.sort()
    return numbers[-1]*numbers[-2]

print(f'test1 = {solution([1,2,3,4,5])}')
print(f'test2 = {solution([0,31,24,10,1,9])}')