# 백준 10828 스택
from sys import stdin
def push(x):
    stack.append(x)

def pop():
    if not stack:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)

def empty():
    return 0 if stack else 1

def top():
    return stack[-1] if stack else -1

stack = []
N = int(stdin.readline())

for _ in range(N):
    word = stdin.readline().rstrip().split()
    order = word[0]
    
    if order == 'push':
        push(word[1])
    elif order == 'pop':
        print(pop())
    elif order == 'size':
        print(size())
    elif order == 'empty':
        print(empty())
    else:
        print(top())
    