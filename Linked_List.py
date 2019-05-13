class Linked_List_Node(object):

    def __init__(self, val, next=0):
        self.val = val
        self.next = next


class Doubly_Linked_List_Node(object):
    
    def __init__(self,val):
        
        self.val = val
        self.next_node = None
        self.prev_node = None