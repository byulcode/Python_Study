# 백준 2206 벽 부수고 이동하기
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    graph.append(list(map(int, input().rstrip())))


def bfs(x, y, w):
    queue = deque()
    queue.append((x, y, w))

    while queue:
        a, b, wall = queue.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if a == N - 1 and b == M - 1:
            return visited[a][b][wall]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 다음 방문할 곳이 벽이고, 벽을 아직 부순 적 없음
                if graph[nx][ny] == 1 and wall == 0:
                    visited[nx][ny][1] = visited[a][b][0] + 1
                    queue.append((nx, ny, 1))
                # 다음 방문할 곳이 벽이 아니고, 아직 방문한 적 없음
                elif graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[a][b][wall] + 1
                    queue.append((nx, ny, wall))
    return -1


print(bfs(0, 0, 0))
