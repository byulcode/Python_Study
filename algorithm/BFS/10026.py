# 백준 10026 적록색약
from collections import deque
from sys import stdin


def bfs(x, y, color_type):
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == color_type and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


N = int(stdin.readline())
graph = [list(stdin.readline()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
queue = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 색약이 아닐 떄
cnt = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = graph[i][j]
            bfs(i, j, color)
            cnt += 1

# 색약일 때
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

color_weakness = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = graph[i][j]
            bfs(i, j, color)
            color_weakness += 1

print(cnt, color_weakness)
