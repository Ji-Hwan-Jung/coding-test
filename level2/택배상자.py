def solution(order):
    i = 1
    sub = []
    idx = 0
    
    while i <= len(order):
        sub.append(i)
        while sub:
            if sub[-1] == order[idx]:
                sub.pop()
                idx += 1
            else:
                break
        i += 1
                
    return idx

print(f'test1 = {solution([4,3,1,2,5])}')
print(f'test2 = {solution([5,4,3,2,1])}')