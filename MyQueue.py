class ListNode(object):
    
    def __init__(self, item = None, link = None):

        '''creates a ListNode with the specified data value and link
        post: creates a ListNode with the specified data value and link'''
        
        self.item = item
        self.link = link

#------------------------------------------------------------------------------#
        
class Queue(object):

    def __init__(self):
        '''post: creates an empty queue (using links)'''
        self.count = 0
        self.head = None #head of the queue is first none
        self.tail = None

    def enqueue(self, item):
        '''post: places item at back of the queue,
        so queue will not be empty'''
       
        if self.head == None:
            self.head = ListNode(item)
            self.tail = self.head
            self.count += 1
        else:
            NewNode = ListNode(item)
            self.tail.link = NewNode
            self.tail = NewNode

            self.count += 1
        return 

    def dequeue(self):
        '''post: removes and returns the front element of 
        the queue'''
        '''pre: queue is not empty'''
        if self.head == None:
            print("The queue is currently empty. No item to dequeue")
        else:
            item = self.head.item
            self.head = self.head.link

            self.count -= 1
            return item

    def front(self):
        '''post: returns the front element of the queue without 
        removing it'''
        '''pre: queue is not empty'''
        if not self.size == 0:
            return self.head.item

    def size(self):
        '''post: returns the number of elements in the queue'''
        return self.count

    def __str__(self):
 
        s = "front|"
        node = self.head
        while node != None:
            s += str(node.item)+"|"
            node = node.link
        s += "back" 
        return s
