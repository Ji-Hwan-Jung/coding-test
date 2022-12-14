def solution(age):
    return ''.join([chr(int(i)+97) for i in str(age)])

print(f'test1 = {soultion(23)}')
print(f'test2 = {soultion(51)}')
print(f'test3 = {soultion(100)}')