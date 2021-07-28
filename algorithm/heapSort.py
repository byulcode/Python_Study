#힙 정렬 : 힙 트리 구조를 이용하는 정렬 방법. 큰 값이 부모노드가 된다
# T(n) = O(n lgn)
#최대힙 : 최대값 구할 때 이용  최소힙:최소값 구할 때 이용
heap = [7,6,5,8,3,5,9,1,6]

def heap_sort(a):
    for i in range(1, len(a)): #최대힙 만들기
        c = i
        while c!= 0:
            root = (c-1) // 2
            if a[root] < a[c]:
                a[root], a[c] = a[c], a[root]
            c = root

    for j in range(len(a)-1, -1, -1): #힙 만들기
        #가장 큰 값 맨 뒤로 보내기
        a[0], a[j] = a[j], a[0]
        root = 0
        c = 1

        while c<j:
            #자식 중에서 더 큰 값 찾기
            c = 2 * root +1
            if c<j-1 and a[c] < a[c+1] :    
                c+=1

            if c<j and a[root] < a[c]:
                a[root], a[c] = a[c], a[root]
            
            root = c

heap_sort(heap)
print(heap)