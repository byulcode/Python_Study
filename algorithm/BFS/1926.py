# 백준 1926 그림
from collections import deque
from sys import stdin


def bfs(x, y):
    each_cnt = 1  # 처음 방문한 노드를 포함하므로 1부터 시작
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    each_cnt += 1
    return each_cnt


N, M = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
paint = []  # 그림의 개수 및 크기 저장

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            paint.append(bfs(i, j))

print(len(paint))
print(max(paint))
