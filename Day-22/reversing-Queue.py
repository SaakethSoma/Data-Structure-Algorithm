'''
#reversing a queue ( by using stack(list))

from collections import deque
q = deque([1,2,3,4,5])
stack = []

#Step-1 : Push into stack
while q:
    stack.append(q.popleft())

#Step-2 : Enqueue back to queue
while stack:
    q.append(stack.pop())

print("Reversed Queue:", q)

'''

'''
#checking if Queue is empty or not
from collections import deque
q = deque([1,2,3,4,5])

if not q:
    print("Queue is empty")
else:
    print("Queue is not empty")

'''

#Implementing Queue using two stacks
class QueueUsingStacks:
    def __init__(self):
        self.s1 = [] #Enqueue 
        self.s2 = [] #Dequeue

    def enqueue(self, x):
        self.s1.append(x)
    
    def dequeue(self):
        if not self.s2: 
            while self.s1:
                self.s2.append(self.s1.pop())

        if not self.s2:
            return "Queue is empty"
        return self.s2.pop()
    
q = QueueUsingStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue()) #10
print(q.dequeue()) #20
print(q.dequeue()) #30
print(q.dequeue()) #Queue is empty