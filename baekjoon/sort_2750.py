#백준 #2750 수 정렬하기
N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))
   
array = sorted(array)
for i in array:
    print(i)
