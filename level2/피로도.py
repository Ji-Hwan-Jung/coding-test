from itertools import permutations

def solution(k, dungeons):
    counter = []
        
    for i in permutations(dungeons,len(dungeons)):
        n, cnt = k, 0
        
        for mins,consume in i:
            if n>=mins and n>=consume:
                n -= consume
                cnt += 1
            else:
                break
        counter.append(cnt)
                
    return max(counter)

print(f'test1 = {solution(80,[[80,20],[50,40],[30,10]])}')