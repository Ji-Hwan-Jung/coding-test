def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    table = [0,0,0]
    
    for i,e in enumerate(answers):
        if one[i%len(one)] == e:
            table[0] += 1
        if two[i%len(two)] == e:
            table[1] += 1
        if three[i%len(three)] == e:
            table[2] += 1
    
    return [i+1 for i,e in enumerate(table) if max(table) == e ]

print(f'test1 = {solution([1,2,3,4,5])}')
print(f'test2 = {solution([1,3,2,4,2])}')