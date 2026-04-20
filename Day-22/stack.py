'''
stack : Data structure that follows the Last In First Out (LIFO) principle. 
Last element inserted is the first one to be removed.

ex : stack of plates, stack of books, stack of cards, etc.
operations : 1) push : add an element to the top of the stack
             2) pop : remove the top element from the stack
             3) peek : view the top element 
             4) isEmpty : check if the stack is empty
             5) size : return the number of elements in the stack  

applications of stack: 1) browsing 
                        2) undo/redo functionality in text editors
                        3) expression evaluation (infix, postfix, prefix)
                        4) function call management (call stack)
                        5) reversing a string or data structure 
             
IDEA : 1) use opening brackets -> (, {, [
       2) when you see closing brackets 
          -> check the top of the stack
          -> if it matches -> pop the top element





class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if  self.is_Empty():
            return "stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if  self.is_Empty():
            return "stack is empty"
        return self.stack[-1]
    
    def is_Empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print("top element:", s.peek())
print("popped element:", s.pop())
print("size of stack:", s.size())
print("is empty:", s.is_Empty())

'''

from collections import deque
stack = deque()

#push elements to stack
stack.append(10)
stack.append(20)


print(stack)

#pop element from stack
stack.pop()
print(stack)

#peek
print(stack[-1])