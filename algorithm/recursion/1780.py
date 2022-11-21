# 백준 1780 종이의 개수

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [0] * 3  # 각 종이의 개수


def func(row, col, n):
    check = graph[row][col]
    for i in range(row, row + n):
        for j in range(col, col + n):
            if check != graph[i][j]:
                check = -2
                break

    if check == -2:
        n = n // 3
        func(row, col, n)
        func(row, col + n, n)
        func(row, col + 2 * n, n)
        func(row + n, col, n)
        func(row + 2 * n, col, n)
        func(row + n, col + n, n)
        func(row + n, col + n * 2, n)
        func(row + n * 2, col + n, n)
        func(row + n * 2, col + n * 2, n)
    elif check == -1:
        result[0] += 1
    elif check == 0:
        result[1] += 1
    else:
        result[2] += 1


func(0, 0, n)
for a in result:
    print(a)
