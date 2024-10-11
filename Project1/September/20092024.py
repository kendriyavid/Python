# ## Tree Matching
# class solution:
#     def __init__(self,edges,n):
#         self.n = n
#         self.adj = [[]for _ in range(self.n)]
#         self.visited = [False]*self.n
#         self.dp = [[0]*2 for _ in range (self.n)]
#         ##graph initialization
#         for u,v in self.edges:
#             self.adj[u].append(v)
    
#     def dfs(self,node):
#         self.visited[node] = True
#         taking = 0
#         ntaking = 0
#         for v in self.adj[node]:
#             if self.visited[v]!=True:
#                 self.dp[v] = self.dfs(v)
#                 ## Taking
#                 ntaking+=max(dp[v][0],dp[v][1])
#                 ## Nottaking
#                 taking = max(taking,ntaking-max(dp[v][0],dp[v][1])+1)
#         dp[node][0] =ntaking
#         dp[node][1] = taking
#         return dp[node]


# ### CSES Tree diameter
# class Solution:
#     def __init__(self,edges):
#         self.n = len(edges)+1
#         self.edges = edges
#         self.adj = [[] for _ in range(self.n)]
#         for u,v in self.edges:
#             self.adj[u].append(v)
#         self.visited = [False]*self.n
#         self.maxPathlength = float('-inf')
    
#     def dfs(self,node):
#         self.visited[node] = True
#         largest = 0
#         secondLargest = 0
#         for v in self.adj[node]:
#             if self.visited[v]!=True:
#                 ans = self.dfs(v)
#                 if largest<ans:
#                     secondLargest = largest
#                     largest = ans
#                 elif secondLargest<ans:
#                     secondLargest = ans
#         self.maxPathlength = max(self.maxPathlength,largest+secondLargest)
#         return 1 + max(largest,secondLargest)


## Tree Diameter
class Solution:
    def __init__(self,