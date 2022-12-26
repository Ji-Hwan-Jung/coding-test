def solution(polynomial):
    v = 0
    c = 0
    s = polynomial.split(" + ")
    
    for e in s:
        if 'x' not in e:
            c += int(e)
        else:
            v += int(e[:-1]) if e != 'x' else 1
            
    if v!=0 and c!=0:
        return f'{v if v != 1 else ""}x + {c}'
    else:
        if v==0:
            return f'{c}'
        elif c==0:
            return f'{v if v != 1 else ""}x'
        else:
            return '0'
        
print(f'test1 = {solution("3x + 7 + x")}')
print(f'test2 = {solution("x + x + x")}')