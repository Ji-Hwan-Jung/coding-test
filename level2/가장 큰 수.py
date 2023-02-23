# 로직은 맞는데 시간초과 발생 (시간복잡도 안 좋음)
def temp(numbers):
    nums = list(map(str, numbers))
    
    while True:
        temp = [s for s in nums]
        for i in range(len(numbers)-1):
            a,b = temp[i],temp[i+1]
            if a+b < b+a:
                temp[i],temp[i+1] = b,a
        if nums == temp:
            break
        else:
            nums = temp
    
    return str(int(''.join(nums)))

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(reverse=True,key=lambda x: x*3)
    return "0" if numbers[0] == "0" else ''.join(numbers)

print(f'test1 = {solution([6,10,2])}')
print(f'test2 = {solution([3,30,34,5,9])}')