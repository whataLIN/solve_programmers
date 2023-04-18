
def solution(arr1, arr2):
    
    result=[]
    for row in range(len(arr1)):
        temprow=[]
        for col in range(len(arr1[0])):
            # print(arr1[row][col])
            temprow.append(arr1[row][col]+arr2[row][col])
        result.append(temprow)
    
    return result

#zip으로 어케 할 수 있을 것 같음