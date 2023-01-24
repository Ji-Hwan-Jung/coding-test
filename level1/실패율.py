def solution(N, stages):
    users = len(stages)
    users_by_stage = {s: 0 for s in range(1,N+1)}
    result = {s: 0 for s in range(1,N+1)}
    
    for stage in stages:
        if stage <= N:
            users_by_stage[stage] += 1
    
    for k,v in users_by_stage.items():
        if users == 0:
            break
        result[k] = v/users
        users -= v
    
    return [i[0] for i in sorted(result.items(), key=lambda x: x[1], reverse=True)]
    
print(f'test1 = {solution(5, [2,1,2,6,2,4,3,3])}')
print(f'test2 = {solution(4, [4,4,4,4,4])}')