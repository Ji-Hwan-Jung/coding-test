def solution(numbers):
    num_strings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i,s in enumerate(num_strings):
        numbers = numbers.replace(s, str(i))
        
    return int(numbers)

print(f'test1 = {solution("onetwothreefourfivesixseveneightnine")}')
print(f'test2 = {solution("onefourzerosixseven")}')