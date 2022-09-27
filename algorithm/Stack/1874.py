from sys import stdin

N = int(stdin.readline())
stack = []
answer = []

cur_num = 1
flag = 0
for i in range(N):
    num = int(stdin.readline())
    while cur_num <= num: #입력받은 정수값보다 작을 경우 계속 push
        stack.append(cur_num)
        answer.append('+')
        cur_num += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        flag = 1

if flag == 0:
    for i in answer:
        print(i)
else:
    print('NO')

    