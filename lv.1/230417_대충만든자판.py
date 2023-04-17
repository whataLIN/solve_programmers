def solution(keymap, targets):
    
    """
    1. 자판 탐색하면서 문자 당 눌러야 하는 최소값을 딕셔너리로 만들기
    2. 타겟 단어들을 한글자씩 탐색
        - 딕셔너리에 해당 문자 있으면 resultnum에 더해줌
        - 없으면 resultnum=0
    """

    whatIsWhere={"None":-1}

    for nthKey in range(len(keymap)):
        for indexOfChar in range(len(keymap[nthKey])):
            keyString=keymap[nthKey]
            keyChar=keyString[indexOfChar]
            if (keyChar not in whatIsWhere):
                whatIsWhere[keyChar]=indexOfChar
            elif (keyChar in whatIsWhere):
                if whatIsWhere[keyChar]>indexOfChar:
                    whatIsWhere[keyChar]=indexOfChar

    answer=[]
    
    for nthTarget in range(len(targets)):
        resultnum=0
        targetString=targets[nthTarget]
        for charIndex in range(len(targetString)):
            targetChar=targetString[charIndex]
            if targetChar not in whatIsWhere:
                resultnum=-1
                break
            else:
                resultnum+=(whatIsWhere[targetChar]+1)
        answer.append(resultnum)

    return answer

"""
이경우 문자열을 돌면서 키패드에서 찾는거보단 키패드에 대한 정보를 아예 구축해놓는 게 더 빠름
"""