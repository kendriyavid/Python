## Revision
## DFS
# class solution:
#     def __init__(self):
#         self.adj = adj
#         self.visited=[False]*len(adj)
#     def dfs(self,u):
#         self.visited[u]=True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.dfs(v)

## BFS
# class solution:
#     def  __init__(self,adj):
#         self.adj = adj
#         self.visited=[False]*len(adj)
#     def bfs(self,u):
#         queue=[u]
#         self.visited[u]=True
#         while queue:
#             u=queue.pop(0)
#             for v in self.adj[u]:
#                 if self.visited[v]!=True:
#                     queue.append(v)
#                     self.visited[v]=True

## Cycle detection directed graphs

# class solution:
#     def __init__(self,adj):
#         self.adj = adj   
#         self.stack=[False]*len(adj)
#         self.visited=[False]*len(adj)
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

## Graph is bipartite:
# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.color=[-1]*len(adj)
#     def dfs(self,u,color):
#         self.color[u]=color
#         for v in self.adj[u]:
#             if self.color[v]==color:
#                 return False 
#             if self.color[v]==-1:
#                 nc  = 1-color
#                 if not dfs(self,v,nc):
#                     return False
#         return True

## BFS approach
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.color = [-1]*len(self.adj)
#     def bfs(self,u,color):
#         queue=[(u,color)]
#         self.color[u]=color
#         while queue:
#             u,color = queue.pop(0)
#             for v in self.adj[u]:
#                 if self.color[v]==color:
#                     return False
#                 if self.color[v]==-1:
#                     nc  =1-color
#                     queue.append((v,nc))
#                     self.color[v] = nc
#         return True


### Topological sorting 
## dfs mULTIPLE
## bfs 

## dsu implementation


# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.parent = [i for i in range(len(self.adj))]
#         self.rank = [0]*len(self.adj)
#     def find(self,e):
#         if self.parent[e] ==e:
#             return e
#         self.parent[e] = self.find(self.parent[e])
#         return self.parent[e]
    
#     def union(self,e1,e2):
#         p1 = self.find(e1)
#         p2 = self.find(e2)
#         if p1==p2:
#             return True
#         if self.rank[p1]>self.rank[p2]:
#             self.parent[p2] = p1
#         elif self.rank[p2]>self.rank[p1]:
#             self.parent[p1] = p2
#         else:
#             self.parent[p2] = p1
#             self.rank[p1]+=1

#Dijsktra Algorithm
# import heapq
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.heap = []
#         heapq.heapify(self.heap)
#         self.result=[float('inf')]*len(self.adj)

#     def Dijsktra(self,source):
#         self.result[source] = 0
#         heapq.heappush(self.heap,(0,source))
#         while self.heap:
#             d,u = heapq.heappop(heap)
#             for v,dv in self.adj[v]:
#                 if d+dv<self.result[v]:
#                     self.result[v] = d+dv
#                     heapq.heappush(heap,(d+dv,v))
#         return self.result

## bFS MATRIX SHORTEST PATH

# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.n=len(matrix)
#         self.queue=[]
#         self.directions=[(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
#     def bmshortest(self,source,destination):
#         self.queue.append((source,1))
#         self.matrix[source[0]][source[1]]=1
#         while self.queue:
#             x,y,distance = self.queue.pop(0)
#             if x==self.n-1 and y==self.n-1:
#                 return self.distance+1
#             for dir in self.directions:
#                 i,j = dir
#                 nx = x+i
#                 ny=y+j
#                 if 0 <= nx < self.n and 0 <= ny < self.n and self.matrix[nx][ny] == 0:
#                     self.matrix[nx][ny] = 1  # Mark as visited
#                     self.queue.append((nx, ny, distance + 1))



## lc 1631 Path with minimum effort
# import heapq
# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.heap =[]
#         self.n = len(matrix)
#         heapq.heapify(self.heap)
#         self.directions=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)]
#         self.result=[[0]*len(self.matrix) for _ in range(len(self.matrix))]
#     def pathwithmineffort(self,source,destination):
#         heapq.heappush((0,(source[1],source[0])))
#         self.result[0][0]=0
#         while queue:
#             w,(x,y) = heapq.heappop(self.heap)
#             if x==self.n-1 and y==self.n-1:
#                 return w
#             for i,j in self.directions:
#                 nx = x+i
#                 ny= y+j
#                 if nx<0 or ny<0 or nx>=self.n or ny>=self.n:
#                     if abs(self.matrix[ny][nx]-self.matrix[y][x])< self.result:
#                         self.matrix[ny][nx] = abs(self.matrix[ny][nx]-self.matrix[y][x])
#                         heapq.heappush(heap,(abs(self.matrix[ny][nx]-self.matrix[y][x]),(nx,ny)))
# return -1

# def dfs(i,j,dp):
#     if i<0 or j<0:
#         return float('inf')
#     if i==0 and j==0:
#         return dp[i][j]
#     l=dfs(i,j-1)
#     r=dfs(i-1,j)
#     if l>r:
#         dp[i][j]=max(r,abs(matrix[i][j+1]-matrix[i][j]))
#     else:
#         dp[i][j]=max(l,abs(matrix[i+1][j]-matrix[i][j]))
#     return dp[i][j]


## Number of Islands
## BFS approach

# class Solution:
#     def __init__(self, matrix):
#         self.n = len(matrix)
#         self.m = len(matrix[0])
#         self.matrix = matrix
#         self.visited = [[False] * self.m for _ in range(self.n)] 
#         self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Add all four directions for BFS

#     def bfs(self, i, j):
#         queue = [(i, j)]
#         self.visited[i][j] = True
#         while queue:
#             x, y = queue.pop(0)
#             for dx, dy in self.directions:
#                 nx = x + dx
#                 ny = y + dy
#                 if 0 <= nx < self.n and 0 <= ny < self.m and self.matrix[nx][ny] == 1 and not self.visited[nx][ny]:
#                     queue.append((nx, ny))
#                     self.visited[nx][ny] = True

#     def NumberofIslands(self):
#         count = 0
#         for i in range(self.n):
#             for j in range(self.m):
#                 if self.matrix[i][j] == 1 and not self.visited[i][j]:
#                     self.bfs(i, j)
#                     count += 1
#         return count


## DFS approach
# class Solution:
#     def __init__(self, matrix):
#         self.matrix = matrix
#         self.n = len(matrix)
#         self.m = len(matrix[0])
#         self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Down, Left, Up
#         self.visited = [[False] * self.m for _ in range(self.n)]

#     def dfs(self, x, y):
#         self.visited[y][x] = True
#         for i, j in self.directions:
#             nx = x + i
#             ny = y + j
#             if 0 <= nx < self.m and 0 <= ny < self.n and not self.visited[ny][nx] and self.matrix[ny][nx] == 1:
#                 self.dfs(nx, ny)

#     def numberOfIslands(self):
#         count = 0
#         for j in range(self.n):
#             for i in range(self.m):
#                 if self.matrix[j][i] == 1 and not self.visited[j][i]:
#                     self.dfs(i, j)
#                     count += 1
#         return count


## DSU approach

# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.n= len(self.matrix)
#         self.m = len(self.matrix[0])
#         self.parent = [[0]*self.m for _ in range(self.n)]
#         self.rank =  [[0]*self.m for _ in range(self.n)]
#         self.direction = [(1,0),(0,-1)]
#         # parent initialization
#         for j in range(self.n):
#             for i in range(self.m):
#                 self.parent[j][i]=(i,j)

#     def find(self,x,y):
#         if self.parent[y][x]==(x,y):
#             return (x,y)
#         self.parent[y][x]=self.find(self.parent[y][x])
#         return self.parent[y][x]
    
#     def union(self,x1,y1,x2,y2):
#         px1,py1 = self.find(x1,y1)
#         px2,py2 = self.find(x2,y2)

#         if p1x==p2x and p1y==p2y:
#             return    
     
#         if self.rank[py1][px1]>self.rank[py2][px1]:
#             self.parent[y2][x2] = (x1,y1)
#         elif self.rank[py1][px1]<self.rank[py2][px1]:
#             self.parent[y1][x1] = (x2,y2)
#         else:
#             self.parent[y2][x2] = (x1,y1)
#             self.rank[y1][x1]+=1

#     def NumberofIslands(self):
#         for j in range(self.n):
#             for i in range(self.m):
#                 for x,y in self.direction:
#                     nx = x+i
#                     ny = x+y
#                     if self.matrix[ny][nx]==1 and 0<nx<=len(self.matrix[0]) and 0<ny<=len(self.matrix):
#                         self.union(x,y,nx,ny)

class Solution:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(self.matrix)
        self.m = len(self.matrix[0])
        self.directions = [(1, 0), (0, 1), (1, 1), (-1, -1)]
        self.visited = [[False] * self.m for _ in range(self.n)]
    
    def floodfill(self, sx, sy, nc):
        queue = [(sx, sy)]
        self.visited[sy][sx] = True
        
        while queue:
            x, y = queue.pop(0)
            self.matrix[y][x] = nc
            
            for dir in self.directions:
                nx = x + dir[0]
                ny = y + dir[1]
                
                if 0 <= nx < self.m and 0 <= ny < self.n and self.matrix[ny][nx] == 1 and not self.visited[ny][nx]:
                    queue.append((nx, ny))
                    self.visited[ny][nx] = True  # Mark as visited
        
        return self.matrix
