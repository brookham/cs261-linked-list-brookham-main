# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.

# Brook Hamilton
# Collaborators:
# Time Spent: 

class LinkedList:
   
    def __init__(self, value = None):
        self.value = value
        self.next = self
        self.previous = self

    def is_sentinel(self):
        if self.value == None:
            return True
        else:
            return False
    
    def is_empty(self):
        if self.next == self and self.previous == self:
            return True
        else:
            return False
        
    def is_last_node(self):
        return self.is_empty() or self.next.is_sentinel()

    
    def last_node(self):
        if self.is_empty() or self.next.is_sentinel():
            return self
        return self.next.last_node()
    
    def append(self, node):
        while not self.next.is_sentinel():
            self = self.next
        left_node = self
        right_node = self.next #senitel node
        node.previous = left_node
        node.next = right_node
        left_node.next = node
        right_node.previous = node
        
        return node


