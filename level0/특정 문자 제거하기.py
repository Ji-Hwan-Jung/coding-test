def solution(my_string, letter):
    return my_string.replace(letter, '')

print(f'test1 = {solution("abcdef", "f")}')
print(f'test1 = {solution("BCBdbe", "B")}')