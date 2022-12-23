def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0,len(my_str),n)]

print(f'test1 = {solution("abc1Addfggg4556b",6)}')
print(f'test2 = {solution("abcdef123",3)}')