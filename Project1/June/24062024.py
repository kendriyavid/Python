# # fIBBONACCHI
# from collections import defaultdict
# dp=defaultdict(int)
# def function(i):
#     if i<=1:
#         return 1
#     if i in dp:
#         return dp[i]
#     dp[i]=function(i-1)+function(i-2)
#     return dp[i]
# print(function(100))

# m=len(grid) 
# n=len(grid[0])
# dp=[[0]*n for _ in range(m)]
# dp[0][0]=max(1,1-grid[0][0])
# for y in range(m):
#     for x in range(n):
#         down=float-('inf')
#         if y>0:
#             down=max(1,dp[x][y]-grid[x][y])
#         right=float-('inf')
#         if x>0:
#             right=max(1,dp[x-1][y]-grid[x][y])
#         dp[x][y]=min(down,up)

# string='babab'
# maxlenght=0
# endpoint=0
# def function(i,j,lenght):
#     if i==j:
#         return 1
#     if i>j:
#         return 0
#     if string[i]==string[j]:
#         lenght=function(i+1,j-1,lenght+1)
#         if lenght>maxlenght:
#             maxlenght=len
#             endpoint=j
#         return lenght
#     else:
#         function(i+1,j-1,0)
#         function(i+1,j-1,0)
#         return 0
# def function(i,backward):
#     if i==x:
#         return 0
#     l=float('inf')
#     if i-b>0 and backward==False and i-b not in forbidden:
#         l=1+function(i-b,True)
#     r=1+function(i+a,False)
#     return min(l,r)

# ## Tree implementation
# class Node:
#     def __init__(val=None):
#         self.val=val
#         self.left=None
#         self.right=None

# class Tree:
#     def __init__():
#         root=None

#     def append(node):
#         i

# class Node:
#     def __init__(self,data=None):
#         self.val=data
#         self.right=None
#         self.left=None
    
# class Tree:
#     def __init__(self):
#         root=None
#     def append(self,val):
#         if self.root==None:
#             self.root=Node(val)
#             return 
#         _append(self.root,val)
#     def _append(self,node,val):
#         if node.val>val:
#             _append(node.right,val)
#         else:
#             _append(node.left,val)

def lcs(i,j):
    if i<0 or j<0:
        return ''
    if (i,j) in dp:
        return dp[(i,j)]
    if str1[i]==str2[j]:
        dp[(i,j)]=lcs(i-1,j-1)
    else:
        l=lcs(i-1,j)
        r=lcs(i,j-1)
    if len(l)>len(r):
        dp[(i,j)]=l
    else:
        dp[(i,j)]=r
    return dp[(i,j)]

# maxlen=0
# def lcsubstring(i,j):
#     if i<0 or j<0:
#         return 0
#     if s1[i]==s2[j]:
#         ans=1+lcsubstring(i-1,j-1)
#         maxlen=max(ans,maxlen)
#         dp[(i,j)]=ans
#     else:
#         lcsubstring(i-1,j)
#         lcsubstring(i,j-1)
#         dp[(i,j)]=0
#     return dp[i,j]

# m=len(str1)
# n=len(str2)
# dp=[[0]*(m+1) for _ in range(n+1)]
# def tablulationlcs(i,j):
#     if i==0 or j==0:
#         dp[i][j]=0
#         continue
#     if str1[i]==str2[j]:
#         dp[i][j]=1+dp[i-1][j-1]
#     else:
#         dp[i][j]=max(dp[i-1][j],dp[i][j-1])


# n=len(str1)
# dp=[[0]*(n+1) for _ in range(n+1)]
# for i in range(1,n+1):
#     dp[i][i]=1
# for i in range(n+1):
#     for j in range(n+1):
#         if i==0 or j==0:
#             dp[i][j]=0
#         if str1[i-1]==str1[j-n]:
#             dp[i][j]=2+dp[i-1][j-1]
#         else:
#             dp[i][j]=max(dp[i-1][j],dp[i][j-1])

# dp=[[0]*(n+1) for _ in range(n+1)]
# def function(i,j):
#     if i>j:
#         dp[i][j]=float('inf')
#     if s[i]==s[j]:
#         dp[i][j]=function(i+1,j-1)
#     else:
#         l=1+ function(i+1,j)
#         r=1+function(i,j+1)
#         dp[i][j]=min(l,r)
#     return dp[i][j]

# from collections import defaultdict
# m=len(word1)
# n=len(word2)
# dp=defaultdict()
# def function(i,j):
#     if i>=m:
#         dp[(i,j)]=n-j
#     if j>=n:
#         dp[(i,j)]=m-i
#     if (i,j) in dp:
#         return dp[(i,j)]
#     if word1[i]==word2[j]:
#         dp[(i,j)]=function(i+1,j+1)
#     else:
#         dp[(i,j)]=1+min(function(i+1,j),function(i,j+1),fucntion(i+1,j+1))
#     return dp[(i,j)]

# arr=[1,2,3,4]
# k=1
# def function(start,mid,count,arr,k):
#     if start >=len(arr):
#         return 0
#     if count>k:
#         return 0
#     total=0
#     for i in range(start,n):
#         if arr[i]%2!=0:
#             count[0]+=1
#         mid.append(arr[i])
#         total+=function(i+1,mid,count,arr,k)
#         mid.pop()
#     return total
    
# def function(start, mid, count, arr, k):
#     if start >= len(arr):
#         return 0
#     if count[0] > k:
#         return 0
    
#     total = 0
#     for i in range(start, len(arr)):
#         if arr[i] % 2 != 0:
#             count[0] += 1
#         if count[0]>k:
#             break
#         mid.append(arr[i])
#         total+=1
#         total += function(i + 1, mid, count, arr, k)
#         mid.pop()
#         if arr[i] % 2 != 0:
#             count[0] -= 1

    
#     return total

# # Example usage
# arr = [1, 2, 3, 4]
# k = 1
# count = [0]  
# mid = []

# print(function(0, mid, count, arr, k))


# def count_valid_subarrays(arr, k):
#     def function(start, mid, count, arr, k):
#         if start >= len(arr):
#             return 0
#         if count[0] > k:
#             return 0
        
#         total = 0
#         for i in range(start, len(arr)):
#             if arr[i] % 2 != 0:
#                 count[0] += 1
#             if count[0] > k:
#                 break
#             mid.append(arr[i])
#             total += 1  # Count this subarray
#             total += function(i + 1, mid, count, arr, k)
#             mid.pop()
#             if arr[i] % 2 != 0:
#                 count[0] -= 1
        
#         return total
    
#     return function(0, [], [0], arr, k)

# # Example usage
# arr = [1, 2, 3, 4]
# k = 1
# print(count_valid_subarrays(arr, k))  # Output should be 8


# def count_valid_subarrays(arr, k):
#     def function(start, count, arr, k):
#         if start >= len(arr):
#             return 0
        
#         total = 0
#         odd_count = 0
        
#         for i in range(start, len(arr)):
#             if arr[i] % 2 != 0:
#                 # odd_count += 1
#             if odd_count > k:
#                 break
#             total += 1  # Count this subarray
        
#         return total + function(start + 1, 0, arr, k)
    
#     return function(0, 0, arr, k)

# # Example usage
# arr = [1, 2, 3, 4]
# k = 1
# print(count_valid_subarrays(arr, k))  # Output should be 8

# dp=[[-1]*n for _ in range(n+1)]
# def function(index,prev):
#     if index>=n:
#         return 0
#     if dp[index][prev-1]!=-1:
#         return dp[index][prev-1]
#     l=0
#     if prev==-1 or arr[prev]<arr[index]:
#         l=1+function(index+1,index)
#     r=function(index+1,prev)
#     dp[index][prev-1]=max(l,r)

# arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

# n = len(arr)  # Assuming `arr` is defined somewhere
# dp = [[-1] * n for _ in range(n + 1)]

# def print_dp():
#     for row in dp:
#         print(row)
#     print("\n")

# def function(index, prev):
#     if index >= n:
#         return 0
#     if prev != -1 and dp[index][prev] != -1:
#         return dp[index][prev]
    
#     l = 0
#     if prev == -1 or arr[prev] < arr[index]:
#         l = 1 + function(index + 1, index)
#     r = function(index + 1, prev)
    
#     if prev != -1:
#         dp[index][prev] = max(l, r)

#     # Print DP matrix at this stage
#     print(f"DP matrix after processing index={index}, prev={prev}:")
#     print_dp()
    
#     return max(l, r)

# n = len(arr)
# print(function(0, -1))  # This should print the length of the LIS

# # Final DP matrix
# print("Final DP matrix:")
# print_dp()
