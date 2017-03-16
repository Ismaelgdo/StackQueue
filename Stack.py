class ListNode(object):
    
    def __init__(self, item = None, link = None):

        '''creates a ListNode with the specified data value and link
        post: creates a ListNode with the specified data value and link'''
        
        self.item = item
        self.link = link

#------------------------------------------------------------------------------#
        
class Stack (object):

    def __init__(self):
        """ creates an empty stack """
        self.head = None #top of the stack
        self.count = 0

    def push(self, item):
        """push a new item on to the stack"""
        if self.size == 0: #if stack is empty, first item becomes new top
            self.head = ListNode(item)
            self.count += 1
        else:
            self.head = ListNode(item, self.head)
            self.count += 1
    
    def size(self):
        """ pre: self.size > 0
        post: returns the number of items on the stack"""
        return self.count
        
    def pop(self):
        """ pre: self.size > 0
        post: pop an item off the top of the stack, and returns it """
        if self.size == 0:
            print("There is no items to be popped from the stack")
        else:
            item = self.head.item
            self.head = self.head.link
            self.count -= 1
            return item #the item that was removed from the stack

    def top(self):
        """pop an item from the top of the top of the stack
        without removing it"""
        return self.head.item

    def __str__(self):
        s = ""
 
        node = self.head
        while node != None:
            print("|", str(node.item), " |")
            node = node.link
        return s 



