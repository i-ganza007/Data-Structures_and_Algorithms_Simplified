# A node is a building block for linked lists and other data structures . It's what gives linked lists their functionalities .
# A node has two parts : the one that contains data and the next part (Containing the memory address for the next Node)
# By default , the next is None 


# DEFINITION

Class Node:
    def __init__(self,data):
        self.Data = data
        self.Next = None

# Why isn't Next in the arguments of the init method ? This is because everything in the init method are compulsory and the next isn't . Since a node could be the last or the only one in the Linked List.

n1 = Node(10)
n2 = Node(20)
n1.next = n2

# And so on and so forth 
