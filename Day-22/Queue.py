'''
Queue : Data structure that follows the First In First Out (FIFO) principle.

ex: queue of people waiting in line, Printer

operations : 1) enqueue : add an element to the rear of the queue
             2) dequeue : remove the front element from the queue
             3) peek : view the front element
             4) isEmpty : check if the queue is empty
             5) size : return the number of elements in the queue


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_Empty():
            return "queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_Empty():
            return "queue is empty"
        return self.queue[0]
    
    def is_Empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue:", q.queue)
print("dequeue:", q.dequeue())
print("peek:", q.peek())
print("size of queue:", q.size())
print("is empty:", q.is_Empty())

'''

from collections import deque

q = deque()
q.append(10)
q.append(20)
q.append(30)
print("Queue:", q)
print("dequeue:", q.popleft()) #removes the front element
print("peek:", q[0]) #view the front element
print("size of queue:", len(q))
print("is empty:", len(q) == 0)