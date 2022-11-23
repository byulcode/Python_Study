# 백준 2630 색종이 만들기

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt = [0] * 2


def func(x, y, n):
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != check:
                check = -1
                break

    if check == -1:
        n = n // 2
        func(x, y, n)
        func(x + n, y, n)
        func(x, y + n, n)
        func(x + n, y + n, n)

    elif check == 0:
        cnt[0] += 1
    else:
        cnt[1] += 1


func(0, 0, N)
for res in cnt:
    print(res)
