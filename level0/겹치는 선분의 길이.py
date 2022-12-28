def solution(lines):
    s = [set(range(min(l),max(l))) for l in lines]
    return len(s[0]&s[1] | s[1]&s[2] | s[0]&s[2])

print(f'test1 = {solution([[0, 1], [2, 5], [3, 9]])}')
print(f'test2 = {solution([[-1, 1], [1, 3], [3, 9]])}')
print(f'test3 = {solution([[0, 5], [3, 9], [1, 10]])}')