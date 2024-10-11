# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Codec:

#     def serialize(self, root):
#         result=''
#         queue=[root]
#         while queue:
#             u = queue.pop(0)
#             if u!='#':       
#                 result+=u.val
#             else:
#                 result+=u
#             if u.left:
#                 queue.append(u.left)
#             else:
#                 queue.append('#')
#             if u.right:
#                 queue.append(u.right)
#             else:
#                 queue.append('#')
#         return result
        

#     def deserialize(self, data):
#         root = TreeNode(data[0])
#         queue = [root]
#         i=1
#         while queue:
#             node = queue.pop(0)
#             if data[i]!='#':
#                 node.left = TreeNode(data[i])
#                 queue.append(node.left)
#             if data[i+1]!="#":
#                 node.right = TreeNode(data[i])
#                 queue.append(node.right)
#             i+=2
#         return root


# # Your Codec object will be instantiated and called as such:
# # ser = Codec()
# # deser = Codec()
# # ans = deser.deserialize(ser.serialize(root))

## Morris Traversal (INORDER)
# class Solution:
#     def __init__(self,root):
#         self.root = root
#         self.result = []
#     def morrisTraversal(self):
#         curr = self.root
#         while curr!=None:
#             if curr.left is None:
#                 self.result.append(curr.val)
#                 curr = curr.right
#             else:
#                 prev = curr.left
#                 while prev.right!=None and prev.right!=curr:
#                     prev = prev.right
#                 if prev.right!=None:
#                     prev.right = curr
#                     curr = curr.left
#                 else:
#                     prev.right = None
#                     result.append(curr.val)
#                     curr = curr.right


## Flatten a binary tree

# Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def dfs(self,node):
#         if not node:
#             return
#         self.cnode.right = TreeNode(node.val)
#         self.cnode = self.cnode.right
#         self.dfs(node.left)
#         self.cnode = self.cnode.right
#         self.dfs(node.right)

#     def flatten(self, root: Optional[TreeNode]) -> None:
#         self.Linkedlist = TreeNode(None)
#         self.currnode = self.Linkedlist
#         return self.Linkedlist.right


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def _flatten(self,node):
#         if not node:
#             return
#         self._flatten(node.right)
#         self._flatten(node.left)
#         node.right = self.prev
#         node.left = None
#         prev = node
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         self.prev = None
#         self._flatten(root)
#         return root

# class Node:
#     def __init__(self,val= None):
#         self.val = val
#         self.right = None
#         self.left = None
    
# class Tree:
#     def __init__(self):
#         self.root = None
    
#     def append(self,val):
#         if not self.root:
#             self.root = Node(val)
#         else:
#             self._append(self,self.root,val)

#     def _append(self,node,val):
#         if val<node.val:
#             if not node.left:
#                 node.left = Node(val)
#             else:
#                 self._append(node.left,val)
#         else:
#             if not node.right:
#                 node.right = Node(val)
#             else:
#                 self._append(node.right,val)
    
#     def search(self,val):
#         if not self.root:
#             return -1
#         else:
#             return self._search(self.root,val)
    
#     def _search(self,node,val):
#         if not node:
#             return False
#         if node.val == val:
#             return True
#         if node.val<val:
#             if self._search(node.left,val):
#                 return True
#         elif node.val>val:
#             if self._search(node.right,val):
#                 return True
    
#     def ceil(self,val):
#         self.result = float('inf')
#         if not self.root:
#             return -1
#         else:
#             self._ceil(self.root,val)
#         if self.result !=float('inf'):
#             return self.result
#         else:
#             return -1
    
#     def _ceil(self,node,val):
#         if node.val==val:
#             self.result = val
#             return
#         elif self.result>node.val>val:
#             self.result = node.val
#         if val>node.val:
#             self._ceil(node.right,val)
#         else:
#             self._ceil(node.left,val)
#     ## result<=inputvalue
#     def floor(self,val):
#         self.result = float('inf')
#         if not self.root:
#             return -1
#         if self.result!=float('inf'):
#             return self.result
#         else:
#             return -1
    
#     def _floor(self,node,val):
#         if not node:
#             return
#         if node.val == val:
#             self.result = val
#             return
#         if node.val<val:
#             self.result = val
#             self._floor(node.left,node.val)
#         else:
#             self._floor(node.right,val)


## Deleting the node in bst 

# class Solution:
#     def deleteNode(self,tnode,root):
#         self.tnode = tnode
#         self.root = root
#         self.prev = None
#         self.curr = self.root
#         self.location =None
#         self.dfs(self.root,None)
#         self.prev.left = self.location.left


#     def dfs(self,node,prev):
#         if node is None:
#             return 
#         if node.val == tnode:
#             self.location = Node
#             self.prev = prev
#             return
#         self.dfs(node.left,node)
#         self.dfs(node.right,node)