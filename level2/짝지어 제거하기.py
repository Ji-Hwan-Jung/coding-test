def solution(s):
    stack = []
    
    for c in s:
        if len(stack) > 0 and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return int(len(stack) == 0)

print(f'test1 = {solution("baabaa")}')
print(f'test2 = {solution("cdcd")}')