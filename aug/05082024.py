## Next Greater Element
# class solution:
#     def __init__(self,arr):
#         self.arr=arr
#         self.n=len(self.arr)
#         self.ansarr=[-1]*self.n
    
#     def ngr(self):
#         self.stack=[]
#         for i in range(self.n-1,-1,-1):
#             if self.stack and self.stack[-1]<=self.arr[i]:
#                 self.stack.pop()
#             if not stack:
#                 self.ansarr[i]=-1
#             else:
#                 self.ansarr[i]=self.stack[-1]
#             self.stack.append(self.arr[i])
#         return self.ansarr

## Next Smaller Element

# class Solution:
#     def __init__(self,arr):
#         self.arr=arr
#         self.n=len(self.arr)
#         self.ansarr=[-1]*self.n
    
#     def nsr(self):
#         self.stack=[]
#         for i in range(self.n-1,-1,-1):
#             while stack and stack[-1]>=self.arr[i]:
#                 self.stack.pop()
#             if not stack:
#                 self.ansarr[i]=-1
#             else:
#                 self.ansarr=self.stack[-1]
#             self.stack.append(self.arr[i])
#         return self.ansarr
    
## Previous Greater Element

# class solution:
#     def __init(self,arr):
#         self.arr=arr
#         self.n=len(self.arr)
#         self.ansarr=[-1]*self.n
    
#     def pgr(self):
#         self.stack=[]
#         for i in range(self.n):
#             while self.stack and self.stack[-1]>=self.arr[i]:
#                 self.stack.pop()
#             if not stack:
#                 self.ansarr[i]=-1
#             else:
#                 self.ansarr[i]=self.stack[-1]
#             self.stack.append(self.arr[i])
#         return self.ansarr


## Stock Span GFG

# class solution:
#     def __init__(self,arr):
#         self.arr=arr
#         self.n=len(self.arr)
#         self.spanarr=[1]*self.n
    
#     def stockSpan(self):
#         self.stack=[]
#         for i in range(self.n):
#             while self.stack and self.stack[-1][0]<=self.arr[i]:
#                 self.stack.pop()
#             if not self.stack:
#                 self.spanarr[i]=1
#             else:
#                 self.spanarr=abs(self.stack[-1][1]-i)
#             stack.append((self.arr[i],i))

#         return self.spanarr


## MINSTACK EXTRA SPACE

# class solution:
#     def __init__(self):
#         self.stack=[]
#         self.supportingstack=[]
    
#     def push(self,value):
#         self.stack.append(value)
#         if not self.supportingstack or value <= self.supportingstack[-1]:
#             self.supportingstack.append(value)
        
#     def pop(self):
#         if not self.stack and not self.supportingstack:
#             return -1
#         elif self.stack[-1]==self.supportingstack[-1]:
#             self.stack.pop()
#             self.supportingstack.pop()
#         else:
#             self.stack.pop()
    
#     def min(self):
#         if not self.supportingstack:
#             return -1
#         else:
#             return self.supportingstack[-1]

# s=solution()
# arr=[1,2,34,5,6,7,8,9]
# for i in range(len(arr)):
#     s.push(arr[i])
# print(s.min())


# arr=[100,80,60,70,60,75,85]
# stack=[]
# ansarr=[0]*len(arr)
# for i in range(len(arr)):
#     while stack and stack[-1][1]<=arr[i]:
#         stack.pop()
#     if not stack:
#         ansarr[i]=i+1
#     else:
#         ansarr[i]=i-stack[-1][0]
#     stack.append((i,arr[i]))
# print(ansarr)

# exp='(1+(4+5+2)-3)+(6+8)'
# def function(index):
#     stack=[]
#     val=0
#     while i<len(exp):
#         if exp[i]=='(':
#             val+=function(i+1)
#         if exp[i]==")":
#             return val+stack[0]
#         if exp[i] in integer:
#             stack.append(exp[i])
#         if exp[i] in ops:
#             ops=exp[i]
#             e1=stack.pop()
#             e2=exp[i+1]
#             if e2=="(":
#                 val+=function(i+1)
#                 if ops=="+":
#                     stack.append(int(e1)+int(e2))
#                 elif ops=='-':
#                     stack.append(int(e1)-int(e2))
#                 i+=1
#             else:
#                 if ops=="+":
#                     stack.append(int(e1)+int(e2))
#                 elif ops=='-':
#                     stack.append(int(e1)-int(e2))
#                 i+=1
#         i+=1
#     return val+stack[0]

# exp='(1+(4+5+2)-3)+(6+8)'
# sign=1
# result=0
# num=0
# stack=[]
# for i in (exp):
#     if i.isdigit():
#         num=(num*10)+int(i)
#     if i=="+":
#         result+=num*sign
#         num=0
#         sign=1
#     if i=="-":
#         result+=num*sign
#         num=0
#         sign=-1
#     if i=="(":
#         stack.append(result)
#         stack.append(sign)
#         result=0
#         sign=1
#         num=0
#     if i==")":
#         result+=num*sign
#         sign=stack.pop()
#         result*=sign
#         result+=stack.pop()
#     result+=num*sign
# return result


# exp = '(1+(4+5+2)-3)+(6+8)'
# sign = 1
# result = 0
# num = 0
# stack = []

# for i in exp:
#     if i.isdigit():
#         num = (num * 10) + int(i)
#     elif i == '+':
#         result += num * sign
#         num = 0
#         sign = 1
#     elif i == '-':
#         result += num * sign
#         num = 0
#         sign = -1
#     elif i == '(':
#         stack.append(result)
#         stack.append(sign)
#         result = 0
#         sign = 1
#     elif i == ')':
#         result += num * sign
#         num = 0
#         sign = stack.pop()
#         result = result * sign + stack.pop()
#     else:
#         # This should be an 'else' since we need to update result
#         result += num * sign
#         num = 0

# # Final addition to include the last number
# result += num * sign

# print(result)  # Output should be 23

### RPN 

# ["2","1","+","3","*"]  

# class solution:
#     def __init__(self,exp):
#         self.exp=exp
#         # self.n=len(self.exp)
    
#     def eval(self):
#         self.stack=[]
#         for token in self.exp:
#             if token.isdigit():
#                 self.stack.append(int(token))
#             elif token=="+":
#                 e1=self.stack.pop()
#                 e2=self.stack.pop()
#                 self.stack.append(e1+e2)
#             elif token=='-':
#                 e1=self.stack.pop()
#                 e2=self.stack.pop()
#                 self.stack.append(e1-e2)
#             elif token=='*':
#                 e1=self.stack.pop()
#                 e2=self.stack.pop()
#                 self.stack.append(e1*e2)
#             elif token=='/':
#                 e1=self.stack.pop()
#                 e2=self.stack.pop()
#                 self.stack.append(e1/e2)
#         print(self.stack[0])

# s=solution(exp=["2","1","+","3","*"])
# s.eval()

# class solution:
#     def __init__(self,path):
#         self.path=path
    
#     def simplify(self):
#         modpath=self.path.split('/')
#         stack=[]
#         for comp in modpath:
#             if comp=="":
#                 continue
#             elif comp=="..":
#                 stack.pop()
#             else:
#                 stack.append(comp)
#         anspath='/'.join(stack)
#         print(anspath)

# s=solution(path='/home/user/Documents/../Pictures')
# s.simplify()

# class solution:
#     def __init__(self,push,pop):
#         self.push=push
#         self.pop=pop
#     def validate(self):
#         stack=[]
#         i=0 # push
#         j=0 # pop
#         while i<len(push) or (stack or stack[-1]==pop[j]):
#             if stack and  stack[-1]==pop[j]:
#                 stack.pop()
#                 j+=1
#                 if j>=len(pop):
#                     break
#             if i<len(push):
#                 stack.append(push[i])
#                 i+=1
            
#         return i>=len(push) and j>=len(pop) and not stack
        
# asteroid=[5,10,-5]
# stack=[]
# for ass in asteroid:
#     while stack and ((stack[-1]>0 and ass<0) or (stack[-1]<0 and ass>0)):
#         if abs(ass)==abs(stack[-1]):
#             stack.pop()
#             break
#         elif abs(ass)>abs(stack[-1]):
#             stack.pop()
#         elif abs(ass)<abs(stack[-1]):
#             break
#     stack.append(ass)
# print(stack)

## Dynamic Programming Knapsack

# weight=[1,2,4,5]
# value=[5,4,8,6]
# n=4
# W=5
# dp=[[-1]*(n+1) for _ in range(W+1)]

# def function(weight,value,W,index):
#     if W<0:
#         return 0
#     if index<0:
#         return 0
#     if dp[index][W]!=-1:
#         return dp[index][W]
#     l=value[index-1]+function(weight,value,W-weight[index-1],index-1)
#     r=function(weight,value,W,index-1)
#     dp[index][W]=max(l,r)
#     return dp[index][W]


# def knapsack(weight, value, W, index):
#     if W == 0 or index == 0:
#         return 0

#     if dp[index][W] != -1:
#         return dp[index][W]

#     if weight[index-1] <= W:
#         l = value[index-1] + knapsack(weight, value, W - weight[index-1], index-1)
#         r = knapsack(weight, value, W, index-1)
#         dp[index][W] = max(l, r)
#     else:
#         dp[index][W] = knapsack(weight, value, W, index-1)

#     return dp[index][W]

# # Initialize the dp array
# dp = [[-1]*(W+1) for _ in range(n+1)]

# # Call the knapsack function
# max_value = knapsack(weight, value, W, n)
# print(max_value)

# n=4
# w=5
# weight=[1,2,4,5]
# value=[5,4,8,6]
# dp=[[-1]*(n+1) for _ in range(w+1)]

# def function(weight,value,idx,w):
#     if w<=0 or idx<=0:
#         return 0
#     if dp[idx][w]!=-1:
#         return dp[idx][w]
#     ## taking
#     if w<=weight[idx-1]:
#         l=value[idx-1]+function(weight,value,idx-1,w-weight[idx-1])
#         r=function(weight,value,idx-1,w)
#         dp[idx][w]=max(l,r)
#     else:
#         dp[idx][w]=function(weight,value,idx-1,w)
#     return dp[idx][w]

# for i in range(n+1):
#     dp[0][i]=0
# for j in range(w+1):
#     dp[i][0]=0

# for j in range(1,w+1):
#     for i in range(1,n+1):
#         if i<=weight[j-1]:
#             l=value[j-1]+dp[i-weight[j-1]][j+1]
#             r=dp[i][j-1]
#             dp[i][j]=max(l,r)
#         else:
#             dp[i][j]=dp[i][j+1]

# return dp[n][w]

# arr=[3,34,4,12,5,2]
# sum=9
# def function(index,sum):
#     if sum==0:
#         return True
#     if sum<0 or index<0:
#         return False
#     l=function(index-1,sum-arr[index])
#     r=function(index-1,sum)
#     return l or r

# dp=[[-1]*(len(arr)+1) for _ in range(10)]

# for i in range(10):
#     dp[i][0]=True

# for j in range(1,10):
#     for i in range(len(arr)+1):
#         l=dp[j-arr[i-1]][i-1]
#         r=dp[j][i-1]
#         dp[j][i]=l or r


# class solution:
#     def __init__(self,arr,target):
#         self.arr=arr
#         self.target=target
#         self.dp = [[-1] * (target + 1) for _ in range(len(arr) + 1)]
    
#     def eqsum(self,index,trgt):
#         if sum==0:
#             return True
#         if index<0 or trgt<0:
#             return False
#         if dp[index][trgt]!=-1:
#             return self.dp[index][trgt]
#         if trgt<=self.arr[index]:
#             # take
#             l= self.eqsum(index-1,trgt-self.arr[index])
#             r=self.eqsum(index-1,trgt)
#             ans=l or r
#         else:
#             ans= self.eqsum(index-1,trgt)
#         self.dp[index][trgt]=ans
#         return self.dp[index][trgt]
    
#     def equalSum(self):
#         if self.target%2!=0:
#             return False
#         else:
#             return self.eqsum((len(self.arr)-1),self.target//2)


## Tabulation of equal sum partition

# class solution:
#     def __init__(self,arr,target):
#         self.target=target
#         self.arr=arr
    
#     def eqsum(self,arr,trgt):
#         self.dp=[[-1]*(trgt+1) for _ in range(len(arr)+1)]
#         ## initialization
#         for i in range(len(self.arr)+1):
#             self.dp[0][i]=True
        
#         for j in range(1,trgt+1):
#             self.dp[i][0]=False

#         for j in range(1,(len(self.arr)+1)):
#             for i in range(1,trgt+1):
#                 if i<=self.arr[j-1]:
#                     l=dp[j-1][i-self.arr[j-1]]
#                     r=dp[j-1][i]
#                     ans=l or r
#                 else:
#                     ans=dp[j-1][i]
#                 dp[j][i]=ans

#     def EqualSumpartition(self,arr,target):
#         if target%2!=0:
#             return False
#         else:
#             return self.eqsum(arr,target//2)


## Count Subsets with sum k

# class solution:
#     def __init__(self,arr,target):
#         self.arr=arr
#         self.target=target
#         self.dp=[[-1]*(target+1) for _ in range(len(self.arr)+1)]
    
#     def numsubsets(self,index,target):
#         if target==0:
#             return 1
#         if target<0 or index<0:
#             return 0
#         if self.dp[index][target]!=-1:
#             return self.dp[index][target]
#         # cantake
#         if self.arr[index]<=target:
#             l=self.numsubsets(index-1,target-self.arr[index])
#             r=self.numsubsets(index-1,target)
#             ans = l+r
#         else:
#             ans=self.numsubsets(index-1,target)
#         self.dp[index][target]=ans
#         return self.dp[index][target]

        
# class solution:
#     def __init__(self,arr,target):
#         self.arr=arr
#         self.target=target
#         self.dp=[[-1]*(target+1) for _ in range(len(self.arr)+1)]
        
#     def numsubsets(self):
#         ## initialization
#         for j in range(len(self.arr)+1):
#             self.dp[j][0]=1
#         for i in range(1,self.target+1):
#             self.dp[0][i]=0
        
#         for j in range(1,len(self.arr)+1):
#             for i in range(1,self.target+1):
#                 if self.arr[j-1]<=i:
#                     l=self.dp[j-1][i-self.arr[j-1]]
#                     r=self.dp[j-1][i]
#                     self.dp[j][i]=l+r
#                 else:
#                     self.dp[j][i]=self.dp[j-1][i]
#         return self.dp[len(self.arr)][self.target]


## MInimum number of subset difference

# class solution:
#     def __init__(self,arr,diff):
#         self.arr=arr
#         self.total=sum(self.arr)
#         self.dp=[[False]*(len(self.arr)+1) for _ in range(self.total+1)]
#         self.initialization()
#         self.diff=diff
    
#     def initialization(self):
#         for i in range(len(self.arr)+1):
#             self.dp[i][0]=True
        
#         for j in range(len(self.arr)+1):
#             for i in range(self.total+1):
#                 if self.arr[j-1]<=i:
#                     l=self.dp[j-1][i-self.arr[j-1]]
#                     r=self.dp[j-1][i]
#                     self.dp[j][i]=l or r
#                 else:
#                     self.dp[j][i]=self.dp[j-1][i]
    
#     def calculation(self,value):
#         return ((2*value )- self.total) == self.diff
    
#     def countdiffsubset(self,arr):
#         count=0
#         for i in range(self.target+1):
#             if self.calculation(i):
#                 count+=1
#         return count

        
## Target Sum
# class solution:
#     def __init__(self,arr,target):
#         self.arr=arr
#         self.target=target
    
#     def function(self,target,index):
#         if target==0 and index<0:
#             return 1
#         if target<0 or index<0:
#             return 0
#         l=function(target+self.arr[index],index-1)
#         r=function(target-self.arr[index],index-1)
#         return l+r
    

# class solution:
#     def __init__(self,arr,target):
#         self.arr=arr
#         self.target=target
#         self.dp=[[-1]*(self.target+1) for _ in range(len(self.arr)+1)]
    
#     def targetsum(self):
#         for j in range(len(self.arr)+1):
#             self.dp[j][0]=1
        
#         for j in range(1,len(self.arr)+1):
#             for i in range(1,self.target+1):
#                 l=dp[j-1][i+self.arr[j-1]]
#                 r=dp[j-1][i-self.arr[j-1]]
#                 dp[j][i]=l+r
#         return dp[self.target][len(self.arr)]

# class Solution:
#     def __init__(self, arr,diff):
#         self.arr = arr
#         self.total = sum(self.arr)
#         self.dp = [[False] * (self.total + 1) for _ in range(len(self.arr) + 1)]
#         self.initialization()
#         self.diff=diff

#     def initialization(self):
#         for j in range(len(self.arr) + 1):
#             self.dp[j][0] = True
        
#         for j in range(1, len(self.arr) + 1):
#             for i in range(1, self.total + 1):
#                 if self.arr[j - 1] <= i:
#                     l = self.dp[j - 1][i - self.arr[j - 1]]
#                     r = self.dp[j - 1][i]
#                     self.dp[j][i] = l or r
#                 else:
#                     self.dp[j][i] = self.dp[j - 1][i]

#     def calculation(self, value):
#         return abs((2 * value) - self.total) == self.diff

#     def minimum_subset_sum(self):
#         count=0
#         for i in range(self.total // 2 + 1):
#             if self.calculation(i):
#                 count+=1
#         return count

# def function(index,l):
#     if l==0:
#         return 0
#     if index<0 or l<0:
#         return float-('inf')
    
#     ## take
#     l=price[index]+function(index,l-lenght[index])
#     r=function(index-1,l)
#     return max(l,r)