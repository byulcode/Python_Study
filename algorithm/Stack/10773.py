 #백준 10773 제로
from sys import stdin
stack = []

N = int(stdin.readline())
stack_sum = 0
for _ in range(N):
    num = int(stdin.readline())
    
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
    
print(sum(stack))

