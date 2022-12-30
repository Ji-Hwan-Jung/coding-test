def solution(id_pw, db):
    id, pwd = id_pw
    db = dict(db)
    
    if id in db:
        return "login" if pwd==db[id] else "wrong pw"
    return "fail"

print(f'test1 = {solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]])}')
print(f'test2 = {solution(["programmer01", "15789"],[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]])}')
print(f'test3 = {solution(["rabbit04", "98761"],[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]])}')