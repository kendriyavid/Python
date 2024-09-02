## Rotten oranges
# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.n = len(matrix)
#         self.m = len(matrix[0])
#         self.directions = [(1,0),(0,1),(-1,0),(0,-1)]
#     def bfs(self,x,y):
#         queue=[(x,y)]
#         count =0
#         while queue:
#             nqueue=[]
#             for x,y in queue:
#                 for i,j in self.directions:
#                     nx = i+x
#                     ny = j+y
#                     if 0<=nx<self.m and 0<=ny<self.n and self.matrix[ny][nx]==1:
#                         nqueue.append((nx,ny))
#                         self.matrix[ny][nx]=2
#             if nqueue:
#                 count+=1
#             queue = nqueue
#         return count
#     def rottenoranges(self,x,y):
#         time = self.bfs()
#         for i in range(self.n):
#             for j in range(self.m):
#                 if self.matrix[j][i]==1:
#                     return -1
#         return count
        
## Find eventual states
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
#         self.stack= [False]*self.n
#         self.result = []
#     def dfs(self,u):
#         self.visited[u]=True
#         self.stack[u]=True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 if self.dfs(v):
#                     return True
#             elif self.stack[v]:
#                 return True
#         self.stack[u]=False
#         return False

#     def eventualState(self):
#         for u in self.n:
#             if self.visited[u]!=True:
#                 if not self.dfs(u):
#                     self.result.append(u)
#         return self.result


# class Solution:
#     def __init__(self, adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False] * self.n
#         self.in_path = [False] * self.n  # This tracks nodes currently in the recursion stack
#         self.result = []

#     def dfs(self, u):
#         self.visited[u] = True
#         self.in_path[u] = True

#         for v in self.adj[u]:
#             if not self.visited[v]:
#                 if self.dfs(v):
#                     return True  # A cycle is detected, no need to proceed
#             elif self.in_path[v]:
#                 return True  # Cycle detected through backtracking

#         self.in_path[u] = False  # Mark the node as not in the recursion stack

        
#         return False

#     def eventualSafeNodes(self):
#         for u in range(self.n):
#             if not self.visited[u]:
#                 if not self.dfs(u):
#                     self.result.append(u)  # Add node to result if no cycle is found through it

#         return sorted(self.result)  # Return the nodes in increasing order


# # Example usage:
# adj = [[1, 2], [2, 3], [5], [0], [5], [], []]
# solution = Solution(adj)
# print(solution.eventualSafeNodes())


## word ladder

# class solution:
#     def __init__(self,wordlist):
#         self.wlist = wordlist
#         self.letters = 'abcdefghijklmnopqrstuvwxyz'
#         self.set = set(self.wlist)
#         self.Flag= True
#         self.result = []
#     def bfs(self,beginword,endword):
#         queue=[[beginword]]
#         while queue:
#             word,distance = queue.pop(0)
#             if word == endword:
#                 self.result.append(word)
#             lword = list(word)
#             for i in range(len(lword)):
#                 c = lword[i]
#                 for char in self.letters:
#                     lword[i] = char
#                     nword = ''.join(lword)
#                     if nword in self.set:
#                         queue.append((nword,distance+1))
#                         self.set.remove(nword)
#                 lword[i]=c


# ## wordladder 2
# class solution:
#     def __init__(self,wordlist):
#         self.wordlist = wordlist
#         self.result = []
#         self.letters  = 'abcdefghijklmnopqrstuvwxyz'
#         self.set = set(self.wordlist)
#         self.found  =False
#     def wordladder2(self,begin,end):
#         queue = [(False,[begin])]
#         while queue:
#             status,path = queue.pop(0)
#             word = path[-1]
#             if word == end:
#                 self.result.append(path)
#                 status = True
#             lword = list(word)
#             for c in self.letters and not status :
#                 lword[i]=c
#                 nword = ''.join(lword)
#                 if nword in self.set:
#                     path.append(nword)
#                     self.set.remove(nword)
#                     queue.append((status,path))
#                 lword = list(word)
#         return self.result

## Bellman Ford Algorithm

# class solution:
#     def __init__(self,edges,n):
#         self.edges  = edges
#         self.n = n
#         self.distance  =[float('inf')]*n
    
#     def bellmanFord(self,source):
#         self.distance[source] = 0
#         for i in range(self.n-1):
#             for u,v,w in self.edges:
#                 if self.distance[u]!=float('inf'):
#                     if self.distance[u]+w<self.distance[v]:
#                         self.distance[v] = self.distance[u]+w
        
#         for u,v,w in self.edges:
#             if self.distance[u]!=float('inf'):
#                 if self.distance[u]+w < self.distance[v]:
#                     return -1

#         return self.distance


# class Solution:
#     def __init__(self, adj):
#         self.adj = adj  # adj[i] = [(v, w), ...]
#         self.n = len(adj)
#         self.dmatrix = [[float('inf')] * self.n for _ in range(self.n)]

#         # Initializing the matrix
#         for u in range(self.n):
#             self.dmatrix[u][u] = 0  # Distance to self is zero
#             for v, w in self.adj[u]:
#                 self.dmatrix[u][v] = w  # Distance from u to v

#     def FloydWarshall(self):
#         for via in range(self.n):
#             for u in range(self.n):
#                 for v in range(self.n):
#                     if self.dmatrix[u][v] > self.dmatrix[u][via] + self.dmatrix[via][v]:
#                         self.dmatrix[u][v] = self.dmatrix[u][via] + self.dmatrix[via][v]
#         return self.dmatrix

# class solution:
#     def __init__(self,edgelist):
#         self.edgelist = edgelist
#         self.n = len(adj)
#         self.distance = [float('inf')]*self.n
    
#     def bellmanford(self,source):
#         self.distance[source] = 0
#         for i in range(self.n-1):
#             for u,v,d in self.edgelist:
#                 if self.distance[u]!=float('inf'):
#                     if d+self.distance[u]<self.distance[v]:
#                         self.distance[v] = d+self.distance[u]
    
#         for u,v,d in self.edgelist:
#             if self.distance[u]!=float('inf') and self.distance[u]+d<self.distance[v]:
#                 return -1
        
#         return self.distance


## prims algorithm
# import heapq
# class solution:
#     def __init__(self,adj):
#         self.adj =adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
#         self.heap = []
#         heapq.heapify(heap)
#         heapq.heappush(heap,(0,0,self.adj[0]))
#         self.parent = [-1]*self.n
#         self.parent[0] = -1

    
#     def Prims(self):
#         while heapq:
#             w,u,v = heapq.heappop(heap)
#             for vv,dv in self.adj[u]:
#                 if dv+

## MINIMUM cost to connect points
# import heapq
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visted = [False]*self.n
#         self.heap = []
#         self.cost = 0
#         heapq.heapify(self.heap)
#         heapq.heappush(self.heap,(0,0))
#         self.visited[u] = True
    
#     def minimumcost(self):
#         while self.heap:
#             w,u = heapq.heappop(self.heap)
#             if self.visted[u]:
#                 continue
#             self.visted[u]=True
#             self.cost+=w
#             for v,d in self.adj[u]:
#                 if self.visted[v]!=True:
#                     heapq.heappush(self.heap,(d,v))
#         return self.cost
# points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# adj = [[]for _ in range(len(points))]
# for i in range(len(points)):
#     for j in range(i+1,len(points)):
#         x1,y1 = points[i]
#         x2,y2 = points[j]
#         dist = abs(x1-x2)+abs(y1-y2)
#         adj[i].append((j,dist))
# print(adj)

import heapq

class Solution:
    def __init__(self, adj):
        self.adj = adj  # Adjacency list
        self.n = len(adj)  # Number of vertices
        self.visited = [False] * self.n  # Track visited vertices
        self.heap = []  # Min-heap to select the minimum weight edge
        self.cost = 0  # To keep track of the total cost of the MST
        heapq.heapify(self.heap)
        heapq.heappush(self.heap, (0, 0))  # Start with the first vertex (index 0)

    def minimumcost(self):
        while self.heap:
            w, u = heapq.heappop(self.heap)  # Get the edge with the smallest weight
            
            # If the vertex u is already visited, skip it
            if self.visited[u]:
                continue
            
            # Mark the vertex as visited and add the weight to the total cost
            self.visited[u] = True
            self.cost += w
            
            # Push all adjacent vertices and their weights to the heap
            for v, d in self.adj[u]:
                if not self.visited[v]:
                    heapq.heappush(self.heap, (d, v))
        
        return self.cost

# Example usage with points
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
adj = [[] for _ in range(len(points))]

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dist = abs(x1 - x2) + abs(y1 - y2)
        adj[i].append((j, dist))
        adj[j].append((i, dist))  # Add the reverse edge since it's an undirected graph

# Print the adjacency list (for verification)
print("Adjacency List:", adj)

# Create the solution object and find the minimum cost
solution = Solution(adj)
min_cost = solution.minimumcost()
print("Minimum Cost of MST:", min_cost)
