def solution(n):
    composite_numbers = 0
    
    for i in range(1,n+1):
        divisors = 0
        for j in range(1, i+1):
            if i%j == 0:
                divisors += 1
            if divisors > 2:
                composite_numbers += 1
                break
    return composite_numbers

print(f'test1 = {solution(10)}')
print(f'test2 = {solution(15)}')