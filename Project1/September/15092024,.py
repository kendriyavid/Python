# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
    
#     def dfs(self,node):
#         self.visited[node] = visited
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.visited[v] = True
#                 self.dfs(v)

# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
    
#     def bfs(self,node):
#         queue = [node]
#         self.visited[node] = True
#         while queue:
#             u = queue.pop(0)
#             for v in self.adj[u]:
#                 if self.visited[v]!=True:
#                     self.visited[v] = True
#                     queue.append(v)

## undirected graph cycle detection
## dfs,bfs approach pass the parent and check for the alreadyvisited nodes
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n =len(adj)
#         self.visited = [False]*self.n
    
#     def dfs(self,node,parent):
#         self.visited[node] = True
#         for v in self.adj[node]:
#             if self.visited[v]!=True:
#                 if self.dfs(v,node):
#                     return True
#             elif parent!=v:
#                 return True
#         return False
            


# ##bfs approach
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
    
#     def bfs(self,node):
#         queue =[(node,-1)]
#         while queue:
#             u,parent = queue.pop(0)
#             for v in self.adj[u]:
#                 if self.visited[v]!=True:
#                     queue.append((v,u))
#                     self.visited[v] = True
#                 elif v!=parent:
#                     return True
#         return False


## Directed graph dfs approach

# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
#         self.stack = [False]*self.n
    
#     def dfs(self,node):
#         self.visited[node] = True
#         self.stack[node] = True
#         for v in self.adj[node]:
#             if self.visited[v]!=True:
#                 if self.dfs(v):
#                     return True
#             elif self.stack[v]==True:
#                 return True
#         self.stack[u] = False
#         return False


## Topological sorting
## dfs method
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.result = []
#         self.visited
#     def Toposorting(self,node):
#         self.visited[node] = True
#         for v in self.adj[node]:
#             if self.visited[v]!=True:
#                 self.adj(v)
#         self.result.append(u)

# ## bfs approach
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.indegree = [0]*self.n
#         for u in range(self.n):
#             for v in self.adj[u]:
#                 self.indegree[v]+=1
#         self.result = []
#     def toposorting(self):
#         queue = []
#         for i in range(len(self.indegree)):
#             if self.indegree[i]==0:
#                 queue.append(i)
#         while queue:
#             u = queue.pop(0)
#             result.append(u)
#             for v in self.adj[u]:
#                 self.indegree[v]-=1
#                 if self.indegree[v]==0:
#                     self.queue.append(v)
            
## Number of provinces
# class Solution:
#     def find(self,e):
#         if self.parent[e] == e:
#             return e
#         self.parent[e] = self.find(e)
#         return self.parent[e]

#     def union(self,e1,e2):
#         p1 = self.find(e1)
#         p2 = self.find(e2)
#         if p1==p1:
#             return 
#         if self.rank[p1]>self.rank[p2]:
#             self.parent[p2] = p1
#         elif self.rank[p2]>self.rank[p1]:
#             self.parent[p1] = p2
#         else:
#             self.parent[p2] = p1
#             self.rank[p1]+=1

#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         self.matrix = isConnected
#         self.n = len(self.matrix)
#         self.rank = [0]*self.n
#         self.parent = [i for i in range(self.n)]
#         provinces = 0
#         for i in range(self.n):
#             for j in range(self.n):
#                 if i==j:
#                     continue
#                 if self.matrix[j][i] ==1:
#                     self.union(i,j)
        
#         for i in range(self.n):
#             for j in range(self.n):
#                 if i==j:
#                     continue
#                 if self.find(i)==self.find(j):
#                     provinces+=1
#         return provinces

# class Solution(object):
#     def bfs(self,ux,uy):
#         queue = [(ux,uy)]
#         self.visited[uy][ux]=True
#         while queue:
#             i,j = queue.pop(0)
#             for x,y in self.directions:
#                 nx= x+i
#                 ny = y+j
#                 if 0<=nx<self.m and 0<=ny<self.n and self.visited[ny][nx]!=True and self.grid[ny][nx]==1:
#                     queue.append((nx,ny))
#                     self.visited[ny][nx] = True

#     def numIslands(self, grid):
#         self.grid = grid
#         self.n = len(grid)
#         self.m = len(grid[0])
#         self.visited = [[False]*self.m for _ in range(self.n)]
#         self.directions =[(0,1),(1,0),(-1,0),(0,-1)]
#         self.islandcount=0
#         for i in range(self.m):
#             for j in range(self.n):
#                 if self.visited[j][i]!=True and self.grid[j][i]==1:
#                     self.islandcount+=1
#                     self.dfs(i,j)
#         return self.islandcount

## multisource bfs
# class Solution:
#     def __init__(self,grid):
#         self.grid = grid
#         self.n =len(grid)
#         self.m= len(grid[0])
#         self.directions  = [(1,0),(0,1),(-1,0),(0,-1)]
#     def bfs(self):
#         queue=[]
#         count = 0
#         for i in range(self.n):
#             for j in range(self.m):
#                 if self.grid[i][j] == 2:
#                     queue.append((j,i))
#                 elif self.grid[i][j]==1:
#                     count+=1
#         totalTime =0
#         while queue:
#             nqueue=[]
#             for x,y in self.directions:
#                 for i,j in self.directions:
#                     nx = i+x
#                     ny = i+y
#                     if 0<=nx<self.m and 0<=ny<self.n and self.grid[ny][nx]==1:
#                         self.queue.append((nx,ny))
#                         self.grid[ny][nx] = 2
#                         count-=1
#         if count==0:
#             return totalTime
#         else:
#             return -1


# class Solution:
#     def __init__(self,grid):
#         self.grid = grid
#         self.n = len(grid)
#         self.m = len(grid[0])
#         self.distance = [[float('inf')]*self.m for _ in range(self.n)]
#         self.directions = [(0,1),(1,0),(-1,0),(0,-1)]
    
#     def bfs(self):
#         queue=[]
#         for i in range(self.n):
#             for j in range(self.m):
#                 if self.grid[i][j]==1:
#                     queue.append((j,i,0))
#         while queue:
#             x,y,d = queue.pop(0)
#             for i,j in self.directions:
#                 nx = i+x
#                 ny = j+y
#                 if 0<=nx<self.m and 0<=ny<self.n and self.grid[ny][nx]==0:
#                     if self.distance[ny][nx]<d+1:
#                         self.distance[ny][nx]=d+1
#                         queue.append((nx,ny,self.distance[ny][nx]))
            
# class Solution:
#     def __init__(self,board):
#         self.board = board
#         self.n = len(board)
#         self.m = len(board[0])
#         self.directions = [(0,1),(1,0),(-1,0),(0,-1)]
#     def bfs(self):
#         queue=[]
#         for i in range(self.m):
#             for j in range(self.n):
#                 if i==0 or j==0 or i==self.m-1 or j==self.n-1:
#                     queue.append((i,j))
#         while queue:
#             x,y = queue.pop(0)
#             for i,j in self.directions:
#                 nx = x+i
#                 ny = y+i
#                 if 0<=nx<self.m and 0<=ny<self.n and self.board[ny][nx]=="O":
#                     self.board[ny][nx] = "T"
#                     queue.append((nx,ny))
        
#         for i in range(self.m):
#             for j in range(self.n):
#                 if self.board[j][i] == "O":
#                     self.board[j][i] = "X"
#                 elif self.board[j][i] =="T":
#                     self.board[j][i] = "O"
#         return self.board

# class solution:
#     def __init__(self,edgelist):
#         self.edgelist = edgelist
#         self.n = len(edgelist)-1
#         self.adj = [[] for _ in range(self.n)]
#         self.visited = [False]*self.n
#         self.stack = [False]*self.n
#         self.result =[]

#     def dfs(self,node):
#         self.visited[node] = True
#         self.stack[node] = True
#         for v in self.adj[u]:
#             if self.adj[v]!=True:
#                 if self.dfs(v):
#                     return True
#             elif self.stack[v]:
#                 return True
#         self.stack[u] = False
#         return False
    
#     def EventualSafestate(self):
#         for u in range(self.n):
#                 if not self.dfs(u):
#                     self.result.append(u)
#         return self.result

# class solution:
#     def __init__(self,deplist):
#         self.deplist = deplist
#         self.n = len(self.deplist)-1
#         self.adj = [[]for _ in range(self.n)]
#         self.inroder = [0]*self.n
#         for u in range(self.n):
#             for v in self.adj[u]:
#                 self.inroder[v]+=1
#         self.result=[]
    
#     def Topological(self):
#         queue =[]
#         for i in range(self.n):
#             if self.inroder[i]==0:
#                 queue.append(i)
#         while queue:
#             u = queue.pop(0)
#             self.result.append(u)
#             for v in self.adj[u]:
#                 self.inroder[v]-=1
#                 if self.inroder[v]==0:
#                     queue.append(v)
        
#         return self.result


# class Solution:
#     def __init__(self,n,k,wordlist):
#         self.n =n
#         self.k =k
#         self.wordlist = wordlist
#         self.adj =[[]for _ in range(26)]
#         for i in range(self.n-1):
#             word1 = self.wordlist[i]
#             word2 = self.wordlist[i+1]
#             i,j=0,0
#             while word1[i]!=word2[j]:
#                 i+=1
#                 j+=1
#             self.adj[self.alphtoascii(word1[i])].append(self.alphtoascii(word2[j]))
#         self.result=[]
#         self.inorder = [0]*26
#         for u in range(26):
#             for v in self.adj[u]:
#                 self.inorder[v]+=1
    
#     def alphtoascii(self,alph):
#         return ord(alph)-ord("a")
    
#     def asciitoalph(self,num):
#         return chr(num+26)

#     def Toposort(self):
#         queue =[]
#         for i in range(26):
#             if self.inorder[i]==0:
#                 queue.append(i)
#         while queue:
#             u = queue.pop(0)
#             self.result.append(self.asciitoalph(u))
#             for v in self.adj[u]:
#                 self.inorder[v]-=1
#                 if self.inorder[v]==0:
#                     queue.append(v)
        
#         return self.result


