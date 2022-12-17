def solution(my_string):
    answer = ""
    
    for i in my_string:
        if i not in answer:
            answer += i
    
    return answer

print(f'test1 = {solution("people")}')
print(f'test2 = {solution("We are the world")}')