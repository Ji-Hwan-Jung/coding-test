def solution(rsp):
    rsp_dict = {'0': '5', '2': '0', '5': '2'}
    return ''.join([rsp_dict[i] for i in rsp])

print(f'test1 = {solution("2")}')
print(f'test2 = {solution("205")}')