# 백준 3986 좋은 단어
from sys import stdin

N = int(stdin.readline().rstrip())
cnt = 0
for i in range(N):
    word = stdin.readline().rstrip()
    stack = []
    for a in word:
        if stack and stack[-1] == a:
            stack.pop()
        else:
            stack.append(a)
    if not stack:
        cnt += 1
print(cnt)
