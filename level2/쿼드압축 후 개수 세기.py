def solution(arr):
    answer = {0: 0, 1: 0}
    
    def quad_tree(arr):
        nonlocal answer
        n = len(arr)
        total = 0
        
        for i in arr:
            total += sum(i)
        
        if total in (0,n*n):
            answer[min(total,1)] += 1
            return
        elif n==2:
            for x,y in arr:
                answer[x] += 1
                answer[y] += 1
            return
        else:
            quad_tree(list(map(lambda x: x[:n//2],arr[:n//2])))
            quad_tree(list(map(lambda x: x[n//2:],arr[:n//2])))
            quad_tree(list(map(lambda x: x[:n//2],arr[n//2:])))
            quad_tree(list(map(lambda x: x[n//2:],arr[n//2:])))
            
    quad_tree(arr)
    
    return list(answer.values())

print(f'test1 = {solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])}')
print(f'test2 = {solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])}')