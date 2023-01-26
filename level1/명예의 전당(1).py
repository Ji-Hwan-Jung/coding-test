def solution(k, score):
    honors = []
    result = []
    
    for i in score:
        honors.append(i)
        if len(honors) > k:
            honors.remove(min(honors))
        result.append(min(honors))
    
    return result

print(f'test1 = {solution(3, [10,100,20,150,1,100,200])}')
print(f'test2 = {solution(4, [0,300,40,300,20,70,150,50,500,1000])}')