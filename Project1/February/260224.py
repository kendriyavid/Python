# selection sort


# for i in range(lenght):
#     maximum = i
#     for j in range(i,lenght):
#         if arr[maximum]<arr[j]:
#             maximum = j
#         else:
#             continue
#     arr[maximum],arr[i] = arr[i],arr[maximum]

# print(arr)


## insertion sort


# for i in range(lenght):
#     for j in range(i,0,-1):
#         if arr[j]>arr[j-1]:
#             arr[j],arr[j-1]  = arr[j-1],arr[j]
#         else:
#             break

# print(arr)

## bubble sort

# for i in range(0,lenght):
#     for j in range(lenght-i-1):
#         if arr[j]<arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#         else:
#             continue

# print(arr)


# array reversal

# arr  = [1,2,3,4,5,6,7,8,9]

# for i in range(lenght//2):
#     arr[i],arr[lenght-i-1] = arr[lenght-i-1],arr[i]

# print(arr)

# array rotation
# arr  = [1,2,3,4,5,6,7,8,9]
# ## arr = [8,9,1,2,3,4,5,6,7]
# k=2
# startingp = lenght-k
# def reversal(arr,k):
#     for i in range(lenght-k,lenght
#     print(arr)

# reversal(arr,2)

# write a program to calc a square of given num 
# wap to detect double space in string
# wap to accept marks of 6 students and display them in sorted manner
# wap to count the number of 0 in in following tuple=  (7,0,8,0,0,9)
# wap to create a dict of hindi words with their english transaltion input from the users

# arr = [1,1,2,3,4,5,6,7,7,7]

# print(arr)
# arr.sort()
# print(arr)

# # j=0

# for i in range(len(arr)-1):
#     if arr[i] ==arr[j]:
#         continue
#     elif arr[i]!=arr[j] or i==0:
#         print(arr[j])
#         j =i


# arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

# arr.sort()
# print(arr)

# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         if i== arr[j]:
#             arr[i],arr[j]  = arr[j],arr[i]
#         else:
#             continue

# print(arr)

# for i in range()
#     # if arr[i]==i:
#     #     continue
#     # elif arr[i]!=i:
#     #     arr[i] = -1

# print(arr)


# Rearrange positive and negative numbers in O(n) time and O(1) extra space

# arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]

# lenght = len(arr)

# for i in range(lenght):

# arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
# lenght = len(arr)
# j=0
# for i in range(lenght):
#     if arr[i]!=0:
#         arr[j],arr[i] = arr[i],arr[j]
#         j=j+1
#     elif arr[i]==0:
#         continue

# print(arr)

# array = [2,1]
# for i in range(1,len(array)):
#     if i !=array[i]:
#         print(i)
#         break
#     elif i == array[i]:
#         continue

# INSERTION SORT

arr = [9,8,7,6,5,4,3,2,1]
lenght = len(arr)

# for i in range(lenght):
#     for j in range(i,0,-1):
#         if arr[j]<arr[j-1]:
#             arr[j],arr[j-1] = arr[j-1],arr[j]
#         else:
#             continue
# print(arr)

## SELECTION SORT

# for i in range(lenght):
#     maximum = i
#     for j in range(i,lenght):
#         if arr[maximum]>arr[j]:
#             maximum = j
#         else:
#             continue
#     arr[maximum],arr[i] = arr[i],arr[maximum]
#     print(arr)

# print(arr)

# BUBBLE SORT

# for i in range(lenght):
#     for j in range(lenght-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#         else:
#             continue

# print(arr)

# arr = [1, 2, 2, 1]
# lenght = len(arr)

# for i in range(1,lenght-1):
#     if i%2==0:
#         if arr[i]>=arr[i-1]:
#             continue
#         elif arr[i]<=arr[i-1]:
#             arr[i],arr[i-1] = arr[i-1],arr[i]
#     else:
#         if arr[i]<=arr[i-1]:
#             continue
#         elif arr[i]>=arr[i-1]:
#             arr[i],arr[i-1] = arr[i-1],arr[i]

# print(arr)

# arr=[1, 2, 3, 4, 5, 6, 7]
# lenght = len(arr)
# result_arr=[]

# for i in range(lenght//2):
#     result_arr.append(arr[lenght-1-i])
#     result_arr.append(arr[i])

# print(result_arr)


arr = [7, 2, 9, 4, 6, 1, 3, 8, 5]
5,8,3,1,6,4,9,2,7

5,8,7,2,9,4,6,1,3
length = len(arr)
# j=0
# for i in range(lenght):
#     if arr[i]%2 ==0:
#         arr[j],arr[i] = arr[i],arr[j]
#         j = j+1
#     else:
#         continue
# print(arr)


# def rotate(k,arr):
#     arr.reverse()
#     lenght = len(arr)
#     print(arr[k],arr[lenght-k-1])
#     for i in range(k,(lenght-k-1)//2):
#         print(arr[lenght-i-1],"i")
#         arr[i],arr[lenght-i-1] = arr[length-i-1],arr[i]
#         print(arr)
#     print(arr)
# rotate(2,arr)

## sliding window


# arr=[2, 5, -1, 7, -3, -1, -2]
# k=4

# for i in range()

