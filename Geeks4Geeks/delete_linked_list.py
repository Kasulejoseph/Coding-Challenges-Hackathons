# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''


def delNode(head, k):
    current = head
    position = 1
    # if node to delete is in first position
    if k == 1:
        current = head.next
        head = current
        return head

    while position + 1 <= k:
        prev = current
        current = current.next
        position += 1

    prev.next = current.next
    current = None
    return head
