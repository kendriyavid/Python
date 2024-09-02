
## LCS
# class solution:
#     def __init__(self,str1,str2):
#         self.str1=str1
#         self.lstr1=len(str1)
#         self.str2=str2
#         self.lstr2=len(str2)
#         self.dp=[[-1]*(self.lstr1+1) for _ in range(self.lstr2+1)]
    
#     def lcs(self,i,j):
#         if i==0 or j==0:
#             return 0
#         # same
#         if dp[i][j]!=-1:
#             return dp[i][j]
#         if self.str1[i-1]==self.str2[j-1]:
#             ans=1+self.lcs(i-1,j-1)
#         else:
#             l=self.lcs(i-1,j)
#             r=self.lcs(i,j-1)
#             ans=max(l,r)
#         dp[i][j]=ans
#         return dp[i][j]


## BOTTOM UP IMPLEMMENTATION

# class Solution:
#     def __init__(self,str1,str2):
#         self.str1=str1
#         self.str2=str2
#         self.n=len(str1)
#         self.m=len(str2)
#         self.dp=[[-1]*(self.n+1)for _ in range(m+1)]
    
#     def lcs(self):
#         ##initialization
#         for i in range(self.n+1):
#             self.dp[0][i]=0
#         for j in range(self.m+1):
#             self.dp[j][0]=0
        
#         for j in range(1,self.m+1):
#             for i in range(1,self.n+1):
#                 if self.str1[i-1]==self.str2[j-1]:
#                     self.dp[j][i]=1+dp[j-1][i-1]
#                 else:
#                     l=self.dp[j][i-1]
#                     r=self.dp[j-1][i]
#                     dp[j][i]=max(l,r)
#         return self.dp[self.m][self.n]


### printing lcs

# class solution:
#     def  __init__(self,str1,str2):
#         self.str1=str1
#         self.str2=str2
#         self.n=len(str1)
#         self.m=len(str2)
#         self.dp=[[-1]*(self.n+1)for _ in range(self.m+1)]
    
#     def printinglcs(self):
#         for i in range(self.n+1):
#             self.dp[0][i]=''
#         for j in range(self.m+1):
#             self.dp[j][0]=''
#         for j in range(1,self.m+1):
#             for i in range(1,self.n+1):
#                 ## if matching
#                 if self.str1[i-1]==self.str2[j-1]:
#                     dp[i][j]=self.str1[i-1]+dp[i-1][j-1]
#                 else:
#                     l=dp[i-1][j]
#                     r=dp[i][j-1]
#                     if len(l)>len(r):
#                         dp[i][j]=l
#                     else:
#                         dp[i][j]=r
#         return dp[self.m][self.n]

## lONGEST REPEATING SUBSEQUENCE K TIMES

# class solution:
#     def __init__(self,str):
#         self.s1=str
#         self.s2=str
#         self.n=len(str)
#         self.dp=[[-1]*(self.n+1) for _ in range(self.n+1)]
#         self.initialization(self.n-1,self.n-1)
#         self.dicti={}
    
#     def initialization(self,i,j):
#         if i==0 or j==0:
#             return 0
        
#         if self.dp[i][j]!=-1:
#             return self.dp[i][j]
        
#         if s1[i-1]==s2[j-1] and i!=j:
#             self.dp[i][j]=1+self.initialization(i-1,j-1)
#         else:
#             l=self.initialization(i-1,j)
#             r=self.initialization(i,j-1)
#             self.dp[i][j]=max(l,r)
#         return self.dp[i][j]
    
#     def lrsk(self):
#         for i in range(1,self.n+1):
#             for j in range(1,self.n+1):
#                 if dp[i][j]!=0:
#                     self.dicti[]
    
# class Solution:
#     def __init__(self, s, k):
#         self.s1 = s
#         self.s2 = s
#         self.n = len(s)
#         self.k = k
#         self.dp = [[0] * (self.n + 1) for _ in range(self.n + 1)]
#         self.initialize_dp()
    
#     def initialize_dp(self):
#         for i in range(1, self.n + 1):
#             for j in range(1, self.n + 1):
#                 if self.s1[i-1] == self.s2[j-1] and i != j:
#                     self.dp[i][j] = self.dp[i-1][j-1] + 1
#                 else:
#                     self.dp[i][j] = max(self.dp[i-1][j], self.dp[i][j-1])
    
#     def find_lrsk(self):
#         subsequence_count = {}
#         longest_subseq = ""
        
#         for i in range(1, self.n + 1):
#             for j in range(1, self.n + 1):
#                 if self.dp[i][j] != 0:
#                     subseq = self._get_subsequence(i, j)
#                     if subseq in subsequence_count:
#                         subsequence_count[subseq] += 1
#                     else:
#                         subsequence_count[subseq] = 1
#                     if subsequence_count[subseq] == self.k:
#                         if len(subseq) > len(longest_subseq):
#                             longest_subseq = subseq
        
#         return longest_subseq
    
#     def _get_subsequence(self, i, j):
#         subseq = []
#         while i > 0 and j > 0:
#             if self.s1[i-1] == self.s2[j-1] and i != j:
#                 subseq.append(self.s1[i-1])
#                 i -= 1
#                 j -= 1
#             elif self.dp[i-1][j] > self.dp[i][j-1]:
#                 i -= 1
#             else:
#                 j -= 1
        
#         return ''.join(reversed(subseq))

# s = "letsleetcode"
# k = 1
# solution = Solution(s, k)
# print(solution.find_lrsk())  

# Matrix Chain multiplication

# s = 'nitin'
# dp = [[-1] * len(s) for _ in range(len(s))]

# def ispalindrome(string):
#     return string == string[::-1]

# def function(i, j):
#     if i >= j:
#         return 0
    
# #     if dp[i][j] != -1:
# #         return dp[i][j]
    
# #     if ispalindrome(s[i:j+1]):
# #         dp[i][j] = 0
# #         return 0
    
# #     result = float('inf')
    
# #     for k in range(i, j):
# #         l = function(i, k)
# #         r = function(k + 1, j)
# #         tempres = 1 + l + r
# #         result = min(result, tempres)
    
# #     dp[i][j] = result
# #     return dp[i][j]

# # print(function(0, len(s) - 1))
# # print(dp)


# ## Boolean Parenthesization

# class solution:
#     def __init__(self,s):
#         self.s=s
#         self.n=len(s)
#     def boolpar(self,i,j,boolval):
#         if i>j:
#            return 0
#         elif i==j:
#             if s[i]==True:
#                 if boolval==True:
#                     return 1
#                 else:
#                     return 0
#             else:
#                 if boolval==False:
#                     return 1
#                 else:
#                     return 0
#         tempans=0
#         for k in range(i,j-1,2):
#             localvalue=0
#             lt=self.boolpar(i,k,True)
#             lf=self.boolpar(i,k,False)
#             rt=self.boolpar(k+1,j,True)
#             rf=self.boolpar(k+1,j,False)
#             if s[k]=='&':
#                 if boolval==True:
#                     localvalue= lt*rt
#                 else:
#                     localvalue= lf*rf + lt*rf + rt*lf
#             elif s[k]=="|":
#                 if boolval==True:
#                     localvalue= lt*rt + rt*lf + lt*rf
#                 else:
#                     localvalue= lf*rf
#             elif s[k]=='^':
#                 if boolval==True:
#                     localvalue= lt*rf +lf*rt
#                 else:
#                     localvalue= lf*rf + rt*lt
#             tempans+=localvalue
#         return tempans
                
                
## Scramble string

# def function(a,b):
#     if len(a)==len(b):
#         return False
#     if a==b:
#         return True    
#     if a=="" and b=="":
#         return True
#     if a=="" or b=="":
#         return False
#     for k in range(len(a)-1):
#         ## noscaramble
#         result=function(a[:k],b[:k]) and function(a[k:],b[k:])
#         if result==True:
#             return True
#         r2=function(a[:k],b[len(b)-1-k:]) and function(a[len(a)-1-k:],b[:k])
#         if result or r2 ==True:
#             return True
#         else:
#             return False


## graph dfs

# def dfs(adj,u,visited):
#     if visited[u]!=False:
#         return 
#     visited[u]=True
#     for i in range(adj[u]):
#         if visited[i]!=True:
#             dfs(adj,i,visited)


# queue=[0]
# while queue:
#     element=queue.pop()
#     for i in adj[element]:
#         if visited[i]!=True:
#             queue.append(i)
#             visited[i]=True


## Cycle detection 

# visited=[False]*len(n-1)
# def function(adj,u,visited,parent):
#     visited[u]=True
#     for i in adj[u]:
#         if visited[i]==False:
#             if function(adj,i,visited,u):
#                 return True
#         elif i != parent:
#             return True
#     return False
    
## BFS


# def lps(pat):
#     m = len(pat)
#     lps = [0] * m
#     length = 0  # Corrected spelling
#     i = 1

#     while i < m:
#         if pat[i] == pat[length]:
#             length += 1
#             lps[i] = length
#             i += 1
#         else:
#             if length != 0:
#                 length = lps[length - 1]
#             else:
#                 lps[i] = 0
#                 i += 1

#     return lps

# def kmp(text, pat):
#     n = len(text)
#     m = len(pat)
#     lps_arr = lps(pat)  # Corrected variable name
#     i = 0
#     j = 0
#     result = []

#     while i < n:
#         if pat[j] == text[i]:  # Corrected indexing
#             i += 1
#             j += 1
        
#         if j == m:
#             result.append((i - j, i - 1))
#             j = lps_arr[j - 1]
#         elif i < n and pat[j] != text[i]:  # Corrected indexing
#             if j != 0:
#                 j = lps_arr[j - 1]
#             else:
#                 i += 1

#     return result

# # Input reading
# text = input().strip()
# pat = input().strip()

# # Finding pattern occurrences
# occurrences = kmp(text, pat)

# # Printing results
# for start, end in occurrences:
#     print(f"({start}, {end})")


# def max_operations(s):
#     n = len(s)
#     memo = {}

#     def dfs(sub_s):
#         if sub_s in memo:
#             return memo[sub_s]
#         if not sub_s:
#             return 0
        
#         max_ops = 1  # Base case: delete the whole string in one operation
        
#         for i in range(1, len(sub_s) // 2 + 1):
#             if sub_s[:i] == sub_s[i:2*i]:
#                 new_s = sub_s[2*i:]
#                 max_ops = max(max_ops, 1 + dfs(new_s))
        
#         memo[sub_s] = max_ops
#         return max_ops

#     return dfs(s)

# # Example usage:
# s = "AAABAAB"
# print(max_operations(s))  # Output: 2



# def deleteString( S):
#     N = len(S)
#     if S.count(S[0]) == N: return N
#     P = [0] * (N + 1)
#     dp = [1] * N
#     for i in range(N - 1, -1, -1):
#         for j in range(i + 1, N):
#             P[j] = P[j + 1] + 1 if S[i] == S[j] else 0
#             if P[j] >= j - i:
#                 dp[i] = max(dp[i], dp[j] + 1)
#     return dp[0]
# print(deleteString('aaabaab'))


# def longest_bitonic_subarray(arr):
#     n = len(arr)
#     if n == 0:
#         return 0, []

#     # Arrays to store lengths of increasing and decreasing subsequences
#     inc = [1] * n
#     dec = [1] * n

#     # Fill the inc array
#     for i in range(1, n):
#         if arr[i] > arr[i - 1]:
#             inc[i] = inc[i - 1] + 1

#     # Fill the dec array
#     for i in range(n - 2, -1, -1):
#         if arr[i] > arr[i + 1]:
#             dec[i] = dec[i + 1] + 1

#     # Find the maximum length bitonic subarray
#     max_len = 0
#     start_index = 0
#     for i in range(n):
#         current_len = inc[i] + dec[i] - 1
#         if current_len > max_len:
#             max_len = current_len
#             start_index = i - inc[i] + 1

#     # Get the longest bitonic subarray
#     bitonic_subarray = arr[start_index:start_index + max_len]

#     return max_len, bitonic_subarray

# # Input handling
# N = int(input())
# arr = list(map(int, input().split()))

# # Function call and output
# length, subarray = longest_bitonic_subarray(arr)
# print(length)
# print(' '.join(map(str, subarray)))



# def find_last_contestant(n):
#     # Create a list of contestants from 1 to n
#     contestants = list(range(1, n + 1))
    
#     # Initialize the direction flag; True means left-to-right, False means right-to-left
#     direction_left_to_right = True
    
#     # Continue until only one contestant remains
#     while len(contestants) > 1:
#         if direction_left_to_right:
#             # Remove every alternate number starting from the left
#             contestants = contestants[1::2]
#         else:
#             # Remove every alternate number starting from the right
#             contestants = contestants[::-1][1::2][::-1]
        
#         # Toggle direction for the next round
#         direction_left_to_right = not direction_left_to_right
    
#     # Return the last remaining contestant
#     return contestants[0]

# # Example usage
# n = int(input("Enter the number of housemates: "))
# print("The house captain for this week is contestant number:", find_last_contestant(n))


# def max_height_difference(heights):
#     if len(heights) < 2:
#         return 0  # Not enough plants to compare
#     min_height = heights[0]
#     max_diff = 0
#     for height in heights[1:]:
#         if height - min_height > max_diff:
#             max_diff = height - min_height
#         if height < min_height:
#             min_height = height
#     return max_diff
# # Example usage
# heights = [8,2,4,6,10,12,8,14,20]
# result = max_height_difference(heights)
# print(f"The maximum height difference is: {result}")


arr=[8,7,6,3,8,7,6,3]
## first pass
p=0
n=1
count=0
while p<=len(arr)-2 and n<=len(arr)-1:
    if arr[p]<arr[n]:
        print(arr[p],arr[n])
        count+=1
        n+=1
        continue
    p=n
    n=n+1
print(count)