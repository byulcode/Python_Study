#삽입 정렬
#시간 best : n-1    worst : n(n-1)/2    --> T(n) = O(N^2)
#삽입정렬 오름차순
def insertionSort_ASC(array):
    for i in range(1, len(array)):
        val = array[i]
        pos = i
        while pos>0 and array[pos -1] > val:
            array[pos] = array[pos-1]
            pos -= 1
        array[pos] = val
    return array
      
#삽입정렬 내림차순
#ef insertionSort_DESC(array):

#선택정렬 --> T(n) = O(N^2)
def selection_sort(array):
    for i in range(len(array)-1):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

array = [1,10,5,8,7,6,4,3,2,9]
print(insertionSort_ASC(array))
print(selection_sort(array))