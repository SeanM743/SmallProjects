class Node:

    def __init__(self,value,next_node):
        self.value = value
        self.next = next_node


    def insert_node_after(self,new_node):
        new_node.next = self.next
        self.next = new_node
        
    def delete_node_after(self):
        self.next = self.next.next

    #delete the node passed into this function
    def delete_node(self,node_to_del):
        node_to_del.value = node_to_del.next.value
        node_to_del.next = node_to_del.next.next

    def merge_sorted_nodes(self,L1,L2):

        dummy_head = temp = Node(0,None)

        while L1 and L2:
            if L1.value < L2.value:
                temp.next = L1
                L1 = L1.next
            else:
                temp.next = L2
                L2 = L2.next
            temp = temp.next
        
        temp.next = L1 or L2
        return dummy_head.next

    def remove_duplicates(self):
        head = L1 = self
        while L1:
            start = L1
            while L1.next and L1.value == L1.next.value:
                L1 = L1.next
            L1 = L1.next                
            start.next = L1            
        return head

    # def right_shift(self,shift):
    #     L = head = self
    #     length = 0
    #     while L:
    #         length += 1
    #         L = L.next
    #     tail = L
    #     tail.next = head

    #     i = length - shift
    #     while i > 0:
    #         head = head.next
    #         i-=1
        
    #     return head
        
    
def build_linked_list(n0,*nodes):
    head = location = Node(n0,None)
    for n in nodes:
        temp = Node(n,None)
        location.next = temp
        location = location.next
    return head

#L = build_linked_list(1,2,2,2,2,2,5,19,35,79,100,2015,3900)
#h = L.remove_duplicates()



import random

class JumpNode():
    
    def __init__(self,value,jump,next):
        self.value = value
        self.jump = jump
        self.next = next
    
def build_jump_list(n0,*nodes):
    n = len(nodes)

    head = location = JumpNode(n0,None,None)
    for value in nodes:
        temp = JumpNode(value,None,None)
        location.next = temp
        location = location.next
    L = head

    while L:
        rand_jump = random.randint(0,n)
        tmp = head
        for _ in range(rand_jump):
            tmp = tmp.next
        L.jump = tmp
        L = L.next

    return head

jmp = build_jump_list(1,13,19,33,12,125,15,90,43,290)               


# n1 = Node(5,None)
# n2 = Node(6,None)
# n3 = Node(23,None)
# n4 = Node(55,None)

# n1.insert_node_after(n2)
# n2.insert_node_after(n3)
# n3.insert_node_after(n4)

# n5 = Node(2,None)
# n6 = Node(4,None)
# n7 = Node(33,None)
# n8 = Node(41,None)
# n5.insert_node_after(n6)
# n6.insert_node_after(n7)
# n7.insert_node_after(n8)

# L1 = n1
# L2 = n5

# L3 = Node(0,None)
# L4 = L3.merge_sorted_nodes(L1,L2)

while(h):
    print(h.value)
    h = h.next