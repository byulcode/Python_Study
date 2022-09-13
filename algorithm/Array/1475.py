#백준 10808 방 번호
num = list(input())
arr = [0] * 10 

for i in range(len(num)):
    if num[i] == '6' or num[i] == '9':
        if arr[6] <= arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[int(num[i])] += 1

print(max(arr))