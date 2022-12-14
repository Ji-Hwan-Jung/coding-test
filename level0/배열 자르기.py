def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

print(f'test1 = {solution([1,2,3,4,5],1,3)}')
print(f'test2 = {solution([1,3,5],1,2)}')