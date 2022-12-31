def solution(bin1, bin2):
    return bin(int(bin1,2)+int(bin2,2))[2:]

print(f'test1 = {solution("10","11")}')