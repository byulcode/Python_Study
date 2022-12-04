# 백준 11728 배열 합치기(Merge Sort)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = []

aidx = 0
bidx = 0
for i in range(n + m):
    if n == aidx:
        result.append(b[bidx])
        bidx += 1
    elif m == bidx:
        result.append(a[aidx])
        aidx += 1
    elif a[aidx] < b[bidx]:
        result.append(a[aidx])
        aidx += 1
    else:
        result.append(b[bidx])
        bidx += 1

for num in result:
    print(num, end=" ")
