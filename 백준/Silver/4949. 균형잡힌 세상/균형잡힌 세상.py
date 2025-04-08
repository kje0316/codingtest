import sys

while True:
    text = input()
    if text == '.':
        break
    stack = []
    answer = True
    for c in text:
        if c == '(' or c == '[':
            stack.append(c)
        elif c ==')':
            if not stack or stack[-1] != '(':
                answer = False
                break
            stack.pop()
        
        elif c == ']':
            if not stack or stack[-1] != '[':
                answer = False
                break
            stack.pop()
    if answer and not stack:
        print('yes')
    else:
        print('no')