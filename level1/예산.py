def soultion(d, budget):
    answer = 0
    
    for i in sorted(d):
        if budget<i:
            break
        budget -= i
        answer += 1
    
    return answer

print(f'test1 = {soultion([1,3,2,5,4],9)}')
print(f'test2 = {soultion([2,2,3,3],10)}')