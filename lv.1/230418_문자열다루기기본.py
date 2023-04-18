def solution(s):
    if len(s)==4 or len(s)==6:
        try:
            s=int(s)
            return True
        except: return False
    else: return False

#좀더 간략화도 가능할듯

#230418=============
def solution(s):
    try:
        int(s)
    except:
        return False
    
    return len(s)==4 or len(s)==6