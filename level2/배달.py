def solution(N, road, K):
    INF = 500000
    graph = [dict() for _ in range(N)]
    v = [False]*N
    d = [0] + [INF]*(N-1)
        
    for a,b,c in road:
        if b-1 not in graph[a-1]:
            graph[a-1][b-1] = INF
        if a-1 not in graph[b-1]:
            graph[b-1][a-1] = INF
            
        graph[a-1][b-1] = min(graph[a-1][b-1], c)
        graph[b-1][a-1] = min(graph[b-1][a-1], c)
    
    def getSmallestNode():
        nonlocal INF,N,d,v
        min_value = INF
        index = 0
        for i in range(N):
            if not v[i] and d[i] < min_value:
                min_value = d[i]
                index = i
                
        return index
    
    d[0] = 0
    v[0] = True
    for j in graph[0].keys():
        d[j] = graph[0][j]
    for _ in range(N-1):
        now = getSmallestNode()
        v[now] = True
        for j in graph[now]:
            cost = d[now] + graph[now][j]
            if cost < d[j]:
                d[j] = cost
    
    return len(list(filter(lambda x: x<=K,d)))

print(f'test1 = {solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)}')
print(f'test2 = {solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4)}')