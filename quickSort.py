arr = [3,7,8,1,5,9,6,10,2,4]
arr2 = [2,6,4,13,34,25,22]
#퀵정렬 --> T(n) = O(n lgn)
#일반적인 방식
def quickSort(data, start, end): 
    if start >= end: #원소가 1개인 경우
        return
    pivot = start
    left = start+1 #왼쪽 출발지점
    right = end     #오른쪽 출발지점

    while(left <= right): #엇갈릴 때까지 반복
        while(left <= end and data[left] <= data[pivot]): #키 값보다 큰 값을 만날 때까지(내림차순은 부등호 방향만 바꾸기)
            left += 1
        while(data[right] >= data[pivot] and right>start): #키 값보다 작은 값을 만날 때까지
            right -=1
        if(right<left):
            data[right], data[pivot] = data[pivot], data[right]
        else:
            data[left], data[right] = data[right], data[left]

    quickSort(data,start,right-1)
    quickSort(data,right+1,end)

#파이썬의 장점을 살린 방식
def quick_sort(data):
    if len(data) <= 1: #리스트의 원소가 하나 이하일 경우 종료
        return data
    pivot = data[0]
    tail = data[1:] #피벗을 제외한 리스트

    left_side = [x for x in tail if x> pivot] #분할된 왼쪽부분
    right_side = [x for x in tail if x <= pivot] #분할된 오른쪽 부분(부등호 바꿈 오름차순)

    #분할 이후 양쪽 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] +quick_sort(right_side)



quickSort(arr, 0, len(arr)-1)
print(arr)
print(quick_sort(arr2))
