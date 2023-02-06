# 유클리드 호제법 => math모듈의 gcd와 걸리는 시간 비슷하게 나옴
def getGCD(a,b):    
    while a!=b and a != 0 and b != 0:
        if a>b: a=a-b*(a//b)
        else: b=b-a*(b//a)
        
    return max(a,b)

def solution(arr):
    result = arr[0]
    
    for i in arr[1:]:
        result = result*i//getGCD(result,i)
        
    return result

print(f'test1 = {solution([2,6,8,14])}')
print(f'test2 = {solution([1,2,3])}')