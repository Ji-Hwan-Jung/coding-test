def solution(n):
    ternary = ""
    while n:
        ternary += str(n%3)
        n = n//3
        
    return int(ternary,3)

print(f'test1 = {solution(45)}')
print(f'test2 = {solution(125)}')