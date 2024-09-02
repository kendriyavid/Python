## Notes revision 
## imp revision
## New Questions
## Trees Revision
## Trees Questions

## Graphs - Trees - Trie - Bitmanipulation - vector algorithms  - Greedy+ Intervals
# Dp - Rangequeries -  Stack - Binary Search - Linked list

## Bellman ford algorithm
# bellman ford algorithm is used for getting single source shortest path algorithm
## in this we relax the vertices of the graph to the v-1 times if the graph relaxes more than 
# v-1 times then there is a negative cycle in the graph the sequence of relaxing the vertices
# should be in the same way

# class solution:
#     def __init__(self,adj):
#         self.adj = adj  ##u,[v,w]
#         self.n = len(adj)
#         self.distance = [float('inf')]*self.n
    
#     def Bellmanford(self,source):
#         self.distance[source] = 0
#         for i in range(self.n-1):
#             for u in range(self.n):
#                 for v,w in self.adj[u]:
#                     if self.distance[indx]!=float('inf') and self.distance[v]>self.distance[u]+w:
#                         self.distance[v] = self.distance[u]+w
#         return self.distance


## Floyd warshall algorithm
## floyd warshall algorithm is used for calculate the distance from every pair of graph its timecomplelxity is n3
# if there are n edges we make matrix and then use via to caluclate the lesser distance, initilizing  - 0 and float inf

# class solution:
#     def __init__(self,adj):
#         self.n = len(adj)
#         self.matrix = [[float('inf')]*self.n for _ in range(self.n)]
#         ## initialization
#         for i in range(self.n):
#             matrix[i][i] = 0
#         for u in range(self.n):
#             v,w = self.adj[u]
#             self.matrix[u][v] = w
    
#     def floydwarshall(self):
#         for via in range(self.n):
#             for u in range(self.n):
#                 for v in range(self.n):
#                     if self.matrix[u][v]<self.matrix[u][via]+self.matrix[via][v]:
#                         self.matrix[u][v] = self.matrxi[u][via]+self.matrix[via][v]
#         return self.matrix


## Leetcode 797 All paths from source to target

# class solution:
#     def __init__(self,adj,target):
#         self.adj = adj
#         self.n = len(adj)
#         self.intermediate  =[]
#         self.result= []
#         self.visited = [False]*self.n
#         self.stack=[False]*self.n
#         self.target = target

#     def dfs(self,u):
#         self.visited[u] = True
#         self.stack[u]=True
#         self.intermediate.append(u)
#         if self.u == target:
#             self.stack.append(self.intermediate.copy())
#         for v in self.adj[u]:
#             if self.stack[u]!=True:
#                 self.dfs(v)
#         self.stack[u] = False
#         self.intermediate.pop()
    
#     def Allpathsfromsourcetotarget(self):
#         self.dfs(0)
#         return self.result



## Minimum time to collect all the apples in the tree

# class solution:
#     def __init__(self,adj,hasapple):
#         self.adj = adj
#         self.time = 0
#         self.hasapple = hasapple
    
#     def dfs(self,u):
#         ans = False
#         for v in self.adj[u]:
#             if self.dfs(v):
#                 self.time+=2
#                 ans = ans or True
#         if self.hasapple[u]:
#             return True
#         return ans

#     def mintimmetocollectapple(self):
#         self.dfs(0)
#         return self.time


##Leetcode 1519

# class solution:
#     def __init__(self,edges,label):
#         self.edges = edges
#         self.adj = [[]*self.n  for _ in range(self.n)]
#         for u,v in self.n:
#             self.adj[u].append[v]
#         self.n = len(edges)
#         self.result =[0]*self.n
#         self.visited = [False]*self.n
#         self.label = label
    
#     def dfs(self,u):
#         self.visited[u] = True
#         dicti=[0]*26
#         for v in self.adj[u]:
#             if self.visited[v]!=True:
#                 temp = self.dfs(v)
#                 for i in range(len(temp)):
#                     dicti[i] = temp[i]+dicti[i]
        
#         dicti[ord(self.label[u])-ord(a)]+=1
#         self.result[u]+=dicti[ord(self.label[u])-ord(a)]
#         return dicti


## Leetcode 2246

class solution:
    def __init__(self,parent,s):
        self.s = s
        self.parent = parent
        self.adj = adj
        self.visited = [False]*len(parent)
    
    def bfs(self,u):
        queue=[(0,s[0])]
        self.visited[u]=True
        count = 1
        while queue:
            nqueue = []
            for u,parent in queue:
                for v in self.adj[u]:
                    if self.visited[v]!=True :
                        self.visited[v] = True
                        if self.s[u]!=parent:
                            nqueue.append((v,self.s[v]))
            if nqueue:
                count+=1
            queue = nqueue
        return count




        
