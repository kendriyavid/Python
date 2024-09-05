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
    
# class Solution:
#     def __init__(self, edges, cstring):
#         self.cstring = cstring
#         self.edges = edges
#         self.n = len(cstring)
#         self.adj = [[] for _ in range(self.n)]
#         ## initialization
#         for u, v in self.edges:
#             self.adj[u].append(v)
#         self.dp = [[0]*26 for _ in range(self.n)]
#         self.visited = [False]*self.n
#         self.stack = [False]*self.n

#     def dfs(self, u):
#         self.visited[u] = True
#         self.stack[u] = True
#         charnum = ord(self.cstring[u]) - ord('a')

#         # Process all adjacent nodes
#         for v in self.adj[u]:
#             if not self.visited[v]:
#                 res = self.dfs(v)
#                 if res == float('inf'):
#                     return res
#             elif self.stack[v]:
#                 return float('inf')

#             # Update dp table by taking the maximum from adjacent nodes
#             for i in range(26):
#                 self.dp[u][i] = max(self.dp[u][i], self.dp[v][i])

#         # Add current node character
#         self.dp[u][charnum] += 1

#         self.stack[u] = False
#         return max(self.dp[u])

#     def maximumcolor(self):
#         res = 0
#         for u in range(self.n):
#             if not self.visited[u]:
#                 result = self.dfs(u)
#                 if result == float('inf'):
#                     return -1
#                 res = max(res, result)
#         return res
# edges = [[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],[5,6],[6,7],[7,8]]
# colors = "nnllnzznn"
# solution = Solution(edges,colors)
# print(solution.maximumcolor())



# class solution:
#     def __init__(self,strs):
#         self.strs = strs
#         self.n = len(strs)
#         self.adj = [[]for _ in range(self.n)]
#         ## adj initialization
#         for i in range(self.n):
#             for j in range(i+1,self.n):
#                 if self.similarity(self.strs[i],self.strs[j]):
#                     self.union(i,j)
#         self.parent = [ i for i in range(self.n)]
#         self.rank  =[0]*self.n
#     def similarity(self,s1,s2):
#         count = 0
#         for i in range(len(s1)):
#             if s1[i]!=s2[i]:
#                 count+=1
#         if count<=2:
#             return True
#         return False
    
#     def find(self,n):
#         if self.parent[n] ==n:
#             return n
#         self.parent[n] = self.find(self.parent[n])
#         return self.parent[n]
    
#     def union(self,e1,e2):
#         p1 = self.parent(e1)
#         p2 = self.parent(e1)
#         if p1==p2:
#             return 
#         if self.rank[p1]>self.rank[p2]:    
#             self.parent[p2] = p1
#         elif self.rank[p2]>self.rank[p1]:
#             self.parent[p1] = p2
#         else:
#             self.parent[p2] = p1
#             self.rank[p1]+=1
    
#     def similarGroup(self):
#         count = [0]*self.n
#         for u in range(self.n):
#             res = self.find(u)
#             count[res]+=1
        
#         return sum(count)


## 01 Knapsack
## we have been given the value and the weight array and a maximum capacity of the knapsack we 
# have to maximize the value of the items in the knapsack, so this is a maximizing 
# problem search for the maximum value of the knapsack, since we have to try each and 
# every combination to find the maximum so we will use the recursion backtracking for 
# searching the maximum value so the recusion will return the maximum value, we cant 
# use the searching or bs because searching or bs requires the data to be monotoinc 
# inorder to implement the bs, for normal searching we cant do the combinations in 
# that.abs

## we will use the cap and index for doing the recussion as they are the states needed
#  for doing the recursion. so for each item we have 2 choices to keep it and to leaveit
# the base conditions are
# if index<0 : return 0
# if cap<0  : return float('-inf')

# class solution:
#     def __init__(self,value,weight,capacity):
#         self.capacity = capacity
#         self.weight = weight
#         self.value = value
#         self.n = len(value)
#         self.capacity = capacity
#         self.dp = [[-1]*self.n for _ in range(capacity+1)]
#     def bfs(self,index,cap):
#         if index<0 or cap==0:
#             return 0
#         elif cap<0:
#             return float('-inf')
#         if self.dp[cap][index]!=-1:
#             return self.dp[cap][index]
#         exlude = self.bfs(index-1,cap)
#         include = 0
#         if cap>=self.weight[index]:
#             include = self.value[index]+self.bfs(index-1,cap-self.weight[index])
#         self.dp[cap][index] = max(include,exlude)
#         return dp[cap][index]


# class solution:
#     def __init__(self,value,weight):
#         self.weight = weight
#         self.value  = value
#         self.n = len(value)
#         self.capacity = capacity
#         self.dp = [[0]*self.n for _ in range(self.capacity+1)]
#         ## initialization
#         for j in range(self.n):
#             self.dp[j][0] = self.weight[j]
        
#     def zeroone(self):
#         for i in range(1,self.weight+1):
#             for j in range(self.n):
#                 exclude = self.dp[i][j-1]
#                 include = 0
#                 if self.weight[i]<=i:
#                     include = self.weight[i] + self.dp[i-self.weight[i]][j-1]
#                 self.dp[i][j] = max(include,exclude)

#         return self.dp[self.capacity][self.n-1]


#subset sum problem
#base conditions - index<0,suma==0: return 0 and suma<0:return -inf, 
# class solution:
#     def __init__(self,n,arr,target):
#         self.arr= arr
#         self.n = len(arr)
#         self.target = target
    
#     def dfs(self,index,currsum):
#         if currsum==0:
#             return True
#         if currsum<0 or index<0:
#             return False
        
#         exlude = self.dfs(index-1,currsum)
#         include = False
#         if self.arr[index]<=currsum:
#             include = self.arr[index] + self.dfs(index-1,currsum - self.arr[index])
#         return exclude or include


## count the number of subsets with given sum

# class solution:
#     def __init__(self,target,arr):
#         self.arr= arr
#         self.target=target
#         self.dp =  [[-1]*(self.target+1) for _ in range(len(self.arr))]
    
#     def dfs(self,index,currsum):
#         if currsum == self.target:
#             return 1
#         if index<0 or currsum>target:
#             return 0
#         if self.dp[index][currsum]!=-1:
#             return self.dp[index][currsum]
#         ## exclude
#         exclude = self.dfs(index-1,currsum)
#         include = 0
#         if self.arr[index]<=currsum:
#             include = self.dfs(index-1,currsum-self.arr[index])
#         self.dp[index][currsum] = include+exclude
#         return self.dp[index][currsum]



