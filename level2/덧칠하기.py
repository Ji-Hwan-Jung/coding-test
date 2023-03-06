# 처음 통과한 방식 - O(n^2)
def solution1(n, m, section):
    tiles = [i for i in range(n)]
    colored = [False for _ in range(n)]
    result = 0
    if m == 1:
        return len(section)
    
    for i in section:
        if colored[i-1]:
            continue
        else:
            for j in tiles[i-1:i-1+m]:
                colored[j] = True
            result += 1
    
    return result

# O(n) 풀이
def solution2(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer

print(f'test1 = {solution1(8,4,[2,3,6])}')
print(f'test2 = {solution2(5,4,[1,3])}')
print(f'test3 = {solution1(4,1,[1,2,3,4])}')