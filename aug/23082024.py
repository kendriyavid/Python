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



# class Solution:
#     def __init__(self, adj, indegree, n, m):
#         self.adj = adj
#         self.indegree = indegree
#         self.m = m
#         self.n = n
#         self.result = []

#     def topo(self):
#         queue = []
#         for i in range(self.n):
#             if self.indegree[i] == 0:
#                 queue.append(i)

#         while queue:
#             u = queue.pop(0)
#             self.result.append(u + 1)  # Store 1-based index in result
#             for v in self.adj[u]:
#                 self.indegree[v] -= 1
#                 if self.indegree[v] == 0:
#                     queue.append(v)

#     def Ordering(self):
#         self.topo()
#         return self.result

# n, m = map(int, input().split())
# adj = [[] for _ in range(n)]
# indegree = [0] * n

# for r in range(m):
#     i, j = map(int, input().split())
#     adj[i - 1].append(j - 1)
#     indegree[j - 1] += 1  


# solution = Solution(adj, indegree, n, m)
# print(solution.Ordering())

## Following orders uva

# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.n=len(adj)
#         self.stack=[]
#         self.list=[]
#         self.variations=[]
    
#     def topological(self,u):
#         self.visited[u]=True
#         for v in self.adj[u]:
#             if visited[v]!=True:
#                 self.topological(v)
#         self.stack.append(u)
    
#     def FollowingOrder(self):
#         for i in range(self.n):
#             if self.visited[i]!=True:
#                 self.topological(i)
#         self.stack.reverse()
#         return self.stack
            


# def ascii(str):
#     return ord(str)-97
# var=list(map(str,input().split()))
# relations=list(map(ascii,input().split()))
# print(relations)
# adj=[[]for _ in range(len(var))]
# for i in range(0,len(relations),2):
#     adj[i[0]].append(i[1])
# Solution=solution(adj)
# print(Solution.FollowingOrder())



# class Solution:
#     def __init__(self, adj, indegree, n):
#         self.adj = adj
#         self.indegree = indegree
#         self.n = n
#         self.current_order = []
#         self.all_orders = []

#     def generate_orders(self):
#         if len(self.current_order) == self.n:
#             self.all_orders.append("".join(chr(i + 97) for i in self.current_order))
#             return
        
#         for u in range(self.n):
#             if self.indegree[u] == 0 and u not in self.current_order:
#                 # Choose node u
#                 self.current_order.append(u)
#                 for v in self.adj[u]:
#                     self.indegree[v] -= 1
                
#                 # Recurse to build further
#                 self.generate_orders()
                
#                 # Un-choose node u (backtrack)
#                 self.current_order.pop()
#                 for v in self.adj[u]:
#                     self.indegree[v] += 1

#     def get_all_orders(self):
#         self.generate_orders()
#         return self.all_orders

# while True:
#     def ascii_to_index(char):
#         return ord(char) - 97
#     # Input Parsing
#     variables = list(map(str, input().split()))  # e.g., x y z
#     constraints = input().split()  # e.g., x y x z

#     n = len(variables)
#     adj = [[] for _ in range(n)]
#     indegree = [0] * n

#     # Convert variables to indices
#     var_index = {var: i for i, var in enumerate(variables)}

#     for i in range(0, len(constraints), 2):
#         u = var_index[constraints[i]]
#         v = var_index[constraints[i + 1]]
#         adj[u].append(v)
#         indegree[v] += 1

#     # Create a solution instance and find all topological orders
#     solution = Solution(adj, indegree, n)
#     all_orderings = solution.get_all_orders()

#     # Print all valid orderings
#     for ordering in all_orderings:
#         print(ordering)
#     break


class Solution:
    def __init__(self, adj, indegree, n):
        self.adj = adj
        self.indegree = indegree
        self.n = n
        self.current_order = []
        self.all_orders = []

    def generate_orders(self):
        if len(self.current_order) == self.n:
            self.all_orders.append("".join(chr(i + 97) for i in self.current_order))
            return
        
        for u in range(self.n):
            if self.indegree[u] == 0 and u not in self.current_order:
                # Choose node u
                self.current_order.append(u)
                for v in self.adj[u]:
                    self.indegree[v] -= 1
                
                # Recurse to build further
                self.generate_orders()
                
                # Un-choose node u (backtrack)
                self.current_order.pop()
                for v in self.adj[u]:
                    self.indegree[v] += 1

    def get_all_orders(self):
        self.generate_orders()
        return self.all_orders

def ascii_to_index(char):
    return ord(char) - 97

try:
    while True:
        # Read the variables
        variables = list(map(str, input().split()))
        
        if not variables:
            break
        
        # Read the constraints
        constraints = input().split()
        
        n = len(variables)
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        
        # Convert variables to indices
        var_index = {var: i for i, var in enumerate(variables)}
        
        for i in range(0, len(constraints), 2):
            u = var_index[constraints[i]]
            v = var_index[constraints[i + 1]]
            adj[u].append(v)
            indegree[v] += 1
        
        # Create a solution instance and find all topological orders
        solution = Solution(adj, indegree, n)
        all_orderings = solution.get_all_orders()
        
        # Print all valid orderings
        all_orderings.sort()
        for ordering in all_orderings:
            print(ordering)

except EOFError:
    # When EOF is reached, the loop will exit
    pass
