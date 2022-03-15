# 백준 2606 dfs or bfs 바이러스. dfs 이용할것! 다시해봐라..

visited = [False] * 9


def dfs(graph, n):
    return n


v = int(input())  # 컴퓨터 수(정점 수)
e = int(input())  # 간선 수
map = list()
for i in range(1, e+1):
    a = int(input())
    b = int(input())
    map[a][b] = 1


print(v, e, map[1][2])
