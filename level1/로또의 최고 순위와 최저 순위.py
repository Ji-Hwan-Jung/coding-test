def solution(lottos, win_nums):
    winnings = [i for i in lottos if i in win_nums]
    lowest = 6-len(winnings) if len(winnings)==0 else 7-len(winnings)
    highest = 6-lottos.count(0)-len(winnings) if lottos.count(0)+len(winnings)==0 else 7-lottos.count(0)-len(winnings)
    
    return [highest, lowest]

print(f'test1 = {solution([44,1,0,0,31,25],[31,10,45,1,6,19])}')
print(f'test2 = {solution([0,0,0,0,0,0],[38,19,20,40,15,25])}')
print(f'test3 = {solution([45,4,35,20,3,9],[20,9,3,45,4,35])}')