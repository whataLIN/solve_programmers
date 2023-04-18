def solution(phone_number):
    return phone_number.replace(phone_number[:-4],"*"*len(phone_number[:-4]))


"""
문자열 곱셈은 떠올렸는데 왜 덧셈까지는 생각 못했을까..
"""