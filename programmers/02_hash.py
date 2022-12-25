# 폰켓몬
'''
nums=[3,1,2,3]
answer=2
'''
def solution(nums):
    count = len(nums)/2
    if len(set(nums))>=count:
        return count
    else:
        return len(set(nums))
