def solution(A, B):
    # cnt = 0
    
    # for _ in range(len(A)):
    #     if A == B:
    #         return cnt
        
    #     temp = list(A)
    #     A = temp.pop() + ''.join(temp)
    #     cnt += 1
    
    # return -1
    return (B+B).find(A)

print(f'test1 = {solution("hello","ohell")}')
print(f'test2 = {solution("apple","elppa")}')