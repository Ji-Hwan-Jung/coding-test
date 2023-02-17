import re

def solution(files):
    p = re.compile("(^\D+)(\d{0,5})(.*)")
    file_list = {}
    
    for i,f in enumerate(files):
        head,number,tail = p.findall(f)[0]
        file_list[f] = [head.lower(),int(number),i]

    files.sort(key=lambda x: (file_list[x][0],file_list[x][1],file_list[x][2]))

    return files

print(f'test1 = {solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])}')
print(f'test2 = {solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])}')