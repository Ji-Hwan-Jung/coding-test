def solution(babbling):
    for i in range(len(babbling)):
        for j in ["aya","ye","woo","ma"]:
            babbling[i] = babbling[i].replace(j*2, "X")
            babbling[i] = babbling[i].replace(j, "O")
            
    return len(list(filter(lambda x: len(x)==x.count("O"), babbling)))

print(f'test1 = {solution(["aya","yee","u","maa"])}')
print(f'test2 = {solution(["ayaye","uuu","yeye","yemawoo","ayaayaa"])}')