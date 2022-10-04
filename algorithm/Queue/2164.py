# 백준 2164 카드2
from sys import stdin
from collections import deque

N = int(stdin.readline())

q = deque([i for i in range(1, N+1)])

while len(q) != 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])
