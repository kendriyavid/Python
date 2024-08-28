# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.directions = [(1,0),(0,1),(-1,0),(0,-1)]
#         self.n = len(matrix)
#         self.m = len(self.matrix[0])
#     def bfs(self,x,y):
#         queue=[(x,y)]
#         count=0
#         minimum=float('inf')
#         while queue:
#             nqueue=[]
#             for x,y in queue:
#                 for i,j in self.directions:
#                     nx = x+i
#                     ny = y+j
#                     if 0<=nx<self.m and 0<=ny<self.n:
#                         if self.matrix[ny][nx]==1:
#                             nqueue.append((nx,ny))
#                         else:
#                             minimum = min(minimum,count)    
#         if nqueue:
#             count+=1
#         queue = nqueue
#         return minimum
        
                
# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.n = len(matrix)
#         self.m = len(matrix[0])
#         self.distance = [[(float(-'inf'))]*self.m for _ in range(self.n)]
#         self.queue=[]
#         for i in range(self.n):
#             for j in range(self.m):
#                 if self.matrix[j][i]=='x':
#                     self.distance[j][i]=0
#                 else:
#                     self.queue.append((i,j))
#         self.directions = [(1,0),(0,1),(-1,0),(0,-1)]

#     def bfs(self):
#         while self.queue:
#             x,y = self.queue.pop(0)
#             for i,j in self.directions:
#                 nx =i+x
#                 ny = j+y
#                 if 0<=nx<self.m and 0<=ny<self.n:
#                     if self.distance[y][x]<self.distance[ny][nx]+1:
#                         self.distance[y][x]=self.distance[ny][nx]+1
#                         self.queue.append((nx,ny))
#         return self.distance

# class Solution:
#     def __init__(self, matrix):
#         self.matrix = matrix
#         self.n = len(matrix)
#         self.m = len(matrix[0])
#         self.visited = [[False] * self.m for _ in range(self.n)]
#         self.result = set()
#         self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
#     def bfs(self, x, y):
#         res = []
#         queue = [(x, y)]
#         bx, by = x, y
#         self.visited[y][x] = True
        
#         while queue:
#             x, y = queue.pop(0)
#             res.append((x - bx, y - by))
#             for i, j in self.directions:
#                 nx = x + i
#                 ny = y + j
#                 if 0 <= nx < self.m and 0 <= ny < self.n and not self.visited[ny][nx] and self.matrix[ny][nx] == 1:
#                     queue.append((nx, ny))
#                     self.visited[ny][nx] = True
#                     res.append((nx - bx, ny - by))
                    
#         return tuple(res)  # Using tuple to make it hashable for the set

#     def distinctIslands(self):
#         for i in range(self.n):
#             for j in range(self.m):
#                 if not self.visited[i][j] and self.matrix[i][j] == 1:
#                     res = self.bfs(j, i)
#                     self.result.add(res)
                    
#         return len(self.result)


# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.stack=[False]*len(self.adj)
#         self.result=[]
#     def dfs(self,u):
#         self.visited[u]=True
#         self.stack[u]=True
#         res=False
#         for v in self.adj[v]:
#             if self.visited[v]!=True:
#                 if self.dfs(v):
#                     res = res or True
#             elif self.stack[u]==True:
#                 res = res or True
#         self.stack[u]=False
#         return res
#     def eventualSafestate(self):
#         for i in range(len(self.adj)):
#             self.visited = [False]*len(self.adj)
#             if self.dfs(i):
#                 self.result.append(i)
#         return self.result

# class Solution:
#     def __init__(self, adj):
#         self.adj = adj
#         self.stack = [False] * len(self.adj)
#         self.visited = [False] * len(self.adj)
#         self.result = []
    
#     def dfs(self, u):
#         self.visited[u] = True
#         self.stack[u] = True
#         res = False
#         for v in self.adj[u]:  # Corrected from self.adj[v] to self.adj[u]
#             if not self.visited[v]:
#                 if self.dfs(v):
#                     res = res or True
#             elif self.stack[v]:  # Corrected from self.stack[u] to self.stack[v]
#                 res = res or True
#         self.stack[u] = False
#         return res
    
#     def eventualSafestate(self):
#         for i in range(len(self.adj)):
#             if not self.visited[i]:
#                 if not self.dfs(i):
#                     self.result.append(i)
#         return self.result


