def solution1(numbers):
    return [i*2 for i in numbers]

def solution2(numbers):
    return list(map(lambda x: x*2, numbers))

test1 = solution1([1,2,3,4,5])
test2 = solution2([1,2,100,-99,1,2,3])

print(f'test1 = {test1}')
print(f'test2 = {test2}')