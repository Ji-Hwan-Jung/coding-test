def solution(s):
    stack_str = ""
    answer = []
    for w in s:
        if w not in stack_str:
            answer.append(-1)
        else:
            answer.append(len(stack_str)-stack_str.rindex(w))
        stack_str += w
        
    return answer

print(f'test1 = {solution("banana")}')
print(f'test2 = {solution("foobar")}')