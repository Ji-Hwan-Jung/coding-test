def solution(babbling):
    for b in ["aya","ye","woo","ma"]:
        babbling = list(map(lambda x: x.replace(b," ").strip(),babbling))
    return babbling.count("")

print(f'test1 = {solution(["aya", "yee", "u", "maa", "wyeoo"])}')
print(f'test2 = {solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])}')