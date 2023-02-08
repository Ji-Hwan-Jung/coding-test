# 해시와 계수의 합을 이용한 풀이
def solution(clothes):
    answer = 1
    species = [i[1] for i in clothes]
    kindOf = {i: species.count(i) for i in set(species)}
    
    for i in kindOf.values():
        answer *= i+1
        
    return answer-1

print(f'test1 = {solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])}')
print(f'test2 = {solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])}')