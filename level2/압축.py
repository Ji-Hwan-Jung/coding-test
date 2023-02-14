def solution(msg):
    answer = []
    mydict = [chr(i) for i in range(65,91)]
    cur = len(msg)
    
    while len(msg) != 0:
        if msg[:cur] in mydict:
            mydict.append(msg[:cur+1])
            answer.append(mydict.index(msg[:cur])+1)
            msg = msg[cur:]
            cur = len(msg)
        else:
            cur -= 1
    
    return answer

print(f'test1 = {solution("KAKAO")}')
print(f'test2 = {solution("TOBEORNOTTOBEORTOBEORNOT")}')
print(f'test3 = {solution("ABABABABABABABAB")}')