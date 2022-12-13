# 백준 1012 유기농 배추
import sys
from collections import deque


def bfs(x, y, cur_graph):
    q = deque()
    q.append((x, y))
    while q:
        cnt_x, cnt_y = q.popleft()
        for i in range(4):
            nx = cnt_x + dx[i]
            ny = cnt_y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and cur_graph[nx][ny] == 1:
                q.append((nx, ny))
                cur_graph[nx][ny] = 0


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

input = sys.stdin.readline
T = int(input())
all_cnt = []
for i in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    cnt = 0
    for j in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1

    for a in range(N):
        for b in range(M):
            if graph[a][b] == 1:
                graph[a][b] = 0
                bfs(a, b, graph)
                cnt += 1
    all_cnt.append(cnt)

for cnt in all_cnt:
    print(cnt)
