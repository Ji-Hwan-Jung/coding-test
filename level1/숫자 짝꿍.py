def solution(X, Y):
    compare = [str(i) for i in range(9,-1,-1)]
    answer = ''
    
    for i in compare:
        answer += i*min(X.count(i), Y.count(i))
    
    if len(answer) != 0:
        if answer.count('0') == len(answer):
            answer = '0'
        return answer
    else:
        return "-1"

print(f'test1 = {solution("100","2345")}')
print(f'test2 = {solution("100","203045")}')
print(f'test3 = {solution("100","123450")}')
print(f'test4 = {solution("12321","42531")}')
print(f'test5 = {solution("5525","1255")}')