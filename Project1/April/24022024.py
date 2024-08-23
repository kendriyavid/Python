# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# class Tree:
#     def __init__(self):
#         self.root = None
    
#     def append(self, val):
#         if self.root is None:
#             self.root = Node(val)
#         else:
#             self._append(self.root, val)

#     def _append(self, node, val):
#         if node.val > val:
#             if node.left is None:
#                 node.left = Node(val)
#             else:
#                 self._append(node.left, val)
#         elif node.val < val:
#             if node.right is None:
#                 node.right = Node(val)
#             else:
#                 self._append(node.right, val)

#     def search(self, val):
#         return self._search(val, self.root)
    
#     def _search(self, val, node):
#         if node is None:
#             return False
#         elif node.val == val:
#             return True
#         elif node.val > val:
#             return self._search(val, node.left)
#         else:
#             return self._search(val, node.right)
    
#     def preorder(self):
#         self._preorder(self.root)
#         print()  # Print a newline after the traversal

#     def _preorder(self, node):
#         if node:
#             print(node.val, end=' ')
#             self._preorder(node.left)
#             self._preorder(node.right)
    
#     def postorder(self):
#         self._postorder(self.root)
#         print()  # Print a newline after the traversal

#     def _postorder(self, node):
#         if node:
#             self._postorder(node.left)
#             self._postorder(node.right)
#             print(node.val, end=' ')
    
#     def inorder(self):
#         self._inorder(self.root)
#         print()  # Print a newline after the traversal

#     def _inorder(self, node):
#         if node:
#             self._inorder(node.left)
#             print(node.val, end=' ')
#             self._inorder(node.right)
#     def inverting(self):
#         if not self.root:
#             return -1
#         else:
#             self._inverting(self.root)
#     def _inverting(self,node):
#         if node:
#             node.left,node.right = node.right,node.left
#             self._inverting(node.left)
#             self._inverting(node.right)

#     def maxdepth(self):
#         if not self.root:
#             return -1
#         else:
#             return self._maxdepth(self.root)
    
#     def _maxdepth(self,node):
#         if not node:
#             return 0
#         l=self._maxdepth(node.left)
#         r = self._maxdepth(node.right)
#         return 1+max(l,r)
    
#     def levelorder(self):
#         queue=[]
#         arr=[]
#         curr = self.root
#         queue.append(curr)
#         while queue:
#             lenght = len(queue)
#             mid=[]
#             for i in range(lenght):
#                 popped = queue.pop(0)
#                 # arr.append(popped.val)
#                 mid.append(popped.val)
#                 if popped.left:
#                     queue.append(popped.left) 
#                 if popped.right:
#                     queue.append(popped.right)
#             arr.append(mid)
#         return arr
    
#     def reverselevelorder(self):
#         queue=[]
#         stack=[]
#         arr = []
#         curr = self.root
#         queue.append(curr)
#         while queue:
#             lenght = len(queue)
#             for i in range(lenght):
#                 popped = queue.pop(0)
#                 stack.append(popped)
#                 if popped.right:
#                     queue.append(popped.right)
#                 if popped.left:
#                     queue.append(popped.left)
#         while stack:
#             i = stack.pop()
#             arr.append(i.val)
#         return arr
    
#     def zigzag(self):
#         queue=[]
#         arr=[]
#         queue.append(self.root)
#         s=True
#         while queue:
#             lenght = len(queue)
#             for i in range(lenght):
#                 if s is True:
#                     popped = queue.pop(0)
#                     arr.append(popped.val)
#                 if s is False:
#                     popped = queue.pop()
#                     arr.append(popped.val)
#                 if s is True:
#                     if popped.right:
#                         queue.append(popped.right)
#                     if popped.left:
#                         queue.append(popped.left)
#                 if s is False:
#                     if popped.left:
#                         queue.append(popped.left)
#                     if popped.right:
#                         queue.append(popped.right)

#             s = not s
#         return arr
    
#     def lavg(self):
#         queue=[]
#         arr=[]
#         queue.append(self.root)
#         while queue:
#             lenght = len(queue)
#             s=0
#             for i in range(lenght):
#                 print(s,lenght)
#                 popped = queue.pop(0)
#                 s+=popped.val
#                 if popped.left:
#                     queue.append(popped.left)
#                 if popped.right:
#                     queue.append(popped.right)
#             arr.append(s/lenght)
#         return arr
    
#     def mindepth(self):
#         if not self.root:
#             return 0
#         else:
#             return self._mindepth(self.root)
    
#     def _mindepth(self,node):
#         if not node:
#             return 0
#         l = self._mindepth(node.left)
#         r= self._mindepth(node.right)
#         return 1+min(l,r)
    
#     def mindepthiterative(self):
#         queue=[]
#         queue.append(self.root)
#         arr=[]
#         f=False
#         while queue:
#             lenght = len(queue)
#             mid=[]
#             for i in range(lenght):
#                 popped = queue.pop(0)
#                 mid.append(popped.val)
#                 if not popped.left or not popped.right:
#                     f = not f
#                     break
#                 if popped.left:
#                     queue.append(popped.left)
#                 if popped.right:
#                     queue.append(popped.right)
#             arr.append(mid)
#             if f:
#                 break
#         return arr


# mtree = Tree()
# values_to_add = [10, 5, 15, 3, 7, 12, 18]
# for value in values_to_add:
#     mtree.append(value)

# print(mtree.mindepthiterative())
arr=["1","2","3","4"]
print((int(''.join(arr))))