## bubble sorting



# for i in range(len(arr)):
#     for j in range(0,len(arr)-1-i):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]  = arr[j+1],arr[j]

# print(arr)

## insertion sorting

# for i in range(len(arr)-1):
#     for j in range(i,0,-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1] =arr[j+1],arr[j]

# print(arr)

# finding the second largest element in the array o(n) time

# arr = [12, 35, 1, 10, 34, 1]
# max = -1
# maxi = -1 
# for i in range(len(arr)):
#     print(arr[i], max, maxi)
#     if arr[i]>max:
#         maxi  = max
#         max = arr[i]
#     elif arr[i] >maxi:
#         maxi = arr[i]

# print(maxi)

## moving the 0 to the end of the array

# arr = [1, 2, 0, 4, 3, 0, 5, 0]
# j=0
# for i in range(len(arr)):
#     print(arr,i,j)
#     if arr[i]!=0:
#         arr[j],arr[i] = arr[i],arr[j]
#         j = j+1
#     else:
#         i=j

# print(arr)

# array segregatoin technique in odd and even

arr = [9,8,7,6,5,4,3,2,1]
arr.reverse()
j=0
for i in range(len(arr)):
    if arr[i]%2!=0:
        arr[j],arr[i] = arr[i],arr[j]
        j=j+1
    else:
        j=i

print(arr)