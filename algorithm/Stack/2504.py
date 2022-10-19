# 백준 2504 괄호의 값
s = input()
stack = []
tmp = 1
answer = 0

for i in range(len(s)):
    if s[i] == '(':
        tmp *= 2
        stack.append(s[i])
    elif s[i] == '[':
        tmp *= 3
        stack.append(s[i])

    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if s[i - 1] == '(':
            answer += tmp
        tmp //= 2
        stack.pop()  # pop도 까먹지 말고 꼭

    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if s[i - 1] == '[':
            answer += tmp
        tmp //= 3
        stack.pop()  # pop 까먹지 말기

if stack:
    answer = 0
print(answer)
