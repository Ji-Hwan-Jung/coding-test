def solution(s):
    array = list(map(lambda x: x.lower(),s))
    answer = [' ']
    
    for i,e in enumerate(array):
        if i>=0 and answer[i] == ' ' and e.isalpha():
                answer.append(e.upper())
        else:
            answer.append(e)
            
    return ''.join(answer[1:])

print(f'test1 = {solution("3people unFollowed me")}')
print(f'test2 = {solution("for the last week")}')