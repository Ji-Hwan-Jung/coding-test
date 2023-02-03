def solution(n, words):
    stack = [words[0]]
    
    for i,e in enumerate(words[1:]):
        if e in stack or stack[-1][-1] != e[0]:
            return [(i+1)%n+1, (i+1)//n+1]
        else:
            stack.append(e)
    return [0,0]

print(f'test1 = {solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])}')
print(f'test2 = {solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])}')
print(f'test3 = {solution(2,["hello", "one", "even", "never", "now", "world", "draw"])}')