# # Palindrome Partitioning
# result=[]

# def ispal(s):
#     return s == s[::-1]

# def Palpart(result,arr,s,start):
#     string = "".join(arr)
#     if ispal(string):
#         if start < len(s):
#             result.append(arr[:])
#         else:
#             result.append(arr[:])
#             return
#     for i in range(start,len(s)):
#         arr.append(s[i])
#         Palpart(result,arr,s,i+1)
#         arr.pop()

# Palpart(result,[],"aac",0)
# print(result)


# def is_palindrome(s):
#     return s == s[::-1]

# def palindrome_partitions(s):
#     result = []

#     def generate_partitions(arr, start):
#         string = ''.join(arr)
#         if is_palindrome(string):
#             if start < len(s):
#                 result.append(arr[:])  # Append a copy of the partition to the result
#             else:
#                 result.append(arr[:])
#                 return
#         for i in range(start, len(s)):
#             arr.append(s[i])
#             generate_partitions(arr, i + 1)
#             arr.pop()

#     generate_partitions([], 0)
#     return result

# # Test the palindrome_partitions function
# input_string = "aac"
# partitions = palindrome_partitions(input_string)
# print(partitions)


#REMOVING DUPLICATES
# arr=[1,1,1,2,2,3]
# i=1
# for j in range(1,len(arr)):
#     if arr[j]==arr[j-1]:
#         continue
#     else:
#         arr[i]=arr[j]
#         i+=1
# print(arr)

## REMOVE DUPLICATES 2
# arr=[1,1,1,2,2,2,3,3,3]
# i=2
# for j in range(2,len(arr)):
#     if arr[j] == arr[j-1]:
#         continue
#     else:
#         arr[i] = arr[j]
#         if arr[i]==arr[i+1]:
#             i+=2
#         else:
#             i+=1

# print(arr[:i+1])

# def rotate( nums, k):
#     for i in range(len(nums)//2):
#         nums[i],nums[len(nums)-1-i] = nums[len(nums)-1-i],nums[i]
#     print(nums)
#     i=0
#     j=k-1
#     while j>i:
#         nums[j],nums[i] = nums[i],nums[j]
#         j=-1
#         i=+1
#     print("midway",nums)
#     j = k
#     i=len(nums)-1
#     while i>j:
#         nums[j],nums[i] = nums[i],nums[j]
#         i=-1
#         j=+1
#     print("here",nums)

# rotate([1,2,3,4,5,6,7],3)
#CYCLIC SORTING
# arr = [5, 4, 3, 2, 1,0]
# i = 0
# while i < len(arr):
#     if arr[i] != i :
#         # Swap arr[i] with arr[arr[i] - 1]
#         temp = arr[i]
#         arr[i] = arr[temp ]
#         arr[temp] = temp
#     else:
#         i += 1

# print(arr)


#LONGEST SUBSTRING WITH ATLEASE K REPEATING CHARS
