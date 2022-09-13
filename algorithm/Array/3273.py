#백준 3273 두 수의 합
# 합-숫자가 배열에 있다면 그거 써!
arr_len = int(input())
arr = input().split()
arr = list(map(int, arr))
compare_num = int(input())

compare_arr = [0] * arr_len
cnt = 0

for i in range(arr_len):
    compare_arr[i] = arr[i]
    if compare_num - arr[i] in compare_arr:
        cnt += 1

print(cnt)
