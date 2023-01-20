import itertools as it

def solution(number):
    answer = 0
    
    for a,b,c in it.combinations(number, 3):
        if a+b+c == 0:
            answer += 1
            
    return answer

print(f'test1 = {solution([-2,3,0,2,-5])}')
print(f'test2 = {solution([-3,-2,-1,0,1,2,3])}')
print(f'test3 = {solution([-1,1,-1,1])}')