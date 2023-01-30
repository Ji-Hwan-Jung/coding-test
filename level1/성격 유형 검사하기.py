def solution(survey, choices):
    types = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    answer = ''
    
    for i in range(len(survey)):
        if choices[i] < 4:
            types[survey[i][0]] += abs(choices[i]-4)
        elif choices[i] > 4:
            types[survey[i][1]] += choices[i]-4
    
    keys = list(types.keys())
    for i in range(0,len(types),2):
        if types[keys[i]] >= types[keys[i+1]]:
            answer += keys[i]
        else:
            answer += keys[i+1]
            
    return answer

print(f'test1 = {solution(["AN","CF","MJ","RT","NA"],[5,3,2,7,5])}')
print(f'test2 = {solution(["TR","RT","TR"],[7,1,3])}')