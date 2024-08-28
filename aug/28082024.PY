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


## Alien Dictionary
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
#         self.result.append(self.itoa(v))
#     def Aliendictionary(self):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 self.Topological(v)
#         return self.stack[::-1]
#     def itoa(self,i):
#         return chr(97+i)
n, k = map(int, input().split())
dict = ["baa", "abcd", "abca", "cab", "cad"]

# Initialize adjacency list
adj = [[] for _ in range(k)]

for i in range(n - 1):
    word1 = dict[i]
    word2 = dict[i + 1]
    min_length = min(len(word1), len(word2))

    # Find the first differing character
    for j in range(min_length):
        if word1[j] != word2[j]:
            # Add an edge from word1[j] to word2[j]
            adj[ord(word1[j]) - 97].append(ord(word2[j]) - 97)
            break

print(adj)
