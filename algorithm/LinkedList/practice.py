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
            현재노드 = 현재노드.next

        return f'[{s[:-2]}]'

    def append(self, data):
        새로운노드 = Node(data)
        self.tail.next = 새로운노드
        self.tail = 새로운노드
        self.데이터수 += 1

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