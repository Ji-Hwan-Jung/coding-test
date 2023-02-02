def solution(n):
    smaller = bin(n).count('1')
    while True:
        n += 1
        if smaller == bin(n).count('1'):
            return n
        
print(f'test1 = {solution(78)}')
print(f'test2 = {solution(15)}')