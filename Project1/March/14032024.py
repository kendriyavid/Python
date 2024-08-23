class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = node()
    
    ## Appending the Node

    def Append(self,data):
        Newnode = node(data)
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.next = Newnode

    ## Length of the List

    def Lenght(self):
        lenght = 0
        curr = self.head.next
        while curr!=None:
            curr = curr.next
            lenght+=1
        print(lenght)

    ## Linked list Traversal vieww

    def Traversal(self):
        curr = self.head
        while curr!=None:
            print(curr.data)
            curr = curr.next
        
    def Get(self,sd):
        curr = self.head.next
        lenght =0
        while curr!=None:
            if curr.data==sd:
                print(lenght)
                return 
            else:
                lenght+=1
                curr = curr.next
        print(-1)
        return

    def delete(self,dd):
        before = self.head
        curr = self.head.next
        while curr !=None:
            if curr.data==dd:
                before.next = curr.next
                print("done")
                return
            else:
                before = curr
                curr = curr.next
        print("No element found")

    def reversingLL(self):
        pivot = self.head
        previous = self.head.next
        current = self.head.next.next
        while current != None:
            previous.next = current.next
            current.next = pivot.next
            pivot.next = current
            current = previous.next
    
    def middleelement(self):
        slow = self.head
        fast = slow
        while fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

    ## Reverse nodes in pair
    def reverseinpair(self):
        pivot = self.head
        prev = self.head.next
        current= prev.next
        while current is not None and current.next is not None:
            prev.next = current.next
            current.next = pivot.next
            pivot.next = current
            pivot = prev
            prev = pivot.next
            current = pivot.next.next
    
    ## Reverse nodes in groups of k

    def reverseink(self,k):
        pivot = self.head
        prev = pivot.next
        current = prev.next
        count  =1
        while


    
    
ll = LinkedList()
ll.Append(1)
ll.Append(2)
ll.Append(3)
ll.Append(4)
ll.Append(5)
ll.Append(6)
ll.Traversal()
# ll.reversingLL()
# ll.Traversal()
ll.reverseinpair()
ll.Traversal()