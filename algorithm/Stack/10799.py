# 백준 10799 쇠 막대기
from sys import stdin

pipes = stdin.readline().rstrip()

stack = []
result = 0
for i in range(len(pipes)):
    if pipes[i] == '(':
        stack.append(pipes[i])
    else:
        stack.pop()
        if pipes[i - 1] == '(':
            result += len(stack)
        else:
            result += 1
print(result)
