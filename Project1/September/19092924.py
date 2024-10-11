### Shortest path in directed acyclic graph
## do the topological sorting 
## relax the edge 1 time with saying the source as 0 


# class Solution:
#     def __init__(self,adj):
#         self.adj =adj
#         self.n = len(adj)
#         self.indegree = [0]*self.n
#         for u in self.n:
#             for v,d in self.adj[u]:
#                 self.indegree[v]+=1
#         self.toporesult=[]

#     def toposorting(self):
#         queue=[]
#         for i in range(self.n):
#             if self.indegree[i]==0:
#                 queue.append(i)
        
#         while queue:
#             u = queue.pop(0)
#             self.toporesult.append(u)
#             for v in self.adj[u]:
#                 self.indegree[v]-=1
#                 if self.indegree[v]==0:
#                     queue.append(v)

#     def shortestpathdag(self,source,destinaiton):
#         self.distance = [float('inf')]*self.n
#         self.distance[source] = 0
#         for u in self.toporesult:
#             d = self.distance[u]
#             for v,vd in self.adj[u]:
#                 if self.distance[v]<d+vd:
#                     self.distance[v] = d+vd
        
#         return self.distance[destination]
        
## Longest path in directed acyclic graph

# class Solution:
#     def __init__(self,adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.visited = [False]*self.n
#         self.dp = [-1]*self.n
    
#     def dfs(self,node):
#         self.visited[node] = True
#         maxweight = 0
#         if self.dp[node]!=-1:
#             return self.dp[node]
#         for v in self.adj[node]:
#             if self.visited[v]!=True:
#                 maxweight = max(maxweight,self.dfs(v))
#         self.dp[node] = 1+maxweight
#         return self.dp[node]
    
#     def longestPathDag(self):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 self.dfs(u)
#         return max(self.dp)

# Sum of distances in tree
# class Solution:
#     def __init__(self,edgelist):
#         self.edgelist = edgelist
#         self.n = len(edgelist)+1
#         self.adj = [[] for _ in range(self.n)]
#         for u,v in self.edgelist:
#             self.adj[u].append(v)
#         self.distance=[0]*self.n
#         self.children = [0]*self.n
#         self.visited = [False]*self.n
    
#     def predfs(self,node):
#         self.visited[node] = True
#         children = 0
#         for v in self.adj[node]:
#             if self.visisted[v]!=True:
#                 child,height = self.predfs(v)
#         return 1+child,1+height


# class Solution:
#     def __init__(self,n,parent):
#         self.n = n
#         self.parent = parent
#         self.adj = [[] for _ in range(self.n)]
#         for i in range(self.n-1):
#             u = i+1
#             self.adj[self.parent[i]-1].append(u)
#         self.result=[0]*self.n
#         # self.result[0] = self.n-1
#         self.visited = [False]*self.n
    
#     def dfs(self,u):
#         self.visited[u] = True
#         child=0
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 child+=self.dfs(v)
#         self.result[u] = child
#         return self.result[u]+1

#     def subordinates(self):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 self.dfs(u)
#         return self.result
# solution = Solution(5,[1,1,2,3])
# print(solution.subordinates())


class Solution:
    def __init__(self,edges):
        self.edges = edges
        self.n = n
        self.adj = [[]for _ in range(self.n)]
        for u,v in self.edges:
            self.adj[u].append(v)
        self.considering = [0]*self.n
        self.notconsidering =[0]*self.n

    def Treematching(self,u):
        cons,notcons = self.dfs(u)
        ## notconsideri
        
        return (self.considering[u],self.notconsidering[u])