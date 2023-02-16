def solution(record):
    types = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    users = {}
    result = []
    
    for r in record:
        arr = r.split()
        if arr[0] in ["Enter","Change"]:
            users[arr[1]] = arr[2]
    
    for r in record:
        arr = r.split()
        if arr[0] != "Change":
            result.append(f"{users[arr[1]]}{types[arr[0]]}")
            
    return result

print(f'test1 = {solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])}')