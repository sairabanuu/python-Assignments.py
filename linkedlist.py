class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    # Print list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
        
def insert_at_beginning(self, data):
    new = Node(data)
    new.next = self.head
    self.head = new
    
def insert_at_position(self, index, data):
    if index == 0:
        self.insert_at_beginning(data)
        return

    new = Node(data)
    temp = self.head
    for _ in range(index - 1):
        if not temp:
            return  # index out of range
        temp = temp.next

    new.next = temp.next
    temp.next = new
    
    
def reverse(self):
    prev = None
    curr = self.head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    self.head = prev
