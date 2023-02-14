def isPrime(n):
    for i in range(2, int(n**0.5+1)):
        if n%i == 0:
            return False
    return True

def solution(n, k):
    convert = ""
    answer = 0
    
    while n>0:
        n,mod = divmod(n,k)
        convert += str(mod)
        
    convert = convert[::-1]
    
    s = list(map(int,filter(lambda x: x != "1",filter(lambda x: len(x)>0,convert.split('0')))))

    for i in s:
        if isPrime(i):
            answer += 1
    
    return answer

print(f'test1 = {solution(437674,3)}')