def solution1(num_list):
    temp = [i for i in num_list if i%2 == 0]
    return [len(temp), len(num_list)-len(temp)]

def solution2(num_list):
    temp = [i%2 for i in num_list]
    return [temp.count(0), temp.count(1)]

print(f'test1 = {solution1([1,2,3,4,5])}')
print(f'test2 = {solution2([1,3,5,7])}')