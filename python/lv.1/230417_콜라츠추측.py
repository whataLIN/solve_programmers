def solution(num):
    
    i=0
    while 0<=i and i<=500:
        if i>=500:       #500번 이상이면 break
            i=-1
            break
        if num==1: break #num이 1이면 break
        
        num=((num*3)+1 if num%2 else num/2)
        i+=1

    return i

