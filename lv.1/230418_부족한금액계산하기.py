def solution(price, money, count):
    lack = money-sum([i*price for i in range(1,count+1)])
    return -lack if lack<0 else 0