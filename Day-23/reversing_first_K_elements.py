'''
# reversing first K elements of a queue
# dq = [1,2,3,4,5] , k= 3 , output : [3,2,1,4,5]

from collections import deque
def reverse(dq, k):
    stack =[]
    for _ in range(k):
        stack.append(dq.popleft())
    while stack:
        dq.appendleft(stack.pop())

    for _ in range(len(dq)-k):
        dq.append(dq.popleft())
    return dq

dq = deque([1,2,3,4,5])
k = 3
print("Result : ", reverse(dq, k))
'''

#is palindrome using deque
from collections import deque 
def is_palindrome(s):
    dq = deque(s)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
s = "madam"
print("Palindrome : ", is_palindrome(s))