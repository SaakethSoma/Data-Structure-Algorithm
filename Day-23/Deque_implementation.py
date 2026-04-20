'''
Deque implimentaton usage of package Deque :
deque -> double ended queue
-> we can insert and delete elements from both ends front(left) and rear(right)

'''

from collections import deque
dq = deque()

#insert elements 
dq.append(10) 
dq.append(20)
dq.appendleft(5)

print("Deque after insertion: ", dq)

#delete elements
dq.pop()
print("after pop : ", dq)

dq.popleft()
print("after popleft : ", dq)

#add more element
dq.append(30)
dq.append(40)

print("final element :", dq)

#peek
print("front element : ", dq[0])
print("rear element : ", dq[-1])

#size
print("size:", len(dq))