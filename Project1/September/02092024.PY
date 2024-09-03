## Revision

## Topological sortin
## dfs
#  -  do the dfs add the node to the stack when we 
# have traversed its parent return the reversed version

# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
#         self.stack = []
    
#     def dfs(self,u):
#         self.visted[u] = True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.dfs(v)
#         self.stack.append(u)
    
#     def Topologicalsorting(self):
#         for u in self.n:
#             if self.visited[u]!=True:
#                 self.dfs(u)
            
#         return self.stack[::-1]

## bfs version
# we create a indegree list and use it as visited 
# list as we traverse the nodes we decrease the values of the indegree and 
# add the 0 indegree to the queue to process

class solution:
    def __init__(self,adj):
        self.adj = adj
        self.n = len(adj)
        self.indegree = [0]*self.n
        for u in range(self.n):
            for v in self.adj[u]:
                self.indegree[v]+=1
        self.result = []
    
    def bfs(self):
        queue=[]
        for i in range(self.n):
            if self.indegree[i]==0:
                queue.append(i)
    
        while queue:
            u = queue.pop(0)
            self.result.append(u)
            for v in self.adj[u]:
                self.indegree[v]-=1
                if self.indegree[v]==0:
                    queue.append(v)
            
        return self.result

## Dijksta's algorithm
## we use minheap for finding the shortest path to the nodes we set the source to the 0  
## adn then loop over the nodes 
# import heapq
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n= len(adj)
#         self.heap =[]
#         heapq.heapify(heap)
#         self.distance = [float('inf')]*self.n
    
#     def Dijkstra(self,source):
#         heapq.heappush(self.heap,(0,source))
#         self.distance[source] = 0
#         while self.heap:
#             d,u = heapq.heappop(self.heap)
#             for v,dv in self.adj[u]:
#                 if dv+u<self.distane[v]:
#                     self.distance = dv+u
#                     heapq.heappush(self.heap,(self.distance[v],v))

## Bellmanford Algorithm
## relax the nodes n-1 rimes

# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.distance = [float('inf')]*self.n
    
#     def Bellmanford(self):
#         for i in range(self.n-1):
#             for u in range(self.n):
#                 for v,u in self.adj[u]:
#                     if self.distance[u]!=float('inf'):
#                         if self.distance[v]>self.distance[u]+u:
#                             self.distance[v] = self.distance[u]+u
        
# ## lONGEST PATH WITH DIFFERENT ADJECENT CHARECTERS
# class solution:
#     def __init__(self,adj,s):
#         self.adj = adj
#         self.n = len(adj)
#         self.s = s
#         self.visited = [False]*self.n
    
#     def bfs(self):
#         queue = [0]
#         lvlcount = 0
#         while queue:
#             nqueue=[]
#             u = queue.pop(0)
#             for v in self.adj[u]:
#                 if self.visited[v]!=True and self.s[u]!=self.s[v]:
#                     nqueue.append(v)
#                     self.visited[v] = True
#             if nqueue:
#                 count+=1
#             queue = nqueue
#         return count



# from collections import deque

# class Solution:
#     def __init__(self, adj, s):
#         self.adj = adj
#         self.n = len(adj)
#         self.s = s
#         self.stack = [False]*self.n
    
#     def bfs(self,u):
#         queue = deque([0])  # Using deque for efficient pop from the left
#         count = 1  # Initial count includes the root node
#         self.visited[u] = True
#         self.stack[u] = True
        
#         while queue:
#             nqueue = []
#             while queue:
#                 u = queue.popleft()  # Efficient pop from the left
#                 for v in self.adj[u]:
#                     if not self.visited[v] and self.s[u] != self.s[v]:
#                         nqueue.append(v)
#                         self.visited[v] = True
#             if nqueue:
#                 count += 1  # Increase the path length when we have nodes to explore
#             queue = deque(nqueue)  # Prepare for the next level
        
#         return count
    
#     def longestpath(self):
#         mcount = 0
#         for u in range(self.n):
#             if self.stack[u]!=True:
#                 self.visited = [False] * self.n
#                 mcount = max(self.bfs(u),mcount)

#         return mcount
            



# # Example usage
# adj = [[1, 2, 3], [0], [0], [0],]  # Example adjacency list
# s = "aabc"  # Example string
# solution = Solution(adj, s)
# print(solution.bfs())  # Output will be the length of the longest path with different adjacent characters

# class solution:
#     def __init__(self,parent,s):
#         self.parent = parent
#         self.n = len(s)
#         self.s = s
#         self.adj = adj
#         self.visited = [False]*self.n

#     def dfs(self,u):
#         self.visited[u] = True
#         for v in self.adj[u]:
# #             result = 0
# #             if self.visited[v]!=True and self.s[u]!=self.s[v]:
# #                 result+=1
# #                 self.dfs(v)
# #         return result

# class Solution:
#     def __init__(self, parent, s):
#         self.parent = parent
#         self.n = len(s)
#         self.s = s
#         self.adj = [[] for _ in range(self.n)]
#         self.visited = [False] * self.n
#         self.max_path = 1  # Initialize with 1, as the minimum path length is 1 (any single node)

#         # Build adjacency list from parent array
#         for child in range(1, self.n):
#             par = self.parent[child]
#             self.adj[par].append(child)

#     def dfs(self, u):
#         self.visited[u] = True
#         max1 = max2 = 0  # Track the two longest paths from this node
        
#         for v in self.adj[u]:
#             if not self.visited[v]:
#                 child_len = self.dfs(v)
#                 if self.s[u] != self.s[v]:
#                     if child_len > max1:
#                         max2 = max1
#                         max1 = child_len
#                     elif child_len > max2:
#                         max2 = child_len
        
#         # Update the global max path by considering the paths from both sides of this node
#         self.max_path = max(self.max_path, max1 + max2 + 1)
        
#         # Return the longest path that includes this node
#         return max1 + 1

#     def longestPath(self):
#         self.dfs(0)  # Start DFS from the root node
#         return self.max_path

## Lexicographically Smallest Equivalent string

# class solution:
#     def __init__(self,s1,s2,baseStr):
#         self.s1 = s1
#         self.s2 = s2
#         self.base = baseStr
#         self.n = len(s1)
#         ## initializing adj list
#         self.seti = set()
#         for i in range(self.n):
#             self.seti.add(self.s1[i])
#             self.seti.add(self.s2[i])
#         self.nodes = len(self.seti)
#         self.parent = [i for i in range(self.nodes)]

#     def find(self,e1):
#         ## preprocessing
#         ne1 = ord(e1) - ord(a)
#         if self.parent[i]==ne1:
#             return ne1
#         self.parent[ne1] = self.find(self.parent[ne1])
#         return self.parent[ne1]

#     def union(self,e1,e2):
        ## preprocessing
    #     ne1 = ord(e1) - ord(a)
    #     ne2 = ord(e2) - ord(a)
    #     p1 = self.find(ne1)
    #     p2 = self.find(ne2)
    #     if p1==p2:
    #         return
    #     if p1>p2:
    #         self.parent[p1] = p2
    #     elif p1<p2:
    #         self.parent[p2] = p1

    # def lexicographicallysmallest(self):
    #     for i in range(self.n):
    #         self.union(self.s1[i],self.s2[i])
    #     nstring = ''
    #     for i in self.base:
    #         nstring+=chr(self.find(i))
    #     return nstring
        

# ## Leetcode 2421 Number of Good Paths 
# ## - Starting and the ending node have the same values
# ##  - nodes bw the path should be less or equal to the values 
# # Rethrn Number of distinct good paths

# class solution:
#     def __init__(self,adj,edges,vals):
#         self.vals = vals
#         self.n = len(vals)
#         self.adj = [[] for _ in range(self.n)]
#         self.edges = edges
#         for u,v in self.edges:
#             self.adj[u].append(v)
#             self.adj[v].append(u)
#         self.nvalue = [[]for _ in range(self.n)]
#         for i in range(self.n):
#             self.nvalue[self.vals[i]].append(i)
#         self.parent = [i for i in range(self.n)]
#         self.rank = [0]*self.n
#         self.isActive = [False]*self.n
        
#     def find(self,e1):
#         if self.parent[e1] ==e1:
#             return e1
#         self.parent[e1] = self.find(self.parent[e1])
#         return self.parent[e1]

#     def union(self,e1,e2):
#         p1= self.find(e1)
#         p2 = self.find(e2)
#         if p1==p2:
#             return
#         if self.rank[p1]>self.rank[p2]:
#             self.parent[p2]= p1
#         elif self.rank[p1]<self.rank[p2]:
#             self.parent[p1] = p2
#         else:
#             self.parent[p2]= p1
#             self.rank[p1]+=1
    
#     def numberofgood(self):
#         count = 0
#         for i in range(self.n):
#             for node in self.nvalue[i]:
#                 self.isActive[node] = True
#             for u in self.nvalue[i]:
#                 for v in self.adj[u]:
#                     if self.isActive[v]:
#                         self.union(u, v)
#             dicti = {}
#             for u in self.nvalue[i]:
#                 par = self.find(u)
#                 if par in dicti:
#                     dicti[par].append(u)
#                 else:
#                     dicti[par] = [u]

#             # Combinatorics: calculating nc2 for each component
#             for key, value in dicti.items():
#                 size = len(value)
#                 if size > 1:
#                     count += (size * (size - 1)) // 2

#         return count + self.n

        
# class Solution:
#     def __init__(self, adj, edges, vals):
#         self.vals = vals
#         self.n = len(vals)
#         self.adj = [[] for _ in range(self.n)]
#         self.edges = edges
#         for u, v in self.edges:
#             self.adj[u].append(v)
#             self.adj[v].append(u)
#         self.parent = [i for i in range(self.n)]
#         self.rank = [0] * self.n
#         self.isActive = [False] * self.n

#     def find(self, e1):
#         if self.parent[e1] == e1:
#             return e1
#         self.parent[e1] = self.find(self.parent[e1])
#         return self.parent[e1]

#     def union(self, e1, e2):
#         p1 = self.find(e1)
#         p2 = self.find(e2)
#         if p1 == p2:
#             return
#         if self.rank[p1] > self.rank[p2]:
#             self.parent[p2] = p1
#         elif self.rank[p1] < self.rank[p2]:
#             self.parent[p1] = p2
#         else:
#             self.parent[p2] = p1
#             self.rank[p1] += 1

#     def numberOfGoodPaths(self):
#         nodes_by_value = [[] for _ in range(max(self.vals) + 1)]
#         for i in range(self.n):
#             nodes_by_value[self.vals[i]].append(i)

#         count = 0
#         for value in range(max(self.vals) + 1):
#             for node in nodes_by_value[value]:
#                 self.isActive[node] = True
#             for u in nodes_by_value[value]:
#                 for v in self.adj[u]:
#                     if self.isActive[v]:
#                         self.union(u, v)
            
#             dicti = {}
#             for u in nodes_by_value[value]:
#                 par = self.find(u)
#                 if par in dicti:
#                     dicti[par].append(u)
#                 else:
#                     dicti[par] = [u]

#             # Counting good paths
#             for key, nodes in dicti.items():
#                 size = len(nodes)
#                 if size > 1:
#                     count += (size * (size - 1)) // 2  # nC2
#                 count += size  # Each node counts as a path

#         return count

# # Test case
# vals = [1,1,2,2,3]
# edges = [[0,1],[1,2],[2,3],[2,4]]

# # Instantiate the Solution class and run the test case
# solution = Solution([], edges, vals)
# result = solution.numberOfGoodPaths()

# print(f"Number of Good Paths: {result}")


# ## 2359 Find the closest node to given 2 nodes
# import heapq
# class solution:
#     def __init__(self,edges,n1,n2):
#         self.n1  =n1
#         self.n2 = n2
#         self.edges = edges
#         self.n = len(edges)
#         self.distance1 = [float('inf')]*self.n
#         self.distance1[n1] = 0
#         self.distance2[n2] = 0
#         self.distance2 = [float('inf')]*self.n
    
#     def dfs(self,visited,distance,u):
#         self.visited[u]=True
#         v = self.edges[u]
#         if self.visited[v]!=True:
#             self.distance[v] = 1+u
#             self.dfs(v)

#     def ClosestNode(self):
#         visited1 = [False]*self.n
#         visited2 = [False]*self.n
#         self.dfs(visited1,self.distance1,n1)
#         self.dfs(visited2,self.distance2,n2)
#         result = float('inf')
#         for i in range(self.n):
#             result = min(result,max(self.distance1[i],self.distance2[i]))
#         return result

## 2492 
# import heapq

# class solution:
#     def __init__(self,n,roads):
#         self.n  = n
#         self.roads = roads
#         self.adj = [[]for _ in range(self.n)]
#         self.distance = [float('inf')]*self.n
#         self.heap = []
#         heapq.heapify(self.heap)
#         self.distance[1] = 0
#         heapq.heappush((float('inf'),1))
#         for u,v,w in self.roads:
#             self.adj[u].append((v,w))
    
#     def dijkstra(self):
#         while self.heap:
#             minimum,u = heapq.heappop(self.heap)
#             for v,vw in self.adj[u]:
#                 if self.distance[v]<min(minimum,vw):
#                     self.distance[v] = min(minimum,vw)

#         return self.distance[self.n]
        

