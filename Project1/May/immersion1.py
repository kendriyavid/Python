## vanilla binary search

# arr=[1,2,3,4,5,6,7,8,9,10]
# i=0
# j=len(arr)-1
# target=9
# while i<=j:
#     mid=(i+j)//2
#     if arr[mid]==target:
#         print(mid)
#         break
#     elif arr[mid]>target:
#         j=mid-1
#     elif arr[mid]<target:
#         i=mid+1


# minimization

# arr=[1,2,3,4,5,6,7,8,9,10]
# i=0
# j=len(arr)-1
# indx=-1
# target=6
# while i<=j:
#     mid=(i+j)//2
#     if arr[mid]>=target:
#         indx=mid
#         j=mid-1
#     else:
#         i=mid+1
    
# print(indx)


# arr=[1,3,5,6]
# i=0
# j=len(arr)-1
# target=-1
# indx=len(arr)-1
# while i<=j:
#     mid=(i+j)//2
#     if arr[mid]>=target:
#         indx=mid
#         j=mid-1
#     else:
#         i=mid+1
# print(indx)

result=[]
nums=[1,2,3]
def subset(result,mid,i,nums):
    if i>=3:
        result.append(mid[:])
        print(result)
        return
    mid.append(nums[i])
    subset(result,mid,i+1,nums)
    mid.pop()
    subset(result,mid,i+1,nums)
subset(result,[],0,nums)
