def solution(cards1, cards2, goal):
    
    for target in goal:
        if cards1 and target==cards1[0]:
            cards1.pop(0)
            answer='Yes'
        elif cards2 and target==cards2[0]:
            cards2.pop(0) 
            answer='Yes'
        else: return 'No'
      
    return answer

'''
원래 아이디어 : 뭉치 중 일치하는 거 있으면 del하고서 재귀함수로 처리하려고 함
근데 answer 정의 문제 때문에 for문으로 돌림...
재귀는 꾸준히 도전해볼 것.
'''