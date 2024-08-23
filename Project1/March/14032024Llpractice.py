class node:
    def __init__(self,data=None):
        self.next = None
        self.data =data
class LinkedList:
    def __init__(self):
        self.head = node()
    
    def append(self,data):
        NewNode = node(data)
        current = self.head
        while current.next!=None:
            current = current.next
        current.next = NewNode

    def traversal(self):
        curr = self.head
        while curr!=None:
            print(curr.data)
            curr= curr.next

    ## lenght
    def length(self):
        curr = self.head.next
        len = 0
        while curr!=None:
            curr = curr.next
            len+=1
        print(len)

    ## reversing the ll
    def reversing(self):
        pivot = self.head
        prev = pivot.next
        curr = prev.next
        while prev.next!=None:
            prev.next = curr.next
            curr.next = pivot.next
            pivot.next = curr
            curr = prev.next
    
    ## reversing in pair

    # def reversingpair(self):
    #     pivot = self.head
    #     prev = self.head.next
    #     curr = prev.next
    #     while curr!=None and curr.next!=None:
    #         prev.next  =curr.next
    #         curr.next = pivot.next
    #         pivot.next = curr
    #         pivot  = prev
    #         prev = pivot.next
    #         curr = pivot.next.next

    # def reverseinpair(self):
    #     pivot = self.head
    #     prev = self.head.next
    #     current= prev.next
    #     while current is not None:
    #         prev.next = current.next
    #         current.next = pivot.next
    #         pivot.next = current
    #         pivot = prev
    #         prev = pivot.next
    #         current = pivot.next.next

    # def reverseinpair(self):
    #     pptr = self.head
    #     ptr=  pptr.next
    #     # cp  =pptr.next
    #     current = pptr.next.next
    #     while current is not None:
    #         pptr.next = current
    #         ptr.next = current.next
    #         current.next = ptr
    #         ptr = pptr.next
    #         current =   ptr.next

    # SWAPPING IN K

    # def swappingink(self,k):
    #     pptr = self.head
    #     ptr = pptr.next
    #     cp = pptr.next
    #     curr = pptr.next.next
    #     count=1
    #     while curr!=None:
    #         if count%k!=0:
    #             pptr.next  =curr
    #             cp.next =curr.next
    #             curr.next = ptr
    #             ptr  = pptr.next
    #             curr = cp.next
    #             count+=1
    #         else:
    #             pptr = cp
    #             ptr  =pptr.next
    #             cp = pptr.next
    #             curr = pptr.next.next
    #             count  +=1




ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.append(5)
ll1.traversal()
ll1.swappingink(3)
ll1.traversal()