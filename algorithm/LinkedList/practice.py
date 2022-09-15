#노드 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        init = Node('init')
        self.head = init
        self.tail = init

        self.현재노드 = None
        self.데이터수 = 0
    
    def __len__(self):
        return self.데이터수

    def __str__(self):
        현재노드 = self.head
        현재노드 = 현재노드.next 
        s = ''
        for i in range(self.데이터수):
            s += f'{현재노드.data}, '
            현재노드 = 현재노드.next #순회

        return f'[{s[:-2]}]'
    
    def __iter__(self): #for문으로 노드를 출력할 수 있게 해줌
        현재노드 = self.head
        현재노드 = 현재노드.next

        while 현재노드:
            yield 현재노드.data
            현재노드 = 현재노드.next

    def append(self, data): #노드를 맨 뒤에 추가
        새로운노드 = Node(data)
        self.tail.next = 새로운노드
        self.tail = 새로운노드
        self.데이터수 += 1

    def insert(self, input_index, input_data):
        현재노드 = self.head

        for i in range(input_index):
            현재노드 = 현재노드.next
        신규노드 = Node(input_data)
        신규노드.next = 현재노드.next
        현재노드.next = 신규노드   

        self.데이터수 += 1

    def pop(self): 
        마지막값 = self.tail.data
        현재노드 = self.head

        for i in range(self.데이터수):
            if 현재노드.next is self.tail:
                self.tail = 현재노드
                break
            현재노드 = 현재노드.next

        self.데이터수 -= 1
        return 마지막값
        
    def find(self, data):
        index = -1 #init노드가 맨 앞에 있기 때문
        현재노드 = self.head

        for i in range(self.데이터수 + 1): #init 노드 때문에 +1
            if 현재노드.data == data:
                self.tail = 현재노드
                return index
            index += 1
            현재노드 = 현재노드.next
        return -1 #못 찾을 경우

l = LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.append(15)

print(l.head.data)
print(len(l))
print(l)
print(l.pop())
print(l)
print(l.find(20))
print(l.find(18))
for i in l:
    print(i)
l.insert(2, 10000)
print(l)