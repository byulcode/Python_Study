'''
w,h값에 따라 삭제되는 정사각형 수:
    if w == h : w or h 개
    if w != h : (w+h - (w, h의 최대공약수))개
'''
import math

def solution(w,h):
    s = 0 # 안멀쩡한 사각형 개수
    if w == h: s = w 
    elif w != h:
        s = w + h - math.gcd(w,h)
    
    answer = w * h - s
    return answer