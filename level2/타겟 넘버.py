def solution(numbers, target):
    answer = 0
    
    def dfs(num, level):
        nonlocal answer
        
        if level == len(numbers):
            if num == target:
                answer += 1
            return
                
        dfs(num + numbers[level], level + 1)
        dfs(num - numbers[level], level + 1)
    
    dfs(numbers[0], 1)
    dfs(-numbers[0], 1)
    
    return answer
    
print(f'test1 = {solution([1,1,1,1,1],3)}')
print(f'test2 = {solution([4,1,2,1],4)}')