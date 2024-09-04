## Leetcode 1466 Reorder routes to make all paths lead to the city 0

class solution:

    def __init__(self,n,connections):
        self.n = n
        self.connections = connections
        # self.conset = set(self.connections)
        self.adj = [[]for _ in range(self.n)]
        ## adj initialization
        for u,v in self.connections:
            self.adj[u].append(v)
            self.adj[v].append(u)
        self.visited = [False]*self.n
        self.count = 0
    
    def dfs(self,u):
        self.visited[u] = True
        for v in self.adj[u]:
            if self.visited[v]!=True:
                self.dfs(v)
                if [v,u] not in self.connections:
                    self.count+=1
    
    def Reorderroutes(self):
        self.dfs(0)
        return self.count
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Solution = solution(n,connections)
print(Solution.Reorderroutes())


# class solution:
#     def __init__(self, n, connections):
#         self.n = n
#         self.connections = connections
#         self.adj = [[] for _ in range(self.n)]
#         self.original_edges = set((u, v) for u, v in connections)
#         self.visited = [False] * self.n
#         self.count = 0
        
#         # Create adjacency list
#         for u, v in self.connections:
#             self.adj[u].append(v)
#             self.adj[v].append(u)
    
#     def dfs(self, u):
#         self.visited[u] = True
#         for v in self.adj[u]:
#             if not self.visited[v]:
#                 # If moving from u to v is not in the original direction, count it as a reverse
#                 if (v, u) not in self.original_edges:
#                     self.count += 1
#                 self.dfs(v)
    
#     def Reorderroutes(self):
#         self.dfs(0)
#         return self.count

# n = 6
# connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
# Solution = solution(n, connections)
# print(Solution.Reorderroutes())  # Output should be 3
