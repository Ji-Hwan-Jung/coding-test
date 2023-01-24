def solution(food):
    result = ""
    for i,e in enumerate(food):
        result += str(i)*(e//2)
    
    return result+"0"+result[-1::-1]

print(f'test1 = {solution([1,3,4,6])}')