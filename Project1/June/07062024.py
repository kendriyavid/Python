
# # # # instring=input()
# # # # teststring=input()
# # # # j=0
# # # # lenght=len(instring)
# # # # flag=False
# # # # for i in range(len(teststring)):
# # # #     if flag and teststring[i%lenght]!=instring[j]:
# # # #         flag=False
# # # #         break
# # # #     if teststring[i%lenght]==instring[j]:
# # # #         flag=True
# # # #         j+=1
# # # # print(flag)
  
# # # # Stock Span Problem
# # # # stack=[]
# # # # span=[0]*len(arr)
# # # # maxlen=1
# # # # arr=list(map(int,input().split()))
# # # # while i<len(arr):
# # # #     if stack and stack[-1]<=arr[i]:
# # # #         stack.pop()
# # # #     if not stack:
# # # #         span[i]=i+1
# # # #     else:
# # # #         arr[i]-stack[-1]
# # # #     i+=1
# # # #     stack.append(arr[i])
# # # # class Node:
# # # #     def __init__(self, val=None):
# # # #         self.next = None
# # # #         self.val = val

# # # class Node:
# # #     def __init__(self, data=None):
# # #         self.data = data
# # #         self.next = None

# # # class LinkedList:
# # #     def __init__(self):
# # #         self.head = Node()  # Dummy head node
    
# # #     def append(self, data):
# # #         new_node = Node(data)
# # #         curr = self.head
# # #         while curr.next is not None:
# # #             curr = curr.next
# # #         curr.next = new_node

# # #     def length(self):
# # #         length = 0
# # #         curr = self.head.next
# # #         while curr is not None:
# # #             length += 1
# # #             curr = curr.next
# # #         return length

# # #     def traversal(self):
# # #         curr = self.head.next
# # #         while curr is not None:
# # #             print(curr.data, end=" -> ")
# # #             curr = curr.next
# # #         print("None")
        
# # #     def get(self, data):
# # #         curr = self.head.next
# # #         index = 0
# # #         while curr is not None:
# # #             if curr.data == data:
# # #                 print(index)
# # #                 return
# # #             index += 1
# # #             curr = curr.next
# # #         print(-1)

# # #     def delete(self, data):
# # #         prev = self.head
# # #         curr = self.head.next
# # #         while curr is not None:
# # #             if curr.data == data:
# # #                 prev.next = curr.next
# # #                 print("Element deleted")
# # #                 return
# # #             prev = curr
# # #             curr = curr.next
# # #         print("No element found")

# # #     def reverse(self):
# # #         prev = None
# # #         curr = self.head.next
# # #         while curr is not None:
# # #             next_node = curr.next
# # #             curr.next = prev
# # #             prev = curr
# # #             curr = next_node
# # #         self.head.next = prev
    
# # #     def middle_element(self):
# # #         slow = self.head.next
# # #         fast = self.head.next
# # #         while fast is not None and fast.next is not None:
# # #             slow = slow.next
# # #             fast = fast.next.next
# # #         if slow:
# # #             print(slow.data)
    
# # #     def reverse_in_pairs(self):
# # #         dummy = Node()
# # #         dummy.next = self.head.next
# # #         prev = dummy
# # #         while prev.next and prev.next.next:
# # #             a = prev.next
# # #             b = a.next
# # #             prev.next, b.next, a.next = b, a, b.next
# # #             prev = a
# # #         self.head.next = dummy.next
    
# # #     def reverseink(self,k):
# # #         node=self.head
# # #         if node is None:
# # #             return None
# # #         ReverseinK(node,k)
# # #     def ReverseinK(self,node,k):
        

# # # # Example usage
# # # ll = LinkedList()
# # # ll.append(1)
# # # ll.append(2)
# # # ll.append(3)
# # # ll.append(4)
# # # ll.append(5)
# # # ll.traversal()  

# # # ll.reverse()
# # # ll.traversal()  

# # # ll.reverse_in_pairs()
# # # ll.traversal()  

# # # ll.middle_element()  # Output: 2

# # def longest_increasing_subsequence(arr):
# #     n = len(arr)
# #     if n == 0:
# #         return []

# #     dp = [1] * n
# #     subsets = {i: [arr[i]] for i in range(n)}
# #     max_size = 1
# #     max_index = 0

# #     for i in range(1, n):
# #         for j in range(i):
# #             if arr[i] > arr[j] and dp[i] < dp[j] + 1:
# #                 dp[/

# # def function(i,j,index,changed):
# #     if j>=len(B):
# #         return index
# #     if i>=len(A):
# #         return float('inf')
# #     if A[i]==B[j]:
# #         index = function(i+1,j+1,i)
# #     if A[i]!=B[j]:
# #         l= function(i+1,j,index)
# #         # changing the B
# #         r=float('inf')
# #         if changed==False:
# #             r=function(i+1,j+1,index,True)

# # def function(A, B):
# #     len_a = len(A)
# #     len_b = len(B)
    
# #     def is_subsequence_with_one_change(i, j, changed, start_index):
# #         if j == len_b:
# #             return start_index + 1
# #         if i == len_a:
# #             return float('inf') 
        
# # #         if A[i] == B[j]:
# # #             return is_subsequence_with_one_change(i + 1, j + 1, changed, start_index)
# # #         else:
# # #             skip_current = is_subsequence_with_one_change(i + 1, j, changed, start_index)
# # #             change_current = float('inf')
# # #             if not changed and j > 0:
# # #                 change_current = is_subsequence_with_one_change(i + 1, j + 1, True, start_index)
# # #             return min(skip_current, change_current)
    
# # #     result = float('inf')
# # #     for i in range(len_a):
# # #         current_result = is_subsequence_with_one_change(i, 0, False, i)
# # #         result = min(result, current_result)
    
# # #     return result if result != float('inf') else -1

# # # A = "daabe"
# # # B = "abe"
# # # result = function(A, B)
# # print(result) 


# # def function(A, B):
# #     len_a = len(A)
# #     len_b = len(B)
# #     memo = {}

# #     def is_subsequence_with_one_change(i, j, changed, start_index):
# #         if j == len_b:
# #             return start_index + 1 
# #         if i == len_a:
# #             return float('inf') 

# #         if (i, j, changed) in memo:
# #             return memo[(i, j, changed)]

# #         if A[i] == B[j]:
# #             result = is_subsequence_with_one_change(i + 1, j + 1, changed, start_index)
# #         else:
# #             skip_current = is_subsequence_with_one_change(i + 1, j, changed, start_index)
# #             change_current = float('inf')
# #             if not changed and j > 0:
# #                 change_current = is_subsequence_with_one_change(i + 1, j + 1, True, start_index)
# #             result = min(skip_current, change_current)
        
# #         memo[(i, j, changed)] = result
# #         return result

# #     result = float('inf')
# #     for i in range(len_a):
# #         current_result = is_subsequence_with_one_change(i, 0, False, i)
# #         result = min(result, current_result)
    
# #     return result if result != float('inf') else -1

# # # Example usage
# # A = "daabe"
# # B = "abe"
# # result = function(A, B)
# # print(result)  # Output should be 2


# # def function(i, j, index, changed):
# #     if j >= len(B):
# #         return index + 1  
# #     if i >= len(A):
# #         return float('inf')
# #     min_index = float('inf')
# #     if A[i] == B[j]:
# #         min_index = function(i + 1, j + 1, index if index != -1 else i, changed)
# #     l = function(i + 1, j, index, changed)
# #     if not changed and j > 0: 
# #         r = function(i + 1, j + 1, index if index != -1 else i, True)
# #         min_index = min(min_index, r)
# #     return min(min_index, l)
# # A = "daabe"
# # B = "abe"
# # result = function(0, 0, -1, False)
# # if result == float('inf'):
# #     result = -1
# # print(result)

# # def lcis(i,j,prev):
# #     if i>=m or j>=n:
# #         return []
# #     if dp[i+1][j+1]!=-1:
# #         return dp[i+1][j+1]
# #     if arr[i]==arr[j] and arr[i]>prev:
# #         res=arr[i]+lcs(i+1,j+1)
# #     else:
# #         l=lcs(i+1,j)
# #         r=lcs(i,j+1)
# #         if len(l)>len(r):
# #             res=l
# #         else:
# #             res=r
# #     dp[i+1][j+1]=res
# #     return(dp[i+1][j+1])

# # # LONGEST DECREASING SUBSEQUENCE
# # arr=[1,6,2,4,3]
# # dp=[1]*len(arr)
# # for index in range(n):
# #     for prev in range(index):
# #         if arr[prev]>arr[index]:
# #             dp[index]=max(dp[index],1+dp[prev])

# # ## r1,c1 (point on top left) (r2,c2) point on bottom right
# # matrix=[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
# # n=len(matrix)
# # dp=[[0]*(n+1) for _ in range(n+1)]
# # for i in range(1,n+1):
# #     for j in range(1,n+1):
# #         dp[i][j]=dp[i-1][j-1]+matrix[i-1][j-1]
# # totalsum=0
# # row=r1
# # while row<=r2:
# #     totalsum=totalsum+(dp[row+1][c2+1]-dp[row+1][c1-1])

# class Solution:
#     def all_lcs(self, str1, str2):
#         n = len(str1)
#         m = len(str2)
#         dp = [[0] * (m + 1) for _ in range(n + 1)]
#         lcs = [[set() for _ in range(m + 1)] for _ in range(n + 1)]

#         # Initialize the lcs list for base cases
#         for i in range(n + 1):
#             lcs[i][0] = {""}
#         for j in range(m + 1):
#             lcs[0][j] = {""}

#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 if str1[i - 1] == str2[j - 1]:
#                     dp[i][j] = 1 + dp[i - 1][j - 1]
#                     for seq in lcs[i - 1][j - 1]:
#                         lcs[i][j].add(seq + str1[i - 1])
#                 else:
#                     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#                     if dp[i][j] == dp[i - 1][j]:
#                         lcs[i][j].update(lcs[i - 1][j])
#                     if dp[i][j] == dp[i][j - 1]:
#                         lcs[i][j].update(lcs[i][j - 1])

#         # Convert the final set to a sorted list
#         result = sorted(list(lcs[n][m]))
#         print(result)
#         return result

# # Example usage
# sol = Solution()
# print(sol.all_lcs("abcabcaa", "acbacba"))  # Output should be ["ace"]

# import math
# class solution:
#     def initialize(self,n,arr):
#         k=math.ceil(math.log2(n))
#         sparsetable=[[0]*k for _ in range(n)]
#         for i in range(n):
#             sparsetable[i][0]=arr[i]
#         i=0
#         for j in range(1,n):
#             while i+(1<<j)<n:
#                 sparsetable[i][j]=min(sparsetable[i][j-1],sparsetable[i+(1<<j)][j-1])
#             i+=1
#     def rmsq(self,i,j):
#         w=j-1+1
#         k=math.floor(math.log2(w))
#         ans=min(sparsetable[i][k],sparsetable[j-(1<<2)+1][k])

# n=int(input())
# arr=list(map(int,input().split()))
# q=int(input())
# solution.i
# for _ in range(q):
#     i,j=map(int,input().split())
#     ans=rmsq(i,j)
#     print(ans)


## CATAPULT THAT BALL
# import math
# class solution:
#     def __init__(self,arr,n,m):
#         self.k=math.ceil(math.log2(n))
#         self.n=n
#         self.arr=arr
#         self.m=m
#         self.sparsetable = sparsetable=[[0]*(self.k+1) for _ in range(self.n)]
#         self.initialize()

#     def initialize(self):
#         for i in range(n):
#             self.sparsetable[i][0]=arr[i]
#         i=0
#         for j in range(k):
#             while i+(1<<j)<=n:
#                 self.sparsetable[i][j]=max(self.sparsetable[i][j-1],self.sparsetable[i+(1<<j)][j-1])
#                 i+=1

#     def ctb(self,a,b):
#         na=a+1
#         nb=b-1
#         w=nb-na+1
#         k=math.floor(math.log2(w))
#         ans=max(self.sparsetable[na][k],self.sparsetable[nb-(1<<j)+1][k])
#         if ans<a:
#             return 1
#         else:
#             return 0


# n,m=map(int,input().split())
# arr=list(map(int,input().split()))
# Solution=solution(arr,n,m)
# count=0
# for _ in range(n):
#     a,b=map(int,input().split())
#     Solution.ctb(a,b)
#     count+=Solution.ctb(a,b)

# return count


## SEGMENT TREE
# import math
# arr=[-1,-1,3,-1,0,3,6]
# class solution:
#     def __init__(self,arr):
#         self.arr=arr
#         self.segarr=[0]*((math.ceil(math.log2(len(self.arr))))-1)
#         cTree(arr,segarr,len(arr)-1,0,0)
#     def cTree(self,arr,segarr,high,low,pos):
#         mid=(high+low)//2
#         if mid==low:
#             segarr[pos]=arr[low]
#             return
#         cTree(arr,segarr,mid,low,(2*pos)+1)
#         cTree(arr,segarr,high,mid+1,(2*pos)+2)
#         segarr[pos]=min(segarr[2*pos+1],segarr[2*pos+1])
#     def _query(self,slow,shigh,high,low,segarr,pos):
#         if slow<=low and shigh>=high:
#             return segarr[pos]
#         elif slow<=low or shigh>=high:
#             return float('inf')
#         mid=(low+high)//2
#         return min(self._query(slow,mid,high,low,segarr,2*pos+1),self._query(mid+1,shigh,high,low,segarr,2*pos+2))
#     def query(self,i,j):
#         return self._query(0,len(self.segarr),j,i,self.segarr,0)
