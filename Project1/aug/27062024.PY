# DFS Undirected Graph

# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n =len(self.adj)
#         self.visited = [False]*self.n
    
#     def dfs(self,u):
#         self.visited[u]=True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.dfs(v)
    
#     def DepthFirst(self):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 self.dfs(u)
        
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
    
#     def bfs(self,u):
#         queue=[u]
#         self.visited[u]=True
#         while queue:
#             u = queue.pop(0)
#             for v in self.adj[u]:
#                 if self.visited[v]!=True:
#                     queue.append(v)
#                     self.visited[v]=True
    
#     def Breadthfirst(self):
#         for u in self.n:
#             if self.visited[u]!=True:
#                 self.bfs(u)
        
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(self.adj)
#         self.visited = [False]*self.n
    
#     def dfs(self,u,parent):
#         self.visited[u]=True
#         for v in self.adj:
#             if self.visited[v]!=True:
#                 if self.dfs(v,u):
#                     return True
#             elif parent!=v:
#                 return True
#         return False

#     def CycleDetection(self):
#         for u in self.n:
#             if self.visited[u]!=True:
#                 if self.dfs(u,-1):
#                     return True
#         return False

# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited  =[False]*self.n
    
#     def bfs(self,u,parent):
#         queue=[(u,parent)]
#         self.visited[u]=True
#         while queue:
#             u,parent = queue.pop(0)
#             for v in self.adj[u]:
#                 if self.visited[v]!=True:
#                     queue.append((v,u))
#                     self.visited[v]=True
#                 elif parent!=v:
#                     return True
#         return False
#     def CycleDetection(self):
#         for u in self.n:
#             if self.visited[u]!=True:
#                 if self.bfs(u,-1):
#                     return True
#         return False
            

# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
#         self.stack=[False]*self.n
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
#     def CycleDetection(self):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 if self.dfs(u):
#                     return True
#         return False

## Flood Fill

# class solution:
#     def __init__(self,adj,marking):
#         self.adj = adj
#         self.marking = marking
#         self.n = len(self.adj)
#         self.visited = [False]*self.n
#     def bfs(self,u):
#         queue=[u]
#         self.visited[u]=True
#         while queue:
#             u = queue.pop(0)
#             ## do the marking
#             for v in self.adj[u]:
#                 if self.visited[v]!=True:
#                     queue.append(v)
#                     self.visited[v]=True


# class solution:
#     def __init__(self,adj,marking):
#         self.adj = adj
#         self.n = len(adj)
#         self.marking =marking
#         self.visited= [False]*self.n
#     def dfs(self,u):
#         self.visited[u]=True
#         ## Do the marking
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.dfs(v)

## Topological sorting

# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
#         self.stack=[]
#     def dfs(self,u):
#         self.visited[u]=True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.dfs(v)
#         self.stack.append(u)
#     def Topological(self):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 self.dfs(u)
#         return self.stack[::-1]


# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n= len(self.adj)
#         self.inorder=[0]*self.n
#         for i in range(self.n):
#             for neighbor in self.adj[i]:
#                 self.in_degree[neighbor] += 1
#         self.queue=[]
#         for i in range(len(self.adj)):
#             if self.inorder[i]==0:
#                 self.queue.append(i)
#         self.result=[]
#     def Topological(self):
#         while self.queue:
#             u = self.queue.pop(0)
#             self.result.append(u)
#             for v in self.adj[u]:
#                 self.inorder[v]-=1
#                 if self.inorder[v]==0:
#                     self.queue.append(v)
#         return self.result

# DSU implemetnation
# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.n=len(adj)
#         self.parent=[i for i in range(self.n)]
#         self.rank = [0]*self.n
    
#     def find(self,element):
#         if self.parent[element] == element:
#             return element
#         self.parent[element] = self.find(self.parent[element])
#         return self.parent[element]
    
#     def union(self,e1,e2):
#         p1 = self.find(e1)
#         p2 = self.find(e2)
#         if p1==p2:
#             return True
#         if self.rank[p1]>self.rank[p2]:
#             self.parent[p2] = p1
#         elif self.rank[p1]<self.rank[p2]:
#             self.parent[p1] = p1
#         else:
#             self.parent[p2]==p1
#             self.rank[p1]+=1
#     def cycleDetection(self):
#         for i in range(self.n):
#             for rel in self.adj[i]:
#                 if self.union(i,rel):
#                     return True
#         return False


## Number of Provinces

## n cities, nxn matrix, if matrix[i][j]==1 then i and j are connected
## Return number of provinces
# class Solution:
#     def __init__(self, matrix):
#         self.matrix = matrix
#         self.n = len(self.matrix)
#         self.parent = [i for i in range(self.n)]
#         self.rank = [0] * self.n  # Initialize rank as a list of zeros
    
#     def find(self, x):
#         if self.parent[x] == x:
#             return x
#         self.parent[x] = self.find(self.parent[x])  # Path compression
#         return self.parent[x]
    
#     def union(self, x, y):
#         p1 = self.find(x)
#         p2 = self.find(y)
#         if p1 == p2:
#             return
#         if self.rank[p1] > self.rank[p2]:
#             self.parent[p2] = p1
#         elif self.rank[p1] < self.rank[p2]:
#             self.parent[p1] = p2
#         else:
#             self.parent[p2] = p1
#             self.rank[p1] += 1
    
#     def NumberofProvinces(self):
#         for i in range(self.n):
#             for j in range(self.n):
#                 if self.matrix[i][j] == 1:
#                     self.union(i, j)
        
#         # Calculate the number of distinct provinces
#         return len(set(self.find(i) for i in range(self.n)))

# # Example usage:
# matrix = [
#     [1, 1, 0],
#     [1, 1, 0],
#     [0, 0, 1]
# ]

# sol = Solution(matrix)
# print(sol.NumberofProvinces())  # Output should be 2

## NUMBER OF ISLANDS
## MXN GRID 1 IS LAND AND 0 IS WATER
## WILL TRAVERSE THE MATRIX AND AT EACH POINT WILL CHEKC UP ADN LEFT FOR 1 IF FOUND THEN DO THE UNION

# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.n = len(self.matrix)
#         self.m = len(self.matrix[0])
#         self.parent = [[(i,j)]for i in range(self.m) for j in range(self.n)]
#         ## inittializing the parent
#         count=0
#         for i in range(self.n):
#             for j in range(self.m):
#                 self.matrix[j][i]=count
#                 count+=1
#         self.rank = [[0]*self.n for _ in range(self.m)]
#     def find(self,x1,y1):
#         if self.parent[y1][x1] ==(x1,y1):
#             return (x1,y1)
#         self.parent[y1][x1] = self.find(self.parent[y1][x1])
#         return self.parent[y1][x1]
    
#     def union(self,x1,y1,x2,y2):
#         p1x,p1y = self.find(x1,y1)
#         p2x,p2y = self.find(x2,y2)
#         if p1x==p2x and p1y==p2y:
#             return
#         if self.rank[p1y][p1x]>self.rank[p2y][p2x]:
#             self.parent[p2y][p2x] = (p1x,p1y)
#         elif self.rank[p1y][p1x]<self.rank[p2y][p2x]:
#             self.parent[p1y][p1x] = (p2x,p2y)
#         else:
#             self.parent[p2y][p2x] = (p1x,p1y)
#             self.rank[p1y][p1x]+=1
    
#     def NumberofIslands(self):
#         for i in range(self.n):
#             for j in range(self.m):
#                 if i-1>=0 and j-1>=0:
#                     if self.matrix[j-1][i-1]==1:
#                         self.union(j,i,j-1,i-1)
        
#         return len(set(self.find(i,j) for i in range(self.n) for j in range(self.m)))
                
## Rotten oranges
## mxn grid  0- empty 1- fresh 2- Rotten evvery minute 

# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.n = len(matrix)
#         self.m = len(matrix[0])
#         self.visited =[[False]*self.m for _ in range(self.n)]
#         self.directions=[(1,0),(0,1),(-1,0),(0,-1)]
    
#     def bfs(self,x,y,):
#         queue=[(x,y)]
#         self.visited[y][x]=True
#         count=0
#         while queue:
#             count+=1
#             nqueue=[]
#             for x,y in queue
#                 for i,j in self.directions:
#                     nx = i+x
#                     ny = j+y
#                     if 0<=nx<self.m and 0<=ny<self.n and self.matrix[ny][nx]==1 and self.visited[ny][nx]!=True:
#                         nqueue.append((nx,ny))
#                         self.visited[ny][nx]=True
#                         self.matrix[ny][mx]=2
#                 queue = nqueue
#         return self.matrix


## 01 MATRIX
# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.n =len(matrix)
#         self.m = len(matrix[0])
#         self.distance = [[float('inf')]*self.n for _ in range(self.m)]
#         self.distance = [(1,0),(0,1),(-1,0),(0,-1)]
#     def bfs(self):
#         queue=[]
#         for i in range(self.n):
#             for j in range(self.m):
#                 if self.matrix[j][i]==1:
#                     queue.append((i,j))
#                 else:
#                     self.distance[j][i]=0
        
#         while queue:
#             x,y = queue.pop(0)
#             for i,j in self.distance:
#                 nx = x+i
#                 ny = y+j
#                 if 0<=nx<self.m and 0<=ny<self.n and self.matrix[ny][mx]==1:
#                     if self.distance[ny][nx]>self.distance[y][x]+1:
#                         self.distance[nt[x]=self.distance[ny][nx]+1
        
#         return self.distance

# ## Number of enclaves
# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.n = len(matrix)
#         self.m =len(matrix[0])
#         self.directions=[(1,0),(0,1),(-1,0),(0,-1)]
#     def bfs(self):
#         queue=[]
#         for i in range(self.n):
#             for j in range(self.m):
#                 if self.matrix[j][i]==1 and(i==0 or j==0 or i==self.n-1 or j==self.m-1):
#                     queue.append((i,j))
#         while queue:
#             x,y = queue.pop(0)
#             for i,j in self.directions:
#                 nx=x+i
#                 ny=y+j
#                 if 0<=nx<self.m and 0<=ny<self.n and self.matrix[ny][nx]==1:
#                     self.matrix[ny][nx]==0
#                     queue.append(nx,ny)
#         count=0
#         for i in range(self.n):
#             for j in range(self.m):
#                 if self.matrix[j][i]==1:
#                     count+=1
#         return count
                
## Find eventual safe state
## DO the dfs and then if the cycle is detected then do not add it ot the result
## will do the dfs and if the node is not visited then visit it elif the node is visited and is also in visited stack then we wont add the node to the safestate else we will add the node

class solution:
    def __init__(self,adj):
        self.adj = adj
        self.n = len(adj)
    
    def dfs(self,u):
        self.vistedStack[u]=True
        for v in self.adj[u]:
            if self.dfs(v):
                return True
            elif self.vistedStack[v]:
                return True
        self.vistedStack[u]=False
        return False
    
    def EventualState(self):
        result=[]
        for u in range(self.n):
            self.vistedStack=[False]*self.n
            if not self.dfs(u):
                result.append(u)
        return result








