import datetime

def solution(a, b):
    d = datetime.datetime(2016,a,b)
    return d.strftime('%c')[0:3].upper()

print(f'test1 = {solution(5,24)}')