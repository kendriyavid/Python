## Merging 1d intervals

# arr=[[1,3],[2,6],[8,10],[15,18]]
# result=[arr[i]]
# def overcheck(i1,i2):
#     maximum=max(i1[0],i1[1])
#     minimum=min(i2[0],i2[1])
#     return maximum-minimum>=0
# for interval in arr:
#     prev=result[-1]
#     if overcheck(interval,prev):
#         n1x=max(interval[0],prev[0])
#         n1y=max(interval[1],prev[1])
#         result.pop()
#         result.append([n1x,n1y])
#     else:
#         result.append(interval)
# import heapq
# buildings=[[2,9,10],[3,7,15],[5,12,12],[15,20,10]]
# filteredarr=[]
# for i in buildings:
#     start=[-i[2],i[0],'s']
#     end=[-i[2],i[1],'e']
#     filteredarr.append(start)
#     filteredarr.append(end)
# filteredarr.sort(key=lambda x:x[0])
# print(filteredarr)
# resultarr=[]
# heap=[]
# maxi=0
# heapq.heapify(heap)
# for point in filteredarr:
#     if point[2]=='s':
#         heapq.heappush(heap,point)
#         if heap and maxi<heap[0][0]:
#             maxi=heap[0]
#             result.append([point[1],-point[0]])
#     elif point[2]=='e':
#         heapq.heappop(heap)
#         if heap and maxi<heap[0][0]:
#             maxi=heap[0]
#             result.append([point[1],-point[0]])
# print(resultarr)
    

## Skyline problem
# import heapq

# class Solution:
#     def __init__(self, buildings):
#         self.buildings = buildings

#     def skyLine(self):
#         self.filarr = []
        
#         # Create a list of all start and end points
#         for building in self.buildings:
#             self.filarr.append((building[0], -building[2], 's'))  # Start point with negative height
#             self.filarr.append((building[1], building[2], 'e'))   # End point with positive height
        
#         # Sort by x, then by height, handling start ('s') before end ('e')
#         self.filarr.sort(key=lambda x: (x[0], x[1]))
        
#         heap = [(0, float('inf'))]  # Initial ground level height
#         result = []
#         prev_max_height = 0
        
#         for point in self.filarr:
#             x, height, typ = point
            
#             if typ == 's':  # Start of a building
#                 heapq.heappush(heap, (height, x))
#             elif typ == 'e':  # End of a building
#                 for i in range(len(heap)):
#                     if heap[i][0] == -height:
#                         del heap[i]
#                         break
#                 heapq.heapify(heap)
            
#             current_max_height = -heap[0][0]
            
#             if current_max_height != prev_max_height:
#                 result.append([x, current_max_height])
#                 prev_max_height = current_max_height
        
#         return result


## SKYLINE PROBLEM USING SEGMENT TREE
