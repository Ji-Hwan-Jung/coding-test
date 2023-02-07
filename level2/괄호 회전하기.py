def solution(s):
    str = s*2
    stack = []
    cnt = 0
    
    for i in range(len(s)):
        stack.clear()
        for c in str[i:i+len(s)]:
            stack.append(c)
            bracket = ''.join(stack[-2:])
            if bracket in ['()','[]','{}']:
                for _ in range(2):
                    stack.pop()
        if len(stack) == 0:
            cnt += 1
                
    return cnt

print(f'test1 = {solution("[](){}")}')
print(f'test2 = {solution("}]()[{")}')
print(f'test3 = {solution("[)(])")}')
print(f'test4 = {solution("}}}")}')