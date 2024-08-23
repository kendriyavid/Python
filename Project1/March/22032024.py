# # result = []
# # array = [2,3,5,7]
# # target = 7
# # def CS(result,array,arr,sum,i,target):
# #     if target == sum:
# #         result.append(arr)
# #         return
# #     if i>len(array)-1 or sum>target:
# #         return
# #     arr.append(array[i])
# #     CS(result,array,arr,sum+array[i],i)
# #     if i+1>len(array)-1:
# #         return
# #     arr.pop()
# #     CS(result,array,arr,sum,i+1)

# # CS(result,array,[],0,0,target)
# # print(result)

# result = []
# array = [2, 3, 5, 7]
# target = 7

# def CS(result, candidates, arr, current_sum, i, target):
#     if target == current_sum:
#         result.append(arr.copy())  
#         return
#     if i > len(candidates) - 1 or current_sum > target:
#         return
#     arr.append(candidates[i])
#     CS(result, candidates, arr, current_sum + candidates[i], i, target)
#     arr.pop()
#     CS(result, candidates, arr, current_sum, i + 1, target)

# CS(result, array, [], 0, 0, target)
# print(result)

# def CS(result,candidatess,target,sum,i,arr):
#     if target ==sum:
#         result.append(arr.copy())
#         return
#     elif i>len(nums)-1 or sum>target:
#         return
#     arr.append(candidates[i])
#     CS(result,candidates,target,sum+candidates[i],i,arr)
#     arr.pop()
#     CS(result,candidates,target,sum,i+1,arr)
# return result


# result=[]
# array = [2,3,5]
# def CS(result,arr,target,sum,start,array):
#     if target==sum:
#         print(arr)
#         return
#     elif target<sum:
#         return

#     for j in range(start,len(array)):
#         arr.append(array[j])
#         CS(result,arr,target,sum+array[j],j+1,array) ## j+1 for not repeating the current element
#         arr.pop()

# CS(result,[],5,0,0,array)
# print(result)


# Subset sum 1

# result =set()
# def SS(result,array,sum,i):
#     if i>len(array)-1:
#         result.add(sum)
#         return
#     SS(result,array,sum+array[i],i+1)
#     SS(result,array,sum,i+1)

# SS(result,[1,2],0,0)
# list(result).sort()
# print(result)

# Subset sum 1 using forloop recursion

# result = []
# array = [1,2,2]
# def CS11(result,array,arr,start):
#     result.append(arr[:])
#     for i in range(start,len(array)):
#         if array[i]==array[i-1]:
#             continue
#         arr.append(array[i])
#         CS11(result,array,arr,i+1)
#         arr.pop()

# CS11(result,array,[],0)
# print(result)


# result = set()

# def CS11(result, array, arr, start):
#     if start >= len(array):  # Include the case where start equals len(array) for the empty subset
#         result.add(tuple(arr[:]))
#         return
#     arr.append(array[start])
#     CS11(result, array, arr, start + 1)  # Include the current element and move to the next index
#     arr.pop()  # Backtrack and exclude the current element
#     CS11(result, array, arr, start + 1)  # Exclude the current element and move to the next index

# CS11(result, [1, 2,2], [], 0)
# print(result)


# result = []

# def CS11(result, array, arr, start):
#     result.append(arr[:])  # Append a copy of arr to result
#     for i in range(start, len(array)):
#         if i > start and array[i] == array[i - 1]:
#             continue  # Skip duplicates
#         arr.append(array[i])
#         CS11(result, array, arr, i + 1)
#         arr.pop()

# array = [1, 2]
# array.sort()  # Sort the input array
# CS11(result, array, [], 0)
# print(result)


# # Binary strings with no consecutive 1s
# result = []
# def binarystrings(result,arr,n,f):
#     if n==4:
#         result.append(''.join(map(str, arr)))
#         return
#     arr.append(0)
#     binarystrings(result,arr,n+1,False)
#     arr.pop()
#     if not arr or arr[-1]==0:
#         arr.append(1)
#         binarystrings(result,arr,n+1,True)
#         arr.pop()
# binarystrings(result,[],0,False)
# print(result)


# result = []
# def binarystrings(result,arr,n,f):
#     if n==4:
#         result.append(''.join(map(str, arr)))
#         return
#     arr.append(0)
#     binarystrings(result,arr,n+1,False)
#     arr.pop()
#     if f==False:
#         arr.append(1)
#         binarystrings(result,arr,n+1,True)
#         arr.pop()
# binarystrings(result,[],0,False)
# print(result)

# result = []

# def binarystrings(result, arr, n):
#     if n == 4:
#         result.append(''.join(map(str, arr)))  # Join the list of integers to form a binary string
#         return
#     arr.append(0)
#     binarystrings(result, arr, n + 1)
#     arr.pop()
#     if not arr or arr[-1] == 0:  # Add 1 only if the last digit is 0 or the list is empty
#         arr.append(1)
#         binarystrings(result, arr, n + 1)
#         arr.pop()

# binarystrings(result, [], 0)
# for binary in result:
#     print(binary)


# result=[]
# def Combinations(result,arr,n,k):
#     if len(arr)==k:
#         print(len(arr))
#         result.append(arr[:])
#         return
#     if n<=0 or k<=0:
#         return
#     arr.append(n)
#     Combinations(result,arr,n-1,k)
#     arr.pop()
#     Combinations(result,arr,n-1,k)
# Combinations(result,[],4,2)
# print(result)

