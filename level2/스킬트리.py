def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        stack = ""
        for c in st:
            if c in skill:
                stack += c
                
        if stack == skill[:len(stack)]:
            answer += 1
            
    return answer

print(f'test1 = {solution("CBD",["BACDE", "CBADF", "AECB", "BDA"])}')