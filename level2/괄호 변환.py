def isCorrect(p):
    stack = []
    for i in p:
        if not stack:
            stack.append(i)
            continue
        if stack[-1] == '(' and i == ')':
            stack.pop()
        else:
            stack.append(i)
            
    return not stack

def getIndex(p):
    bracket = {'(': 0, ')': 0}
    for i in range(len(p)):
        bracket[p[i]] += 1
        if bracket['('] == bracket[')']:
            return i+1
                
def solution(p):
    def recursive(p):
        if not p:
            return p
        
        u = p[:getIndex(p)]
        v = p[getIndex(p):]
        
        if isCorrect(u):
            return u + recursive(v)
        else:
            reverse = ''.join(list(map(lambda x: '(' if x == ')' else ')',u[1:-1])))
            return '(' + recursive(v) + ')' + reverse
        
    return p if isCorrect(p) else recursive(p)

print(f'test1 = {solution("(()())()")}')
print(f'test2 = {solution(")(")}')
print(f'test3 = {solution("()))((()")}')