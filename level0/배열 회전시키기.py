def solution(numbers, direction):
    if direction == "right":
        numbers.insert(0, numbers.pop())
    else:
        numbers.append(numbers.pop(0))
        
    return numbers

print(f'test1 = {solution([1,2,3], "right")}')
print(f'test1 = {solution([4,455,6,4,-1,45,6], "left")}')