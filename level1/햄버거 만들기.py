def solution(ingredient):
    result = 0
    stack = []
    
    for i in ingredient:
        stack.append(i)
        if stack[-4::] == [1,2,3,1]:
            result += 1
            for _ in range(4):
                stack.pop()
    
    return result

print(f'test1 = {solution([2,1,1,2,3,1,2,3,1])}')
print(f'test2 = {solution([1,3,2,1,2,1,3,1,2])}')