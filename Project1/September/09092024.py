## minimum spanning tree
# import heapq

# class Solution:
#     def __init__(self, adj):
#         self.adj = adj
#         self.n = len(adj)
#         self.heap = []  # Initialize the heap correctly
#         self.total = 0
#         self.visited = [False] * self.n
#         self.parent = [i for i in range(self.n)]

#     def MinimumSpanningTree(self, start):
#         heapq.heappush(self.heap, (0, start))
#         while self.heap:
#             d, u = heapq.heappop(self.heap)
#             if self.visited[u]:
#                 continue
#             self.visited[u] = True
#             self.total += d  # Add the weight of the selected edge to the total
#             for v, vd in self.adj[u]:
#                 if not self.visited[v]:
#                     heapq.heappush(self.heap, (vd, v))
#                     self.parent[v] = u 
#         return self.total, self.parent


## Kruskal's algorithm

# edges = [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]
# edges.sort(key=lambda x: x[2])  # Sort by the third element in each sublist
# print(edges)

# class solution:
#     def __init__(self,edges):
#         self.edges = edges.sort(key = lambda x:x[2])
#         self.result = []
#         self.n = len(edges)
#         self.visited = [False]*self.n
#         self.parent = [i for i in range(self.n)]

#     def find(self,e1):
#         if e1 == self.find(self.parent[e1]):
#             return e1
#         self.parent[e1] = self.find(self.parent[e1])
#         return self.parent[e1]
    
#     def union(self,e1,e2):
#         p1 = self.find(e1)
#         p2 = self.find(e2)
#         if p1==p2:
#             return
#         if self.rank[p1]>self.rank[p2]:
#             self.parent[p2] = p1
#         elif self.rank[p2]>self.rank[p1]:
#             self.parent[p1] = p2
#         else:
#             self.parent[p2] = p1
#             self.rank[p1]+=1
    
#     def mst(self,index):
#         if all(self.visited) == True:
#             self.result.append(self.parent[:])
#         p1 = self.find(self.edges[index][0])
#         p2 = self.find(self.edges[index][1])
#         v1 =self.visited[self.edges[index][1]]
#         v2 = self.visited[self.edges[index][2]]
#         if p1!=p2:
#             self.union(self.edges[index][0],self.edges[index][1])
#             self.visited[self.edges[index][0]] = True
#             self.visited[self.edges[index][1]] = True
#         for i in range(index+1):
#             if self.edges[i][2] == self.edges[index][2]:
#                 self.mst(i)
#         self.parent[edges[index][0]] = p1
#         self.parent[edges[index][0]] = p2
#         self.visited[self.edges[index][1]] = v1
#         self.visited[self.edges[index][2]] = v2

# class Solution:
#     def __init__(self, edges, num_nodes):
#         # Sort edges by weight
#         self.edges = sorted(edges, key=lambda x: x[2])
#         self.result = []  # To store the possible MSTs
#         self.n = num_nodes  # Number of nodes
#         self.visited = [False] * self.n
#         self.parent = [i for i in range(self.n)]
#         self.rank = [0] * self.n  # Rank for union-find

#     def find(self, node):
#         # Find with path compression
#         if node != self.parent[node]:
#             self.parent[node] = self.find(self.parent[node])
#         return self.parent[node]

#     def union(self, node1, node2):
#         # Union by rank
#         root1 = self.find(node1)
#         root2 = self.find(node2)
#         if root1 != root2:
#             if self.rank[root1] > self.rank[root2]:
#                 self.parent[root2] = root1
#             elif self.rank[root1] < self.rank[root2]:
#                 self.parent[root1] = root2
#             else:
#                 self.parent[root2] = root1
#                 self.rank[root1] += 1

#     def backtrack_mst(self, edge_idx, mst_edges):
#         # Base case: if we have n - 1 edges, it's a valid MST
#         if len(mst_edges) == self.n - 1:
#             self.result.append(mst_edges[:])
#             return

#         for i in range(edge_idx, len(self.edges)):
#             u, v, w = self.edges[i]
#             root_u = self.find(u)
#             root_v = self.find(v)

#             if root_u != root_v:  # Check if adding the edge forms a cycle
#                 # Backup state
#                 parent_backup = self.parent[:]
#                 rank_backup = self.rank[:]

#                 # Add this edge to the MST
#                 mst_edges.append((u, v, w))
#                 self.union(u, v)

#                 if w == self.edges[i+1][2]:
#                     self.backtrack_mst(i + 1, mst_edges)

#                 # Backtrack: restore state
#                 mst_edges.pop()
#                 self.parent = parent_backup
#                 self.rank = rank_backup

#     def find_all_msts(self):
#         self.backtrack_mst(0, [])
#         return self.result

# # Example usage
# edges = [
#     [0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2],
#     [0, 4, 3], [3, 4, 3], [1, 4, 6]
# ]
# num_nodes = 5  # Number of nodes

# sol = Solution(edges, num_nodes)
# all_msts = sol.find_all_msts()

# # Print all MSTs found
# for i, mst in enumerate(all_msts, 1):
#     print(f"MST {i}: {mst}")

# class solution:
#     def __init__(self,n,m,group,beforeItems):
#         self.n =n
#         self.m = m
#         self.group = group
#         self.beforeItems = beforeItems
#         self.adjItems = [[] for _ in range(self.n)]
#         ##initializing Items
#         for i in range(len(self.beforeItems)):
#             for nodes in self.beforeItems[i]:
#                 self.adjItems[nodes].append(i)
    
#         self.adjGroup = [[] for _ in range(self.m)]
#         ## initializing Group
#         # for i in range(len(self.group)):
#         #     if self.group[i]!=-1
#         #         self.adjGroup[i]
#         self.indegreeBefore = [0]*self.n
#         ## initialization of before indegree
#         for i in self.adjItems:
#             for nodes in i:
#                 self.indegreeBefore[nodes]+=1
#         self.indegroup = [0]*self.m
#         ## initialization of group indegree
#         self.beforeVisited = [False]*self.n
#         self.groupVisited = [False]*self.m
#         self.beforeResult = []
#         self.groupResult = []
#     def Topological(self,queue,visited,res):
#         while queue:
#             u = queue.pop(0)
#             res.append(u)
#             for v in self.adj[u]:
#                 if self.visited[v]!=True:

#                     queue.append(v)
#                     visited[v] = True
#     def sortItemsbyDependencies(self):
#         queue =[]
#         for i in range(len(self.indegreeBefore)):
#             if self.indegreeBefore[i]==0:
#                 queue.append(i)
#         self.Topological(queue,self.groupVisited,self.beforeResult)
#         queue =[]
#         for i in range(len(self.indegroup)):
#             if self.indegroup[i]==0:
#                 queue.append(i)
#         self.Topological(queue,self.groupResult,self.groupResult)

