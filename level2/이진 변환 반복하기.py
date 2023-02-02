def solution(s):
    cov_cnt = 0
    zero_cnt = 0
    
    while s != '1':
        zero_cnt += s.count('0')
        s = bin(len(s.replace('0','')))[2:]
        cov_cnt += 1
    
    return [cov_cnt, zero_cnt]

print(f'test1 = {solution("110010101001")}')
print(f'test2 = {solution("01110")}')
print(f'test3 = {solution("1111111")}')