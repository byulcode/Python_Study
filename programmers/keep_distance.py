'''
<거리두기 확인하기>
대기실은 5개, 각 대기실은 5X5 크기 
P : 응시자 자리    O : 빈 테이블    X : 파티션
거리를 지키면 1 리턴 / 한 명이라도 안지키면 0 리턴

[문제 풀이]
- 대기실의 모든 자리를 탐색하면서 모든 P의 자리 찾기
- bfs를 돌면서 맨해튼 거리 2 이내에 P가 있는지 확인
- 거리 1에는 X,O만 올 수 있음. P가 있을 경우 0리턴
- 거리 1에 X가 있을 경우 탐색 그만해도 됨
'''
from collections import deque


def solution(places):
    answer = []

    return answer


def bfs(p):
    start = []  # P의 좌표들

    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    print(start)
    return 0


p = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                    "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

for place in p:
    bfs(place)
