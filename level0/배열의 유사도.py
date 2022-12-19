def solution(s1, s2):
    return len(set(s1)&set(s2))

print(f'test1 = {solution(["a","b","c"],["com","b","d","p","c"])}')
print(f'test2 = {solution(["n","omg"],["m","dot"])}')