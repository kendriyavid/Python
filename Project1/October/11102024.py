# # # # class Solution:
# # # #     def __init__(self,adj):
# # # #         self.adj = adj
# # # #         self.n = len(adj)
# # # #         self.visited = [False]*self.n
    
# # # #     def dfs(self,u):
# # # #         self.visited[u] = True
# # # #         for v in self.adj[u]:
# # # #             if self.visited[v]!=True:
# # # #                 self.dfs(v)
    
# # # #     def DepthFirst(self):
# # # #         for i in range(self.n):
# # # #             if self.visited[i]!=True:
# # # #                 self.dfs(i)

        
# # # # class Solution:
# # # #     def __init__(self,adj):
# # # #         self.adj = adj
# # # #         self.n = len(adj)
# # # #         self.visited = [False]*self.n
    
# # # #     def bfs(self,u):
# # # #         queue= [u]
# # # #         while queue:
# # # #             u = queue.pop(0)
# # # #             self.visited[u] = True
# # # #             for v in self.adj[u]:
# # # #                 if self.visited[v]!=True:
# # # #                     queue.append(v)
    
# # # #     def BreadthFirst(self):
# # # #         for i in range(self.n):
# # # #             if self.visited[i]!=True:
# # # #                 self.bfs(i)

# # # # # cycle detection in the graphs

# # # # # undirected dfs graph

# # # # class Solution:
# # # #     def __init__(self,adj):
# # # #         self.adj = adj
# # # #         self.n = len(adj)
# # # #         self.visited = [False]*n

# # # #     def dfs(self,u,parent):
# # # #         self.visited[u] = True
# # # #         for v in self.adj[u]:
# # # #             if self.visited[v]!=True:
# # # #                 if self.dfs(v):
# # # #                     return True
# # # #             elif v!=parent:
# # # #                 return True
# # # #         return False
# # # #     def cycleDetection(self):
# # # #         for i in range(self.n):
# # # #             if self.visited[i]!=True:
# # # #                 if self.dfs(i):
# # # #                     return True
# # # #         return False


# # # # undirected graph bfs


# # # # class Solution:
# # # #     def __init__(self,adj):
# # # #         self.adj = adj
# # # #         self.n = len(adj)
# # # #         self.visited = [False]*self.n
    
# # # #     def bfs(self,u):
# # # #         queue = [(u,-1)]
# # # #         self.visited[u] = True
# # # #         while queue:
# # # #             curr,parent = queue.pop(0)
# # # #             for v in self.adj[curr]:
# # # #                 if self.visited[v]!=True:
# # # #                     queue.appdend((v,curr))
# # # #                     self.visited[v]= True
# # # #                 elif v!=parent:
# # # #                     return True
# # # #         return False
    
# # # #     def Ccycledetection(self):
# # # #         for i in range(self.n):
# # # #             if self.visited[i]!=True:
# # # #                 if self.bfs(i):
# # # #                     return True
        
# # # #         return False

# # # # class Solution:
# # # #     def __init__(self,adj):
# # # #         self.adj = adj
# # # #         self.n = len(adj)
# # # #         self.visited = [False]*self.n
# # # #         self.stack = [False]*self.n
    
# # # #     def dfs(self,u):
# # # #         self.visited[u] = True
# # # #         self.stack[u] = True
# # # #         for v in self.adj[u]:
# # # #             if self.visited[v]!=True:
# # # #                 if self.dfs(v):
# # # #                     return True
# # # #             elif self.stack[v]:
# # # #                 return True
# # # #         self.stack[u] = False
# # # #         return False
    
# # # #     def cycleDetection(self):
# # # #         for i in range(self.n):
# # # #             if self.visited[i]!=True:
# # # #                 if self.dfs(i):
# # # #                     return True
# # # #         return False

# # # # # Topological Sorting

# # # # class Solution:
# # # #     def __init__(self,adj):
# # # #         self.adj = adj
# # # #         self.n = len(adj)
# # # #         indegree = [0]*self.n
# # # #         for u in range(self.n):
# # # #             for v in self.adj[u]:
# # # #                 indegree[v]+=1
    
# # # #     def toposort(self):
# # # #         queue=[]
# # # #         for i in range(self.n):
# # # #             if indegree[i]==0:
# # # #                 queue.append(i)
# # # #         result=[]
# # # #         while queue:
# # # #             u = queue.pop(0)
# # # #             result.append(u)
# # # #             for v in self.adj[u]:
# # # #                 indegree[v]-=1
# # # #                 if indegree[v]==0:
# # # #                     queue.append(v)
# # # #         return result

# # # # # DSU

# # # # class Solution:
# # # #     def __init__(self,adj):
# # # #         self.adj = adj
# # # #         self.n = len(adj)
# # # #         self.rank = [0]*self.n
# # # #         self.parent = [0]*self.n
# # # #         for u in range(self.n):
# # # #             self.parent[u] = u
    
# # # #     def find(self,e1):
# # # #         if parent[e1] == e1:
# # # #             return e1
# # # #         parent[e1] = self.find(self.parent[e1])
# # # #         return self.parent[e1]
    
# # # #     def union(self,e1,e2):
# # # #         p1 =self.find(e1)
# # # #         p2 = self.din(e2)
# # # #         if p1==p2:
# # # #             return 
# # # #         if self.rank[p1]>self.rank[p2]:
# # # #             self.parent[p2]  = p1
# # # #         elif self.rank[p2]>self.rank[p2]:
# # # #             self.parent[p1] = p2
# # # #         else:
# # # #             self.parent[p2] =p1
# # # #             self.rank[p1]+=1

# # # # from collections import Counter

# # # # def x_sum(arr, x):
# # # #     if len(set(arr)) < x:
# # # #         return sum(arr)
    
# # # #     count = Counter(arr)
# # # #     top_x = sorted(count.items(), key=lambda item: (-item[1], -item[0]))[:x]
# # # #     return sum(element * count for element, count in top_x)

# # # # def solve(nums, k, x):
# # # #     n = len(nums)
# # # #     answer = []
    
# # # #     for i in range(n - k + 1):
# # # #         subarray = nums[i:i+k]
# # # #         answer.append(x_sum(subarray, x))
    
# # # #     return answer

# # # # # Example usage:
# # # # nums = [1,1,2,2,3,4,2,3]
# # # # k = 6
# # # # x = 2
# # # # result = solve(nums, k, x)
# # # # print(result)



# # # class TreeNode:
# # #     def __init__(self, val=0, left=None, right=None):
# # #         self.val = val
# # #         self.left = left
# # #         self.right = right

# # # class Solution:
# # #     def kthLargestPerfectSubtree(self, root, k):
# # #         """
# # #         :type root: TreeNode
# # #         :type k: int
# # #         :rtype: int
# # #         """
# # #         perfect_subtrees = []
        
# # #         def dfs(node):
# # #             if not node:
# # #                 return 0
            
# # #             left_height = dfs(node.left)
# # #             right_height = dfs(node.right)
            
# # #             if left_height == right_height:
# # #                 size = 2 ** (left_height + 1) - 1
# # #                 perfect_subtrees.append(size)
# # #                 return left_height + 1
            
# # #             return max(left_height, right_height)
        
# # #         dfs(root)
# # #         perfect_subtrees.sort(reverse=True)
        
# # #         return perfect_subtrees[k-1] if k <= len(perfect_subtrees) else -1



# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# # class Solution:
# #     def kthLargestPerfectSubtree(self, root: TreeNode, k: int) -> int:
# #         # To store sizes of all perfect binary subtrees
# #         perfect_subtree_sizes = []
        
# #         # Helper function to calculate height and size of perfect binary subtrees
# #         def check_perfect_subtree(node):
# #             if not node:
# #                 return (0, 0)  # Height 0, Size 0 for an empty subtree
            
# #             left_height, left_size = check_perfect_subtree(node.left)
# #             right_height, right_size = check_perfect_subtree(node.right)
            
# #             # If left and right subtrees have the same height, it's a perfect binary tree
# #             if left_height == right_height:
# #                 subtree_size = 1 + left_size + right_size
# #                 perfect_subtree_sizes.append(subtree_size)
# #                 return (left_height + 1, subtree_size)  # New height and size of this subtree
            
# #             return (max(left_height, right_height) + 1, 0)  # Not perfect, size 0
        
# #         # Start recursive checking from the root
# #         check_perfect_subtree(root)
        
# #         # Sort the sizes of perfect subtrees in descending order
# #         perfect_subtree_sizes.sort(reverse=True)
        
# #         # Return the k-th largest perfect subtree size or -1 if it doesn't exist
# #         return perfect_subtree_sizes[k-1] if len(perfect_subtree_sizes) >= k else -1

# # # Test case
# # root = TreeNode(10)
# # root.left = TreeNode(6)
# # root.right = TreeNode(2)
# # root.left.right = TreeNode(11)
# # root.right.left = TreeNode(10)

# # k = 3
# # solution = Solution()
# # print(solution.kthLargestPerfectSubtree(root, k))



# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# # class Solution:
# #     def kthLargestPerfectSubtree(self, root: TreeNode, k: int) -> int:
# #         # List to store sizes of all perfect binary subtrees
# #         perfect_subtree_sizes = []
        
# #         # Helper function to check if a subtree is perfect and get its height and size
# #         def check_perfect_subtree(node):
# #             if not node:
# #                 return (0, 0, True)  # (height, size, is_perfect)

# #             if not node.left and not node.right:
# #                 # It's a leaf node, so it's a perfect binary tree of size 1
# #                 return (1, 1, True)

# #             left_height, left_size, left_perfect = check_perfect_subtree(node.left)
# #             right_height, right_size, right_perfect = check_perfect_subtree(node.right)

# #             # A node is the root of a perfect binary tree if:
# #             # - both left and right subtrees are perfect
# #             # - the heights of left and right subtrees are equal
# #             if left_perfect and right_perfect and left_height == right_height:
# #                 # The subtree rooted at this node is perfect
# #                 current_size = 1 + left_size + right_size
# #                 perfect_subtree_sizes.append(current_size)
# #                 return (left_height + 1, current_size, True)

# #             return (max(left_height, right_height) + 1, 0, False)

# #         # Start the recursive check from the root
# #         check_perfect_subtree(root)
        
# #         # Sort the perfect subtree sizes in descending order
# #         perfect_subtree_sizes.sort(reverse=True)
        
# #         # Return the k-th largest perfect subtree size, or -1 if not enough subtrees
# #         return perfect_subtree_sizes[k - 1] if len(perfect_subtree_sizes) >= k else -1


# # # Test case
# # root = TreeNode(10)
# # root.left = TreeNode(6)
# # root.right = TreeNode(2)
# # root.left.right = TreeNode(11)
# # root.right.left = TreeNode(10)

# # k = 3
# # solution = Solution()
# # print(solution.kthLargestPerfectSubtree(root, k))



# # def count_inaccurate_processes(n, processOrder, executionOrder):
# #     # Step 1: Map each process in processOrder to its intended position
# #     position_map = {process: i for i, process in enumerate(processOrder)}

# #     # Step 2: Track the maximum index of processes executed correctly
# #     max_executed_index = -1
# #     inaccurate_count = 0

# #     # Step 3: Check each process in executionOrder
# #     for process in executionOrder:
# #         intended_position = position_map[process]

# #         # If the current process's intended position is less than max_executed_index, it fails
# #         if intended_position < max_executed_index:
# #             inaccurate_count += 1
# #         else:
# #             max_executed_index = max(max_executed_index, intended_position)

# #     return inaccurate_count

# # # Example usage:
# # n = 6
# # processOrder = [4,2,3,5,1,6]
# # executionOrder = [2,3,5,1,6,4]
# # print(count_inaccurate_processes(n, processOrder, executionOrder))  # Output should be 2



# # def count_inaccurate_processes(n, processOrder, executionOrder):
# #     # Step 1: Map each process in `processOrder` to its index
# #     index_map = {process: i for i, process in enumerate(processOrder)}
    
# #     # Track the maximum position in `processOrder` that has been processed correctly
# #     max_position = -1
# #     inaccurate_count = 0

# #     # Step 2: Traverse each process in `executionOrder`
# #     for process in executionOrder:
# #         current_position = index_map[process]

# #         # If the current position is before max_position, it's executed too early
# #         if current_position < max_position:
# #             inaccurate_count += 1
# #         else:
# #             # Update max_position to the highest position of correctly executed processes
# #             max_position = current_position

# #     return inaccurate_count

# # # Example usage
# # n = 6
# # processOrder = [4, 2, 3, 5, 1, 6]
# # executionOrder = [2, 3, 5, 1, 6, 4]
# # print(count_inaccurate_processes(n, processOrder, executionOrder))  # Expected Output: 5



# def getInaccurateProcesses(processOrder, executionOrder):
#     """
#     Determine count of processes that give inaccurate results due to incorrect execution order.
    
#     Args:
#         processOrder: List of integers representing the correct order of processes
#         executionOrder: List of integers representing the actual execution order
    
#     Returns:
#         int: Count of processes that will give inaccurate results
#     """
#     n = len(processOrder)
#     # Keep track of the first occurrence position of each process in executionOrder
#     first_execution = {}
#     for i, process in enumerate(executionOrder):
#         if process not in first_execution:
#             first_execution[process] = i
            
#     # Keep track of required prerequisites for each process
#     prerequisites = {}
#     for i, process in enumerate(processOrder):
#         prerequisites[process] = set(processOrder[:i])
    
#     inaccurate = 0
#     # Check each process when it's first executed
#     executed_processes = set()
    
#     for process in executionOrder:
#         if process in executed_processes:
#             continue
            
#         executed_processes.add(process)
#         # Check if all prerequisites were executed before this process
#         required_prereqs = prerequisites[process]
#         for prereq in required_prereqs:
#             # If prerequisite hasn't been executed yet or was executed after current process
#             if prereq not in first_execution or first_execution[prereq] > first_execution[process]:
#                 inaccurate += 1
#                 break      
#     return inaccurate
# print(getInaccurateProcesses([4, 2, 3, 5, 1, 6],[2,3,5,1,6,4]))


