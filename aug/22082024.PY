### dfs implementation graph

# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.visited=[False]*len(adj)

#     def dfs(self,u,visited):
#         visited[u]=True
#         for v in self.adj[u]:
#             if visited[v]!=True:
#                 self.dfs(v,visited)

### bfs implementation graph

# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.visited=[False]*len(adj)
#     def bfs(self,v,visited):
#         queue=[0]
#         while queue:
#             u=queue.pop(0)
#             for v in self.adj[u]:
#                 if visited[v]!=True:
#                     queue.append(v)
#                 visited[v]=True

## Detection of cycle in undirected graphs
## DFS approach

# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.visited=[False]*len(adj)
#     def cycleDetection(self):
#         for u in range(self.n):
#             if visited[u]!=True:
#                 if self.dfscycle(u,-1):
#                     return True
#         return False
    
#     def dfscycle(self,u,parent):
#         self.visited[u]=True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 if self.dfscycle(v,u):
#                     return True
#             elif v!=parent:
#                 return True
#         return False

## BFS approach
# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.n=len(adj)
#         self.visited=[False]*self.n
#     def cycleDetection(self):
#         for u in (self.n):
#             if self.visited[u]!=True:
#                 if self.bfsCycle(u,-1):
#                     return True
#         return False
                
#     def bfsCycle(self,u):
#         queue=[(u,-1)]
#         cycle=False
#         while queue:
#             u,parent=queue.pop(0)
#             for v in adj[u]:
#                 if self.visited[v]!=True:
#                     queue.append((v,u))
#                     self.visited[v]=True
#                 elif v!=parent:
#                     cycle=True
#                     break
#             if cycle:
#                 break
#         return cycle

# directed Graph dfs cycle detection:
# class solution:
#     def __init__(self):
#         self.adj=adj
#         self.n=len(adj)
#         self.visited=[False]*self.n
#         self.stack=[False]*self.n
    
#     def cycleDetection(self):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 if self.dfsCycle(u):
#                     return True
#         return False

#     def dfsCycle(self,u):
#         self.visited[u]=True
#         self.stack[u]=True
#         for v in adj[u]:
#             if self.visited[v]!=True:
#                 if self.dfsCycle(v):
#                     return True
#             elif self.stack[u]:
#                 return True
#         self.stack[u]=False
#         return False

# result=[]
# while queue:
#     u=queue.pop(0)
#     result.append(u)
#     for v in adj[u]:
#         indegree[v]-=1
#         if visited[v]!=True:
#             if indegree[v]==0:
#                 queue.append(v)
#                 visited[v]=True


## Bipartite Graph DFS
# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.cv=[-1]*len(adj)
#     def dfs(self,cv,u,adj,color):
#         self.cv[u]=color
#         for v in self.adj[u]:
#             if color==cv[v]:
#                 return False
#             if color[v]==-1:
#                 nc=-1
#                 if color==1:
#                     nc=0
#                 else:
#                     nc=1
#                 if self.dfs(cv,v,adj,nc)==False:
#                     return False
#         return True
            
## Disjoint Set union  (Union Find)

# def find(e,parent):
#     if e==parent[e]:
#         return e
#     res=find(parent[e],parent)
# def union(e1,e2):
#     p1=find(e1,parent)
#     p2=find(e2,parent)
#     if p1==p2:
#         return p1
#     parent[p1]=p2
#     return p2

## equation satisfiability dsu

# class solution:
#     def __init(self,adj):
#         self.adj=adj
#         self.parent=[i for i in range(len(self.adj))]
#         self.rank=[0]*len(self.adj)
#     def find(self,element):
#         if self.parent[element]==element:
#             return element
#         self.parent[element]=self.find(self.parent[element])
#         return self.parent[element]
#     def union(self,e1,e2):
#         p1=self.find(e1)
#         p2=self.find(e2)
#         if p1==p2:
#             return False
#         if self.rank[p1]>self.rank[p2]:
#             self.parent[p2]=p1
#         elif self.rank[p1]<self.rank[p2]:
#             self.parent[p2]=p1
#         else:
#             self.parent[p2]=p1
#             self.rank[p1]+=1
#         return True
#     def satisfiability(self):
#         for eq in self.adj:
#             if eq[1]=="=":
#                 if not self.union(eq[0],eq[3]):
#                     return False
#             elif eq[1]=="!":
#                 if not self.union(eq[0],eq[3]):
#                     return False
#         return True

## Number of operations to make the components connected

# class solution:
#     def __init__(self,n,connections):
#         self.connections=connections
#         self.n=n
#         self.rank=[0]*self.n
#         self.parent=[i for i in range(self,n)]
#     def find(self,element):
#         if self.parent[element]==element:
#             return element
#         self.parent[element]=self.find(self.parent[element])
#         return self.parent[element]
#     def union(self,e1,e2):
#         p1=self.find(e1)
#         p2=self.find(e2)
#         if p1==p2:
#             return False
#         if self.rank[p1]>self.rank[p2]:
#             self.parent[p2]=p1
#         elif self.rank[p1]<self.rank[p2]:
#             self.parent[p1]=p2
#         else:
#             self.parent[p2]=p1
#             self.rank[p1]+=1
#         return True
#     def numberofopsconnected(self):
#         count=0
#         for conn in self.connections:
#             if self.union(conn[0],conn[1])==False:
#                 count+=1
#         return count
# n=4
# connections=[[0,1],[0,2],[1,2]]
# sol= solution(n,connections)
# if len(connections)==n-1:
#     print(-1)
# else:
#     print(sol.numberofopsconnected())


class Solution:
    def __init__(self, n, connections):
        self.connections = connections
        self.n = n
        self.rank = [0] * self.n
        self.parent = [i for i in range(self.n)]  # Fix here

    def find(self, element):
        if self.parent[element] != element:
            self.parent[element] = self.find(self.parent[element])
        return self.parent[element]

    def union(self, e1, e2):
        p1 = self.find(e1)
        p2 = self.find(e2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True

    def numberofopsconnected(self):
        count = 0
        for conn in self.connections:
            if not self.union(conn[0], conn[1]):
                count += 1
        return count

n = 12
connections = [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]
sol = Solution(n, connections)
if len(connections) < n - 1:
    print(-1)
else:
    print(sol.numberofopsconnected())


