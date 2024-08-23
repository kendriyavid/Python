 ## Representation of Graph

## DFS of a graph

# def dfs(u,adj,visited):
#     if visited[u]==True:
#         return 
#     visited[u]=True
#     for v in range(adj[u]):
#         if visited[v]!=True:
#             dfs(v,adj,visited)


## BFS of a graph
# queue=[adj[0]]
# while queue:
#     u=queue.pop(0)
#     for v in range(adj[u]):
#         if visited[v]!=True:
#             queue.append(v)
#             visited[v]=True


## Cycle detection in ug graph  (dfs approach)
## return BOOL
# def dfs(adj,u,visited,parent):
#     visited[u]=True
#     res=False
#     for v in (adj[u]):
#         if visited[v]==False and parent!=v:
#             res= res or dfs(adj,v,visited,u)
#         if visited[v]==True and parent!=v:
#             return True
#     return res

## Cycle detection using bfs Undirected Graph

# queue=[(0,-1)]
# cycle=False
# while queue:
#     u=queue.pop(0)
#     for v in (adj[u]):
#         if not visited[v]:
#             queue.append((v,u))
#             visited[v]=True
#         elif u!=v(1):
#             cycle=True
#             break

## Directed Graph DFS Cycle detection:

# def dfs(adj,u,visited):
#     if visited[u]:
#         return True
#     visited[u]=True
#     for v in adj[u]:
#         if dfs(adj,v,visited):
#             return True
#     return False

# def dfs(adj,u,visited,inrec):
#     visited[u]=True
#     inrec[u]=True
#     for v in adj[u]:
#         if visited[v]!=True:
#             if dfs(adj,v,visited,increc):
#                 return True
#         elif inrec[v]:
#             return True
#     return False

## Topological Sorting dfs
# stack=[]
# def dfs(u,visited,adj):
#     for v in adj[u]:
#         visited[u]=True
#         if visited[v]!=True:
#             dfs(v,visited,adj)
#     stack.append(u)

# for u in adj:
#     if visited[u]!=True:
#         dfs(u,visited,adj)

# def bfs(u):
#     stack=[]
#     queue=[0]
#     while queue:
#         u=queue.pop(0)
#         stack.append(u)
#         for v in adj[u]:
#             if visited[v]!=True:
#                 queue.append(v)
#     return stack
# result=[] 
# for u in range(n):
#     if visited[u]!=True:
#         stack=bfs(u)
#     result.append(stack[::-1])