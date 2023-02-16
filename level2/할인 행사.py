def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount)-9):
        wants = {k: v for k,v in zip(want,number)}
        arr = discount[i:i+10]
        d = {i: arr.count(i) for i in set(arr)}
        for k in wants.keys():
            if k in d.keys():
                wants[k] -= d[k]
            
        if len(list(filter(lambda x: wants[x] > 0, wants))) == 0:
            answer += 1
            
    return answer

print(f'test1 = {solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])}')
print(f'test2 = {solution(["apple"],[10],["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])}')