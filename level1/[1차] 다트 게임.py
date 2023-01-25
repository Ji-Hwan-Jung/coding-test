import re

def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('\d+[SDT]\*?\#?')
    score = p.findall(dartResult)
    
    for i,e in enumerate(score):
        if '*' in e or '#' in e:
            if '*' in e and i>0:
                score[i-1] *= 2
            score[i] = int(e[0:-2])**bonus[e[-2]]*option[e[-1]]
        else:
            score[i] = int(e[0:-1])**bonus[e[-1]]
    
    return sum(score)

print(f'test1 = {solution("1S2D*3T")}')
print(f'test2 = {solution("1D2S#10S")}')