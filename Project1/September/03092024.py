## Sum of distance in tree Leetcode Hard
## do the dfs and simultaneously calculate the 
#  - total nodes
#   -  total distance of the first parent
#    - child array
## loop over the array to find the distance information


# class solution:
#     def __init__(self,edges,n):
#         self.n = n
#         self.edges =edges
#         self.adj = [[]for _ in range(self.n)]
#         ## initialization of the adj
#         for u,v in self.edges:
#             self.adj[u].append(v)
#         self.distance = [0]*self.n
#         self.children = [0]*self.n
#         self.visited = [False]*self.n
#         self.result = [0]*self.n

# ## return the value of the number of nodes and total distance
#     def predfs(self,u,depth):
#         self.visited[u]=True
#         distance =depth
#         children = 1
#         for v in self.adj[u]:
#             d,c=self.dfs(v,depth+1)
#             distance+=d
#             children+=c
#         self.children[u] = children
#         return distance,children
    
#     def dfs(self,u):
#         self.visited[u] = True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.distance[v] = self.distance[u] - self.children[v] +(self.n - self.children[v])
    
#     def SumofDistance(self):
#         self.distance[0] = self.predfs(0)
#         self.visited = [False]*self.n
#         self.dfs(0)
#         return self.distance

# class solution:
#     def __init__(self,graph):
#         self.adj= graph
#         self.n = len(graph)
#         self.result = []
#         self.visited = [False]*self.n
#         self.end = self.n-1
    
#     def dfs(self,u,path):
#         self.visited[u]=True
#         path.append(u)
#         if u==self.end:
#             self.result.append(path)
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.dfs(v)
#         path.pop()
#         self.visited[u] = False
    
#     def allpaths(self):
#         return self.dfs(0,[])
    
# class Solution:
#     def __init__(self,edges,hasApple,n):
#         self.edges =edges
#         self.hasApple = hasApple
#         self.n = n
#         self.adj = [[]for _ in range(self.n)]
#         ## initialization of the adj:
#         for u,v in self.edges:
#             self.adj[u].append(v)
#             self.adj[u].append(v)
#         self.visited = [False]*(self.n)
#         self.time = 0
    
#     def dfs(self,u):
#         self.visited[u] = True
#         apple = self.hasApple[u]  # Start by considering if current node has an apple
#         for v in self.adj[u]:
#             if not self.visited[v]:
#                 if self.dfs(v):
#                     self.time += 2  # Add time for going to and coming back from v
#                     apple = True
#         return apple
    
#     def mintimeApple(self):
#         self.dfs(0)
#         return self.time

# edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
# n = 7
# hasApple = [False,False,True,False,True,True,False]
# solution = Solution(edges,hasApple,n)
# print(solution.mintimeApple())


## 2246 Longest path with different adjecent nodes

# class Solution:
#     def __init__(self,parent,s):
#         self.parent = parent
#         self.n = n
#         self.adj = [[]for _ in range(self.n)]
#         for i in range(1,len(self.parent)):
#             self.adj[i].append(self.parent[i])
#             self.adj[self.parent[i]].append(i)
#         self.visited = [False]*self.n
#         self.maxpath = float('-inf')
    
#     def dfs(self,u):
#         self.visited[u]=True
#         m1 = 0
#         m2 = 0
#         for v in self.adj[u]:
#             if self.visited[u]!=True and self.parent[u]!=self.parent[v]:
#                 if self.dfs(v)>m1:
#                     m2 = m1
#                     m1 = self.dfs(v)
#                 elif self.dfs(v)>m2:
#                     m2 = self.dfs(v)
#         self.maxpath = max(self.maxpath,(1+m1+m2))
#         return 1+max(m1,m2)

# Minimum score 2492
# import heapq
# class solution:
#     def __init__(self,n,roads):
#         self.n = n
#         self.roads= roads
#         self.adj = [[]for _ in range(self.n)]
#         ## initialization of adj
#         for u,v,w in self.roads:
#             self.adj[u-1].append((v-1,w))
#             self.adj[v-1].append((u-1,w))
#         self.score  =[float('inf')]*self.n
#         self.queue = [(float('inf'),0)]
#         # heapq.heapify(self.heap)
#         # heapq.heappush(self.heap,(float('inf'),0))
#     def bfs(self):
#         self.score[0] = 0
#         while self.queue:
#             uw,u = self.queue.pop(0)
#             for v,w in self.adj[u]:
#                 if self.score[v]>min(w,uw):
#                     self.score[v] = min(w,uw)
#                     self.queue.append((self.score[v],v))
#     def minimumScore(self):
#         self.bfs()
#         return self.score[n-1]
# n = 4
# roads = [[1,2,2],[1,3,4],[3,4,7]]
# Solution = solution(n,roads)
# print(Solution.minimumScore())


import heapq

class Solution:
    def __init__(self, n, roads):
        self.n = n
        self.roads = roads
        self.adj = [[] for _ in range(self.n)]
        ## initialization of adj
        for u, v, w in self.roads:
            self.adj[u-1].append((v-1, w))
            self.adj[v-1].append((u-1, w))
        self.score = [float('inf')] * self.n
        self.queue = [(float('-inf'), 0)]  # start with a score of -inf to ensure the first path is explored

    def bfs(self):
        self.score[0] = float('inf')
        heapq.heapify(self.queue)
        
        while self.queue:
            uw, u = heapq.heappop(self.queue)
            uw = -uw  # converting back to positive since we store as negative for max-heap behavior
            for v, w in self.adj[u]:
                min_score = min(uw, w)
                if self.score[v] > min_score:
                    self.score[v] = min_score
                    heapq.heappush(self.queue, (-self.score[v], v))

    def minimumScore(self):
        self.bfs()
        return self.score[self.n - 1]

n = 4
roads =[[1,2,9],[2,3,6],[2,4,5],[1,4,7]]


Solution = Solution(n, roads)
print(Solution.minimumScore())

