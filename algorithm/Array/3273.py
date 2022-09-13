#백준 3273 두 수의 합
# 합-숫자가 배열에 있다면 그거 써!
from sys import stdin
arr_len = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
x = int(stdin.readline())

arr.sort()
left = 0
right = arr_len - 1
cnt = 0

while left < right:
    sum = arr[left] + arr[right]
    if sum > x:
        right -= 1
    elif sum < x:
        left += 1
    else:
        cnt += 1
        left += 1
        right -= 1
print(cnt)
