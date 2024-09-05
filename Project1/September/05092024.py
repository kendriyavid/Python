# 1857 Largest color value in a Directed Graph

# class solution:
#     def __init__(self,edges,color):
#         self.color = color
#         self.edges = edges
#         self.n = len(color)
#         self.adj = [[] for _ in range(self.n)]
#         ## adj construction
#         for u,v in self.edges:
#             self.adj[u].append(v)
#         self.visited = [False]*self.n
#         self.stack = [False]*self.n
#         self.maxcolor = -1
#         self.colorarr = [0]*26
    
#     def directedcycle(self,u):
#         self.visited[u] = True  
#         self.stack[u] = True
#         charnum = ord(self.color[u])- ord('a')
#         self.colorarr[charnum]+=1
#         self.maxcolor = max(self.maxcolor,self.colorarr[charnum])
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 if self.directedcycle(v):
#                     return True
#             elif self.stack[v]:
#                 return True
#         self.colorarr[charnum]-=1
#         self.stack[u] = False
#         return False
    
#     def largestColorvalue(self):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 if self.directedcycle(u):
#                     return -1
#         return self.maxcolor
# color = "nnllnzznn"
# edges = [[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],[5,6],[6,7],[7,8]]
# Solution = solution(edges,color)
# print(Solution.largestColorvalue())


#Dfs with dynamic programming

# class solution:
#     def __init__(self,edges,cstring):
#         self.cstring = cstring
#         self.edges = edges
#         self.n = len(cstring)
#         self.adj = [[] for _ in range(self.n)]
#         ##initialization
#         for u,v in self.edges:
#             self.adj[u].append(v)
#         self.dp = [[0]*26 for _ in range(self.n)]
#         self.visited = [False]*self.n
#         self.stack = [False]*self.n
    
#     def dfs(self,u):
#         self.visited[u] = True
#         self.stack[u] = True
#         charnum = ord(self.cstring[u]) - ord('a')
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 res = self.dfs(u)
#                 if res==float('inf'):
#                     return res
                
#             elif self.stack[v]:
#                 return float('inf')
#         self.stack[u] = False
#         return max(dp[charnum])

#     def maximumcolor(self):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 res = max(res,self.dfs(u))
        
#         if res==float('inf'):
#             return -1
#         return res
    
class Solution:
    def __init__(self, edges, cstring):
        self.cstring = cstring
        self.edges = edges
        self.n = len(cstring)
        self.adj = [[] for _ in range(self.n)]
        ## initialization
        for u, v in self.edges:
            self.adj[u].append(v)
        self.dp = [[0]*26 for _ in range(self.n)]
        self.visited = [False]*self.n
        self.stack = [False]*self.n

    def dfs(self, u):
        self.visited[u] = True
        self.stack[u] = True
        charnum = ord(self.cstring[u]) - ord('a')

        # Process all adjacent nodes
        for v in self.adj[u]:
            if not self.visited[v]:
                res = self.dfs(v)
                if res == float('inf'):
                    return res
            elif self.stack[v]:
                return float('inf')

            # Update dp table by taking the maximum from adjacent nodes
            for i in range(26):
                self.dp[u][i] = max(self.dp[u][i], self.dp[v][i])

        # Add current node character
        self.dp[u][charnum] += 1

        self.stack[u] = False
        return max(self.dp[u])

    def maximumcolor(self):
        res = 0
        for u in range(self.n):
            if not self.visited[u]:
                result = self.dfs(u)
                if result == float('inf'):
                    return -1
                res = max(res, result)
        return res
edges = [[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],[5,6],[6,7],[7,8]]
colors = "nnllnzznn"
solution = Solution(edges,colors)
print(solution.maximumcolor())