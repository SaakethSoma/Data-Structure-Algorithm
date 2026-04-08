class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #inserting operations
    #inserting at the beginning
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head :
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_at_pos(self, data, pos):
        new_node = Node(data)

        if pos == 0:
            self.insert_at_beginning(data)
            return

        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        new_node.next = temp.next   # correct forward link

        if temp.next:
            temp.next.prev = new_node   # fix backward link

        temp.next = new_node
        new_node.prev = temp


    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()
dll.insert_at_beginning(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_pos(15, 1)

dll.display()