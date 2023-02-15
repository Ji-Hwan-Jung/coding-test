from math import ceil

def solution(fees, records):
    answer = []
    stt,stf,ext,exf = fees
    t = {i[6:10]: 0 for i in records}
    
    for r in records:
        time, num, kind = r.split()
        h,m = map(int,time.split(':'))
        if kind == "IN":
            t[num] -= h*60+m
        else:
            t[num] += h*60+m
    
    for num,v in t.items():
        if v <= 0:
            t[num] += 24*60-1
            
    for num,time in sorted(t.items()):
        if time <= stt:
            answer.append(stf)
        else:
            answer.append(stf+(ceil((time-stt)/ext)*exf))
        
    return answer

print(f'test1 = {solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])}')
print(f'test2 = {solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])}')
print(f'test3 = {solution([1, 461, 1, 10],["00:00 1234 IN"])}')