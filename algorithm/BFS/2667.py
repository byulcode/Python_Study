# 백준 2667 단지번호
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    each_cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and visit[nx][ny] == 0:
                visit[nx][ny] = True
                q.append((nx, ny))
                each_cnt += 1
    return each_cnt


N = int(input())
visit = [[False] * N for _ in range(N)]
graph = [list(map(int, input().rstrip())) for _ in range(N)]
cnt = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visit[i][j]:
            cnt.append(bfs(i, j))

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)
