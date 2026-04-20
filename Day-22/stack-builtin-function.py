#By using linked list(Built-in)

stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("stack after peek :", stack)
print("stack after pop :", stack.pop())

#top element
top = stack[-1]
print("top element:", top)

#is stack empty
print("is stack empty:", len(stack) == 0)

#size of stack
print("size of stack:", len(stack))