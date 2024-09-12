import heapq
class Graph:
    def __init__(self, n: int, edges):
        self.n = n
        self.edges = edges
        self.adj = [[]for _ in range(self.n)]
        for u,v,w in self.edges:
            self.adj[u].append((v,w))
        
    def addEdge(self, edge) -> None:
        fr =edge[0]
        to = edge[1]
        weight = edge[2]
        self.adj[fr].append((to,weight))
        
    def shortestPath(self, node1: int, node2: int) -> int:
        def dijkstra(node1,node2):
            heap = []
            heapq.heapify(heap)
            distance = [float('inf')]*self.n
            heapq.heappush(heap,(0,node1))
            distance[node1] = 0
            while heap:
                d,u = heapq.heappop(heap)
                if u==node2:
                    return distance[u]
                for v,vd in self.adj[u]:
                    if vd+d<distance[v]:
                        distance[v] = vd+d
                        heapq.heappush(heap,(distance[v],v))
            return -1
        return dijkstra(node1,node2)
n = 4
edges = [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]
graph = Graph(n,edges)
print(graph.shortestPath(0,3))
graph.addEdge([1,3,4])
print(graph.shortestPath(0,3))
            
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)