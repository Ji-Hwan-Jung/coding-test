def solution(s):
    stack = []
    
    for i in s:
        stack.append(i)
        if stack[-2:] == ['(',')']:
            for _ in range(2):
                stack.pop()
    
    return len(stack) == 0

print(f'test1 = {solution("()()")}')
print(f'test2 = {solution("(())()")}')
print(f'test3 = {solution(")()(")}')
print(f'test4 = {solution("(()(")}')