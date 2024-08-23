# ##Aggressive Cows


# testcases=int(input())
# for i in range(testcases):
#     n,c=map(int,input().split())
#     arr=[]
#     for i in range(n):
#         temp=int(input())
#         arr.append(temp)
#     arr.sort()
#     i=1
#     j=max(arr)
#     indx=0
#     def function(mid):
#         # total=0
#         count=1
#         lastpos=arr[0]
#         for i in range(1,len(arr)):
#             diff=arr[i]-lastpos
#             if diff>=mid:
#                 count+=1
#                 lastpos=arr[i]
#         return count>=c
#     while j>=i:
#         mid=(i+j)//2
#         if function(mid):
#             indx=i
#             i=mid+1
#         else:
#             j=mid-1
#     print(indx)


## Dynamic programming

## Climbing stairs
# total=[0]
# def climbing(n,count,total):
#     if count==n:
#         total[0]+=1
#         return
#     elif count>n:
#         return
#     for i in range(1,3):
#         climbing(n,count+i,total)
# climbing(3,0,total)
# print(total[0])

## Climbing stairs
# target = 5
# dp = {}
# def climb(count, target):
#     if count == target:
#         return 1
#     elif count > target:
#         return 0
#     if count in dp:
#         return dp[count]
#     lvl = 0
#     for i in range(1, 3):
#         lvl += climb(count + i, target)
#     dp[count] = lvl
#     return lvl
# print(climb(0, target))

arr=[2,1,4,9]
dp={}
def altcomb(arr,index,sumation):
    if index>len(arr)-1:
        return sumation
    if index in dp:
        return dp[index]
    l=altcomb(arr,index+2,sumation+arr[index])
    r=altcomb(arr,index+1,sumation)
    maximum=max(l,r)
    dp[index]=maximum
    return maximum
print(altcomb(arr,0,0))