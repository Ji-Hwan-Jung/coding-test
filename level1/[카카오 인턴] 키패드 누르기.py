def solution(numbers, hand):
    l_cur = '*'
    r_cur = '#'
    points = {1: [0,0], 2: [0,1], 3: [0,2], 4: [1,0], 5: [1,1], 6: [1,2], 7: [2,0], 8: [2,1], 9: [2,2], '*': [3,0], 0: [3,1], '#': [3,2]}
    answer = []
    
    
    for i in numbers:
        if i in range(1,8,3):
            answer.append("L")
            l_cur = i
        elif i in range(3,10,3):
            answer.append("R")
            r_cur = i
        else:
            lx, ly = points[l_cur]
            rx, ry = points[r_cur]
            mx, my = points[i]
            
            if (abs(lx-mx)+abs(ly-my)) < (abs(rx-mx)+abs(ry-my)):
                answer.append("L")
                l_cur = i
            elif (abs(lx-mx)+abs(ly-my)) > (abs(rx-mx)+abs(ry-my)):
                answer.append("R")
                r_cur = i
            else:
                if hand == "left":
                    answer.append("L")
                    l_cur = i
                else:
                    answer.append("R")
                    r_cur = i
                
    return ''.join(answer)

print(f'test1 = {solution([1,3,4,5,8,2,1,4,5,9,5],"right")}')
print(f'test2 = {solution([7,0,8,2,8,3,1,5,7,6,2],"left")}')
print(f'test3 = {solution([1,2,3,4,5,6,7,8,9,0],"right")}')