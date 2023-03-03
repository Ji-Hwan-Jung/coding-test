from collections import deque

# 내가 처음 통과한 풀이
def solution1(x, y, n):
    queue = deque([x])
    d = {i: 0 for i in range(1,1000001)}
    
    while queue:
        value = queue.popleft()
        if value == y:
            return d[value]
        elif value < y:
            for i in [value+n, value*2, value*3]:
                if i <= 1000000 and d[i] == 0:
                    queue.append(i)
                    d[i] = d[value]+1
                
    return -1

# set을 이용한 풀이
def solution2(x, y, n):
    q = set([x])
    depth = 0
    
    while q:
        temp = set()
        
        if y in q:
            return depth
        
        for i in q:
            if i+n <= y:
                temp.add(i+n)
            if i*2 <= y:
                temp.add(i*2)
            if i*3 <= y:
                temp.add(i*3)
        
        q = temp
        depth += 1
        
    return -1

print(f'test1 = {solution1(10,40,5)}')
print(f'test2 = {solution2(10,40,30)}')
print(f'test3 = {solution1(2,5,4)}')