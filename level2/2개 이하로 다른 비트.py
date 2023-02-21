def solution(numbers):
    result = []
    
    for i in numbers:
        result.append(((i^(i+1))>>2) + i + 1)
        
    return result

print(f'test1 = {solution([2,7])}')