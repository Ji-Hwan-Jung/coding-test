import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville) > 1:
        f1 = heapq.heappop(scoville)
        f2 = heapq.heappop(scoville)
        heapq.heappush(scoville, f1+f2*2)
        cnt += 1
        
    return cnt if scoville[0] >= K else -1

print(f'test1 = {solution([1, 2, 3, 9, 10, 12],7)}')