from collections import deque

def solution(bridge_length, weight, truck_weights):
    passing = deque([0]*bridge_length)
    waiting = deque(truck_weights)
    times = 0
    total = 0
    
    while passing:
        total -= passing.popleft()
        if waiting:
            if total+waiting[0] <= weight:
                t = waiting.popleft()
                total += t
                passing.append(t)
            else:
                passing.append(0)
        times += 1
        
    return times

print(f'test1 = {solution(2,10,[7,4,5,6])}')
print(f'test2 = {solution(100,100,[10])}')
print(f'test3 = {solution(100,100,[10,10,10,10,10,10,10,10,10,10])}')