## Reconstruct Itenary

# class Solution:
#     def __init__(self,tickets):
#         self.tickets = tickets
#         self.stations = set()
#         for u,v in self.tickets:
#             self.stations.add(u)
#             self.stations.add(v)
#         self.n = len(self.stations)
#         self.stationList = list(self.stations)
#         self.stationList.sort()
#         self.stationMapping = {}
#         for i in self.stationList:
#             self.stationMapping[self.stationList[i]] = i
#         self.adj = [[]for _ in range(self.n)]
#         self.dicti = {}
#         ## initializing the dicti and adj list:
#         for u,v in self.tickets:
#             self.adj[self.stationMapping[u]].append(self.stationMapping[v])
#             if self.dicti[u]:
#                 self.dicti[u]+=1
#             else:
#                 self.dicti[u] = 1

#     def Backtrackdfs(self,path,u):
#         self.dicti[u]-=1
#         self.path.append(u)
#         if all(self.dicti.values)==0:
#             return path
#         for v in self.adj[u]:
#             if self.dicti[v]!=0:
#                 return self.Backtrackdfs(path,v)
#         self.dicti[u]+=1
#         self.path.pop()

#     def ReconstructItenary(self):
#         result = self.Backtrackdfs([],self.stationMapping["JFK"])
#         fresult = []
#         for i in res:
#             fresult.append(self.stationlist[i])
#         return fresult
        


# class Solution:
#     def __init__(self, tickets):
#         self.tickets = tickets
#         self.stations = set()
#         for u, v in self.tickets:
#             self.stations.add(u)
#             self.stations.add(v)
#         self.n = len(self.stations)
        
#         # Create sorted list of stations for consistent ordering
#         self.stationList = sorted(self.stations)
        
#         # Mapping station names to indices
#         self.stationMapping = {station: idx for idx, station in enumerate(self.stationList)}
        
#         # Initialize adjacency list and dicti
#         self.adj = [[] for _ in range(self.n)]
#         self.dicti = {station: 0 for station in self.stations}  # To track the number of tickets from each station
        
#         # Initialize adjacency list and the ticket counts
#         for u, v in self.tickets:
#             self.adj[self.stationMapping[u]].append(self.stationMapping[v])
#             self.dicti[u] += 1
        
#         # Sort adjacency lists for lexical order traversal
#         for i in range(self.n):
#             self.adj[i].sort()

#     def Backtrackdfs(self, path, u):
#         # Reduce ticket count from station u
#         self.dicti[self.stationList[u]] -= 1
#         path.append(u)
        
#         # If all tickets have been used, return the path
#         if all(count == 0 for count in self.dicti.values()):
#             return path
        
#         # Explore neighbors of the current station
#         for v in self.adj[u]:
#             if self.dicti[self.stationList[v]] > 0:
#                 result = self.Backtrackdfs(path, v)
#                 if result:
#                     return result
        
#         # Backtrack if no valid path is found
#         self.dicti[self.stationList[u]] += 1
#         path.pop()
#         return None

#     def ReconstructItenary(self):
#         # Start DFS from "JFK"
#         start_station = self.stationMapping["JFK"]
#         result = self.Backtrackdfs([], start_station)
        
#         # Convert indices back to station names
#         if result:
#             return [self.stationList[i] for i in result]
#         return []
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# solution = Solution(tickets)
# print(solution.ReconstructItenary())

# class Solution:
#     def __init__(self, tickets):
#         self.tickets = tickets
#         self.stations = set()
#         for u, v in self.tickets:
#             self.stations.add(u)
#             self.stations.add(v)
#         self.n = len(self.stations)
        
#         # Create sorted list of stations for consistent ordering
#         self.stationList = sorted(self.stations)
        
#         # Mapping station names to indices
#         self.stationMapping = {station: idx for idx, station in enumerate(self.stationList)}
        
#         # Initialize adjacency list and dicti
#         self.adj = [[] for _ in range(self.n)]
#         self.dicti = {station: 0 for station in self.stations}  # To track the number of tickets from each station
        
#         # Initialize adjacency list and the ticket counts
#         for u, v in self.tickets:
#             self.adj[self.stationMapping[u]].append(self.stationMapping[v])
#             self.dicti[u] += 1
        
#         # Sort adjacency lists for lexical order traversal
#         for i in range(self.n):
#             self.adj[i].sort()

#     def Backtrackdfs(self, path, u):
#         path.append(self.stationList[u])
        
#         if len(path) == len(self.tickets) + 1:
#             return path
        
#         for v in self.adj[u]:
#             if self.dicti[self.stationList[u]] > 0:
#                 self.dicti[self.stationList[u]] -= 1
#                 result = self.Backtrackdfs(path, v)
#                 if result:
#                     return result
#                 self.dicti[self.stationList[u]] += 1
        
#         path.pop()
#         return None

#     def ReconstructItenary(self):
#         start_station = self.stationMapping["JFK"]
#         result = self.Backtrackdfs([], start_station)
#         return result if result else []

# # Test the solution
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# solution = Solution(tickets)
# print(solution.ReconstructItenary())


# class solution:
#     def __init__(self,rChild,lChild,n):
#         self.rChild = rChild
#         self.lChild = lChild
#         self.n = n
#         self.adj = [[] for _ in range(self.n)]
#         ## adj initialization
#         for i in range(self.n):
#             if self.rChild[i]!=-1:
#                 self.adj[i].append(self.rChild[i])
#             if self.lChild[i]!=-1:
#                 self.adj[i].append(self.lChild[i])
#         self.visited = [False]*self.n
#         self.currstack = [False]*self.n
    
#     def dfs(self,u):
#         self.visited[u] = True
#         self.currstack[u] = True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 if not self.dfs(v):
#                     return False
#             elif self.currstack[v]:
#                 return False
#         self.currstack[u] = False
#         return True

#     def ValidateBinarytree(self):
#         l = False
#         r = False
#         if self.lChild[0]!=-1:
#             l = self.dfs(self.lChild[0])
#         if self.rChild[0]!=-1:
#             r = self.dfs(self.rChild[0])
#         return l or r
# leftChild = [1,-1,3,-1]
# rightChild = [2,3,-1,-1]
# Solution = solution(rightChild,leftChild,4)
# print(Solution.ValidateBinarytree())



# class solution:
#     def __init__(self,lchild,rchild,n):
#         self.n = n
#         self.rchild = rchild
#         self.lchild = lchild
#         self.parent = [i for i in range(self.n)]
#         self.rank = [0]*self.n

#     def find(self,e):
#         if self.parent[e] == e:
#             return e
#         self.parent[e] = self.find(self.parent[e])
#         return self.parent[e]
    
#     def union(self,e1,e2):
#         if e1==-1 or e2==-1:
#             return True
#         p1 = self.find(e1)
#         p2 = self.find(e2)
#         if p1!=e1 or p2!=e2:
#             return False
#         pp1 = self.find(p1)
#         pp2 = self.find(p2)
#         if pp1==e1 or pp2 ==e2:
#             return False
#         if self.rank[p1]>self.rank[p2]:
#             self.parent[p2] = p1
#         elif self.rank[p1]<self.rank[p2]:
#             self.parent[p1] = p2
#         else:
#             self.rank[p1]+=1
#             self.parent[p2] = p1
#         return True

#     def validateBinaryTree(self):
#         for i in range(self.n):
#             if not self.union(i,self.lchild[i]):
#                 return False
#             if not self.union(i,self.rchild[i]):
#                 return False
#         return True


# class Solution:
#     def __init__(self,relations,n,times):
#         self.relations = relations
#         self.time =time
#         self.n = n
#         self.adj = [[] for _ in range(self.n)]
#         ## initialization
#         self.indegree = [0]*self.n
#         for u,v in self.relations:
#             self.adj[u].append(v)
#             self.indegree[v]+=1

#     def parallelCoursesthree(self):
#         queue=[]
#         for i in range(self.n):
#             if self.indegree[i]==0:
#                 queue.append((i,self.time[i]))
#         maxtime=float('-inf')
#         while queue:
#             course,time = queue.pop(0)
#             maxtime = max(maxtime,time)
#             for v in self.adj[u]:
#                 queue.append(v,time+self.time[v])

#         return maxtime

# from collections import deque

# class Solution:
#     def __init__(self, relations, n, times):
#         self.relations = relations
#         self.time = times
#         self.n = n
#         self.adj = [[] for _ in range(self.n)]
#         self.indegree = [0] * self.n

#         # Initialize adjacency list and in-degree count
#         for u, v in self.relations:
#             self.adj[u].append(v)
#             self.indegree[v] += 1

#     def parallelCourses(self):
#         queue = deque()
#         for i in range(self.n):
#             if self.indegree[i] == 0:
#                 queue.append((i, self.time[i]))  # Start with courses that have no prerequisites
        
#         maxtime = float('-inf')
#         while queue:
#             course, current_time = queue.popleft()  # Efficient queue operation with deque
#             maxtime = max(maxtime, current_time)

#             for v in self.adj[course]:
#                 self.indegree[v] -= 1  # Decrease the in-degree of the next course
#                 if self.indegree[v] == 0:  # If the next course has no prerequisites left
#                     queue.append((v, current_time + self.time[v]))  # Add the course and cumulative time

#         return maxtime

# # Relations now have 3 courses and time for each course
# relations = [[0, 2], [1, 2]]  # Courses 0 and 1 lead to course 2
# time = [3, 2, 5]  # Course 0 takes 3, Course 1 takes 2, Course 2 takes 5
# n = 3

# solution = Solution(relations, n, time)
# print(solution.parallelCourses())  # Expected output: 8


# class Node:
#     def __init__(self,val = None):
#         self.left = None
#         self.right = None
#         self.val = val
    
# class Tree:
#     def __init__(self):
#         self.root = None
    
#     def append(self,val):
#         if self.root == None:
#             return -1
#         self._append(self.root,val)
    
#     def _append(self,node,val):
#         if node.val>val:
#             if node.right is None:
#                 node.right = Node(val)
#             else:
#                 self._append(node.right,val)
#         else:
#             if node.left is None:
#                 node.left = Node(val)
#             else:
#                 self._append(node.left,val)
    
#     def levelorder(self):
#         result=[]
#         queue=[self.root]
#         level=1
#         while queue:
#             nqueue=[]
#             for node in queue:
#                 result.append(node.val)
#                 if node.left!=None:
#                     nqueue.append(node.left)
#                 elif node.right!=None:
#                     nqueeu.append(node.right)
#             if nqueue!=None:
#                 level+=1
#             queue = nqueue
#         return (result,level)

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         def dfs(self,node):
#             if node.left==None and node.right==None:
#                 return 1
#             l=0
#             if node.left:
#                 l = self.dfs(node.left)
#             r = 0
#             if node.right:
#                 r = self.dfs(node.right)
#             return 1+max(l,r)

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         def dfs(node):
#             if node.left is None and node.right is None:
#                 return (1,0)
#             ld,lmax = dfs(node.left)
#             rd,rmax = dfs(node.right)
#             maxd = max(ld,rd)
#             maxdif = max(abs(ld-rd),lmax,rmax)
#             return (maxd,maxdif)
        
#         depth,maxdiff = dfs(root)
#         return maxdiff<=1


# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         def dfs(node):
#             if node is None:
#                 return (0,0)
#             ldia,lmax = self.dfs(node.left)
#             rdia,rmax = self.dfs(node.right)
#             maxdia = max(ldia,rrdia,lmax+rmax+1)
#             maxh = 1+max(lmax,rmax)
#             return (maxdia,maxh)
#         maximumDiameter,maxheight = dfs(root)
#         return maximumDiameter


## Binary Tree Maximum Path sum


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def dfs(self,node):
#         if not node:
#             return (0,0)
#         lmax,lhmax = self.dfs(node.left)
#         rmax,rhmax = self.dfs(node.right)
#         maxpath = max(lmax,rmax,lhmax+rhmax+node.val)
#         maxh = node.val+max(lhmax,rhmax)
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         maxpathsum,maxheight = self.dfs(root)
#         return maxpathsum

# class solution:
#     def dfs1(self,node,stack):
#         stack.append(node.val)
#         if not node.left and not node.right:
#             return 
#         if not node.left:
#             self.dfs1(node.right,stack)
#         else:
#             self.dfs1(node.left,stack)
#     def dfs2(self,node,stack):
#         if not node.left and not node.right:
#             return 
#         if not node.right:
#             self.dfs2(node.left,stack)
#         else:
#             self.dfs2(node.right,stack)
#         stack.append(node.val)
        
#     def inorder(self,node,stack):
#         self.inorder(node.left)
#         if not node.left and not node.right:
#             stack.append(node.val)
#         self.inorder(node.right)

#     def boundaryTraversal(self):
#         self.stack1 = []
#         self.stack2 = []
#         self.stack3 = []
#         self.result = []
#         self.dfs1(root,stack1)
#         self.dfs(root,stack2)
#         self.inorder(root,stack3)
#         return self.stack1+self.stack3+self.stack2

## Vertical order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        columns = defaultdict(list)
        
        def dfs(node, col):
            if not node:
                return
            
            columns[col].append(node.val)
            
            dfs(node.left, col - 1)
            dfs(node.right, col + 1)
        
        dfs(root, 0) 
        
        # Sort the result
        return [sorted(columns[col]) for col in sorted(columns.keys())]        