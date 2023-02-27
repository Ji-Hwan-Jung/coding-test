def solution(number, k):
    stack = []
    for i in number:
        while stack and k > 0 and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)
        
    return ''.join(stack)[:len(number)-k]

print(f'test1 = {solution("1924",2)}')
print(f'test2 = {solution("1231234",3)}')
print(f'test3 = {solution("4177252841",4)}')