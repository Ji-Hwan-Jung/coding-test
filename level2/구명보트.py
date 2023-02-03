def solution(people, limit):
    cnt = 0
    left = 0
    right = len(people)-1
    people.sort(reverse=True)
    
    while left <= right:
        if people[left]+people[right] <= limit:
            left += 1
            right -= 1
        else:
            left += 1
        cnt += 1
    
    return cnt

print(f'test1 = {solution([70,50,80,50],100)}')
print(f'test2 = {solution([70,80,50],100)}')