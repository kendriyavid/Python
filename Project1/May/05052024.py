# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# class Tree:
#     def __init__(self):
#         self.root = None

#     def append(self, val):
#         if not self.root:
#             self.root = Node(val)
#         else:
#             self._append(self.root, val)

#     def _append(self, node, val):
#         if val < node.val:
#             if not node.left:
#                 node.left = Node(val)
#             else:
#                 self._append(node.left, val)
#         elif val > node.val:
#             if not node.right:
#                 node.right = Node(val)
#             else:
#                 self._append(node.right, val)

#     def search(self, val):
#         return self._search(self.root, val) if self.root else False

#     def _search(self, node, val):
#         if not node:
#             return False
#         elif node.val == val:
#             return True
#         elif val < node.val:
#             return self._search(node.left, val)
#         else:
#             return self._search(node.right, val)
    
#     def levelorder(self):
#         queue=[]
#         queue.append(self.root)
#         arr=[]
#         while queue:
#             lenght = len(queue)
#             mid=[]
#             for i in range(len(queue)):
#                 popped = queue.pop(0)
#                 if popped.left:
#                     queue.append(popped.left)
#                 if popped.right:
#                     queue.append(popped.right)
#                 mid.append(popped.val)
#             arr.append(mid[:])
#         print(arr)
    
#     def preorder(self):
#         stack=[]
#         stack.append(self.root)
#         arr=[]
#         while stack:
#             popped = stack.pop()
#             arr.append(popped.val)
#             if popped.right:
#                 stack.append(popped.right)
#             if popped.left:
#                 stack.append(popped.left)
#         print(arr)
    
#     def inorder(self):

    
# tree = Tree()
# tree.append(5)
# tree.append(3)
# tree.append(7)
# tree.append(1)
# tree.append(4)
# print(tree.search(3))  # Output: True
# print(tree.search(6))  # Output: False
# print(tree.levelorder())
# print(tree.preorder())
## maximum subarray with given sum
arr=[2,5,1,7,10]
k=14
# maxlen=0
# subarr=[]
# for i in range(len(arr)):
#     sum=0
#     for j in range(i,len(arr)):
#         sum+=arr[j]
#         if sum<=k:
#             maxlen=max(maxlen,j-i+1)
#             subarr=arr[i:j+1]
#             print(subarr)
# print(maxlen)
# # # print(subar)

# l=0
# r=0
# maxlen=0
# sum=0
# maxsubarr=[]
# while r<len(arr):
#     sum = sum+arr[r]
#     while sum>k:
#         sum=sum-arr[l]
#         l+=1
#     if sum<=k:
#         if maxlen<r-l+1:
#             maxlen=r-l+1
#             maxsubarr=arr[l:r+1]
#     r+=1
# print(maxlen)
# print(maxsubarr)


