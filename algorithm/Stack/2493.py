#백준 2493 탑
from sys import stdin

N = int(stdin.readline())
top_list = list(map(int, stdin.readline().rstrip().split()))  #입력받은 탑들
stack = [] # [[index, top], [...]]
answer = [0] * N #수신할 탑을 저장한 배열

for i in range(N):
    while stack:
        if stack[-1][1] <= top_list[i]:
            stack.pop()
            
        else:
            answer[i] = stack[-1][0] + 1
            break
        
    if not stack: #비교할 값이 없는 경우
        answer[i] = 0
    stack.append([i, top_list[i]])

print(*answer)