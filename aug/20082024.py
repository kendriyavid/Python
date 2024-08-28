## Topological sorting 


# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.visited=[False]*len(adj)
#         self.variations=[]
#     def Topological(self,u,stack):
#         self.visited[u]=True
#         if len(stack)==len(self.adj):
#             self.visited.append(chr(97+stack).join(''))
#         for v in adj[u]:
#             if self.visited[v]!=True:
#                 stack.append(v)
#                 self.dfs(v,stack)
#                 stack.pop()
#         self.visited[u]=True
#     def followingOrders(self):
#         for i in range(len(self.adj)):
#             if self.visited[i]!=True:
#                 self.Topological()
#         return self.variations

# ## input
# var=list(map(str,input().split()))
# constraint=list(map(str,input().split()))
# adj=[[] for _ in range(len(var))]
# ##adj initialization
# for i in var:
#     adj[var[i[0]]].append(var[i[1]])
# Solution=solution(adj)
# print(Solution.followingOrders())


## DIJSTRA ALGORITHM
# import heapq
# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.heap=[]
#         heapq.heapify(self.heap)
#         self.result=[float('inf')]*len(adj)
#     def dijstra(self,source):
#         heapq.heappush(heap,[0,source])
#         self.result[source]=0
#         while heap:
#             u,w = heapq.heappop(self.heap)
#             for v, weight in self.adj[u]:
#                 if w + weight < self.result[v]:
#                     self.result[v] = w + weight
#                     heapq.heappush(self.heap, [self.result[v], v])

#         return self.result


## Disjoint set uninon

# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.parent=[i for _ in range(len(self.adj))]
#         self.rank=[0]*len(adj)
#     def find(self,e):
#         if self.parent[e]==e:
#             return e
#         self.parent[e]=self.find(self.parent[e])
#         return self.parent[e]
    
#     def union(self,e1,e2):
#         p1=self.find(e1)
#         p2=self.find(e2)
#         if p1==p2:
#             return True
#         if self.rank[p1] > self.rank[p2]:
#             self.parent[p2] = p1
#         elif self.rank[p1] < self.rank[p2]:
#             self.parent[p1] = p2
#         else:
#             self.parent[p2] = p1
#             self.rank[p1] += 1

##  Count the numbeof unreachable pair of nodes 
# class solution:
#     def __init__(self,adj):
#         self.adj=adj
#         self.parent=[i for i in range(len(adj))]
#         self.rank=[0]*len(adj)
#         self.map={}
#         self.n=n
    
#     def find(self,e):
#         if e==self.parent[e]:
#             return e
#         self.parent[e]=self.find(parent[e])
#         return self.parent[e]
    
#     def union(self,e1,e2):
#         p1=self.find(e1)
#         p2=self.find(e2)
#         if self.rank[p1]>self.rank[p2]:
#             self.parent[p2]=p1
#         elif self.rank[p1]<self.rank[p2]:
#             self.parent[p1]=p2
#         else:
#             self.rank[p1]+=1
#             self.parent[p2]=p1
    
#     def componentCreation(self):
#         for rel in self.adj:
#             self.union(rel[0],rel[1])
    
#     def mapfilling(self):
#         for i in range(self.n):
#             if map[self.find(i)]:
#                 map[self.find(i)]+=1
#             else:
#                 map[self.find(i)]=1
    
#     def nonconnectedComponent(self):
#         rem=self.n
#         total=0
#         for key,value in self.map:
#             total+= value(rem-value)


# edges = edges
# parent = [i for i in range(n)]
# rank = [0] * n
# component_map = {}
# n = n

# def find( e):
#     if e == parent[e]:
#         return e
#     parent[e] = find(parent[e])  # Corrected reference to parent
#     return parent[e]

# def union( e1, e2):
#     p1 = find(e1)
#     p2 = find(e2)
#     if p1 != p2:
#         if rank[p1] > rank[p2]:
#             parent[p2] = p1
#         elif rank[p1] < rank[p2]:
#             parent[p1] = p2
#         else:
#             rank[p1] += 1
#             parent[p2] = p1

# def componentCreation():
#     for rel in edges:
#         union(rel[0], rel[1])

# def mapfilling():
#     for i in range(n):
#         root = find(i)
#         if root in component_map:
#             component_map[root] += 1
#         else:
#             component_map[root] = 1

# def nonconnectedComponent():
#     componentCreation()
#     mapfilling()
#     rem = n
#     total = 0
#     for key, value in component_map.items():
#         total += value * (rem - value)
#         rem -= value
#     return total

# # Example usage
# n = 7
# edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
# solution = Solution(edges, n)
# print(solution.nonconnectedComponent())


# class Solution(object):
#     def countPairs(self, n, edges):
#         parent = [i for i in range(n)]
#         rank = [0] * n
#         component_map = {}

#         def find(e):
#             if e == parent[e]:
#                 return e
#             parent[e] = find(parent[e])  # Path compression
#             return parent[e]

#         def union(e1, e2):
#             p1 = find(e1)
#             p2 = find(e2)
#             if p1 != p2:
#                 if rank[p1] > rank[p2]:
#                     parent[p2] = p1
#                 elif rank[p1] < rank[p2]:
#                     parent[p1] = p2
#                 else:
#                     rank[p1] += 1
#                     parent[p2] = p1

#         def componentCreation():
#             for rel in edges:
#                 union(rel[0], rel[1])

#         def mapFilling():
#             for i in range(n):
#                 root = find(i)
#                 if root in component_map:
#                     component_map[root] += 1
#                 else:
#                     component_map[root] = 1

#         def nonConnectedComponent():
#             componentCreation()
#             mapFilling()
#             rem = n
#             total = 0
#             for value in component_map.values():
#                 total += value * (rem - value)
#                 rem -= value
#             return total 

#         return nonConnectedComponent()

# # Example usage:
# n = 7
# edges = [[0,2], [0,5], [2,4], [1,6], [5,4]]
# solution = Solution()
# result = solution.countPairs(n, edges)
# print(result)  # Output should be the number of unreachable pairs


# import heapq

# class Solution:
#     def __init__(self, adj):
#         self.adj = adj
#         self.heap = []
#         heapq.heapify(self.heap)
#         self.result = [float('inf')] * len(self.adj)

#     def dijkstra(self, source, end):
#         heapq.heappush(self.heap, (0, source, [source]))
#         self.result[source] = 0
        
#         while self.heap:
#             d, u, path = heapq.heappop(self.heap)
            
#             if u == end:
#                 return path
            
#             for v, dv in self.adj[u]:
#                 if d + dv < self.result[v]:
#                     self.result[v] = d + dv
#                     heapq.heappush(self.heap, (d + dv, v, path + [v]))
        
#         return []

# # Example input
# # Number of nodes
# n = int(input())

# # Edges input as u1, v1, w1, u2, v2, w2, ...
# array = list(map(int, input().split()))

# # Source and destination
# source, destination = map(int, input().split())

# # Adjust for 0-based indexing
# source -= 1
# destination -= 1

# # Initialize adjacency list
# adj = [[] for _ in range(n)]
# for i in range(0, len(array), 3):
#     u = array[i] - 1
#     v = array[i+1] - 1
#     w = array[i+2]
#     adj[u].append((v, w))
#     adj[v].append((u, w))

# # Output adjacency list for debugging
# print(adj)

# # Run Dijkstra's algorithm
# solution = Solution(adj)
# shortest_path = solution.dijkstra(source, destination)

# # Print the shortest path
# print(shortest_path)

## Network delay Time

import heapq
class solution:
    def __init__(self,adj,n):
        self.adj=adj
        self.heap=[]
        heapq.heapify(self.heap)
        self.result=[float('inf')]*n
    def Djksistra(self,source):
        heapq.heappush(self.heap,[0,source])
        self.result[source]=0
        while self.heap:
            d,u=heapq.heappop(self.heap)
            for v,dv in self.adj[u]:
                if d+dv<self.result[v]:
                    self.result[v]=d+dv
                    heapq.heappush(self.heap,[d+dv,v])
        return self.result
n,k=map(int,input().split())
array=list(map(int,input().split()))
adj = [[] for _ in range(n)]
for i in range(0, len(array), 3):
    u = array[i] - 1
    v = array[i+1] - 1
    w = array[i+2]
    adj[u].append((v, w))
    adj[v].append((u, w))
Solution=solution(adj,n)
result=Solution.Djksistra(k)
print(max(result))

