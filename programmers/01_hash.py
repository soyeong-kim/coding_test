# 완주하지 못한 선수
'''
participant=["leo", "kiki", "eden"]
completion=["eden", "kiki"]
answer="leo"
'''
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[i+1]
