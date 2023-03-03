def getMelody(m):
    m = m.replace('C#','c')
    m = m.replace('D#','d')
    m = m.replace('F#','f')
    m = m.replace('G#','g')
    m = m.replace('A#','a')
    return m

def solution(m, musicinfos):
    m = getMelody(m)
    d = dict()
    
    for i,mi in enumerate(musicinfos):
        start,end,title,melody = mi.split(',')
        start,end = list(map(int,start.split(':'))), list(map(int,end.split(':')))
        playtime = (end[0]-start[0])*60 + (end[1]-start[1])
        melody = getMelody(melody)
        melody = melody*(playtime//len(melody))+melody[:playtime%len(melody)]
        d[title] = [i,playtime,melody,False]
        
    for info in d.values():
        if m in info[-2]:
            info[-1] = True
            
    thatSongJustNow = list(filter(lambda x: d[x][-1], d.keys()))
    
    if len(thatSongJustNow) == 0:
        return "(None)"
    else:
        return max(thatSongJustNow, key=lambda x: (d[x][1],-d[x][0]))
    
print(f'test1 = {solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])}')
print(f'test2 = {solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])}')
print(f'test3 = {solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])}')