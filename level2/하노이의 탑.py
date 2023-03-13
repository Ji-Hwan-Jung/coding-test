def solution(n):
    result = []
    
    def hanoi(frm, to, n):
        if n == 1:
            result.append([frm,to])
        else:
            other = 6-frm-to
            hanoi(frm,other,n-1)
            result.append([frm,to])
            hanoi(other,to,n-1)
            
    hanoi(1,3,n)
    
    return result

print(f'test1 = {solution(2)}')