## Leetcode 1466 Reorder routes to make all paths lead to the city 0

# class solution:

#     def __init__(self,n,connections):
#         self.n = n
#         self.connections = connections
#         # self.conset = set(self.connections)
#         self.adj = [[]for _ in range(self.n)]
#         ## adj initialization
#         for u,v in self.connections:
#             self.adj[u].append(v)
#             self.adj[v].append(u)
#         self.visited = [False]*self.n
#         self.count = 0
    
#     def dfs(self,u):
#         self.visited[u] = True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.dfs(v)
#                 if [v,u] not in self.connections:
#                     self.count+=1
    
#     def Reorderroutes(self):
#         self.dfs(0)
#         return self.count
# n = 6
# connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Solution = solution(n,connections)
# print(Solution.Reorderroutes())


# # class solution:
# #     def __init__(self, n, connections):
# #         self.n = n
# #         self.connections = connections
# #         self.adj = [[] for _ in range(self.n)]
# #         self.original_edges = set((u, v) for u, v in connections)
# #         self.visited = [False] * self.n
# #         self.count = 0
        
# #         # Create adjacency list
# #         for u, v in self.connections:
# #             self.adj[u].append(v)
# #             self.adj[v].append(u)
    
# #     def dfs(self, u):
# #         self.visited[u] = True
# #         for v in self.adj[u]:
# #             if not self.visited[v]:
# #                 # If moving from u to v is not in the original direction, count it as a reverse
# #                 if (v, u) not in self.original_edges:
# #                     self.count += 1
# #                 self.dfs(v)
    
# #     def Reorderroutes(self):
# #         self.dfs(0)
# #         return self.count

# # n = 6
# # connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
# # Solution = solution(n, connections)
# # print(Solution.Reorderroutes())  # Output should be 3


# Leetcode 2360 Longest cycle in a graph

# class solution:
#     def __init__(self,edges):
#         self.edges = edges
#         self.n = len(edges)
#         self.visited  =[False]*self.n
#         self.stack = [False]*self.n    
#         self.adj = [[]for _ in range(self.n)]
#         self.nodecount = [0]*self.n
#         ## initialization of the adj
#         for i in range(self.n):
#             self.adj[i].append(self.edges[i])
#         self.maxlen = -1


#     def dfs(self,u):
#         self.visited[u]=True
#         self.stack[u] = True
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 self.nodecount[v] = 1+self.nodecount[u]
#                 if self.dfs(v):
#                     return True
#             elif self.stack[v]:
#                 self.maxlen = max(self.maxlen,self.nodecount[u]-self.nodecount[v]+1)
#                 return True
#         self.nodecount[u] = 0
#         self.stack[u] = False
#         return False
    
#     def Longestcycle(self):
#         for i in range(self.n):
#             if self.visited[i]!=True:
#                 self.dfs(i)
#         return self.maxlen


### Dynamic Programming 
## maximize the values
# class solution:
#     def __init__(self,weight,value,capacity):
#         self.weight = weight
#         self.value = value
#         self.n = len(weight)
#         self.capacity = capacity
#         self.dp = [[-1]*(self.capacity+1) for _ in range(self.n+1)]

#     def zeroOneKnapsack(self,W,index):
#         if W<=0 or index<0:
#             return 0
#         if self.dp[index][W]!=-1:
#             return self.dp[index][W]
#         ## Have the capacity
#         if self.weight[index]<=W:
#             ## taking
#             l = self.value[index]+self.zeroOneKnapsack(W-self.weight[i],index-1)
#             ## ntaking
#             r = self.zeroOneKnapsack(W,index-1)
#             self.dp[index][W] = max(l,r)
#         ## no capacity
#         else:
#             self.dp[index][W] = self.zeroOneKnapsack(W,index-1)
#         return self.dp[index][W]


## Subset sum problem

# class solution:
#     def __init__(self,target,arr):
#         self.arr = arr
#         self.n = len(arr)
#         self.target = target
#         self.dp = [[None]*(self.n+1) for _ in range(target+1)]

#     def Subsetsum(self,sumation,index):
#         if sumation==0:
#             return True
#         if index <=0 or sumation<0:
#             return False
#         if self.arr[index]==sumation:
#                 return True
        
#         if self.dp[index+1][sumation+1] is not None:
#             return self.dp[index+1][sumation+1]
        
#         ## taking:
#         exlude = self.Subsetsum(sumation,index-1)
#         include = False
#         if sumation>=self.arr[index]:
#             include = self.arr[index]+self.Subsetsum(sumation-self.arr[index],index-1)
#             dp[index+1][sumation+1] = include or exclude
#         else:
#             dp[index+1][sumation+1] = self.Subsetsum(sumation,index-1)
        
#         return dp[index+1][sumation+1]

## PARTIIONT SUBSET SUM EQUAL

# class solution:
#     def __init__(self,nums):
#         self.nums = nums
#         self.n = n
#         self.total = sum(self.nums)
    
#     def Partition(self):
#         if self.total%2!=0:
#             return False
#         return self.PSEQ(self.total//2,self.n-1)
#         self.dp = [[None]*self.n for _ in range(self.total//2+1)]
        
#     def PSEQ(self,target,index):
#         if target==0:
#             return True
#         if target<0 or index<0:
#             return False
        
#         if dp[index][target-1] is not None:
#             return dp[index][target-1] 
#         #not include
#         exclude = self.PSEQ(target,index-1)
#         include = False
#         if target>=self.nums[index]:
#             include = self.PSEQ(target-self.nums[index],index-1)
        
#         dp[index][target-1] = include or exclude
        
#         return dp[index][target-1]
