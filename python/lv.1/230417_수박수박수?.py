def solution(n):
    answer=''
    for i in range(n):
        answer+='박' if i%2 else '수'
    return answer

"""
홀수번째는 무조건 수, 짝수번째는 짝이 오니까 answer string에 더해줌
n만큼 더하고 홀수면 자르는 방식은 코드가 길어질 것 같았음,,
"""