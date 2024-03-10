## printing 1ton

# def oneton(x,z):
#     if x<=0:
#         return
#     print(z)
#     oneton(x-1,z+1)

# oneton(5,1)

## backtracking
# def oneton(x):
#     if x<=0:
#         print
# nums=[1,3,4]
# x = 0 
# for i in range(len(nums) - 1, 0, -1):  # Corrected range
#     print(nums[i],nums[i-1])
#     if nums[i] > nums[i - 1]:
#         x = i-1
#         break 
# print(x)

# ## finding bigger than x but smallest
# i = x
# min_index = i+1  # Changed variable name to min_index to avoid conflict with built-in function min()
# while i < len(nums):
#     if nums[x] < nums[i] < nums[min_index]:  # Corrected condition
#         min_index = i
#     i += 1  # Increment i within the loop
# # Swapping
# nums[x], nums[min_index] = nums[min_index], nums[x - 1]
# print(nums)
## Working on x

## Remove duplicates 1

# nums=[1, 1, 1, 2, 2, 3, 3, 4]
# z=1
# for i in range(len(nums)):
#     if nums[i]!=nums[z] and nums[i]!=nums[z-1]:
#         nums[i],nums[z] = nums[z],nums[i]
#         z=z+1
# print(nums)

## SLIDING WINDOWS

# arr = [7,1,5,9,3,6,4]
# i=0
# j = len(arr)-1
# max=-9999
# while i<j:
#     sum = arr[j]-arr[i]
#     if max<sum:
#         max = sum
#     elif arr[i]>arr[i+1]:
#         i = i+1
#     elif arr[j]<arr[j-1]:
#         j = j-1
#     elif arr[i]<arr[i+1] and arr[j]>arr[j-1]:
#         break

# print(max)

# arr = [7,1,5,3,6,4]
# i=0
# j=1
# max = -9999
# while i<j:
#     if j>=len(arr):
#         break
#     sum = arr[j]-arr[i]
#     if max<sum:
#         max =sum
#         print(max,arr[i],arr[j],)
#     if arr[j]<arr[i]:
#         i = j
#     j=j+1

# print(max)

# str = 'pwwkew'
# sets = set()
# i = 0
# j=0
# maximum = -1
# while j<len(s):
#     summation= j-i
#     print(i,j)
#     maximum = max(summation,maximum)
#     if s[j] in sets:
#         i = j
#         sets.clear()
#     else:
#         sets.add(s[j])
#         j = j+1

# print(maximum)

# arr = "AABABBA"
# k = 1
# i = 0
# maximum = 0
# for j in range(len(s)):
#     sumation = j-i+1
#     maximum = max(maximum,sumation)
#     if s[j]=="A":
#         continue
#     else:
#         if k>0:
#             k = k-1
#         else:
#             if s[i] == "B":
#                 k = k+1
#                 i = i+1
#             else:
#                 i =i+1
    

# print(maximum)
# s = "the sky is blue"

# arr=[]
# sub = []
# for i in range(len(s)):
    
#     if s[i]!=" ":
#         sub.append(s[i])
#         print(sub)
#     else:
#         arr.append(sub)
#         print(arr)
#         sub.clear()

# print(arr)

# s = "AABB"
# string = list(s)
# count = 0
# for i in range(len(string)-1):
#     if string[i]!=string[i+1]:
#         string[i],string[i+1] = string[i+1],string[i]
#         print(string)
#         count +=1

# print(count)

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
j=0
for i in range(len(arr)):
    if arr[i]==-1:
        continue
    else:
        if arr[arr[i]] == -1:
            
        print(arr[i],arr[arr[i]])
        arr[i], arr[arr[i]] = arr[arr[i]],arr[i]
        print(arr)
    
    
print(arr)