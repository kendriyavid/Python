# # Trees + Segment Trees
# # Stack
# Heap
# Greedy
# Binary Search
# # Dynamic Programming

# # Subset sum equal k

# arr=[1,2,3,4]
# k=5
# dp=[[-1]*(k+1)for _ in range(len(arr)-1)]

# for _ in range(len(arr)-1):
#     dp[i][0]= True if arr[i]<=0 else False:


# def function(index,target):
#     if target==0:
#         return True
    
#     if index>=len(arr):
#         return False
    
#     if dp[index][target]!=-1:
#         return dp[index][target]
#     # Not Take
#     l=function(index+1,target)

#     # Take
#     r=False
#     if target>=arr[index]:
#         r=function(index+1,target-arr[index])
#     dp[index][target]=l or r
#     return dp[index][target]

# class Solution:
#     def __init__(self,n):
#         self.n=n
#         self.board=[["."]*(self.n) for _ in range(self.n)]
#         self.pos=set()
#         self.neg=set()

#     def function(self,i,j,count):
#         if i>=self.n or j>=self.n or i<0 or j<0:
#             return False
#         if (i+j) in self.pos:
#             return False
#         if (i/j) in self.neg:
#             return False

#         if count>=self.n+1:
#             return True
        
#         board[i][j]='Q'
#         self.pos.add(i-1+j-1)
#         self.neg.add(i-1/j-1)
#         up=self.function(i-1,j-1,count+1)
#         self.pos.remove(i-1+j-1)
#         self.neg.remove(i-1/j-1)

#         self.pos.add(i+1+j+1)
#         self.neg.add(i+1/j+1)
#         down=self.function(i+1,j+1,count+1)
#         self.pos.remove(i+1+j+1)
#         self.neg.remove(i+1/j+1)

#         self.pos.add(i-1+j+1)
#         self.neg.add(i-1/j+1)
#         left=self.function(i-1,j+1,count+1)
#         self.pos.remove(i-1+j+1)
#         self.neg.remove(i-1/j+1)

#         self.pos.add(i+1+j-1)
#         self.neg.add(i+1/j-1)
#         right=self.function(i+1,j-1,count+1)
#         self.pos.remove(i+1+j-1)
#         self.neg.remove(i+1/j-1)

#         board[i][j]='.'

#         return up or down or left or right


# # Obstacle Grid

# obsgrid=[[0,0,0],[0,1,0],[0,0,0]]
# n=len(obsgrid)
# dp=[[-1]*n for _ in range(n)]

# def function(i,j):
#     if i>=n or j>=n or obsgrid[i][j]==1:
#         return 0

#     if i==n-1 and j==n-1:
#         return 1
    
#     if dp[i][j]!=-1:
#         return dp[i][j]
    
#     right=function(i+1,j)
#     left=function(i,j+1)

#     dp[i][j]=max(left,right)
#     return dp[i][j]

# MINIMUM PATH SUM

# grid=[[1,3,1],[1,5,1],[4,2,1]]
# n=len(grid)
# dp=[[float('inf')*(n+1) for _ in range(n+1)]]
# dp[1][1]=grid[0][0]
# for i in range(n):
#     for j in range(n):
#         if i==0 and j==0:
#             continue
#         dp[i+1][j+1]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])


# class Solution:
#     def __init__(self,grid):
#         self.grid=grid
#         self.n=len(grid)
#         self.dp=[[float('inf'),-float('inf')]*n for _ in range(n)]
#         self.dp[0][0][0]=self.grid[0][0]
#         self.dp[0][0][1]=self.grid[0][0]

#     def function(self):
#         for j in range(n):
#             for i in range(n):
#                 if i==0 and j==0:
#                     continue
#                 if i>0:
#                     minprod=min(minprod,dp[i-1][j][0]*grid[i][j])
#                     maxprod=max(maxprod,dp[i-1][j][1]*grid[i][j])
#                 if j>0:
#                     minprod=min(minprod,dp[i][j-1][0]*grid[i][j])
#                     maxprod=max(maxprod,dp[i][j-1][1]*grid[i][j])
#                 dp[i][j][0]=minprod
#                 dp[i][j][1]=maxprod
    
#         return dp[self.n-1][self.n-1][1]


# class solution:
#     def __init__(self):
#         self.grid=[[-2,-3,3],[-5,-10,1],[10,30,-5]]
#         self.n=len(grid)
#         self.dp=[[float('inf')]*n for _ in range(n)]
#         self.dp[self.n-1][self.n-1]=1 if self.grid[self.n-1 ][self.n-1]>0 else 1+(-self.grid[self.n-1 ][self.n-1])
#     def function(self):
#         for i in range(self.n,-1,-1):
#             for j in range(self.n,-1,-1):
#                 if i==self.n-1 and j==self.n-1:
#                     continue
#                 subsu=self.grid[i][j-1]
#                 subsl=self.grid[i-1][j]
#                 self.dp[i][j]=min()


# ## Segment Tree
# import math
# from math import gcd
# class solution:
#     def __init__(self):
#         self.arr=arr
#         self.n=len(arr)
#         self.segarr=[0]*2*(1<<(math.ceil(math.log2(self.n))))

#     def initialize(self,low,high,pos):
#         if low==high:
#             self.segarr[pos]=self.arr[pos]
#             return
#         mid=(low+high)//2
#         self.initialize(low,mid,2*pos+1)
#         self.initialize(mid+1,high,2*pos+2)
#         self.segarr[pos]=gcd(self.segarr[2*pos+1],self.segarr[2*pos+2])
    
#     def _query(self,l,r,low,high,pos):
#         ## No overlap
#         if l>high or r<low:
#             return float('inf')
        
#         ## Total overlap
#         if l<=low and r>=high:
#             return self.segarr[pos]
        
#         ## Partial Overlap
#         mid=(high+low)//2
#         return min(self._query(l,r,low,mid,p2*pos+1),self._query(l,r,mid+1,high,2*pos+2))


#     def query(self,l,r):
#         return self._query(l,r,0,self.n,0)


## R2d2 and Droid Army

# n droids - a1 a2 a3 am   (ai is the number of details of the i-th type in this droid's mechanism.)
# r2d2 wants to destroy maximum lenght of consequtive droids

