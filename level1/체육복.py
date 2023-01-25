def solution(n, lost, reserve):
    students = {i for i in range(1, n+1)}
    lost_stu = set(lost) - (set(lost)&set(reserve))
    reserve_stu = set(reserve) - (set(lost)&set(reserve))
    
    for i in list(lost_stu):
        if i-1 in reserve_stu:
            lost_stu.remove(i)
            reserve_stu.remove(i-1)
        elif i+1 in reserve_stu:
            lost_stu.remove(i)
            reserve_stu.remove(i+1)
    
    return len(students-lost_stu)

print(f'test1 = {solution(5,[2,4],[1,3,5])}')
print(f'test2 = {solution(5,[2,4],[3])}')
print(f'test3 = {solution(3,[3],[1])}')