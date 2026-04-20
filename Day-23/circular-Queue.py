'''
Cirucular Queue : it is a data structure that follos the FIFO principle but the last 
position is connected to the first position to make a circle(ring structure).

Instead of moving in one direction like in a normal queue, it wraps around using modulo(%)
operation.

working of circular queue: It uses two pointers
1) front: points to the first element in the queue
2) rear: points to the last element in the queue

Formula : 
- Insertion: (rear + 1) % size
- Deletion: (front + 1) % size
This makes movement circular

Why do we need circular queue?
Queue size = 5
insert : 10,20,30,40,50 -> [10,20,30,40,50]
delete starting 2 values : 10,20 -> [_,_,30,40,50] 30-> front, 50-> rear

now , if i am going to insert 2 values then overflow will occur

Solution Circular Queue: Instead of wasting space , we can reuse it 
Add 60 -> rear = (rear+1) % size = (4+1) % 5 = 5%5 = 0
[60,_,20,30,40] 60-> rear, 20-> front

Advantages of Circular Queue:
1)efficicent memory utilization
2) better performance 
3) ideal for continuous data flow
4) no false overflow

Disadvantages of Circular Queue:
1) slightly more complex implementation

''' 

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def is_empty(self):
        return self.front == -1
    
    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data
        print(f"Inserted: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        data = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Deleted: {data}")
        return data
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue elements: ", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()

cq.dequeue()
cq.display()

cq.enqueue(40)
cq.enqueue(50)
cq.display()

cq.enqueue(60)  
cq.display()

print("Front element: ", cq.peek())

cq.dequeue()
cq.dequeue()
cq.display()