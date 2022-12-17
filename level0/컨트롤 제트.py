def solution(s):
    s = s.split(' ')
    numbers = []
    
    for i in s:
        if i == "Z":
            numbers.pop()
        else:
            numbers.append(int(i))
            
    return sum(numbers)

print(f'test1 = {solution("1 2 Z 3")}')
print(f'test2 = {solution("10 20 30 40")}')
print(f'test3 = {solution("10 Z 20 Z 1")}')