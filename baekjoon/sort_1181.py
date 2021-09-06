# 백준 #1181 단어 정렬
# sys.stdin.readline() 사용 -> 132ms
# input() 사용 -> 1072ms

import sys
N = int(sys.stdin.readline())  # 입력받을 단어 수
word_list = []

for _ in range(N):
    word_list.append(sys.stdin.readline().strip())

# set: 중복 제거(집합이기 때문에 중복 안됨)
word = list(set(word_list))

# len(x)를 설정해 단어 길이 먼저 정렬 후 사전순으로 정렬
word.sort(key=lambda x: (len(x), x))

for i in word:
    print(i)
