'''
	Your task is to complete both
	these functions given below.

	Function Arguments: a (linked list) and value (value to be inserted)
	Return Type: None
'''
'''    
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def__init__(self. head=Node):
        self.head = head

'''


# function should insert new node at the
# beigning of the list
def insertAtBegining(a, value):
    new_node = Node(value)
    tmp = a.head
    a.head = new_node
    a.head.next = tmp


# function should insert new node at the
# end of the list
def insertAtEnd(a, value):
    new_node = Node(value)
    current = a.head
    if not current:
        a.head = new_node
    else:
        last = a.head
        while last.next:
            last = last.next
        last.next = new_node
