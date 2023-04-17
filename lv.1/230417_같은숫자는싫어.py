def solution(arr):
    # 바로 직전 추가한 값과 같으면 pass, 아니면 append
    
    answer = []
    answer.append(arr[0])
    ans_idx=0
    
    for num in arr:
        if [num]!=answer[-1:]: 
            answer.append(num)
        
    return answer

"""
빈 리스트에서 -1:로 슬라이싱해도 ㄱㅊ!!!!!!!!!!!!
"""