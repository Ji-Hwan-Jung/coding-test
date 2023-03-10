def dfs(graph, visited, p):
    visited[p] = True
    for i in graph[p]:
        if not visited[i]:
            dfs(graph, visited, i)

def solution(n, wires):
    d = {i: set() for i in range(1,n+1)}
    connections = []
    
    for p1,p2 in wires:
        d[p1].add(p2)
        d[p2].add(p1)
    
    for p1,p2 in wires:
        graph = {i: {j for j in d[i]} for i in range(1,n+1)}
        visited = {i: False for i in range(1,n+1)}
        graph[p1].remove(p2)
        graph[p2].remove(p1)
        
        dfs(graph, visited, p2)
        
        connections.append(len(list(filter(lambda x: visited[x], graph))))
        
    return min(map(lambda x: abs(n-x*2), connections))

print(f'test1 = {solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])}')
print(f'test2 = {solution(4,[[1,2],[2,3],[3,4]])}')
print(f'test3 = {solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])}')