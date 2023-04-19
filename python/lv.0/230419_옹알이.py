def solution(babbling):
    
    can=['aya','ye','woo','ma']
    total=0
    for b in babbling:
        for c in can:
            if c in b:
                b=b.replace(c," ")
                test=b[:].strip(" ")
                if test=="":
                    total+=1
                    break
            else: pass
            
    return total

    #아니... 0단계인데 생각보다 어렵다; 1단계같음