from itertools import product as pd

def solution(word):
    vowels = ['A','E','I','O','U']
    d = []
    
    for i in range(1,6):
        d += list(map(lambda x: ''.join(x),pd(vowels, repeat=i)))
        
    return sorted(d).index(word)+1

print(f'test1 = {solution("AAAAE")}')
print(f'test2 = {solution("AAAE")}')
print(f'test3 = {solution("I")}')
print(f'test4 = {solution("EIO")}')