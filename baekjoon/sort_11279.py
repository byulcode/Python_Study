# 백준 #11279 최대 힙, 시간제한 1초
# heapq 모듈 사용
# heapq 는 최소 힙으로 구현되어 있다
# input()보다 sys.stdin.readline()이 속도 더 빠름
import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:  # 원소가 존재하면
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-num, num))


# # 백준 #11279 최대 힙(처음 한 방법..시간 초과)
# def heap_sort(a):  # 최대 힙 정렬
#     for i in range(len(a)):
#         c = i
#         while c != 0:
#             r = (c-1)//2
#             if a[r] < a[c]:
#                 a[r], a[c] = a[c], a[r]
#             c = r


# number = int(input())
# array = list()
# for i in range(number):
#     n = int(input())  # 자연수면 배열에 추가, 0이면 배열에서 가장 큰 값 추가
#     if n > 0:
#         array.append(n)
#         heap_sort(array)
#     else:
#         if not array:
#             print(0)
#         else:
#             print(array.pop())
