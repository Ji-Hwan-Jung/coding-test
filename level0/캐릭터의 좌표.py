def solution(keyinput, board):
    direction = {"up": [0,1], "down": [0,-1], "left": [-1,0], "right": [1,0]}
    max_x,max_y = [i//2 for i in board]
    x,y = 0,0
    
    for dir in keyinput:
        dx,dy = direction[dir][0],direction[dir][1]
        if abs(x+dx)>max_x or abs(y+dy)>max_y: continue
        x+=dx
        y+=dy
    
    return [x,y]

print(f'test1 = {solution(["left", "right", "up", "right", "right"], [11, 11])}')
print(f'test2 = {solution(["down", "down", "down", "down", "down"], [7, 9])}')