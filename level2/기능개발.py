# 일일이 날짜를 더하면서 푸는 방식
def solution1(progresses, speeds):
    complete = []
    result = []
    
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        while progresses[0] >= 100:
            complete.append(progresses.pop(0))
            speeds.pop(0)
            if len(progresses) == 0:
                break
        
        if len(complete) > 0:
            result.append(len(complete))
            complete.clear()
        
    return result


# 작업 완료에 필요한 날짜를 계산하여 푸는 방식
def solution(progresses, speeds):
    complete = []
    result = []
    
    for p,s in zip(progresses, speeds):
        day = (100-p)//s+1 if (100-p)%s != 0 else (100-p)//s
        
        if len(complete) == 0 or complete[0] >= day:
            complete.append(day)
        else:
            result.append(len(complete))
            complete.clear()
            complete.append(day)
            
    result.append(len(complete))
    
    return result
            

print(f'test1 = {solution([93, 30, 55],[1, 30, 5])}')
print(f'test2 = {solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])}')