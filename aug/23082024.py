## DFS of a graph


# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.n=len(adj)
#         self.visited=[False]*self.n
#     def dfs(self,adj,visited,u):
#         visited[u]=True
#         for v in adj[u]:
#             if visited[v]!=True:
#                 dfs(adj,visited,v)

# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.n=len(adj)
#         self.visited=[False]*self.n
    
#     def bfs(self,u):
#         queue=[u]
#         visted[u]=True
#         while queue:
#             u=queue.pop(0)
#             for v in adj[u]:
#                 if visted[v]!=True:
#                     queue.apepnd(v)
#                     visited[v]=True
    
## Cyccle ddeteciotn undirected Graph
## BFS

# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.visited=[False]*len(adj)
#     def bfs(self,u):
#         queue=[(u,-1)]
#         selfvisted[u]=True
#         while queue:
#             u,parent=queue.pop(0)
#             for v in adj[u]:
#                 if self.visted[v]!=True:
#                     queue.append([v,u])
#                     self.visited[v]=True
#                 elif v!=parent:
#                     return True
#         return False
#     def cycleDetection(self):
#         for i in range(self.n):
#             if self.visited[i]!=True:
#                 if self.bfs(i):
#                     return True
#         return False

#directed Graph cycle detection
# dfs
# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.n=len(adj)
#         self.visited=[False]*self.n
#         self.stack=[False]*self.n
#     def dfs(self,u):
#         self.visited[u]=True
#         self.stack[u]=True
#         for v in adj[u]:
#             if visited[v]!=True:
#                 if self.dfs(v):
#                     return True
#             elif self.stack[v]==True:
#                 return True
#         self.stack[u]=False
#         return False
#     def cycleDetection(self):
#         for i in adj:
#             if visited[i]!=True:
#                 if self.dfs(i):
#                     return True
#         return False

# Topological sorting Cycle detection

# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.n=len(self.adj)
#         self.visited=[False]*self.n
#         self.result=[]
#     def dfs(self,u):
#         self.visited[u]=True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.dfs(v)
#         self.result.append(v)
#     def toposort(self):
#         for i in adj:
#             if visited[i]!=True:
#                 self.dfs(i)
#         return self.result[::-1]

## uva 10305

## n tasks not independent

## input
# 5 4
# 1 2
# 2 3
# 1 3
# 1 5
# 0 0

#output
# 1 4 2 5 3

# 0<n<=100
# m - number of relaitons given
## i-->j

# class solution:
#     def __init__(self,adj,indegree,n,m):
#         self.adj=adj
#         self.indegree = indegree
#         self.m=m
#         self.n=n
#         self.result=[]

#     def topo(self):
#         queue=[]
#         for i in range(self.n):
#             if self.indegree[i]==0:
#                 queue.append(i)
#         # print(queue)
#         # print(self.indegree)
#         # print(self.adj)
#         while queue:
#             u=queue.pop(0)
#             self.result.append(u+1)
#             print(u,self.adj[u])
#             for v in self.adj[u]:
#                 self.indegree[v]-=1
#                 if self.indegree[v]==0:
#                     queue.append(v)
#     def Ordering(self):
        
#         self.topo()
#         return self.result
# n,m=map(int,input().split())
# adj=[[]for _ in range(n)]
# indegree = [0]*(n)
# for r in range(m):
#     i,j = map(int,input().split())
#     adj[i-1].append(j-1)
#     indegree[i-1]+=1
# Solution = solution(adj,indegree,n,m)
# print(Solution.Ordering())



class Solution:
    def __init__(self, adj, indegree, n, m):
        self.adj = adj
        self.indegree = indegree
        self.m = m
        self.n = n
        self.result = []

    def topo(self):
        queue = []
        for i in range(self.n):
            if self.indegree[i] == 0:
                queue.append(i)

        while queue:
            u = queue.pop(0)
            self.result.append(u + 1)  # Store 1-based index in result
            for v in self.adj[u]:
                self.indegree[v] -= 1
                if self.indegree[v] == 0:
                    queue.append(v)

    def Ordering(self):
        self.topo()
        return self.result

# Input handling
n, m = map(int, input().split())
adj = [[] for _ in range(n)]
indegree = [0] * n

for r in range(m):
    i, j = map(int, input().split())
    adj[i - 1].append(j - 1)
    indegree[j - 1] += 1  # Increase indegree for the destination node

# Create a solution instance and perform the topological sort
solution = Solution(adj, indegree, n, m)
print(solution.Ordering())
