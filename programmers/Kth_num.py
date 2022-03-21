'''
K번째 수
'''

def solution(array, commands):
    answer = []
    command = []

    for i in commands:
        command.append(i)

    for c in command:
        res = array[c[0]-1:c[1]]
        res.sort()
        answer.append(res[c[2]-1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))

'''
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
'''

'''
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''