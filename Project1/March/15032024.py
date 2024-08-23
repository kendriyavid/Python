# class Node:
#     def __init__(self,data=None):
#         self.next = None
#         self.data = data
    
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self,data):
#         Newnode = Node(data)
#         if self.head==None:
#             self.head  =Newnode
#             return
#         curr = self.head
#         while curr.next!=None:
#             curr = curr.next
#         curr.next  = Newnode

#     def traversal(self):
#         curr = self.head
#         while curr!=None:
#             print(curr.data)
#             curr  =curr.next
    
# ll= LinkedList()
# ll.append(3)
# ll.traversal()

## selection sorting

arr=[1,2,3,4,5,6,7,8,9]
# arr.reverse()

# for i in range(len(arr)):
#     max = i
#     for j in range(i,len(arr)):
#         if arr[max]<arr[j]:
#             max = j
#     arr[max],arr[i]  =arr[i],arr[max]

# print(arr)

## insertion sorting

# for i in range(len(arr)):
#     for j in range(i,0,-1):
#         if arr[j]>arr[j-1]:
#             arr[j],arr[j-1] = arr[j-1],arr[j]
# print(arr)

## Bubble Sorting

# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]  = arr[j+1],arr[j]
# print(arr)

    