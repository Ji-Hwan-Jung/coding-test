def solution(s, n):
    answer = ""
    
    for c in s:
        if c.isalpha():
            if c.isupper():
                answer += chr(ord('A')+((ord(c)+n)%ord('A'))%26)
            else:
                answer += chr(ord('a')+((ord(c)+n)%ord('a'))%26)
        else:
            answer += c
            
    return answer

print(f'test1 = {solution("AB", 1)}')
print(f'test1 = {solution("z", 1)}')
print(f'test1 = {solution("a B z", 4)}')