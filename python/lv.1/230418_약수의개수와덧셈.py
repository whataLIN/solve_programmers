def solution(left, right):
        
    return sum([-i if len([j for j in range(1,i+1) if not i%j])%2 else i for i in range(left, right+1)])

#좀 더 알아보기 쉽게 가능 ?,,,