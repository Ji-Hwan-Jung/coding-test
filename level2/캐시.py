def solution(cacheSize, cities):
    cities = list(map(lambda x: x.lower(),cities))
    cache = ['' for _ in range(cacheSize)]
    runtime = 0
    
    if cacheSize == 0:
        return 5*len(cities)
    
    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            runtime += 1
        else:
            cache.pop(0)
            cache.append(city)
            runtime += 5
            
    return runtime

print(f'test1 = {solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])}')
print(f'test2 = {solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])}')
print(f'test3 = {solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])}')
print(f'test4 = {solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])}')
print(f'test5 = {solution(2,["Jeju", "Pangyo", "NewYork", "newyork"])}')
print(f'test6 = {solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])}')