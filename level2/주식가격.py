def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        stack = [prices[i]]
        for j in range(i+1,len(prices)):
            stack.append(prices[j])
            if stack[0] > stack[-1]:
                break
        answer.append(len(stack)-1)
    
    return answer

print(f'test1 = {solution([1,2,3,2,3])}')