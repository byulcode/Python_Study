from itertools import combinations


def is_prime_number(x):  # 소수 판정 함수
    a = 0
    for i in range(2, x):
        if x % i == 0:
            a += 1
    if a > 0:
        return False
    else:
        return True


def solution(nums):
    answer = 0
    for i in combinations(nums, 3):  # 원소 3개씩 조합
        total = sum(i)
        if(is_prime_number(total)):
            answer += 1
    return answer


lst = [1, 2, 7, 6, 4]
print(solution(lst))
