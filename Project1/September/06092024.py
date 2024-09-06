## using dijkstra, storing the result of the computation for future reuse
# import heapq
# class solution:
#     def __init__(self,edges,n,querylist):
#         self.edges = edges
#         self.n = n
#         self.querylist = querylist
#         self.adj = [[]for _ in range(self.n)]
#         for u,v,w in edges:
#             self.adj[u].append((v,w))
#             self.adj[v].append((u,w))
#         self.memo = {} # (u,v)  = distance
#         self.result = [False]*len(self.querylist)
#     def dijkstra(self,start,end):
#         heapq.heappush(self.heap,(0,start))
#         self.distance[start] = 0
#         while self.heap:
#             w,u = heapq.heappop(self.heap)
#             for v,vw in self.adj[u]:
#                 if v == end:
#                     return vw+w
#                 if (u,v) in self.memo:
#                     self.distance[v] = self.memo[(u,v)]
#                     continue
#                 if vw+w<self.distance[v]:
#                     self.distance[v] = vw+w
#                     heapq.heappush(self.heap,(self.distance,v+vw))
    
#     def checkingexistence(self):
#         for i in range(len(self.querylist)):
#             self.distance = [float('inf')]*self.n
#             self.heap = []
#             heapq.heapify(self.heap)

#             u,v,l = self.querylist[i]
#             res = self.dijkstra(u,v)
#             self.memo[(u,v)] = res
#             if l>=res:
#                 print(res,l)
#                 self.result[i]=True
#         return self.result
# edges = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
# n= 3
# queries =[[0,1,2],[0,2,5]]
# Solution = solution(edges,n,queries)
# print(Solution.checkingexistence())


# import heapq

# class solution:
#     def __init__(self, edges, n, querylist):
#         self.edges = edges
#         self.n = n
#         self.querylist = querylist
#         self.adj = [[] for _ in range(self.n)]
        
#         # Build adjacency list from edges
#         for u, v, w in edges:
#             self.adj[u].append((v, w))
#             self.adj[v].append((u, w))
            
#         self.memo = {}  # Memoization for (u,v) = distance
#         self.result = [False] * len(self.querylist)
    
#     def dijkstra(self, start, end):
#         # If the distance between start and end is already memoized, return it
#         if (start, end) in self.memo:
#             return self.memo[(start, end)]
        
#         self.distance = [float('inf')] * self.n
#         self.distance[start] = 0
#         self.heap = [(0, start)]
        
#         while self.heap:
#             w, u = heapq.heappop(self.heap)
#             if u == end:
#                 self.memo[(start, end)] = self.distance[u]
#                 return self.distance[u]
            
#             if w > self.distance[u]:
#                 continue
                
#             for v, vw in self.adj[u]:
#                 if self.distance[u] + vw < self.distance[v]:
#                     self.distance[v] = self.distance[u] + vw
#                     heapq.heappush(self.heap, (self.distance[v], v))
        
#         # No path found, memoize and return infinity
#         self.memo[(start, end)] = float('inf')
#         return float('inf')
    
#     def checkingexistence(self):
#         for i in range(len(self.querylist)):
#             u, v, l = self.querylist[i]
#             res = self.dijkstra(u, v)
            
#             if res < l:
#                 self.result[i] = True
        
#         return self.result

# edges = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]]
# n = 5
# queries = [[0,4,14],[1,4,13]]
# Solution = solution(edges, n, queries)
# print(Solution.checkingexistence())

        

## Checking existence of edge limited paths
# class solution:
#     def __init__(self,edges,n,query):
#         self.edges = edges
#         self.n = n
#         self.query = query
#         self.parent = [0]*self.n
#         for i in range(self.n):
#             self.parent[i] = i
#         self.rank = [0]*self.n
    
#     def find(self,e):
#         if self.parent[e]==e:
#             return e
#         self.parent[e] = self.find(self.parent[e])
#         return self.parent[e]
    
#     def union(self,e1,e2):
#         p1 =self.find(e1)
#         p2 = self.find(e2)
#         if p1==p2:
#             return
#         if self.rank[p1]>self.rank[p2]:
#             self.parent[p2] = p1
#         elif self.rank[p2]>self.rank[p1]:
#             self.parent[p1] = p1
#         else:
#             self.parent[p2] = p1
#             self.rank[p1]+=1
    
#     def checkingexistence(self):
#         result=[]
#         for start,end,limit in self.query:
#             for u,v,w in self.edges:
#                 if limit>w:
#                     self.union(u,v)
#             result.append(self.find(u)==self.find(v))
#         return result

# remove maximum number of the edgesto keep the graph fully connected
# class solution:
#     def __init__(self,edges,n):
#         self.edges = edges
#         self.n = n 
#         self.parent = []*self.n
#         ## parent initialization
#         for i in range(self.n):
#             self.parent[i] = (i,i)  ## parent,type
#         self.rank = [0]*self.n
    
#     def find(self,e,type):
#         if self.parent[e][type-1] == e:
#             return e
#         self.parent[e][type-1] = self.find(self.parent[e],type)
#         return self.parent[e]
    
#     def union(self,e1,e2,t):
#         p1= self.find(e1,type)
#         p2 = self.find(e2,type)
#         if p1==p2:
#             return
#         if self.rank[p1]>self.rank[p2]:
#             if t==3:
#                 self.parent[p2][0] =p1    ## type1 connectivity
#                 self.parent[p2][1] = p1     ## type2 connectivity
#             else:
#                 self.parent[p2][t-1] = p1
#         if self.rank[p2]<self.rank[p1]:
#             if t==3:
#                 self.parent[p1][0] =p2   ## type1 connectivity
#                 self.parent[p1][1] = p2     ## type2 connectivity
#             else:
#                 self.parent[p1][t-1] = p2
#         else:
#             if t==3:
#                 self.parent[p2][0] =p1    ## type1 connectivity
#                 self.parent[p2][1] = p1     ## type2 connectivity
#             else:
#                 self.parent[p2][t-1] = p1
#             self.rank[p1]+=1                ##rank updation
    
#     def removeEdges(self):
#         count=0
#         for u,v,t in self.edges:
#             if find(u,t)!=self.find(v,t):
#                 self.union(u,v,t)
#                 count+=1
#         for node in range(self.n):
#             self.find
        
#         return self.n-count


## 1557 Minimum number of vertices to reach all nodes

# class solution:
#     def __init__(self,equations,value,queries):
#         self.equations =equations
#         self.queries = queries
#         self.value = value
#         self.seti = set()
#         for u,v in self.equations:
#             seti.add(u)
#             seti.add(v)
#         self.n = len(seti)
#         self.adj = [[]for _ in range(self.n)]  ## u,v,w
#         for i in range(len(self.equations)):
#             for u,v in self.equations[i]:
#                 uint = ord(u) - ord('a')
#                 vint = ord(v) - ord('a')
#                 self.adj[uint].append(vint,self.value[i])
#                 self.adj[vint].append(uint,1/self.value[i])
#         self.result=[]

#     def dfs(self,u,end):
#         ans=1
#         if u==end:
#             return ans
#         for v,w in self.adj[u]:
#             ans*=self.dfs(v,end)
#         return ans*w

#     def evaluate(self):
#         for u,v in self.queries:
#             if u not in self.seti or v not in self.seti:
#                 self.result.append(-1.0)
#             else:
#                 self.result.append(self.dfs(u,v))
#         return self.result


# class solution:
#     def __init__(self,adj):
#         self.adj =adj
#         self.n = len(adj)
#         self.visited = visited


