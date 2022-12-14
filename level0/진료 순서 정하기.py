def solution(emergency):
    return [sorted(emergency, reverse=True).index(i)+1 for i in emergency]

print(f'test1 = {solution([3,76,24])}')
print(f'test2 = {solution([1,2,3,4,5,6,7])}')
print(f'test3 = {solution([30,10,23,6,100])}')