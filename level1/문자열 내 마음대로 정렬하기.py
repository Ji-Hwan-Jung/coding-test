def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n],x))

print(f'test1 = {solution(["sun","bed","car"],1)}')
print(f'test2 = {solution(["abce","abcd","cdx"],2)}')