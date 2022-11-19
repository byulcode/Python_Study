# 백준 2468 안전 영역
import sys
from collections import deque

N = int(input())
height = []
maximum = 0
result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    height.append(list(map(int, input().split())))
    for j in range(N):
        if height[i][j] > maximum:
            maximum = height[i][j]


def bfs(x, y, h, visit):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and height[nx][ny] > h:
                queue.append((nx, ny))
                visit[nx][ny] = True


for i in range(maximum):
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for j in range(N):
        for k in range(N):
            if height[j][k] > i and not visited[j][k]:
                bfs(j, k, i, visited)
                cnt += 1
    if result < cnt:
        result = cnt
print(result)
