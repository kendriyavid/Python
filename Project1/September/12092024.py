# import heapq
# class Graph:
#     def __init__(self, n: int, edges):
#         self.n = n
#         self.edges = edges
#         self.adj = [[]for _ in range(self.n)]
#         for u,v,w in self.edges:
#             self.adj[u].append((v,w))
        
#     def addEdge(self, edge) -> None:
#         fr =edge[0]
#         to = edge[1]
#         weight = edge[2]
#         self.adj[fr].append((to,weight))
        
#     def shortestPath(self, node1: int, node2: int) -> int:
#         def dijkstra(node1,node2):
#             heap = []
#             heapq.heapify(heap)
#             distance = [float('inf')]*self.n
#             heapq.heappush(heap,(0,node1))
#             distance[node1] = 0
#             while heap:
#                 d,u = heapq.heappop(heap)
#                 if u==node2:
#                     return distance[u]
#                 for v,vd in self.adj[u]:
#                     if vd+d<distance[v]:
#                         distance[v] = vd+d
#                         heapq.heappush(heap,(distance[v],v))
#             return -1
#         return dijkstra(node1,node2)
# n = 4
# edges = [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]
# graph = Graph(n,edges)
# print(graph.shortestPath(0,3))
# graph.addEdge([1,3,4])
# print(graph.shortestPath(0,3))
            
        


# # Your Graph object will be instantiated and called as such:
# # obj = Graph(n, edges)
# # obj.addEdge(edge)
# # param_2 = obj.shortestPath(node1,node2)


# ## Leetcode 815 Bus routes
# import heapq
# class solution:
#     def __init__(self,routes):
#         self.routes = routes
#         self.nodes = set()
#         self.nodelist = list(self.nodes).sort()
#         self.mapping = {}
#         for route in self.routes:
#             for stops in route:
#                 self.node.add(stop)
#         self.n = len(self.nodes)
#         for i in range(self.n):
#             self.mapping[self.nodelist[i]] = i
#         self.parent = [i for i in range(self.n)]
#         self.rank = [0]*self.n
#         self.adj = [[] for _ in range(self.n)]
#         for route in self.routes:
#             for i in range(1,len(route)):
#                 self.adj[self.mapping[route[i-1]]].append(self.mapping[route[i]])
        
#     def find(self,e):
#         if e==self.parent[e]:
#             return e
#         self.parent[e] = self.find(self.parent[e])
#         return self.parent[e]
    
#     def union(self,e1,e2):
#         p1 = self.find(e1)
#         p2 = self.find(e2)
#         if p1==p2:
#             return
#         if self.rank[p1]>self.rank[p2]:
#             self.parent[p1] = p2
#         elif self.rank[p2]>self.rank[p1]:
#             self.parent[p2] = p1
#         else:
#             self.rank[p1]+=1
#             self.parent[p2] = p1
    
#     def dijkstra(self,source,end):
#         distance =[float('inf')]*self.n
#         distance[source] = 0
#         heap = []
#         heapq.heapify(heap)
#         heapq.heappush(heap,(0,source))
#         while heap:
#             d,u = heapq.heappop(heap)
#             if u==end:
#                 return distance[u]
#             for v,vd in self.adj[u]:
#                 if vd+d<distance[v]:
#                     distance[v] = v+vd
#                     heapq.heappush(heap,(distance[v],v))
#         return -1

#     def numBusestoDestination(self,source,desitnation):
#         p1 = self.find(self.mapping[source])
#         p2 = self.find(self.mapping[destination])
#         if p1!=p2:
#             return -1
#         else:
#             return self.dijkstra(self.mapping[source],self.mapping[destination])
    

# import heapq

# heap=[]
# heapq.heapify(heap)
# baseTime = float('inf')
# for i in range(len(tasks)):
#     baseTime = min(baseTime,tasks[i][0])
# heapq.heappush(heap,())


# class node:
#     def __init__(self,val=None):
#         self.left = None
#         self.right = None
#         self.val = val
    
# class Tree:
#     def __init__(self):
#         self.root = None
    
#     def append(self,val):
#         if self.root is None:
#             return -1
#         self._append(self.root,val)
#     def _append(self,node,val):
#         if self.val>val:
#             if self.right is None:
#                 self.right = node(val)
#             else:
#                 self._append(self.right,val)
#         else:
#             if self.left is None:
#                 self.left = node(val)
#             else:
#                 self._append(self.left,val)


## Balanced Binary Tree

# class Solution:
#     def dfs(self,node):
#         if node is None:
#             return (0,0)
#         maxdiffl,maxhl = self.dfs(node.left)
#         maxdiffr,maxhr = self.dfs(node.right)
#         maxdiff = max(maxdiffl,maxdiffr,abs(maxhl-maxhr))
#         maxh = 1+max(maxhl,maxhr)
#         return (maxdiff,maxh)

#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         maxdifference,maxheight = self.dfs(root)
#         return 1>=maxdifference


## Diameter of binary Tree

# class Solution:

#     def dfs(self,node):
#         if not node:
#             return 0
#         lh = self.dfs(node.left)
#         rh = self.dfs(node.right)
#         maxh = 1+max(lh,rh)
#         self.diameter = max(self.diameter,lh+rh)

#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         self.diameter = float('-inf')


## identical trees 

# class Solution:
#     def dfs(self,node1,node2):
#         if not node1 and not node2:
#             return True
#         if not node1 or not node2:
#             return False
#         if node1.val!=node2.val:
#             return False
#         return (self.dfs(node1.left,node2.left)) and (self.dfs(node1.right,node2.right))

#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         return self.dfs(node1,node2)


# ## Boundary Traversal of Binary Tree
# class Solution:
#     def dfs(self,node,result):
#         if not node:
#             return 
#         result.append(node.val)
#         if not node.left:
#             self.dfs(node.right,result)
#         else:
#             self.dfs(node.left,result)
    
#     def inroder(self,node,result):
#         if not node:
#             return 
#         self.dfs(node.left,result)
#         if not node.left and not node.right:
#             result.append(node.val)
#         self.dfs(node.right,result)
    

#     def boundaryTraversal(self,root):


# class Solution:
#     def dfs(self,node1,node2):
#         if not node1 and node2:
#             return True
#         if (not node1.left and not node1.right) or (not node1.right and not node2.left):
#             return True
#         else:
#             return False
#         if node1.val!=node2.val:
#             return False
         
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        