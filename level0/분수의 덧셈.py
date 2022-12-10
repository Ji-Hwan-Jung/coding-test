import fractions

# fractions 모듈 사용
def solution1(denum1, num1, denum2, num2):
    return fractions.Fraction(denum1,num1) + fractions.Fraction(denum2, num2)

# 모듈 사용 X
def solution2(denum1, num1, denum2, num2):
    numerator = denum1*num2+denum2*num1
    denominator = num1*num2
    gcd = 0
    
    for i in range(min(numerator,denominator),-1,-1):
        if denominator%i == 0 and numerator%i == 0:
            gcd = i
            break
            
    return [numerator//gcd, denominator//gcd]

test1 = solution1(1,2,3,4)
test2 = solution2(9,2,1,3)

print(f'test1 : {[test1.numerator, test1.denominator]}')
print(f'test2 : {test2}')