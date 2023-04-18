def solution(absolutes, signs):
    return sum([(abs if s else -abs) for abs, s in zip(absolutes, signs)])


"""
처음 코드
sum=0
for abs, s in zip(absolutes, signs):
    sum += abs if s else (abs*(-1))

만족스럽다^-^
"""