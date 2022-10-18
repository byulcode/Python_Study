# 백준 4949 균형잡힌 세상
while True:
    text = input()
    if text == '.':
        break
    stack = []
    isValid = True

    for a in text:
        if a == '(' or a == '[':
            stack.append(a)
        elif a == ')':
            if not stack or stack[-1] != '(':
                isValid = False
                break
            else:
                stack.pop()
        elif a == ']':
            if not stack or stack[-1] != '[':
                isValid = False
                break
            else:
                stack.pop()
    if not stack and isValid:
        print("yes")
    else:
        print("no")
