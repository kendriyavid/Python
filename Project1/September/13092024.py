# ## Lowest Common anscestor of Binary Tree
# class Solution:
#     def dfs(self,node):
#         if not node:
#             return None
#         l = self.dfs(node.left)
#         r = self,dfs(node.right)
#         if node.val == p:
#             return p
#         elif node.val == q:
#             return q
#         if l and r:
#             return node.val
#         elif l:
#             return l
#         elif r:
#             return r

#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         self.p = p
#         self.q = q
#         lca = self.dfs(root)
#         return lca


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         queue = [(root,0)]
#         while queue:
#             nqueue=[]
#             minimum = queue[0][1]
#             for node,Id in queue:
#                 if node.left:
#                     nid = 2*Id+1-minimum
#                     nqueue.append((node.left,nid))
#                 if node.right:
#                     nid = 2*Id+2-minimum
#                     nqueue.append((node.right,nid))
#             if nqueue:
#                 queue = nqueue
#         ans = queue[len(queue-1)]-queue[0]+1
#         return ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def dfs(self, node):
#         if not node or (node.left is None and node.right is None):
#             return

#         # If the node has both left and right children, update their values if needed
#         if node.left and node.right:
#             lval = node.left.val
#             rval = node.right.val
            
#             # Update left and right child values if needed based on some condition
#             if lval + rval < node.val:
#                 node.left.val = node.val
#                 node.right.val = node.val
        
#         # Recursive DFS on left and right children
#         self.dfs(node.left)
#         self.dfs(node.right)

#         # After recursion, update the current node value if necessary
#         if node.left and node.right:
#             lval_updated = node.left.val
#             rval_updated = node.right.val
#             if lval_updated + rval_updated > node.val:
#                 node.val = lval_updated + rval_updated

#     def checkTree(self, root: Optional[TreeNode]) -> bool:
#         self.dfs(root)
#         return root

        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## Parent Pointer Method

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     # to create undirected tree like using parent pointers
#     def dfs(self,node,parent):
#         if not root:
#             return
#         self.ppDictionary[node] = parent
#         self.Visitednodes[node] = False
#         self.dfs(node.left,node)
#         self.dfs(node.right,node)
#         if node.val==self.target.val:
#             self.startnode = node
    
#     def bfs(self):
#         queue = [(self.startnode,0)]  ## node  , distance
#         self.Visitednodes[node] =True
#         while queue:
#             u,d = queue.pop(0)
#             if d==k:
#                 self.result.append(u.val)
#             ## dfs(nodeleft)
#             if self.Visitednodes[u.left]!=True:
#                 queue.append((u.left,d+1))
#                 self.Visitednodes[u.left]=True
#             if self.Visitednodes[u.right]!=True:
#                 queue.append((u.right,d+1))
#                 self.Visitednodes[u.right]=True
#             if self.Visitednodes[self.ppDictionary[u]]!=True:
#                 queue.append((self.ppDictionary[u],d+1))
#                 self.Visitednodes[self.ppDictionary[u]]=True

#     def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
#         self.ppDictionary = {}
#         self.Visitednodes = {}
#         self.startnode = None
#         self.target = target
#         self.k = k
#         self.result = []
#         self.dfs(root,-1)
#         self.bfs()
#         return self.result

# class Solution:
#     def dfs(self, node, parent):
#         if not node:
#             return
#         self.parentPointers[node] = parent  # Store parent pointer for each node
#         self.visitedNodes[node] = False  # Mark all nodes as unvisited initially
#         self.dfs(node.left, node)  # Recursive DFS for the left subtree
#         self.dfs(node.right, node)  # Recursive DFS for the right subtree
    
#     def bfs(self, stnode):
#         queue = [stnode]  # BFS queue initialized with the start node
#         self.visitedNodes[stnode] = True  # Mark the start node as visited
#         time = 0
        
#         while queue:
#             nqueue = []  # List to hold nodes to burn in the next time unit
#             for node in queue:
#                 # Check if the left child can be burned
#                 if node.left and not self.visitedNodes[node.left]:
#                     nqueue.append(node.left)
#                     self.visitedNodes[node.left] = True
                
#                 # Check if the right child can be burned
#                 if node.right and not self.visitedNodes[node.right]:
#                     nqueue.append(node.right)
#                     self.visitedNodes[node.right] = True
                
#                 # Check if the parent can be burned
#                 if self.parentPointers[node] and not self.visitedNodes[self.parentPointers[node]]:
#                     nqueue.append(self.parentPointers[node])
#                     self.visitedNodes[self.parentPointers[node]] = True
            
#             if nqueue:  # Increment time only if there are nodes to burn
#                 time += 1
            
#             queue = nqueue  # Move to the next level
        
#         return time

#     def MinimumTimetoBurn(self, root, start):
#         self.start = start
#         self.parentPointers = {}  # Dictionary to store parent pointers
#         self.visitedNodes = {}  # Dictionary to track visited nodes
        
#         self.dfs(root, None)  # Perform DFS to set up parent pointers
#         time = self.bfs(self.start)  # Perform BFS to calculate burn time
        
#         return time

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftHeight(self,node):
        if not node:
            return 0
        return 1+ self.leftHeight(node.left)

    def rightHeight(self,node):
        if not node:
            return 0
        return 1+self.rightHeight(node.right)
    
    def nodeCalulation(self,node):
        if not node:
            return 0
        lh = self.leftHeight(node)
        rh = self.rightHeight(node)
        if lh!=rh:
            return 1+self.nodeCalulation(node.left)+self.nodeCalulation(node.right)
        else:
            return 2**(lh)-1

    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.nodeCalculation(root)
        