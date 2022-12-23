def solution(array):
    return ''.join(map(str,array)).count('7')

print(f'test1 = {solution([7,77,17])}')
print(f'test2 = {solution([10,29])}')