def solution(s):
    numbers = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    for e in numbers.keys():
        s = s.replace(e, numbers.get(e))
        
    return int(s)

print(f'test1 = {solution("one4seveneight")}')
print(f'test2 = {solution("23four5six7")}')
print(f'test3 = {solution("2three45sixseven")}')
print(f'test4 = {solution("123")}')