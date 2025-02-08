class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
            
            
class LinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        temp = self.head 
        if self.head is None:
            print('No items')
        while temp:
            print(temp.data)
            temp = temp.next

nb = Node(10)
n1 = Node(20)
n2 = Node(30)
n3 = Node(40)
n4 = Node(50)
L1 = LinkedList()
self.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
ne = Node('Bomboclat')
nm = Node('Huzzzz')

#How to put a node at the beginning of a LinkedList : nb

nb.next = self.head 
self.head = nb

# How to insert at the end of the Linkedlist : ne
# To get to the last element to change its next pointer , we need to iterate to the last part
temp = self.head
while temp.next:
    # If the next value is none , since the last element's next is None then the loop is exited 
    temp = temp.next
temp.next = ne

# How to insert at the middle of the Linkelist : nm
#Using positioning we will insert it in the middle
position = 3 #example 
temp = self.head
for i in range(position-1):
    temp = temp.next
nm.next = temp.next
temp.next = nm

 
        
        


