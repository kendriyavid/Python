## printing name 5 times

# def print5times(x):
#     if x<=0:
#         return
#     print("harshdeep")
#     print5times(x-1)

# print5times(5)

### Printing 1 to N

# def print1N(x,p):
#     if p>x:
#         return
#     print(p)
#     print1N(x,p+1)

# print1N(5,1)

# def printnto1(x):
#     if x<=0:
#         return
#     print(x)
#     printnto1(x-1)

# printnto1(5)

## print 1ton Backtrack

# def print1Back(x):
#     if x<=0:
#         return
#     print1Back(x-1)
#     print(x)

# print1Back(5)

## print nto1 Backtrack

# def printnBacktrack(x,p):
#     if p>x:
#         return
#     print(p)
#     printnBacktrack(x,p+1)
# printnBacktrack(5,1)

## sum of first n numbers parameterized and recursive

# def sumnpara(n,sum,i):
#     if i>n:
#         print(sum)
#         return
#     sumnpara(n,sum+i,i+1)

# sumnpara(10,0,0)

## sum of first n numbers functioal

# def sumnfunctional(n):
#     if n<=0:
#         return 0 
#     return sumnfunctional(n-1) + n

# print(sumnfunctional(10))


## multiplication of first n numbers parameterized

# def mulnpara(n,mul,i):
#     if i>n:
#         print(mul)
#         return
#     mulnpara(n,mul*i,i+1)    

# mulnpara(10,1,1)


## multiplication of firsr n numbers functional

# def mulnfunctional(n):
#     if n<=1:
#         return 1
#     return mulnfunctional(n-1)*n

# print(mulnfunctional(10))


## recursive array reversal

# def recursivearray(arr,i):
#     if i>len(arr)//2:
#         print(arr)
#         return
#     print(arr[i],arr[len(arr)-i-1])
#     arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
#     recursivearray(arr,i+1)

# 
# recursivearray(arr,0)

## 2 pintes

# def recursivearray(arr,i,j):
#     if i>=j:
#         print(arr)
#         return
#     arr[i],arr[j] = arr[j],arr[i]
#     recursivearray(arr,i+1,j-1)

# arr=[1,2,3,4,5,6,7]
# recursivearray(arr,0,len(arr)-1)


# string = "aabbaa"
# def recursivepal(string,i):
#     if i>=len(string)//2:
#         return True
#     if string[i]!=string[len(string)-1-i]:
#         return False
#     return recursivepal(string,i+1)

# print(recursivepal(string,0))


## Fibbonacchi recursion
# def fibb(n):
#     if n<=1:
#         return n
#     return fibb(n-1)+fibb(n-2)

# print(fibb(9))

# arr=[1,2,3]
# def printsuseq(i,arr,mid):
#     if i>len(arr)-1:
#         print(mid)
#         return
#     mid.append(arr[i])
#     printsuseq(i+1,arr,mid)
#     mid.pop()
#     printsuseq(i+1,arr,mid)

# printsuseq(0,arr,[])

## for looping version

# def subseq(arr,result,start):
#     print(result)
#     for i in range(start,len(arr)):
#         result.append((arr[i]))
#         subseq(arr,result,i+1)
#         result.pop()
    
# subseq([1,2,3],[],0)

## Having sum k


# def subseqsumk(arr,result,k,sum,mid,i):
#     if sum==k:
#         result.append(mid[:])
#         return
#     elif sum>k:
#         return
#     if i>=len(arr):
#         return
#     mid.append(arr[i])
#     subseqsumk(arr,result,k,sum+arr[i],mid,i+1)
#     mid.pop()
#     subseqsumk(arr,result,k,sum,mid,i+1)
# result = []
# subseqsumk([1,2,3,4,5],result,5,0,[],0)
# print(result)

# def subseqsumk(arr,result,start,k,sum,mid):
#     if sum==k:
#         result.append(mid[:])
#         return
#     elif sum>k:
#         return
#     for i in range(start,len(arr)):
#         mid.append(arr[i])
#         subseqsumk(arr,result,i+1,k,sum+arr[i],mid)
#         mid.pop()
# result = []
# subseqsumk([1,2,3,4,5],result,0,5,0,[])
# print(result)

## Subsetsum

# arr=[1,2,3,4,5]
# result=[]
# def subset(sum,i,result,arr):
#     if i==len(arr):
#         result.append(sum)
#         return
#     subset(sum+arr[i],i+1,result,arr)
#     subset(sum,i+1,result,arr)
# subset(0,0,result,arr)
# print(result)

# arr=[1,2,3]
# result=[]

# def permutations(arr,mid,result,map):
#     if len(arr)==len(mid):
#         result.append(mid[:])
#         return
#     for i in range(0,len(arr)):
#         if map[i] == 1:
#             continue
#         mid.append(arr[i])
#         map[i]=1
#         permutations(arr,mid,result,map)
#         mid.pop()
#         map[i]=0

# permutations(arr,[],result,[0,0,0])
# print(result)

## PALINDROME PARTITIONINIG
# string='aabb'
# result=[]
# def ispal(s,i,j):
#     while i<j:
#         if s[i]!=s[j]:
#             return False
#         i+=1
#         j-=1
#     return True

        
# def palpart(s,result,start,mid):
#     if start==len(s):
#         result.append(mid[:])
#         return
#     for i in range(start,len(s)):
#         if ispal(s,start,i):
#             mid.append(s[start:i+1])
#             palpart(s,result,i+1,mid)
#             mid.pop()
# palpart(string,result,0,[])
# print(result)

## WORD BREAK
# string='leetcode'
# wordDict = ["leet","code"]
# def wordbreak(string,wordDict,start):
#     if start==len(string):
#         return True
#     for i in range(start,len(string)):
#         if string[start:i+1] in wordDict:
#             if wordbreak(string,wordDict,i+1):
#                 return True
#     return False

# print(wordbreak(string,wordDict,0))


## Factor combinations
# result=[]
# def fc(mid,result,start,product,n):
#     if product==n:
#         result.append(mid[:])
#         return
#     for i in range(start,n):
#         mid.append(i)
#         fc(mid,result,start,product*i,n)
#         mid.pop()

# fc([],result,2,1,8)

## String splitting
# string="ababccc"
# def maxstringSplitting(string,start,mid,count):
#     if start==len(string):
#         count = max(count,len(mid))
#         return
#     for i in range(start,len(string)):
#         if string[start:i+1] not in mid:
#             mid.append(string[start:i])
#             maxstringSplitting(string,i,mid,count)
#             mid.pop()


# def max_string_splitting(string):
#     def helper(start, mid, count):
#         if start == len(string):
#             return max(count, len(mid))  # Return the updated count
#         max_count = count  # Initialize max_count to current count
#         for i in range(start + 1, len(string) + 1):  # Ensure complete substrings
#             substr = string[start:i]  # Correctly extract substring
#             if substr not in mid:  # Check if the substring is not already used
#                 mid.append(substr)  # Add new substring to the list
#                 new_count = helper(i, mid, count)  # Recursive call
#                 max_count = max(max_count, new_count)  # Update max_count with the return value
#                 mid.pop()  # Backtrack by removing the last added substring
#         return max_count  # Return the maximum count found in the recursive stack

#     return helper(0, [], 0)  # Initial call to helper with start = 0, empty list, and count = 0

# # Testing the function
# string = "ababccc"
# print(max_string_splitting(string))  # Example call to the function


# arr=[73,74,75,71,69,72,76,73]
# stack=[]
# result = [0]*len(arr)
# for i in range(len(arr)-1,-1,-1):
#     while stack and arr[i]>stack[-1]:
#         stack.pop()
#     if len(stack)==0:
#         result[i]=0
#     else:
#         result[i] = stack[-1]
#     stack.append(arr[i])

# print(result)


# arr=[13,18,1,5,2,5,9,7,6,12]
# result = [0]*len(arr)
# stack=[]
# for i in range(len(arr)-1,-1,-1):
#     while stack and stack[-1]>arr[i]:
#         stack.pop()
#     if not stack:
#         result[i]=0
#     else:
#         result[i] = stack[-1]
#     stack.append(arr[i])
# print(result)

# arr=[13,18,1,5,2,5,9,7,6,12]
# result = [0]*10
# stack=[]
# for i in range(0,len(arr)):
#     while stack and stack[-1]>arr[i]:
#         stack.pop()
#     if not stack:
#         result[i]=0
#     else:
#         result[i]=stack[-1]
#     stack.append(arr[i])

# print(result)


## NEXTGREATER STRICTLY INCREASING

# arr=[13,18,1,5,2,5,9,7,6,12]
# stack=[]
# result=[0]*len(arr)
# for i in range(len(arr)-1,-1,-1):
#     while stack and stack[-1]<=arr[i]:
#         stack.pop()
#     if not stack:
#         result[i]=-1
#     else:
#         result[i] = stack[-1]
#     stack.append(arr[i])

# print(result)


## Previous Greater
# arr=[13,18,1,5,2,5,9,7,6,12]
# result = [0]*len(arr)
# stack=[]
# for i in range(len(arr)):
#     while stack and stack[-1]<arr[i]:
#         stack.pop()
#     if not stack:
#         result[i] = -1
#     else:
#         result[i] = stack[-1]
#     stack.append(arr[i])
# print(result)

## Next greater circular

# arr=[1,2,1]
# result=[0]*len(arr)
# stack=[]
# for i in range(2*len(arr)-1,-1,-1):
#     while stack and stack[-1]<=arr[i%len(arr)]:
#         stack.pop()
#     if not stack:
#         result[i%len(arr)]=-1
#     else:
#         result[i%len(arr)] = stack[-1]
#     stack.append(arr[i%len(arr)])    
# print(result)

# num = 12
# strnum = list(str(num))
# stack=[]
# i=0
# while i<len(strnum):
#     if not stack:
#         stack.append(i)
#     if stack and stack[-1]>int(strnum[i]):
#         stack.append(i)
#     else:
#         break
# ## swapping
# strnum[stack[-1]],strnum[i] = strnum[i],strnum[stack[-1]]
# print(strnum[stack[-1]],strnum[i])
# print(int(''.join(strnum)))


# def next_greater_element(num):
#     strnum = list(str(num))
#     stack = []
#     i = len(strnum) - 1

#     # Find the first decreasing digit from the right
#     while i > 0 and strnum[i-1] >= strnum[i]:
#         i -= 1

#     if i == 0:  # If no decreasing element is found, no greater number can be formed
#         return num

#     # The pivot is at position i-1
#     pivot = i - 1

#     # Use the stack to find the smallest number greater than the pivot
#     stack.append(i)
#     i += 1
#     while i < len(strnum):
#         if strnum[i] > strnum[pivot]:
#             while stack and strnum[stack[-1]] >= strnum[i]:
#                 stack.pop()
#             stack.append(i)
#         i += 1

#     # Swap the pivot with the smallest number greater than the pivot
#     smallest = stack.pop()
#     strnum[pivot], strnum[smallest] = strnum[smallest], strnum[pivot]

#     # Reverse the part after the pivot
#     strnum = strnum[:pivot + 1] + sorted(strnum[pivot + 1:])

#     return int(''.join(strnum))

# # Test the function
# num = 12
# print(next_greater_element(num))

## passed 73 out of 107 testcases

# arr=[1,2,3,4]
# def one(arr):
#     stack=[]
#     for i in range(len(arr)):
#         print(stack)
#         while len(stack)>2 and arr[i]<stack[-1]:
#             return True
#         stack.append(arr[i])
#     return False
# print(one(arr))
    
# arr=[3, 1, 4, 2]
# def one(arr):
#     stack=[]
#     last = -111111
#     for i in range(len(arr)-1,-1,-1):
#         if last>arr[i]:
#             return True
#         while stack and stack[-1]<arr[i]:
#             last = stack.pop()
#         stack.append(arr[i])
        
#     return False
# print(one(arr))

## REMOVE K DIGITS
nums=112
ns = list(str(nums))
stack=[]
n=1
rem=0
for i in range(len(ns)):
    while stack and stack[-1]>ns[i] and rem<n:
        stack.pop()
        rem+=1
    stack.append(ns[i])
stack = stack[:len(stack)-rem]
nv = ''.join(stack)
print(int(nv))