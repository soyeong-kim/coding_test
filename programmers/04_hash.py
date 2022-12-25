# 위장
'''
clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	
answer=5
'''
def solution(clothes):
    dic = {}
    for clothe in clothes:
        dic[clothe[1]] = dic.get(clothe[1], 0) + 1

    s = 1
    for i in dic.values():
        s *= i+1
    
    return s-1
