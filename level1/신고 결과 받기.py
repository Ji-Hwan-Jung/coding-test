def solution(id_list, report, k):
    reported = {id: [] for id in id_list}
    report_num = {id: 0 for id in id_list}
    
    for e in report:
        accuser, accused = e.split()
        if accused not in reported[accuser]:
            reported[accuser].append(accused)
            report_num[accused] += 1
        
    for id in id_list:
        reported[id] = [report_num[i] for i in reported[id] if report_num[i] >= k]
            
    return [len(i) for i in reported.values()]

print(f'test1 = {solution(["muzi","frodo","apeach","neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)}')
print(f'test2 = {solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)}')