## Find eventual States

# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
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

#     def EventualStates(self):
#         result=[]
#         for i in range(self.n):
#             self.visited=[False]*self.n
#             self.stack=[False]*self.n
#             if not self.dfs(i):
#                 result.append(i)
#         return result


# class Solution:
#     def __init__(self, adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False] * self.n
#         self.stack = [False] * self.n
#         self.safe=[True]*self.n

#     def dfs(self, u):
#         if self.visited[u]:
#             return self.safe[u]
#         self.visited[u] = True
#         self.stack[u] = True

#         for v in self.adj[u]:
#             if not self.visited[v]:
#                 if self.dfs(v):
#                     self.safe[v]=False
#                     return True
#             elif self.stack[v]:
#                 self.safe[v]=False
#                 return True

#         self.stack[u] = False
#         return False

#     def EventualStates(self):
#         result = []
#         for i in range(self.n):
#             # Check if the node is part of a cycle
#             if not self.dfs(i):
#                 result.append(i)

#         return result
# solution = Solution(adj=[[1,2],[2,3],[5],[0],[5],[],[]])
# print(solution.EventualStates)

### Course Schedule 2
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
#         self.stack=[]
#     def Topological(self,u):
#         self.visited[u]=True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.dfs(v)
#         self.stack.append[u]
#     def cs2(self):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 self.dfs(u)
#         if len(self.stack)==self.n:
#             return self.stack[::-1]
#         else:
#             return []


# Alien Dictionary
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
#         self.stack=[]
#     def Topological(self,u):
#         self.visited[u]=True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.Topological(v)
#         self.result.append(self.itoa(u))
#     def Aliendictionary(self):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 self.Topological(v)
#         return self.stack[::-1]
#     def itoa(self,i):
#         return chr(97+i)
# n, k = map(int, input().split())
# dict = ["baa", "abcd", "abca", "cab", "cad"]

# # Initialize adjacency list
# adj = [[] for _ in range(k)]

# for i in range(n - 1):
#     word1 = dict[i]
#     word2 = dict[i + 1]
#     min_length = min(len(word1), len(word2))

#     # Find the first differing character
#     for j in range(min_length):
#         if word1[j] != word2[j]:
#             # Add an edge from word1[j] to word2[j]
#             adj[ord(word1[j]) - 97].append(ord(word2[j]) - 97)
#             break

# print(adj)


# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.parent = [i for i in range(self.n)]
#         self.rank=[0]*self.n

#     def find(self,e):
#         if self.parent[e]==e:
#             return e
#         self.parent[e] = self.find(self.parent[e])
#         return self.parent[e]
    
#     def union(self,e1,e2):
#         p1 = self.find(e1)
#         p2 = self.find(e2)
#         if self.rank[p1]>self.rank[p2]:
#             self.parent[p2]=p1
#         elif self.rank[p2]>self.rank[p1]:
#             self.parent[p1] = p2
#         else:
#             self.parent[p2]=p1
#             self.rank[p1]+=1

#     def countunreachable(self):
#         for i in range(self.n):
#             for j in range(self.adj[i]):
#                 if i<self.adj[i][j]:
#                     self.union(i,self.adj[i][j])
#         dict={}
#         for u in range(self.n):
#             p = self.find(u)
#             if dict[p]:
#                 dict[p]+=1
#             else:
#                 dict[p]=1
        
#         m= self.n
#         total=0
#         for key,value in range(self.n):
#             total+=dict[key](m-dict[key])
#             m = m-dict[key]
#         return total

# n = int(input())
# adj=[[]for _ in range(n)]
# edges=[[0,2],[0,5],[2,4],[1,6],[5,4]]
# for rel in edges:
#     adj[rel[0]].append(rel[1])
#     adj[rel[1]].append(rel[0])
# Solution = solution(adj)
# print(Solution.countunreachable)

# class Solution:
#     def __init__(self, adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.parent = [i for i in range(self.n)]
#         self.rank = [0] * self.n

#     def find(self, e):
#         if self.parent[e] == e:
#             return e
#         self.parent[e] = self.find(self.parent[e])
#         return self.parent[e]
    
#     def union(self, e1, e2):
#         p1 = self.find(e1)
#         p2 = self.find(e2)  # Corrected typo here
#         if self.rank[p1] > self.rank[p2]:
#             self.parent[p2] = p1
#         elif self.rank[p2] > self.rank[p1]:
#             self.parent[p1] = p2
#         else:
#             self.parent[p2] = p1
#             self.rank[p1] += 1

#     def count_unreachable(self):
#         # Union all nodes that are directly connected
#         for i in range(self.n):
#             for j in range(len(self.adj[i])):  # Fixed the loop
#                 if i < self.adj[i][j]:  # Ensure we don't double count
#                     self.union(i, self.adj[i][j])

#         # Count the size of each component
#         component_size = {}
#         for u in range(self.n):
#             p = self.find(u)
#             if p in component_size:
#                 component_size[p] += 1
#             else:
#                 component_size[p] = 1

#         # Calculate the number of unreachable pairs
#         m = self.n
#         total = 0
#         for key, value in component_size.items():  # Corrected iteration
#             total += component_size[key] * (m - component_size[key])
#             m -= component_size[key]
        
#         return total

# # Example usage
# n = int(input())
# adj = [[] for _ in range(n)]
# edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
# for rel in edges:
#     adj[rel[0]].append(rel[1])
#     adj[rel[1]].append(rel[0])

# solution = Solution(adj)
# print(solution.count_unreachable())  # Corrected method call


#Dikstra's Algorithm
# import heapq
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(self.adj)
#         self.heap=[]
#         heapq.heapify(self.heap)
#         self.distance=[float('inf')]*self.n
    
#     def Dijkstra(self,source):
#         self.distance[source] = 0
#         heapq.heappush(self.heap,(0,source))
#         while self.heap:
#             d,u = heapq.heappop(self.heap)
#             for v,dv in self.adj[u]:
#                 if d+dv<self.distance[v]:
#                     self.distance[v] = d+dv
#                     heapq.heappush(self.heap,(dv+d,v))
#         return self.distance


## network delay
# import heapq
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.distance = [float('inf')]*self.n
#         self.heap = []
#         heapq.heapify(self.heap)
#     def Dijkstra(self,source):
#         self.distance[source]=0
#         heapq.heappush(self.heap,(0,source))
#         while self.heap:
#             w,u = heapq.heappop(self.heap)
#             for v,vw in self.adj[u]:
#                 if self.distance[v]>w+vw:
#                     self.distance[v] = w+vw
#                     heapq.heappush(heap,(self.distance[v],v))
#     def NetworkDelay(self):
#         mdist = float(-'inf')
#         for dist in self.distance:
#             if dist==float('inf'):
#                 return -1
#             else:
#                 mdist = max(mdist,dist)
#         return mdist
# import heapq
# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.n  = len(self.matrix)
#         self.m = len(self.matrix[0])
#         self.distance = [[float('inf')]*self.m for _ in range(self.n)]
#         self.heap=[]
#         heapq.heapify(self.heap)
#         self.directions=[(1,0),(0,1),(-1,0),(0,-1)]
    
#     def Dijkstra(self):
#         heapq.heappush(self.heap,(0,(0,0)))
#         self.distance[0][0] = 0
#         while self.heap:
#             w,x,y = heapq.heappop(self.heap)
#             for i,j in self.directions:
#                 nx = x+i
#                 ny = y+j
#                 if 0<=nx<self.m and 0<=ny<self.n:
#                     currdiff = abs(self.matrix[ny][nx]-self.matrix[y][x])
#                     if self.distance[ny][nx]>max(currdiff,w):
#                         self.distance[ny][nx] = max(currdiff,w)
#                         heapq.heappush(heap,(self.distance[ny][nx],(nx,ny)))
#         return self.distance[self.m-1][self.n-1]


# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.distance = [float('inf')]*self.n
#         self.stack=[]
#         self.visited = [False]*self.n
#     def Topological(self,u):
#         self.visited[u]=True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.Topological(v)
#         self.stack.append(u)
#     def DAGshortest(self,source):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 self.Topological(u)
#         self.distance[source]=0
#         while self.stack:
#             u = self.stack.pop()
#             distance  = self.distance[u]
#             for v,d in self.adj[u]:
#                 if self.distance[v]>distance+d:
#                     self.distance[v] = distance+d
#         return self.distance

## Word Ladder 1
# class solution:
#     def __init__(self,beginword,endword,wlist):
#         self.beginword = beginword
#         self.endword = endword
#         self.wlist = wlist
#         self.set = set(self.wlist)
#         self.letters='abcdefghijklmnopqrstuvwxyz'
#         self.result = []
#         self.found=False
#     def bfs(self,beginword):
#         queue=[([beginword],beginword)]
#         while queue:
#             reslist,word =queue.pop(0)
#             lword = list(word)
#             for i in len(lword):
#                 for l in self.letters:
#                     lword[i] = l
#                     w = ''.join(lword)
#                     if w == self.endword:
#                         self.result.append(reslist)
#                         self.found=True
#                     if w in self.set and self.found==False:
#                         queue.append((reslist.append(w),w))
#                         self.set.remove(w)
#         if self.result:
#             return self.result
#         else:
#             return []

## shortest path in binary matrix
## return distance, if there is no path return -1
## 8 directions
## Source  -  n-1,n-1

# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.n = len(matrix)
#         self.directions=[(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,1)]
#     def bfs(self):
#         queue=[(0,(0,0))]    # dist,x,y
#         self.matrix[0][0]=1
#         while queue:
#             w,x,y = queue.pop(0)
#             if x==self.n-1 and y==self.n-1:
#                 return w
#             for i,j in self.directions:
#                 nx = i+x
#                 ny = j+y
#                 if 0<=nx<self.n and 0<=ny<self.m or self.matrix[ny][nx]==0:
#                     queue.append((w+1,(nx,ny)))
#                     self.matrix[ny][nx]=1

## Shortest path in binary matrix using dijkstra algorithm
##use minheap, first instance givces minimum distance
## maintiain the distance matrix
# import heapq
# class solution:
#     def __init__(self,matrix):
#         self.matrix = matrix
#         self.n = len(matrix)
#         self.distance = [[float('inf')]*self.n for _ in range(self.n)]
#         self.heap = []
#         heapq.heapify(self.heap)
#         self.directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
#     def Dijkstra(self):
#         ## initializing the heap
#         heapq.heappush(self.heap,(0,(0,0)))
#         self.distance[ny][nx]=0
#         while self.heap:
#             w,x,y = heapq.heappop(self.heap)
#             for i,j in self.directions:
#                 nx = i+x
#                 ny = j+y
#                 if 0<=nx<self.n and 0<=ny<self.n and self.matrix[ny][nx]==0:
#                     if w+1<self.distance[ny][nx]:
#                         self.distance[ny][nx] = w+1
#                         heapq.heappush(self.heap,(self.distance[ny][nx](nx,ny)))
#         return self.distance[self.n-1][self.n-1]


# Cheapest Flight within k stops
# import heapq
# class solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.heap =[]
#         heapq.heapify(self.heap)
#         self.distance  =[float('inf')]*self.n
#     def Dijkstra(self,src,dst,k):
#         heapq.heappush(self.heap,(0,src,0))
#         self.distance[src] = 0
#         while self.heap:
#             w,u,stops=heapq.heappop(self.heap)
#             if stops<=k:
#                 for v,vw in self.adj[u]:
#                     if self.distance[v]>w+vw:
#                         self.distance[v]=w+vw
#                         heapq.heappush(self.heap,(self.distance[v],v,stops+1))
#         if self.distance[dst]!=float('inf'):
#             return self.distance[dst]
#         else: 
#             return -1
    
# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600]]
# n = int(input())
# src,dst,k = map(int,input().split())
# adj=[[]for _ in range(n)]
# for rel in flights:
#     adj[rel[0]].append((rel[1],rel[2]))
# Solution = solution(adj)
# print(Solution.Dijkstra(src,dst,k))




