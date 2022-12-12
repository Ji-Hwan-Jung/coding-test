def solution(my_string, n):
    return ''.join(map(lambda x: x*n, my_string))

print(f'test1 = {solution("hello", 3)}')
print(f'test2 = {solution("world", 3)}')