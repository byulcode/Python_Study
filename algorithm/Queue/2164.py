# 백준 2164 카드2
from sys import stdin
from collections import deque

N = int(stdin.readline())
q = deque([])

for i in range(N):
    q.append(i + 1)

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])
