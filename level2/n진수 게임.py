def convert(k, n):
    cov = {k: v for k,v in zip(range(0,16),"0123456789ABCDEF")}
    s = ""
    
    while True:
        if k>=n:
            k, mod = divmod(k,n)
            s += cov[mod]
        else:
            s += cov[k]
            break
        
    return s[::-1]

def solution(n, t, m, p):
    answer = ""
    numbers = ""
    index = 0
    
    while len(answer) < t:
        numbers += convert(index,n)
        if index%m == p-1:
            answer += numbers[index]
        index += 1
        
    return answer

print(f'test1 = {solution(2,4,2,1)}')
print(f'test2 = {solution(16,16,2,1)}')
print(f'test3 = {solution(16,16,2,2)}')