def solution(wallpaper):
    
    """
    1. 파일 위치 탐색
    2. 제일 위/왼쪽에 있는 파일
    3. 제일 아래/오른쪽에 있는 파일
    4. 위에 있는 파일의 y좌표, 왼쪽에 있는 파일의 x좌표 가져옴
    5. 아래 있는 파일의 y좌표+1, 오른쪽에 있는 파일의 x+1좌표 가져옴
    6. 반환
    """

    filecoordX, filecoordY = [],[]

    #파일탐색
    for x in range(len(wallpaper)):      #열 차례로 탐색. y번째 열
        for y in range(len(wallpaper[0])):  #행 차례로 탐색. x번째 열
            if wallpaper[x][y]=="#":
                if not x in filecoordX:
                    filecoordX.append(x)
                if not y in filecoordY:
                    filecoordY.append(y)
            else: continue

    filecoordX.sort()
    filecoordY.sort()
    
    answer= [filecoordX[0], filecoordY[0], filecoordX[-1]+1, filecoordY[-1]+1 ]

    return answer


"""
처음엔 가장 왼쪽/위, 오른쪽/아래 파일 탐색해서 하나하나 좌표 반환받으려고 했었는데
이러면 코드가 너무 길어짐
-> 차라리 좌표를 전부 찾아서 좌표로 판단

바탕화면 크기가 커지고, 파일 개수가 더 많아지면 어떨까?
"""

"""
+) 230417. sort할필요 없이 min하면 됐군아 ... ...
"""