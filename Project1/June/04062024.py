# class Node:
#     def __init__(self, val=None):
#         self.val = val
#         self.right = None
#         self.left = None

# class Tree:
#     def __init__(self):
#         self.root = None
    
#     def Append(self, val):
#         if not self.root:
#             self.root = Node(val)
#         else:
#             self.append(self.root, val)
    
#     def append(self, node, val):
#         if val < node.val:
#             if not node.left:
#                 node.left = Node(val)
#             else:
#                 self.append(node.left, val)
#         else:
#             if not node.right:
#                 node.right = Node(val)
#             else:
#                 self.append(node.right, val)
    
#     def preordertraverse(self):
#         if not self.root:
#             return 'Tree is empty'
#         self.preTraverse(self.root)
    
#     def preTraverse(self, node):
#         if not node:
#             return
#         print(node.val, end=' ')
#         self.preTraverse(node.left)
#         self.preTraverse(node.right)
    
#     def postordertraverse(self):
#         if not self.root:
#             return 'Tree is empty'
#         self.postTraverse(self.root)
    
#     def postTraverse(self, node):
#         if not node:
#             return
#         self.postTraverse(node.left)
#         self.postTraverse(node.right)
#         print(node.val, end=' ')
    
#     def inordertraverse(self):
#         if not self.root:
#             return 'Tree is empty'
#         self.inTraverse(self.root)
    
#     def inTraverse(self, node):
#         if not node:
#             return
#         self.inTraverse(node.left)
#         print(node.val, end=' ')
#         self.inTraverse(node.right)

#     def iterpreorder(self):
#         stack=[]
#         stack.append(self.root)
#         while stack:
#             popped=stack.pop()
#             if popped.right:
#                 stack.append(popped.right)
#             if popped.left:
#                 stack.append(popped.left)
#             print(popped.val)
    
#     def iterpostorder(self):
#         stack=[]
#         stack.append(self.root)
#         arr=[]
#         while stack:
#             popped=stack.pop()
#             if popped.left:
#                 stack.append(popped.left)
#             if popped.right:
#                 stack.append(popped.right)
#             arr.append(popped.val)
#         arr.reverse()
#         return arr

#     def iterinroder(self):
#         stack=[]
#         stack.append(self.root)
#         arr=[]
#         while stack:
#             curr=stack.pop()
#             while curr!=None:
#                 stack.append(curr)
#     def inverting(node):
#         if not node:
#             return None
#         node.left=inverting(node.right)
#         node.right=inverting(node.left)
#         return node

#     def dia(node):
#         if not node:
#             return 0
#         l=1+dia(node.left)
#         r=1+dia(node.right)
#         path=max(path,l+r)
#         return max(l,r)

#     def same(self,node1,node2):
#         if node1.val!=node2.val:
#             return False
#         l=same(node1.left,node2.left)
#         r=same(node1.right,node2.right)
#         return l and r
    
#     def lot(self):
#         queue=[]
#         queue.append(self.root)
#         result=[]
#         while queue:
#             arr=[]
#             lenght=len(queue)
#             for i in range(lenght):
#                 popped=queue.pop(0)
#                 arr.append(popped.val)
#                 if popped.left:
#                     queue.append(popped.left)
#                 if popped.right:
#                     queue.append(popped.right)
#             result.append(arr[:])
#         print(result)
        
#     maxi=self.root
#     def cgn(self,maxi,node):
#         if not node:
#             return 0
#         maxi=max(maxi,max)
#         value=0
#         if node.val>=maxi:
#             value=1
#         return l+r+value
#         l=cgn(maxi,node.left)
#         r=cgn(maxi,node.right)

# # Example usage:
# tree = Tree()
# values = [10, 5, -3, 3, 2, 11, 3, -2, 1]
# for value in values:
#     tree.Append(value)

# print("Preorder Traversal:")
# tree.lot()

## Sudoku Solver
# import defaultdict
# rowset=collections.defaultdict(set)
# colset=collections.defaultdict(set)
# blockset=collections.defaultdict(set)
# result=None
# def sudoku(i,j):
#     if i,j==9,9:
#         result=board
#         return True
#     for i in range(9):
#         for j in range(9):
#             if board[i][j]!='.':
#                 continue
#             i=0
#             while i<10:
#                 if num in rowset([i][j]) or num in colset([i][j]) or num in blockset([i/3][j/3]):
#                     continue
#                 board[i][j]=num
#                 val=sudoku()
#                 if val:
#                     return True
#                 sudoku[i][j]="."
#             if i>=10:
#                 return 
# lstring = list('1?11?00?1?')
# result = []

# def wildcard(result, index, lstring):
#     if index >= len(lstring):
#         result.append(''.join(lstring))
#         return
#     for i in range(index, len(lstring)):
#         if lstring[i] == '?':
#             lstring[i] = '0'
#             wildcard(result, i + 1, lstring)
#             lstring[i] = '1'
#             wildcard(result, i + 1, lstring)
#             lstring[i] = '?'
#             return  # Return after handling the first wildcard to avoid duplicate work

# wildcard(result, 0, lstring)
# print(result)

## Climbing stairs
# from collections import defaultdict
# n=3
# dp=defaultdict(int)
# def stairs(count,n,dp):
#     if count>n:
#         return 0 
#     elif count==n:
#         return 1
#     if count in dp:
#         return dp[count]
#     l=stairs(count+1,n,dp)
#     r=stairs(count+2,n,dp)
#     res=l+r
#     dp[count]=res
# print(stairs(0,n,dp))    


# from collections import defaultdict

# # Define the number of steps
# n = 3

# # Initialize the memoization dictionary
# dp = defaultdict(int)

# def stairs(count, n, dp):
#     if count > n:
#         return 0
#     elif count == n:
#         return 1
#     if count in dp:
#         return dp[count]
    
#     l = stairs(count + 1, n, dp)
#     r = stairs(count + 2, n, dp)
    
#     # Store the result in the dp dictionary and return it
#     dp[count] = l + r
#     return dp[count]

# # Print the number of ways to climb n stairs starting from step 0
# print(stairs(0, n, dp))
# arr = [10, 20, 30, 20]
# n = len(arr) - 1
# dp = {}

# def frog(curr, dp, arr):
#     if curr > n:
#         return float('inf')
#     if curr == n:
#         return 0  
#     if curr in dp:
#         return dp[curr]

#     l = abs(arr[curr + 1] - arr[curr]) + frog(curr + 1, dp, arr) if curr + 1 <= n else float('inf')
#     r = abs(arr[curr + 2] - arr[curr]) + frog(curr + 2, dp, arr) if curr + 2 <= n else float('inf')

#     dp[curr] = min(l, r)
#     return dp[curr]

# result = frog(0, dp, arr)
# print(result)

## Constant window 
# arr=[-1,2,3,3,4,5,-1]
# k=4
# i=0
# sum=0
# while i<k:
#     sum+=arr[i]
#     i+=1
# i=0
# maxsum=0
# while i<len(arr)-k+1:
#     maxsum=max(maxsum,sum)
#     sum=sum-arr[i]+arr[i+k-1]
#     i+=1

# print(maxsum)

## Subset sum k
# dp=defaultdict(bool)
# def subsetsumk(index,k):
#     if k<0:
#         return False
#     if k==0 and index>=len(arr):
#         return True
#     if index>=len(arr):
#         return False
#     if (index,k) in dp:
#         return dp[(index,k)]
#     l=subsetsumk(index+1,k-arr[index])
#     r=subsetsumk(index,l)
#     dp[(index,k)]= l or r
#     return dp[(index,k)]

# nums = [3, 1, 5, 2, 8]
# total_sum = sum(nums)
# target = total_sum // 2

# def mindiff(index, target, total):
#     if total > target:
#         return float('inf')
#     if index == len(nums):
#         return abs(total_sum - 2 * total) 
#     l = mindiff(index + 1, target, total + nums[index])
#     r = mindiff(index + 1, target, total)
#     return min(l, r)

# result = mindiff(0, target, 0)
# print(result)  


## infix to postfix conversion

# ##unbounded knapsack infinite supply
# from collections import defaultdict
# weight=[2,4,6]
# value=[5,11,18]
# max_weight=10
# dp=defaultdict(int)
# def uk(index,total):
#     if total>max_weight:
#         return -float('inf')
#     if (index,total) in dp:
#         return dp[(index,total)]
#     take=uk(index,total+weight[index])+value[index]
#     ntake=uk(index+1,total)
#     return max(take,ntake)


## Rod cutting problem
# from collections import defaultdict
# length=[1,2,3,4,5,6,7,8,9,10]
# price=[1,5,8,9,10,17,24,30]
# dp=defaultdict(int)
# def rodcutting(index,l):
#     if l<1:
#         return -float('inf')
#     if l==1:
#         return price[0]
#     if (index,l) in dp:
#         return dp[(index,l)]
#     maxi=-float('inf')
#     for i in range(index,len(lenght)-1):
#         value=price[i-index]+rodcutting(i,l-i-indeX)
#         maxi=max(maxi,value)
#     return maxi
# rodcutting(0,5)

# from collections import defaultdict
# dp=defaultdict(str)
# def plcs(i,j):
#     if i<0 or j<0:
#         return ""
#     if (i,j)in dp:
#         return dp[(i,j)]
#     if str1[i]==str2[i]:
#         dp[(i,j)]=str1[i]+plcs(i-1,j-1)
#         return dp[(i,j)]
#     elif str1[i]!=str2[j]:
#         l=plcs(i-1,j)
#         r=plcs(i,j-1)
#         if len(l)<len(r):
#             return r
#         else:
#             return l


# from collections import defaultdict
# dp=defaultdict(int)
# maxlen=0
# endindex=0
# def lcstring(i,j,count,maxlen,endindex):
#     if i==len(str1) or j==len(str2):
#         return count
#     if (i,j,count) in dp:
#         return dp[(i,j,count)]
#     if str1[i]==str2[j]:
#         lcstring(i-1,j-1,count+1,endindex)
#         if count>maxlen:
#             maxlen=count
#             endindex=i
#     else:
#         lcstring(i-1,j,0,endindex)
#         lcstring(i,j-1,0,endindex)


# arr=[8,7,6,5,4,3,2,1]
# userinput=int(input("enter the nth largest"))
# i=0
# while i<userinput-1:
#     i+=1
# print(arr[i])

arr=[1,2,3,4,5,6,7,8]
largest=-float('inf')
secondlargest=-float('inf')
for i in range(len(arr)):
    if arr[i]>largest:
        secondlargest=largest
        largest=arr[i]
    elif arr[i]>secondlargest:
        secondlargest=arr[i]
print(secondlargest)