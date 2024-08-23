# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         newNode = Node(data)
#         if self.head is None:
#             self.head = newNode
#             return
#         curr = self.head
#         while curr.next is not None:
#             curr = curr.next
#         curr.next = newNode

#     def recursion_traverse(self):
#         def recursion(curr):
#             if curr is None:
#                 return
#             print(curr.data)
#             recursion(curr.next)
        
#         recursion(self.head)

#     def reversing1(self):
#         prev = self.head
#         curr = prev.next
#         while curr.next!=None:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
#         self.head.next = None
#         curr.next = prev
#         self.head = curr

#     # def recursive_reversing(self):
#     #     prev = self.head
#     #     curr = prev.next
#     #     def rec_rev(prev,curr):
#     #         if curr==None:
#     #             return
#     #         temp = curr.next
#     #         curr.next = prev
#     #         rec_rev(curr,temp)
#     #     newhead = rec_rev(prev,curr)
#     #     self.head.next = None
#     #     self.head = newhead


#     def recursive_reversing(self):
#         prev = self.head
#         curr = prev.next
        
#         def rec_rev(prev, curr):
#             if curr is None:
#                 return prev
#             temp = curr.next
#             curr.next = prev
#             return rec_rev(curr, temp)
    
#         new_head = rec_rev(prev, curr)
#         self.head.next = None  # Set the next of the original head to None in the reversed list
#         self.head = new_head  # Update the head to the new head of the reversed list

            

# # Example usage
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.recursive_reversing()
# ll.recursion_traverse()

# generating subarray using recursion

# array = [1,2,3,4,5,6]

# def gensubarray(array,arr,i,):
#     if len(arr)-i==0:
#         print(arr)
#     else:
#         return

#     for j in range(i,len(array)):
#         arr.append(array[i])
#         gensubarray(array,arr,j+1)
#         arr.pop()
    
# gensubarray(array,[],0)


def generate_subarrays(array, start, end, result):
    if start > end:
        return

    for i in range(start, end + 1):
        subarray = array[start:i + 1]
        result.append(subarray)
        generate_subarrays(array, i + 1, end, result)

def all_subarrays(array):
    result = []
    generate_subarrays(array, 0, len(array) - 1, result)
    return result

# Example usage:
array = [1, 2, 3]
subarrays = all_subarrays(array)
for subarray in subarrays:
    print(subarray)
