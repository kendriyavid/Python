#LOWER BOUND IMPLEMENTATION
# arr=[1,2,3,4,6,7,8,9]
# low=0
# high=len(arr)-1
# val=5
# while low<high:
#     ans=len(arr)
#     mid=int((low+high)/2)
#     if arr[mid]>=val:
#         high = mid-1
#         ans = mid
#     else:
#         low = mid+1
# print(ans)

## FIND ELEMENT IN SORTED ARRAY WITH DUPLICATES

# arr=[1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# low=0
# high = len(arr)-1
# ans=-1
# while high>low:
#     if arr[mid]==val:
#         ans = mid
#         while arr[mid]==val:
#             mid-=1
#             ans=mid
#         break
#     elif arr[mid]>val:
#         low = mid+1
#     elif arr[mid]<val:
#         high = mid-1

## LOWER BOUND is just bigger
# arr=[1,2,3,5,6,7,8,9]
# low=0
# val=4
# index=-1
# high=len(arr)-1
# while low<=high:
#     mid=int((low+high)/2)
#     if val>=arr[mid]:
#         index=mid
#         high=mid-1
#     else:
#         low=mid+1
# print(index)


## UPPER BOUND
# arr=[1,1,2,2,3,3,4,4]
# low=0
# high=len(arr)-1
# val=1
# index=-1
# while low<high:
#     mid=int((low+high)/2)
#     if arr[mid]>val:
#         index=mid
#         high=mid-1
#     elif arr[mid]<val:
#         low=mid+1
# print(index)

# arr=[13,8,1,5,2,5,9,7]
# res=[0]*len(arr)
# stack=[]
# for i in range(len(arr)-1,-1,-1):
#     while stack and stack[-1]<arr[i]:
#         stack.pop()
#     if not stack:
#         res[i]=-1
#     else:
#         res[i]=stack[-1]
#     stack.append(arr[i])

# print(res)

# nums=[1,2,1]
# res=[0]*len(nums)
# stack=[]
# for i in range(2*(len(nums))-1,-1,-1):
#     index = len(nums)%i
#     while stack and stack[-1]<=nums[index]:
#         stack.pop()
#     if not stack:
#         res[index] = -1
#     else:
#         res[index] = stack[-1]
#     stack.append(nums[index])
# print(res)

# while True:
#     line = input()
#     if input=="":
#         break
#     matrix.append(list(input.split()))

# arr=[2, 5, -1, 7, -3, -1, -2]
# ts=0
# k=4
# for i in range(len(arr)-k+1):
#     minimum = min(arr[i:i+k])
#     maximum = max(arr[i:i+k])
#     print(minimum+maximum)
#     ts=ts+minimum+maximum
# print(ts)

# nums=[1,1,1,2,2,3,3,3]
# z=2
# for i in range(2,len(nums)):
#     if nums[z-2] == nums[i]:
#         continue
#     else:
#         nums[z] = nums[i]
#         z+=1
# print(nums)

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)

# class Node:
#     def __init__(self,val,next=None):
#         self.val = val
#         self.next = next

# class LL:
#     def __init__(self):
#         self.head = None
#     def append(self,val):
#         if self.head==None:
#             self.head = Node(val)
#             return 
#         else:
#             curr = self.head
#             while curr.next!=None:
#                 curr = curr.next
#             curr.next = Node(val)
#             return
#     def traverse(self):
#         curr =self.head
#         while curr!=None:
#             print(curr.val)
#             curr = curr.next

# arr=list(map(int,input().split('-')))
# print(arr)
# nll = LL()
# for i in range(len(arr)):
#     nll.append(arr[i])
# nll.traverse()

## gcd

# def gcd(a,b):
#     if b==0:
#         return a
#     return gcd(b,a%b)

# def lcm(a,b):
#     greater = max(a,b)
#     while True:
#         if (greater%a==0) and (greater%b==0):
#             print(greater)
#             break
        
## decimal to hex conversion

# string='0123456789abcdef'
# number = int(input("enter the number: "))
# result=''
# while number>0:
#     rem = number%16
#     result+=str(string[rem])
#     number = int(number/16)


## DIV 4A (Short Sort)  
str='cab'
def Short(str):
    lstr=list(str)
    for i in range(len(str)):
        for j in range(len(str)):
            print(lstr)
            lstr[i],lstr[j]=lstr[j],lstr[i]
            print(lstr)
            nstr="".join(lstr)
            if nstr=='abc':
                return True
    return False
print(Short(str))

## GOOD KIDS

arr=[2,2,1,2]
minimum=0

