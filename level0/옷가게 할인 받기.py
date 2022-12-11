def solution(price):
    if price >= 500000:
        return int(price * 0.8)
    elif price >= 300000:
        return int(price * 0.9)
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price
    
print(f'test1 = {solution(150000)}')
print(f'test2 = {solution(580000)}')