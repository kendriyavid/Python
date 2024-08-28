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


class Solution:
    def __init__(self, adj):
        self.adj = adj
        self.n = len(adj)

    def dfs(self, u):
        self.visited[u] = True
        self.stack[u] = True

        for v in self.adj[u]:
            if not self.visited[v]:
                if self.dfs(v):
                    return True
            elif self.stack[v]:
                return True

        self.stack[u] = False
        return False

    def EventualStates(self):
        result = []
        for i in range(self.n):
            self.visited = [False] * self.n
            self.stack = [False] * self.n
            # Check if the node is part of a cycle
            if not self.dfs(i):
                result.append(i)

        return result
solution = Solution(adj=[[1,2],[2,3],[5],[0],[5],[],[]])
print(solution.EventualStates())

