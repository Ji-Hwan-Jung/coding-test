def solution(elements):
    elements = elements*2
    result = []

    for i in range(len(elements)//2):
        temp = []
        for j in range(len(elements)//2):
            temp.append(sum(elements[j:j+i+1]))
        for n in set(temp):
            result.append(n)

    return len(set(result))


print(f'test1 = {solution([7,9,1,1,4])}')