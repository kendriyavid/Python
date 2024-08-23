# arr = [2,7,10,11]
# dicti = {}
# target = 17
# for i in range(len(arr)):
#     val = target-arr[i]
#     if arr[i] in dicti:
#         print(i,dicti[arr[i]])
#         break
#     else:
#         dicti[val] = i

# print(dicti)

## Remove duplicates

arr= [1,1,1,2,2,3]
# arr.sort()
# print(arr)
# z=1
# j = len(arr)
# count = 0
# for i in range(1,len(arr)):
#     if arr[i] ==arr[i-1]:
#         count+=1
#         continue
#     elif arr[i]!=arr[i-1]:
#         arr[z] = arr[i]
#         z+=1
# print(arr)

# i = 1
# count = 1
# for j in range(len(arr)):
#     if count<2:
#         if arr[j] == arr[j-1]:
#             count+=1
#         else:
#             arr[i] = arr[j]
#             i+=1
#     else:
#         if arr[i] == arr[i-1]:
#             continue
#         else:
#             arr[i]  = arr[j]
#             i+=1
# print(arr)


# Removing duplicates

arr=[1,1,1,1,2,2,2,3]
# j=1
# for i in range(1,len(arr)):
#     if arr[i-1] == arr[i]:
#         continue
#     elif arr[i-1] !=arr[i]:
#         arr[j] = arr[i]
#         j+=1
    

## Removing duplicates 2
# count = 1
# slow=0
# for i in range(1, len(arr)):
#     if count < 2:
#         if arr[slow] == arr[i]:
#             count += 1
#             slow += 1
#         else:
#             count = 1
#             slow += 1
#             arr[slow] = arr[i]
#     else:
#         if arr[slow] == arr[i]:
#             count += 1
#         else:
#             slow += 1
#             arr[slow] = arr[i]
#             count = 1

# print(arr)
nums = [4,3,2,7,8,2,3,1]
n = len(nums)
i = 0
result = []

# Cyclic sort to rearrange the numbers
while i < n:
    if nums[i] < n and nums[i] != nums[nums[i]-1]:
        nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    else:
        i += 1

# Iterate through the sorted array to find disappeared numbers
for i in range(n):
    if nums[i]-1 != i:
        result.append(i)

print(result)