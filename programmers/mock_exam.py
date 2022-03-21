'''
모의 고사
1번 수포자 : 12345 반복
2번 수포자 : 21232425 반복
3번 수포자 : 3311224455 반복
'''

def solution(answers):
    students = {1:[1,2,3,4,5], 2: [2,1,2,3,2,4,2,5], 3 : [3,3,1,1,2,2,4,4,5,5]}
    score = {1:0, 2:0, 3:0}
    
    for i, answer in enumerate(answers):
        for key, val in students.items(): #key, val 한번에 for반복
            if answer == val[i % len(val)]:
                score[key] += 1
    
    highest = max(score.values())
    result = [key for key, value in score.items() if value == highest]
    
    return result