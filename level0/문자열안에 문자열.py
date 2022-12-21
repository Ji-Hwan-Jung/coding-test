def solution(str1, str2):
    return 1 if str2 in str1 else 2

print(f'test1 = {solution("ab6CDE443fgh22iJKlmn1o", "6CD")}')
print(f'test2 = {solution("ppprrrogrammers", "pppp")}')