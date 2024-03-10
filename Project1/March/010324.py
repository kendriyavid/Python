# bubble sorting

arr = [1,2,3,4,5,6,7,8,9]
lenght = len(arr)

# for i in range(lenght):
#     for j in range(0,lenght-1):
#         if arr[j]<arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
        
# print(arr)

# # printing 1ton

# def onetoN(x,y):
#     if y==x+1:
#         return
#     print(y)
#     onetoN(x,y+1)
# onetoN(11,1)

# # parameterized recursion

# def Ntoone(x):
#     if x==0:
#         return
#     print(x)
#     Ntoone(x-1)

# Ntoone(5)

# reversing the array using recursion

# def reversearray(arr,lenght,x):
#     if x>=lenght//2:
#         arr[x],arr[lenght-x-1] = arr[lenght-x-1],arr[x]
#         return arr
#     reversearray(arr,lenght,x+1)
#     arr[x],arr[lenght-x-1] = arr[lenght-x-1],arr[x]
#     return arr

# print(reversearray(arr,lenght,0))


# string = "abaaa"
# print(string)

# lambai = len(string)

# def checkPalindrome(string,lenght,x):
#     if x>=lenght//2:
#         return True
#     if string[x]!=string[lenght-x-1]:
#         return False
#     return checkPalindrome(string,lenght,x+1)

# print(checkPalindrome(string,lambai,0))

arr= [1,2,3,5,-1,6]
# def printsubsequence(arr,x,internalarray):
#     if x>=3:
#         print(internalarray)
#         return
#     internalarray.append(arr[x])
#     printsubsequence(arr,x+1,internalarray)
#     internalarray.pop()
#     printsubsequence(arr,x+1,internalarray)


# def psubsumk(arr,internalarray,x,target):
#     if x>=len(arr):
#         sum=0
#         for i in internalarray:
#             sum = sum+i
#         if sum == target:
#             print(internalarray)
#             return True
#         return False
#     internalarray.append(arr[x])
#     flag = psubsumk(arr,internalarray,x+1,target)
#     if flag:
#         return True
#     internalarray.pop()
#     flag = psubsumk(arr,internalarray,x+1,target)
#     if flag:
#         return True

# psubsumk(arr,[],0,5)


# arr=[1,2,3,6,7]
# target =5
# for j in range(len(arr)-1,0,-1):
#     sum=0
#     if target//arr[j]>0:
#         sum = (target//arr[j])*arr[j]
#         if sum == target:
#             print(sum,arr[j])
#         else:
#             for k in arr:
#                 sum = sum+k
#                 if target==sum:
#                     print(sum,k,arr[j],"her")


# arr = [1, 2, 3, 6, 7]
# target = 5

# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if arr[i] + arr[j] == target:
#             print(arr[i], arr[j])
                   

# def find_combinations(arr, target, current_sum, start_index, path):
#     if current_sum == target:
#         print(path)
#         return
#     if current_sum > target:
#         return

#     for i in range(start_index, len(arr)):
#         find_combinations(arr, target, current_sum + arr[i], i, path + [arr[i]])

# arr = [1, 2, 3, 6, 7]
# target = 5
# find_combinations(arr, target, 0, 0, [])

# def sumfinding(arr,target,internal,sum):
#     if sum == target:
#         print(internal)
#         return
#     elif sum>target:
#         return
#     for i in range(len(arr)):
#         sumfinding(arr,target,internal+[arr[i]],sum+arr[i])

# sumfinding(arr,5,[],0)

 
# def Sumfinding(arr,target,internal):
#         for i in arr:
#             sum=0
#             if target//i>0:
#                 for j in range(target//i):
#                     internal.append(i)
#                     sum = sum+i
#             print(internal)
#             if sum==target:
#                 break
#             else:
#                 for k in range(i+1,len(arr)):

# Sumfinding(arr,5,[])


# arr=[1,2,3]

# def printsumk(arr,k,sum,internal,target):
#     if k>=len(arr):
#         if sum==target:
#             print(internal)
#             return
#         return
#     # adding
#     internal.append(arr[k])
#     printsumk(arr,k+1,sum+arr[k],internal,target)
#     #removing
#     internal.pop()
#     printsumk(arr,k+1,sum,internal,target)

# printsumk(arr,0,0,[],5)


# def Sumcombination(result, candidates, x, total_sum, internal, target):
#     if x == len(candidates):
#         if total_sum == target:
#             result.append(internal[:])  # Append a copy of internal
#         return
#     if total_sum < target:
#         internal.append(candidates[x])
#         Sumcombination(result, candidates, x, total_sum + candidates[x], internal[:], target)  # Pass a copy of internal
#         internal.pop()
#         Sumcombination(result, candidates, x + 1, total_sum, internal[:], target)  # Pass a copy of internal

# result = []
# Sumcombination(result, [1, 2, 3, 4, 5], 0, 0, [], 5)
# print(result)

## Merge Sorting
# arr =[1,2,3,4,5,6,7,8,9,10 ]
# arr.reverse()
# def MergeSort(arr,i,j):
#     if i>=j:
#         print(i,j)
#     mid = (i+j)//2
#     MergeSort(arr,i,mid)
#     MergeSort(arr,mid+1,j)
# MergeSort(arr,0,len(arr)-1)
# print(arr)

# def Sumcombination(candidates,target,x,sum,internal,result):
#             if x==len(candidates):
#                 if sum ==target:
#                     result.append(internal)
#                     return
#             if sum<target:
#                 internal.append(candidates[x])
#                 print(internal)
#                 Sumcombination(candidates,target,x,sum+candidates[x],internal,result)
#                 internal.pop()
#                 Sumcombination(candidates,target,x+1,sum,internal,result)
# sum = 0
# internal=[]
# result = []
# candidates=[10,1,2,7,6,1,5]
# target = 8
# Sumcombination(candidates,target,0,sum,internal,result)

# print(result)

# def Sumcombination(candidates, target, x, sum, internal, result):
#     if x == len(candidates):
#         if sum == target:
#             result.append(internal[:])  # Append a copy of internal
#         return
#     if sum < target:
#         internal.append(candidates[x])
#         Sumcombination(candidates, target, x + 1, sum + candidates[x], internal, result)
#         internal.pop()
#         Sumcombination(candidates, target, x + 1, sum, internal, result)

# sum = 0
# internal = []
# result = []
# candidates = [10, 1, 2, 7, 6, 1, 5]
# target = 8
# Sumcombination(candidates, target, 0, sum, internal, result)
# print(result)

# s1=set()
# s1.add(1)
# print(s1)

# mod=5
# candidates = [10, 1, 2, 7, 6, 1, 5]
# hasharr=[0]*mod


# def hash(i,candidates,mod):
#     for i in range(len(candidates)):
#         return candidates[i]%mod
# for i in range(len(candidates)):
#     h = hash(i,candidates,mod)
#     hasharr[h] = hasharr[h]+1



# print(hasharr)


# def isAnagram(s, t):
#         s1 = atoi(s)
#         s2 = atoi(t)
#         s1.sort()
#         t.sort()
#         for i in range(len(s)):
#             if s1[i]==t[i]:
#                 continue
#             else:
#                 return False
#                 break
# s="anagram"
# t="nagaram"
# print(isAnagram(s, t))


class emp:
    def __init__ (self,init,ename):
        self.eid = eid
        self_ename = ename
    def display(self):
        print(self_eid)
        print(self_ename)

class dept(emp):
    def__init__(self,eid,ename,lname):
        super()__init__(eid,ename)
        sefl_dname  = sefl_dname
    def display (self):
        self_dname = dname
    
    def display(self):
        self_display()
        print(self_dname)

    