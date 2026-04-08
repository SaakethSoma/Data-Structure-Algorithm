'''
Linked List : 
node : data | pointer | 
    - data
    - next
    linked list is like connecting of all nodes 
    Each node has: -> data(values)
                   -> pointer(to store next node address)
unlike arrays: -> no contiguous memory allocation
                -> dynamic size
operations: -> insertion at beginning
-> insertion at end
-> Deletion at beginning
-> Deletion at end
-> searching for an element
-> displaying linked list  

time complexity: -> insertion at beginning: O(1)
                 -> insertion at end: O(n)
                 -> searching for an element: O(n)

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    def delete_from_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next

    
    def delete_at_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def insert_at_position(self,pos,data):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos-1):
            if temp is None:
                return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    
    def delete_value(self,key):
        if self.head is None:
            return
    
        if self.head.data == key:
            self.head = self.head.next
            return
    
        temp = self.head
        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                return
            temp = temp.next
    
    def delete_at_position(self,pos):
        if pos == 0:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(pos-1):
            if temp.next is None:
                return
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def get(self,pos):      # 5->10->15->20          #pos=2
        temp = self.head    # temp = 5  # temp = 10
        for _ in range(pos):  #(2) 1st iter     2nd iter  
            if temp is None: 
                return None
            temp = temp.next   #temp = 10     #temp = 15
        return temp.data if temp else None 
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next #store next node
            curr.next = prev      #reversed linked list
            prev = curr      #move to previous node
            curr = next_node  #move curr
        self.head = prev   

    #function to detect cycle(floyd's Algorithm)
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.nextfast = fast.next.next
            if slow == fast:
                return True
        return False  
        

ll= LinkedList()

ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_position(2,15)
ll.delete_value(30)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.display()         
print(ll.search(20))  
ll.reverse()
ll.display()
ll.delete_from_beginning()
ll.display()          

ll.delete_at_end()
ll.display()   

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3
ll = LinkedList()
ll.head = n1
print(ll.has_cycle())

