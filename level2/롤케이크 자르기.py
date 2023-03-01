def solution(topping):
    result = 0
    chulsu = set(topping)
    brother = set()
    topp = dict()
    
    for t in topping:
        if t not in topp:
            topp[t] = 0
        topp[t] += 1
    
    for i in range(len(topping)):
        temp = topping.pop()
        brother.add(temp)
        topp[temp] -= 1
        if topp[temp] == 0:
            chulsu.remove(temp)
        if len(chulsu) == len(brother):
            result += 1
        
    return result

print(f'test1 = {solution([1, 2, 1, 3, 1, 4, 1, 2])}')
print(f'test2 = {solution([1, 2, 3, 1, 4])}')