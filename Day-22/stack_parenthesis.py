def isinvalid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for ch in s: 
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return len(stack) == 0

s = input("Enter the string of brackets: ")

if isinvalid(s):
    print("Valid parentheses")
else:
    print("Invalid parentheses")


def isBalanced(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0
s = input("Enter the string of parentheses: ")
if isBalanced(s):
    print("Valid parentheses")
else:
    print("Invalid parentheses")

    

