## Bellman ford algorithm
# class Solution:
#     def __init__(self,edgelist):
#         self.n = len(edgelist)-1
#         self.edgelist = edgelist
#         self.distance  = [float('inf')]*self.n
    
#     def Bellmanford(self,source):
#         for i in range(self.n-1):
#             for u,v,d in self.edgelist:
#                 if self.distance[u]!=float('inf') and self.distance[v]>self.distance[u]+d:
#                     self.distance[v] = self.distance[u]+d
        
#         ## cycle detection

#         for u,v,d in self.edgelist:
#             if self.distance[u]!=float('inf') and self.distance[v]>self.distance[u]+d:
#                 return -1

#         return self.distance

## Shortest path in weighted dag
# class Solution:
#     def __init__(self, edgelist):
#         self.edgelist = edgelist
#         self.n = len(edgelist)  # Initialize n with the length of the edge list
#         self.adj = [[] for _ in range(self.n)]
#         # Initialize adjacency list
#         for u, v, d in edgelist:
#             self.adj[u].append((v, d))
        
#         self.distance = [float('inf')] * self.n
#         self.indegree = [0] * self.n
        
#         # Calculate indegrees
#         for u in range(self.n):
#             for v, d in self.adj[u]:
#                 self.indegree[v] += 1
        
#         self.toposort = []
    
#     def toposorting(self):
#         queue = []
#         result = []
        
#         # Enqueue all nodes with 0 indegree
#         for i in range(self.n):
#             if self.indegree[i] == 0:
#                 queue.append(i)
        
#         while queue:
#             u = queue.pop(0)
#             result.append(u)
#             for v, d in self.adj[u]:
#                 self.indegree[v] -= 1
#                 if self.indegree[v] == 0:
#                     queue.append(v)
        
#         # Check if topological sorting is possible
#         if len(result) == self.n:
#             self.toposort = result
    
#     def shortestpath(self, source):
#         self.distance[source] = 0
        
#         # Iterate over the topological order
#         for u in self.toposort:
#             for v, d in self.adj[u]:
#                 if self.distance[v] > self.distance[u] + d:
#                     self.distance[v] = self.distance[u] + d
        
#         return self.distance


## Prims algorithm
## algorithm
# - use heap to do the greedy choice of the smallest node, 
# - add the node to the vissited wehen it is popped as it means the edge is in the mst
# - total weight of the mst is recorded
# import heapq
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.heap = []
#         heapq.heapify(self.heap)
#         self.visited = [False]*self.n
#         self.mst = []
#         self.total = 0
    
#     def Prims(self,source):
#         heapq.heapify(self.heap,(0,source))
#         while self.heap:
#             u,ud = heapq.heappop(self.heap)
#             self.visited[u] = True
#             self.total+=ud
#             self.mst.append(u)
#             for v,d in self.adj[u]:
#                 if self.visited[v]!=True:
#                     heapq.heappush(self.heap,(d,v))

## Most stones removed from same row/column
# class solution:
#     def __init__(self,stones,grid):
#         self.stones = stones
#         self.n = len(stones)
#         self.parent = [i for i in range(self.n)]
#         self.rank = [0]*(self.n)
    
#     def find(self,e):
#         if self.parent[e]==e:
#             return e
#         self.parent[e] = self.find(self.parent[e])
#         return self.parent[e]
    
#     def union(self,e1,e2):
#         p1 = self.find(e1)
#         p2 = self.find(e2)
#         if p1==p2:
#             return
#         if self.rank[p1]>self,rank[p2]:
#             self.parent[p2] = p1
#         elif self.rank[p2]>self.rank[p1]:
#             self.parent[p1] = p2
#         else:
#             self.parent[p2] = p1
#             self.rank[p1]+=1
    
#     def mostStonesremoved(self):
#         for i in range(self.n):
#             for j in range(i+1,self.n):
#                 if self.stones[i][0]==self.stones[j][0] or self.stones[i][1]==self.stones[i][1]:
#                     self.union(self.stones[i],self.stoness[j])
        
#         components=set()
#         for i in range(self.n):
#             components.add(self.find(i))


# class solution:
#     def __init__(self,n,edges):
#         self.n = n
#         self.edges = edges
#         self.parent1 = [i for i in range(self.n)]
#         self.parent2 = [i for i in range(self.n)]
#         self.rank1 = [0]*self.n
#         self.rank2 = [0]*self.n
    
#     def find(self,e,parent):
#         if e ==self.parent[e]:
#             return e
#         self.parent[e] = self.find(self.parent[e],parent)
#         return self.parent[e]
    
#     def union(self,e1,e2,t):
#         if t==0:
#             p1 = self.find(e1,self.parent1)
#             p2 = self.find(e2,self.parent2)
#             if self.rank1[p1]>self.rank1[p2]:
#                 self.parent1[p2] = p1
#             elif self.rank1[p2]>self.rank1[p1]:
#                 self.parent1[p1] = p2
#             else:
#                 self.rank1[p1]+=1
#                 self.parent1[p2] = p1
#         if t==1:
#             p1 = self.find(e1,self.parent2)
#             p2 = self.find(e2,self.parent2)
#             if self.rank2[p1]>self.rank2[p2]:
#                 self.parent2[p2] = p1
#             elif self.rank2[p2]>self.rank2[p1]:
#                 self.parent2[p1] = p2
#             else:
#                 self.rank2[p1]+=1
#                 self.parent2[p2] = p1
#         elif t==2:
#             p1 = self.find(e1,self.parent1)
#             p2 = self.find(e2,self.parent2)
#             if self.rank1[p1]>self.rank1[p2]:
#                 self.parent1[p2] = p1
#             elif self.rank1[p2]>self.rank1[p1]:
#                 self.parent1[p1] = p2
#             else:
#                 self.rank1[p1]+=1
#                 self.parent1[p2] = p1
#             p1 = self.find(e1,self.parent2)
#             p2 = self.find(e2,self.parent2)
#             if self.rank2[p1]>self.rank2[p2]:
#                 self.parent2[p2] = p1
#             elif self.rank2[p2]>self.rank2[p1]:
#                 self.parent2[p1] = p2
#             else:
#                 self.rank2[p1]+=1
#                 self.parent2[p2] = p1
#     def MaxRemoval(self):



## Trees
class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
class Tree:
    def __init__(self):
        self.root = None
    
    def append(self,val):
        if self.root==None:
            self.root = self.Node(val)
            return
        self._append()
          
    def _append(self,val):
        if self.left==None:


