# #inputting the string
# string = string(input())
# #inputing the int values
# number = int(input())
# # inputting the array
# arr= list(map(int,input().split()))
# inputting a matrix
# height = int(input())
# width = int(input())
# mat = [[0]* width for _ in range(height)]
# print(mat)

## grid traversal , array problems standard, sorting algo
#string problem, recursion problems

# target = int(input())
# arr = list(map(int,input().split()))
# result=[]
# def combinationSum(i,arr,currsum,temp,target):
#     nonlocal result
#     if(i>=len(arr)):
#         return 
#     if(currsum==target):
#         result.append(temp)
#     ## not choosing
#     combinationSum(i+1,arr,currsum,temp)
#     ## choosing
#     if(currsum+arr[i]<=target):
#         temp.append(arr[i])
#         combinationSum(i+1,arr,currsum+arr[i],temp)
#         temp.pop()

## palindrome paritioning

# string = input()
# def isPal(string):
#     if string==string[::-1]:
#         return True
#     return False
# result=[]
# def palparting(string,start,temp):
#     nonlocal result
#     if start>=len(string):
#         result.append(temp)
#         return
#     for i in range(start,len(string)):
#         if(isPal(string[start:i+1])):
#             temp.append(string[start:i+1])
#         palparting(string,i+1,temp)
#         temp.pop()
# palparting(string,0,[])
# print(result)

# arr = list(map(int,input().split()))

# class Solution:
#     def __init__(self,arr):
#         self.arr = arr
#         self.result=[]
    
#     def subsetSum(self,start,temp):
#         self.result.append(temp[:])
#         for i in range(start, len(self.arr)):
#             temp.append(self.arr[i])
#             self.subsetSum(i+1,temp)
#             temp.pop()
# solution=  Solution(arr)
# solution.subsetSum(0,[])
# print(solution.result)


## ss2

# class Solution:
#     def __init__(self,arr):
#         self.arr = arr
#         arr.sort()
#         self.result = []
    
#     def subsetSum(self,start,temp):
#         self.result.append(temp[:])
#         for i in range(start,len(self.arr)):
#             if(i>start and self.arr[i] == self.arr[i-1]):
#                 continue
#             temp.append(self.arr[i])
#             self.subsetSum(i+1,temp)
#             temp.pop()

# arr = list(map(int,input().split()))
# solution = Solution(arr)
# solution.subsetSum(0,[])
# print(solution.result)

# class Solution:
#     def __init__(self,arr):
#         self.arr = arr
#         self.seti = set()
#         self.result =[]
    
#     def permutations(self,temp):
#         if start>len(self.result):
#             return 
#         if len(temp)==len(self.arr):
#             self.result.append(temp)
#             return 
#         for i in range(0,len(self.arr)):
#             if(self.arr[i] not in self.seti):        
#                 self.seti.add(self.arr[i])
#                 temp.append(self.arr[i])
#                 self.permutations(temp)
#                 temp.pop()
#                 self.seti.remove(self.arr[i])
    
## nqueens

# class Solution:
#     def __init__(self,n):
#         self.n = n
#         self.board =[[""]*n for _ in range(self.n)]
#         self.result=[]
#         self.positive = set()
#         self.negative = set()
#         self.vertical = set()
#     def nqueens(self,placed,j):
#         if(self.n==placed):
#             self.result.append(self.board.copy())
#             return
#         if(0>j or j>=self.n):
#             return
#         for i in range(self.n):
#             if(i not in self.vertical or i/j not in self.positive or i+j not in self.negative):
#                 self.board[j][i] = "Q"
#                 self.vertical.add(i)
#                 self.positive.add(i/j)
#                 self.negative.add(i+j)
#                 self.nqueens(placed+1,j+1)
#                 self.vertical.remove(i)
#                 self.positive.remove(i/j)
#                 self.negative.remove(i+j)
#                 self.board[j][i] = ""


### unique paths

# class Solution:
#     def __init__(self, n,m):
#         self.n = n
#         self.m =m
#         self.matrix = [[-1]*n for _ in range(self.m)]
#         self.paths=0
#         for i in range(self.n):
#             self.matrix[0][i]=1
#             self.matrix[i][0]=1
    
#     def paths(self,i,j):
#         if(0>i or 0>j or self.n<=i or self.m<=j):
#             return
#         if(i==self.n-1 and j == self.m-1):
#             self.paths+=1
#             return
#         if(self.matrix[j][i]!=-1):
#             return self.matrix[j][i]
#         ## moving down
#         l = self.paths(i,j-1)
#         ## moving left
#         r = self.paths(i-1,j)
#         self.matrix[j][i]=l+r
#         return self.matrix[j][i]

# arr1 = list(map(int,input().split()))
# arr2 = list(map(int,input().split()))
# dicti={}
# for i in range(len(arr1)):
#     dicti[arr2[i]] = arr1[i]

# arr2.sort()
# print(arr2)
# for i in range(len(arr1)):
#     arr2[i] = dicti[arr2[i]]

# print(arr2)
# result = list(zip(arr1,arr2))
# for i in range(len(arr1)):
#     print(result[i])

# dicti = {}
# for i in range(len(arr1)):
#     dicti[arr1[i]]  = arr2[i]


# print(dicti.items())

string = input()
lstring =list(string)
lstring.sort()
print("".join(lstring))