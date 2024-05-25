# A Singly Linked List is a data structure that relies on Nodes and their properties. 
# The first node in a Singly Linked List is called a head, and the last one's Next value is None since it holds no memory address. 

Class SLL:
    def __init__(self):
        self.head = None

   # To display all the data in the list, we must traverse it by setting a temporary value, temp.
    
   def display(self):
     temp = self.head
     if temp is None:
       print("List is empty")
       return
     while temp:
       temp = temp.Next

 # We first assign the head(The first node to a temporary value)
# If the head is not present, the list is empty 
# But if the head is present, the temp variable updates itself to the address of the next node until the last one 
      
