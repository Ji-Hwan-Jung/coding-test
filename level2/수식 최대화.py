def calc(a, b, op):
    if op == '*':
        return a*b
    elif op == '-':
        return a-b
    else:
        return a+b
    
def solution(expression):
    result = []
    priority = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
    op = ['-','+','*']
    operation = list(filter(lambda x: not x.isdigit(), expression))
    expression = ' '.join(expression.split('*'))
    expression = ' '.join(expression.split('-'))
    expression = ' '.join(expression.split('+'))
    expression = list(map(int,expression.split()))
    
    temp = []
    for i in range(len(expression)):
        temp.append(expression[i])
        if i < len(operation):
            temp.append(operation[i])
    
    for prior in priority:
        a = [i for i in temp]
        b = []
        for p in prior:
            while a:
                t = a.pop(0)
                if type(t) == int or op[p] != t:
                    b.append(t)
                else:
                    oper1 = b.pop()
                    oper2 = a.pop(0)
                    b.append(calc(oper1,oper2,t))
            a = [i for i in b]
            b.clear()
        result.append(a[0])
    
    return abs(max(result,key=lambda x: abs(x)))

print(f'test1 = {solution("100-200*300-500+20")}')
print(f'test2 = {solution("50*6-3*2")}')