# 백준 7562 나이트의 이동
from sys import stdin
from collections import deque

# 나이트의 좌표 이동
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]


def bfs():
    queue = deque()
    queue.append((start_x, start_y))
    while queue:
        cur_x, cur_y = queue.popleft()
        if cur_x == end_x and cur_y == end_y:
            return graph[cur_x][cur_y] - 1
        for i in range(8):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if 0 <= nx < L and 0 <= ny < L and graph[nx][ny] == 0:
                graph[nx][ny] = graph[cur_x][cur_y] + 1
                queue.append((nx, ny))


n = int(stdin.readline().rstrip())
for _ in range(n):
    L = int(stdin.readline().rstrip())
    graph = [[0] * L for _ in range(L)]
    start_x, start_y = map(int, stdin.readline().rstrip().split())
    end_x, end_y = map(int, stdin.readline().rstrip().split())
    graph[start_x][start_y] = 1
    print(bfs())
