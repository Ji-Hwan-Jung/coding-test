def solution(arr1, arr2):
    answer = []
    # 직관적인 방법 => pythonic한 방법보다 더 빠름
    arr2 = [[arr2[j][i] for j in range(len(arr2))] for i in range(len(arr2[0]))]
    # arr2 = list(zip(*arr2)) => pythonic한 방법
    
    for a in arr1:
        row = []
        for b in arr2:
            e = 0
            for i in range(len(a)):
                e += a[i]*b[i]
            row.append(e)
        answer.append(row)
            
    return answer

print(f'test1 = {solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]])}')
print(f'test2 = {solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]])}')