def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    
    for i in range(len(A)):
        answer += A[i] * B[i]
        
    return answer

print(f'test1 = {solution([1,4,2],[5,4,4])}')
print(f'test2 = {solution([1,2],[3,4])}')