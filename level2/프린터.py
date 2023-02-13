def solution(priorities, location):
    temp = [i for i in enumerate(priorities)]
    stack = []
    
    while len(temp) != 0:
        if temp[0] == max(temp,key=lambda x: x[1]):
            stack.append(temp[0])
            temp = temp[1:]
        else:
            temp.append(temp.pop(0))
        
    for i,v in enumerate(stack):
        if v[0] == location:
            return i+1
        
print(f'test1 = {solution([2,1,3,2],2)}')
print(f'test2 = {solution([1,1,9,1,1,1],0)}')