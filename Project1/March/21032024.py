# count=0
# def printN(count):
#     if count<5:
#         return
#     print(count)
#     printN(count+1)

# printN(count)

## Backtracking
# def print0toN(count):
#     if count>=5:
#         print(count)
#         return
#     print0toN(count+1)
#     print(count)
# print0toN(0)


# print name 5 times

# def print5times(count):
#     if count>=5:
#         return
#     print("harshdeepsingh")
#     print5times(count+1)

# print5times(0)

##PRINT LINEARLY FROM 1 TO N

# def print1toN(count):
#     if count<=0:
#         return
#     print1toN(count-1)
#     print(count)

# print1toN(5)

## Sum of first5 numbers
# sum=0
# def sumoffirst5(n,sum):
#     if n>5:
#         print(sum)
#         return
#     sumoffirst5(n+1,sum+n)

# sumoffirst5(0,sum)

## SUm of first5 with backtracking

# def sumof5(n):
#     if 0>=n:
#         return 0
#     return sumof5(n-1)+n

# print(sumof5(5))

## REVERSE AN ARRAY

# arr  = [1,2,3,4,5,6,7,8]

# def arrayreverse(lenght,i):
#     if i>=lenght//2:
#         print(arr[i],arr[lenght-i-1])
#         arr[i],arr[lenght-i-1] = arr[lenght-i-1],arr[i]
#         print(arr)
#         return
#     arr[i],arr[lenght-i-1] = arr[lenght-i-1], arr[i]
#     arrayreverse(lenght,i+1)

# arrayreverse(len(arr),0)


## fIBBONACCHI

# def fibb(n):
#     if n==0 or n==1:
#         return n
#     return fibb(n-1)+fibb(n-2)

# print(fibb(10))

# Printing all the subsequences

arr = [1,2,3,4]

def printsub(result,i):
    if i>len(arr)-1:
        print(result)
        return
    result.append(i)
    printsub(result,i+1)
    result.pop()
    printsub(result,i+1)

printsub([],0)


##print subsequences having sum k

# arr = [1,2,3]
# target = 3
# def subsum(result,i,sum):
#     if sum==target:
#         print(result)
#         return
#     elif sum>target or i>len(arr)-1:
#         return
#     result.append(arr[i])
#     subsum(result,i+1,sum+arr[i])
#     result.pop()
#     subsum(result,i+1,sum)

# subsum([],0,0)


## Combinaiton sum
# array = [2, 3, 6, 7]
# target = 7
# result=[]
# def Conbinaitonsum(arr,i,sum):
#     if sum==target:
#         result.append(arr)
#     elif sum>target or i>len(array)-1:
#         return
#     arr.append(array[i])
#     Conbinaitonsum(arr,i,sum+array[i])
#     arr.pop()
#     Conbinaitonsum(arr,i+1,sum)
# print(result)
# return result

# Conbinaitonsum([],0,0)

# result = []
# array = [2, 3, 6, 7]
# target = 7

# def CombinationSum(arr, i, sum, target, result):
#     if sum == target:
#         result.append(arr.copy()) 
#     elif sum > target or i >= len(array):
#         return
#     arr.append(array[i])
#     CombinationSum(arr, i, sum + array[i], target, result)
#     arr.pop() 
#     CombinationSum(arr, i + 1, sum, target, result)

# CombinationSum([], 0, 0, target, result)
# print(result)


# def CombinationSum(arr, i, sum, target, result):
#     if sum == target:
#         result.append(arr.copy())  # Append a copy of the current combination to the result list
#     elif sum < target:
#         # Include the current element in the combination and recursively explore further combinations
#         arr.append(array[i])
#         CombinationSum(arr, i, sum + array[i], target, result)
#         arr.pop()  # Backtrack by removing the last element from the combination
#         # Move to the next element and recursively explore combinations
#         CombinationSum(arr, i + 1, sum, target, result)

# # Initialize the result list
# result = []
# # Sample array and target sum (you need to define these)
# array = [2, 3, 6, 7]
# target = 7
# # Call the function with initial parameters
# CombinationSum([], 0, 0, target, result)
# # Print the result after the function has been called
# print(result)
