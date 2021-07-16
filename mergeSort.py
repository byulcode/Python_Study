#병합정렬 : 반으로 쪼개 나중에 합쳐서 정렬 --> O(n lgn) 보장
def merge_sort(arr):
    if len(arr)<2:
        return arr

    mid = len(arr) // 2     
    g1 = merge_sort(arr[:mid])  #재귀 호출로 첫 번째 그룹을 정렬
    g2 = merge_sort(arr[mid:])  #재귀 호출로 두 번째 그룹을 정렬

    sorted = []

    while g1 and g2:    #두 그룹에 모두 자료가 남아 있는 동안 반복
        if g1[0] < g2[0]:   #두 그룹의 맨 앞 자료값을비교
            sorted.append(g1.pop(0))
        else:
            sorted.append(g2.pop(0))
#아직 남아 있는 데이터들 추가
    while g1:
        sorted.append(g1.pop(0))
    while g2:
        sorted.append(g2.pop(0))
    return sorted

array = [1,5,8,6,2,4,7]
print(merge_sort(array))