def solution(quiz):
    answer = []
    
    for e in quiz:
        q = e.split(" = ")
        
        if "+" in q[0]:
            t = list(map(int, q[0].split(" + ")))
            if t[0]+t[1] == int(q[1]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            t = list(map(int, q[0].split(" - ")))
            if t[0]-t[1] == int(q[1]):
                answer.append("O")
            else:
                answer.append("X")
        
    return answer

print(f'test1 = {solution(["3 - 4 = -3", "5 + 6 = 11"])}')
print(f'test2 = {solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"])}')