def solution(s):
    leng = len(s)//2
    return s[leng] if len(s)%2 else s[leng-1:leng+1]

#else문 안쓰고도 할 수 있을까?