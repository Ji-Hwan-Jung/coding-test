def solution(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4:]

print(f'test1 = {solution("01033334444")}')
print(f'test2 = {solution("027778888")}')