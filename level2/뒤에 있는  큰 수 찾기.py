def solution(numbers):
    result = [-1]*len(numbers)
    stack = []

    for i in range(len(result)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]
        stack.append(i)
    return result

print(f'test1 = {solution([2, 3, 3, 5])}')
print(f'test2 = {solution([9, 1, 5, 3, 6, 2])}')