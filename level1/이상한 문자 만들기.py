def solution(s):
    array = s.split(' ')
    
    for i,e in enumerate(array):
        temp = ""
        for j,c in enumerate(e):
            if j%2 == 0:
                temp += c.upper()
            else:
                temp += c.lower()
        array[i] = temp
    
    return ' '.join(array)

print(f'test1 = {solution("try hello world")}')