## Array reversal algorithm

# arr = [1,2,3,4,5,6,7,8,9]
# for i in range(len(arr)//2):
#     print(arr[i],arr[len(arr)-i-1])
#     arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i],arr[i]

# print(arr)


## array rotation k
# k=2
# arr=[1,2,3,4,5,6,7,8,9]
# arr.reverse()
# j=0
# l=k-1
# while (l>j):
#     arr[j],arr[l] = arr[l],arr[j]
#     j=j+1
#     l = l-1
# j =j+1
# l= len(arr)-1
# while(l>j):
#     arr[j],arr[l] = arr[l],arr[j]
#     j=j+1
#     l = l-1
# print(arr)

# printing the distinct element
# arr=[12, 10, 9, 45, 2, 10, 10, 45]
# hashset = set()
# for i in range(len(arr)):
#     if arr[i] in hashset:
#         continue
#     else:
#         hashset.add(arr[i])
# print(list(hashset))

# arr = [12, 10, 9, 45, 2, 10, 10, 45]
# ## selection sort

# for i in range(len(arr)):
#     maximum = i
#     for j in range(i+1,len(arr)):
#         if arr[j]>arr[maximum]:
#             maximum = j
#     arr[maximum],arr[i] = arr[i],arr[maximum]

# print(arr)
# j=0
# for i in range(len(arr)):
#     if arr[j]!=arr[i]:
#         arr[j],arr[i] = arr[i],arr[j]
#         j = j+1
#     else:
#         j = i
# print(arr)

# nums = [3,2,4]
# print(nums)
# target = 6
# x=0
# y=len(nums)-1
# while x<y:
#     if nums[x]+nums[y]>target:
#         y = y-1
#     elif nums[x]+nums[y]<target:
#         x =x+1
#     elif nums[x]+nums[y]==target:
#         print(nums[x]+nums[y])
#         print([x,y])
#         break

# arr=[1,3,2,4]
# target = 4
# j=0
# for i in range(len(arr),0,-1):
