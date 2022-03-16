# 더 맵게. heap을 이용한 스코빌 지수 섞기
import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()
    heapq.heapify(scoville)  # scoville을 heap으로 변경

    while scoville[0] < K:

        if len(scoville) < 2:  # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
            return -1

        min_ = heapq.heappop(scoville)  # 가장 낮은 스코빌지수
        min_2 = heapq.heappop(scoville)  # 두번째로 안매운 스코빌지수
        heapq.heappush(scoville, min_ + min_2 * 2)  # 두 음식 섞기
        answer += 1

    return answer
