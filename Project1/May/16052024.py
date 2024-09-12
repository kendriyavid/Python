# arr=[5,7,7,8,8,10]
# target=6
# i=0
# j=len(arr)-1
# prev=len(arr)-1
# while i<=j:
#     mid=(i+j)//2
#     if arr[mid]>=target:
#         if arr[mid]==target:
#             prev=mid
#         j=mid-1
#     else:
#         i=mid+1
# print(prev)

## Upper bound

# arr=[0,3,5,9,12]
# i=0
# j=len(arr)-1
# target=10
# prev=0
# while i<=j:
#     mid=(i+j)//2
#     if arr[mid]>target:
#         prev=mid
#         print(prev)
#         j=mid-1
#     else:
#         i=mid+1
# # if arr[prev-1] !=target:
# #     prev=-1
# print(prev)

# arr=[True,True,True,True,False,False,False,False,False]
# i=0
# j=len(arr)-1
# indx=0

##### FIRST FALSE (minimization)
# while i<=j:
#     mid=(i+j)//2
#     if arr[mid]:
#         i=mid+1
#     else:
#         indx=mid
#         j=mid-1
# print(indx)

##### FIRST TRUE (maximization)
# while i<=j:
#     mid=(i+j)//2
#     if arr[mid]:
#         indx=mid
#         j=mid-1
#     else:
#         i=mid+1
# print(indx)

# arr=["x","x","y","y"]
# i=0
# j=len(arr)-1
# indx=0
# target='x'
# # while i<=j:
# #     mid=(i+j)//2
# #     if arr[mid]>target:
# #         indx=mid
# #         j=mid-1
# #     else:
# #         i=mid+1

# while i<=j:
#     mid=(i+j)//2
#     if arr[mid]<=target:
#         i=mid+1
#     else:
#         indx=mid
#         j=mid-1
# print(arr[indx])
# print(indx)
