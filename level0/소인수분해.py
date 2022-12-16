def solution(n):
    answer = []
    p = 2
    while n>=p:
        if n%p == 0:
            n//=p
            if p not in answer:
                answer.append(p)
        else:
            p += 1
            
    return answer

print(f'test1 = {solution(12)}')
print(f'test1 = {solution(17)}')
print(f'test1 = {solution(420)}')