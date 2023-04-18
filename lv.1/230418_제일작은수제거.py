def solution(arr):
    if len(arr)>1:
        arr.remove(min(arr))
    else: return [-1]
    return arr

"""
뭔가줄일방법없나...
"""