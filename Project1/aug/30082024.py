## leetcode 433 Minimum Genetic Mutation

# class solution:
#     def __init__(self,bank,stgene,endgene):
#         self.stgene = stgene
#         self.endgene = endgene
#         self.set = set(bank)
#         self.genes = 'ATGC'
    
#     def bfs(self):
#         if self.endgene not in self.set:
#             return -1
#         queue = [(self.stgene,1)]
#         while queue:
#             cgene,d = queue.pop(0)
#             clgene = list(cgene)
#             if cgene == self.endgene:
#                 return d
#             for i in range(8):              ## gene length is explicitly given as 8
#                 t = clgene[i]
#                 for g in self.genes:
#                     clgene[i] = g
#                     ngene = ''.join(clgene)
#                     if ngene in self.set:
#                         queue.append((ngene,d+1))
#                         self.set.remove(ngene)


# ## lc 947 Most stones removed with same row or column
# class solution:
#     def __init__(self,points):
#         self.points = points
#         self.parent = [[(i,j)for i in range(self.n)] for j in range(self.n)]
#         self.rank= [[0]*self.n for _ in range(self.n)]
#         self.n = len(self.points)
    
#     def find(self,x,y):
#         if self.parent[y][x]==(x,y):
#             return (x,y)
#         x1,y1 = self.parent[y][x]
#         self.parent[y][x] = self.find(x1,y1)
#         return self.parent[y][x]

#     def union(self,x1,y1,x2,y2):
#         p1x,p1y = self.find(x1,x2)
#         p2x,p2y = self.find(x2,y2)

#         if self.rank[p1y][p1x]>self.rank[p2y][p2x]:
#             self.parent[p2y][p2x] = self.parent[p1y][p1x]
#         elif self.rank[p1y][p1x]<self.rank[p2y][p2x]:
#             self.parent[p1y][p1x] = self.parent[p2y][p2x]
#         else:
#             self.parent[p2y][p2x] = self.parent[p1y][p1x]
#             self.rank[p1y][p1x]+=1
        
#     def Moststonesremoved(self):
#         for i in range(self.n):
#             for j in range(i+1,self.n):
#                 if self.points[i][0] == self.points[j][0] or self.points[i][1] ==self.points[j][1]:
#                     self.union(self.points[i][0],self.points[i][1],self.points[j][0],self.points[j][1])
        
## Leetcode 1926 Nearest exit from the entrace

# class solution:
#     def __init__(self,matrix,entrance):
#         self.matrix = matrix
#         self.n = len(matrix)
#         self.m = len(matrix[0])
#         self.ex = entrance[0]
#         self.ey = entrance[1]
#         self.distance = [(1,0),(0,1),(-1,0),(0,-1)]
#     def bfs(self):
#         queue = [(0,self.ex,self.ey)]
#         self.matrix[self.ey][self.ex] = "+"
#         while queue:
#             d,x,y = queue.pop(0)
#             if (x==0 or y==0 or x==self.m-1 or y==self.n-1) and (x!=self.ex and y!=self.ey):
#                 return d
#             for i,j in self.distance:
#                 nx = i+x
#                 ny = j+x
#                 if 0<=nx<self.m and 0<=ny<self.n and self.matrix[ny][nx]==".":
#                     self.matrix[ny][nx]="+"
#                     queue.append((d+1,nx,ny))
#         return -1
# matrix = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
# entrance = [1,2]
# Solution = solution(matrix,entrance)
# print(Solution.bfs())
        
# ## Leetcode 841 Keys and Rooms
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
    
#     def dfs(self,u):
#         self.visited[u]=True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.dfs(v)
    
#     def KeysRooms(self):
#         self.dfs(0)
#         for val in self.visited:
#             if not val:
#                 return False
#         return True

## Leecode 886 Possible Bipartiiton

# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.color = [-1]*self.n
#         self.visited = [False]*self.n
    
#     def dfs(self,u,color):
#         self.visited[u]=True
#         for v in self.adj[u]:
#             if self.color[v]==color:
#                 return False
#             if self.visited[v]!=True and self.color[v]==-1:
#                 nc = 1-color
#                 self.color[v]=nc
#                 if not self.dfs(v,nc):
#                     return False
#         return True

## Leetcode 834 Sum of Distance in Tree
# class solution:
#     def __init__(self,edges,n):
#         self.adj = edges
#         self.n = n
#         self.matrix = [[float('inf')]*self.n for _ in range(self.n)]
#         ## initializing matrix
#         for i,j in self.edges:
#             self.matrix[j][i]=1
#             self.matrix[i][j]=1
#         for i in range(self.n):
#             self.matrix[i][i]=0
#         self.distance = [0]*self.n
        
#     def Floydwarshall(self):
#         for via in range(self.n):
#             for v in range(self.n):
#                 for u in range(self.n):
#                     if self.matrix[u][v] > self.matrix[u][via] + self.matrix[via][v]:
#                         self.matrix[u][v] = self.matrix[u][via] + self.matrix[via][v]
#                     if self.matrix[v][u] > self.matrix[v][via] + self.matrix[via][u]:
#                         self.matrix[v][u] = self.matrix[v][via] + self.matrix[via][u]
        
        
#         for i in range(self.n):
#             count=0
#             for j in range(self.n):
#                 count+=self.matix[i][j]
#             self.distance[i] = count
#         return self.distance
                

