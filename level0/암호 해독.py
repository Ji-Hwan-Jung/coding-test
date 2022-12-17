def solution(cipher, code):
    return cipher[code-1::code]

print(f'test1 = {solution("dfjardstddetckdaccccdegk",4)}')
print(f'test1 = {solution("pfqallllabwaoclk",2)}')