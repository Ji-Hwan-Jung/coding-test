import re

def solution(new_id):
    #step 1
    answer = new_id.lower()
    #step 2
    answer = re.compile('[^a-z0-9-_.]').sub('', answer)
    #step 3
    answer = re.compile('\.{2,}').sub('.', answer)
    #step 4
    answer = re.compile('^\.|\.$').sub('', answer)
    #step 5
    if len(answer) == 0: answer = "a"
    #step 6
    if len(answer) >= 16: answer = ''.join(list(answer[0:15]))
    answer = re.compile('\.$').sub('', answer)
    #step 7
    while len(answer) < 3:
        answer += answer[-1]
        
    return answer

print(f'test1 = {solution("...!@BaT#*..y.abcdefghijklm")}')
print(f'test2 = {solution("z-+.^.")}')
print(f'test3 = {solution("=.=")}')
print(f'test4 = {solution("123_.def")}')
print(f'test5 = {solution("abcdefghijklmn.p")}')