def solution(arr, divisor):
    arr.sort()
    answer = [arr for i in arr if arr%divisor]
    return answer if len(answer)>0 else [-1]

"""
arr
"""