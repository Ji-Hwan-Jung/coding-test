def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] else -absolutes[i] for i in range(len(signs))])

print(f'test1 = {solution([4,7,12],[True,False,True])}')
print(f'test2 = {solution([1,2,3],[False,False,True])}')