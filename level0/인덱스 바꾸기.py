def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    
    return ''.join(my_string)

print(f'test1 = {solution("hello",1,2)}')
print(f'test2 = {solution("I love you",3,6)}')