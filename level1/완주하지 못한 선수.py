def solution(participant, completion):
    result = {e: 0 for e in set(participant)}
    
    for e in participant:
        result[e] += 1
    for e in completion:
        result[e] -= 1
            
    return max(result,key=lambda x: result[x])

print(f'test1 = {solution(["leo","kiki","eden"],["eden","kiki"])}')
print(f'test2 = {solution(["marina","josipa","nikola","vinko","filipa"],["josipa","filipa","marina","nikola"])}')
print(f'test3 = {solution(["mislav","stanko","mislav","ana"],["stanko","ana","mislav"])}')