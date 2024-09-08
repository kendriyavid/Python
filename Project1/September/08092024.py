## 01 knapsack


# class solution:
#     def __init__(self,value,weight,capacity):
#         self.value = value
#         self.weight = weight
#         self.capacity = capacity
#         self.dp = [[-1]*(self.weight+1) for _ in range(len(self.value))]
    
#     def knapsack(index,cap):
#         ## basecondition
#         if cap==0:
#             return 0
#         if index<0:
#             return float('-inf')
        
#         if self.dp[cap][index]!=-1:
#             return self.dp[cap][index]
        
#         ## nottake
#         exclude = self.knapsack(index-1,cap)
#         # taking
#         include = 0
#         if cap>=self.weight[index]:
#             include = self.weight[index]+self.knapsack(index-1,cap-self.weight[index])
#         self.dp[cap][index] = max(include,exclude)
#         return self.dp[cap][index]



# class solution:
#     def __init__(self,nums):
#         self.nums = nums
#         self.total = sum(nums)
    
#     def partitionEqual(self):
#         if self.total%2!=0:
#             return False
#         return self.knapsack(len(self.nums)-1,self.total//2)

#     def knapsack(self,index,cap):
#         if cap==0:
#             return True
#         if index<0 or cap<0:
#             return False
        
#         ## not taking
#         exclude = self.knapsack(index-1,cap)
#         include = False
#         if cap>=self.nums[index]:
#             include = self.knapsack(index-1,cap-self.nums[index])
#         return include or exclude

# class solution:
#     def __init__(self,nums,target):
#         self.nums = nums
#         self.target = target
    
#     def knapsack(self,index,cap):
#         if cap==0:
#             return 1
#         if index<0:
#             return 0
#         ## nottaking
#         exlude = self.knapsack(index-1,cap)
#         ##including
#         include = 0
#         if cap>=self.nums[index]:
#             include = self.knapsack(index-1,cap-self.nums[index])
#         return include+exclude


## Minimum subset sum difference

# class solution:
#     def __init__(self,nums):
#         self.nums = nums
#         self.total = sum(sums)
#         self.dp = [[None]*(self.total+1) for _ in range(len(self.nums))]
    
#     def knapsack(self,index,cap):
#         if index<0 or cap<0:
#             return False
#         if index==0:
#             return True
        
#         ##excluding
#         excluding = self.knapsack(index-1,cap)
#         ## include
#         include = False
#         if cap>=self.nums[index]:
#             include = self.knapsack(index-1,cap-self.nums[index])
#         self.dp[index][cap] = include or exclude
#         return self.dp[index][cap]
    
#     def minimumsum(self):
#         minimum=float('inf')
#         for i in range(len(self.nums)):
#             if self.dp[len(self.nums)-1][i]:
#                 computed = abs(2*i-self.total)
#                 minimum = min(min,computed)
#         return minimum


# Unbounded knapsack problem
# maximize the value of the knpasack if the item can be picked any number of times

# class solution:
#     def __init__(self,value,weight,capacity):
#         self.weight = weight
#         self.value = value
#         self.capacity = capacity
    
#     def ubkpsack(self,index,cap):
#         if index<0:
#             return float('-inf')
#         if cap==0:
#             return 0
        
#         ## exclude
#         exclude = self.ubkpsack(index-1,cap)
#         include = 0
#         if cap>=self.weight[index]:
#             include = self.value[index] + self.ubkpsack(index,cap-self.weight[index])
#         return max(include,exclude)

## Rod cutting 
# class solution:
#     def __init__(self,length,cost):
#         self.cost = cost
#         self.length = length
    
#     def rodcutting(self,index,l):
#         if index==0:
#             return 0
        
#         #exclude
#         exclude = self.rodcutting(index-1,l)
#         include = 0
#         if l>=index:
#             include = self.cost[index-1] + self.rodcutting(index,l-index)
#         return max(include,exclude)

## coinchange

# class solution:
#     def __init__(self,coins,target):
#         self.coins = coins
#         self.target =target
    
#     def CC(self,index,t):
#         if index<0:
#             return float('inf')
#         if t==0:
#             return 0
#         ##exclude
#         exclude = self.CC(index-1,t)
#         include = float('inf')
#         if t>=self.coins[index]:
#             include = 1+self.CC(index-1,t-self.coins[index])
#         return min(include,exclude)


## Minimum for ticket
# class solution:
#     def __init__(self,days,costs):
#         self.days = days
#         self.costs = costs
#         self.n = len(days)
    
#     def dayfinder(self,d):
#         for i in range(self.n):
#             if self.days[i]==d:
#                 return i
#         return -1
    
#     def minTicket(self,currdaypointer):
#         if currdaypointer==self.n:
#             return 0

#         ##onedayticket
#         oneday = float('inf')
#         if self.dayfinder(self.days[currdaypointer]+1 )!=-1:
#             oneday = self.costs[0]+self.minTicket(self.dayfinder(self.days[currdaypointer]+1 ))
#         ## sevendayticket
#         sevenday = float('inf')
#         if self.dayfinder(self.days[currdaypointer]+7 )!=-1:
#             seven = self.cost[1]+self.minTicket(self.dayfinder(self.days[currdaypointer]+7 ))
#         thirty = float('inf')
#         if self.dayfinder(self.days[currdaypointer]+30 )!=-1:
#             thirty = self.cost[2]+self.minTicket(self.dayfinder(self.days[currdaypointer]+30 ))
#         return min(one,seven,thrity)


## Longest common subsequence

# class solution:
#     def __init__(self,text1,text2):
#         self.text1 = text1
#         self.text2 = text2
#         self.n = len(text1)
#         self.m = len(text2)
#         self.dp = [[-1]*(self.n+1) for _ in range(self.m+1)]
    
#     def lcs(self,i,j):
#         if i<=0 or j<=0:
#             return 0
#         if self.dp[j][i]!=-1:
#             return self.dp[j][i]
        
#         ## matching
#         if self.text1[i-1] == self.text2[j-1]:
#             self.dp[j][i] =  1+self.lcs(i-1,j-1)
#         ## not matching
#         else:
#             left = self.lcs(i-1,j)
#             right = self.lcs(i,j-1)
#             self.dp[j][i]=max(left,right)
#         return self.dp[j][i]
    
#     def printinglcs(self):
        
## Longest common substring
# class solution:
#     def __init__(self,text1,text2):
#         self.text1 = text1
#         self.text2 = text2
#         self.n = len(text1)
#         self.m = len(text2)
#         self.dp = [[-1]*(self.n+1) for _ in range(self.m+1)]
#         self.maxlength = 0
#         self.startindex = -1
    
#     def lcs(self,i,j):
#         if i<=0 or j<=0:
#             return 0
        
#         ##matching
#         if self.dp[j][i]!=-1:
#             return self.dp[j][i]
#         if self.text1[i-1] == self.text2[j-1]:
#             self.dp[j][i] = 1+self.lcs(i-1,j-1)
#             if self.maxlength>self.dp[j][i]:
#                 self.maxlength  = self.dp[j][i]
#                 self.endindex = i

#         else:
#             self.lcs(i-1,j)
#             self.lcs(i,j-1)
#             self.dp[j][i] = 0 ## no matching
#         return self.dp[j][i]    

#     def printing(self):
#         self.lcs(self.n,self.m)
#         return self.text1[self.endindex-self.maxlength:self.endindex+1]


## Detonate Maximum Bombs

# class solution:
#     def __init__(self,bombs):
#         self.bombs = bombs
#         self.n = len(bombs)
#         self.visited = [False]*self.n
#         self.maximum = 1
#         self.adj = [[] for _ in range(self.n)]
#         ## adj initialization
#         for i in range(self.n):
#             ux,uy,ur = self.bombs[i]
#             for j in range(i+1,self.n):
#                 vx,vy,vr = self.bombs[j]
#                 if i==j:
#                     continue
#                 else:
#                     print(i,j)
#                     if ur*ur<=(abs(ux-vx)*abs(ux-vx))+(abs(uy-vy)*abs(uy-vy)):
#                         self.adj[i].append(j)
#                     elif vr*vr<=(abs(ux-vx)*abs(ux-vx))+(abs(uy-vy)*abs(uy-vy)):
#                         self.adj[j].append(i)

#     def bfs(self,i):
#         queue = [i]
#         explodedCount = 1
#         while queue:
#             i= queue.pop(0)
#             ux,uy,r = self.bombs[i]
#             for vj in self.adj[i]:
#                 if self.exploded[vj]!=True:
#                     explodedCount+=1
#                     self.exploded[vj] = True
#                     queue.append(vj)
#         return explodedCount

#     def maximumBombs(self):
#         for u in range(self.n):
#             if self.visited[u]!=True:
#                 self.exploded = [False]*self.n
#                 self.maximum = max(self.maximum,self.bfs(self.bombs[u][0],self.bombs[u][1],self.bombs[u][2]))
#                 self.visited[u] = True
#         return self.maximum
# bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
# Solution = solution(bombs)
# print(Solution.maximumBombs())


class solution:
    def __init__(self, bombs):
        self.bombs = bombs
        self.n = len(bombs)
        self.adj = [[] for _ in range(self.n)]
        
        for i in range(self.n):
            ux, uy, ur = bombs[i]
            for j in range(self.n):
                if i != j:
                    vx, vy, vr = bombs[j]
                    if ur**2 >= (ux-vx)**2 + (uy-vy)**2:
                        self.adj[i].append(j)

    def bfs(self, start):
        queue = [start]
        exploded = [False] * self.n
        exploded[start] = True
        explodedCount = 1

        while queue:
            i = queue.pop(0)
            for j in self.adj[i]:
                if not exploded[j]:
                    exploded[j] = True
                    explodedCount += 1
                    queue.append(j)

        return explodedCount

    def maximumBombs(self):
        return max(self.bfs(i) for i in range(self.n))

bombs = [[2,1,3],[6,1,4]]
Solution = solution(bombs)
print(Solution.maximumBombs())