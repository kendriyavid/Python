# //////////////////////////////////finding the 3 greatest elemetn in array

# arr = [7, 2, 9, 4, 6, 1, 3, 8, 5]
# lenght = len(arr)
# x  =0
# y=0
# z=0
# for i in range(0,lenght):
#     if arr[i]>x:
#         z=y
#         y=x
#         x= arr[i]
#     elif arr[i]>y:
#         z=y
#         y = arr[i]
#     elif arr[i]>z:
#         z=arr[i]

# print(x,y,z)

# /////////////////////////////////////////////// selection sort

# arr = [7, 2, 9, 4, 6, 1, 3, 8, 5]

# lenght = len(arr)

# for i in range(0,lenght):
#     maximum = i
#     for j in range(i,lenght):
#         if arr[maximum]<arr[j]:
#             maximum = j
#         else:
#             continue
#     arr[i],arr[maximum] = arr[maximum],arr[i]

# print(arr)


# ///////////////////////////////////////// Insertion sort

# arr = [7, 2, 9, 4, 6, 1, 3, 8, 5]

# length = len(arr)

# for i in range(0,length):
#     for j in range(i,0,-1):
#         # print(i,j)
#         if arr[j]>arr[j-1]:
#             break
#         else:
#             arr[j],arr[j-1] = arr[j-1],arr[j]

# print(arr)

#////////////////////////// move all zeros to the end of the array

# arr =[ 1, 2, 0, 4, 3, 0,0, 5, 0]

# length = len(arr)
# z=0
# for i in range(0, length):
#     if arr[i] ==0:
#         continue
#     else:
#         arr[i],arr[z] = arr[z],arr[i]
#         z =z+1

# print(arr)

# even positions should be greater than the odd ones 


# arr=[1, 3, 2, 2, 5 ]
# lenght = len(arr)

# for i in range(1,lenght):
#     if i%2!=0:
#         if arr[i]<=arr[i-1]:
#             arr[i],arr[i-1] = arr[i-1],arr[i]
#         else:
#             continue
#     else:
#         continue
# print(arr)

## list slicing 


# arr =[ 1, 2, 0, 4, 3, 0,0, 5, 0]

# insertion sort

# lenght = len(arr)
# for i in range(0,lenght):
#     for j in range(i,0,-1):
#         print(j,j-1)
#         if arr[j]<arr[j-1]:
#             arr[j-1],arr[j] = arr[j],arr[j-1]
#         else:
#             break

# print(arr)

#Rearrange an array in maximum minimum form using Two Pointer Technique

# arr=[1,2,3,4,5,6,7,8,9]

# length = len(arr)
# temp = []
# flag = True
# j=0
# k=0
# for i in range(0,length):
#         if flag:
#             temp.append(arr[length-1-k])
#             k = k+1
#         else:
#             temp.append(arr[j])
#             j = j+1
#         flag = not flag 
#         print(temp)

# print(temp)


# segregate even and odd numbers


# arr=[7, 2, 9, 4, 6, 1, 3, 8, 5]
# j=0
# length = len(arr)
# for i in range(0,length):
#     if arr[i]%2!=0:
#         continue
#     else:
#         arr[j],arr[i] = arr[i],arr[j]
#         j =j+1

# print(arr)

# ## reversing the array using auxiliary space
# n=2
# arr = [7, 2, 9, 4, 6, 1, 3, 8, 5]
# length = len(arr)

# j=0
# for i in range(length-n,length):
#     arr[i],arr[j] = arr[j],arr[i]
#     j = j+1

# print(arr)

# temp  = arr[length-n:]+arr[:length-n]
# print(temp)

## reversing wihtout using the auxiliary space

# for i in range(n+1):
#     last = arr.pop()
#     print(last,arr)
#     arr.insert(0,last)

# print(arr)
# n=2

# arr = [7, 2, 9, 4, 6, 1, 3, 8,4]
# length= len(arr)

# for i in range(length//2):
#     arr[i],arr[length-i-1] = arr[length-i-1],arr[i]
#     print(arr)

# for i in range(len(arr[])//2):

# print(arr)

flag = False
arr = [10, 5, 6, 3, 2, 20, 100, 80]

length = len(arr)

# for i in range(1,length):
#     if flag:
#         if arr[i-1]<=arr[i]>=arr[i+1]:
#             continue
#         elif arr[i-1]>=arr[i]>=arr[i+1]:
#             arr[i-1],arr[i] =arr[i],arr[i-1]
#         elif arr[i-1]<=arr[i]<=arr[i+1]:
#             arr[i+1],arr[i] =arr[i],arr[i+1]
#     else:
#         if arr[i-1]=>arr[i]<=arr[i+1]:
#             continue
#         elif arr[i-1]>=arr[i]>=arr[i+1]:
#             arr[i-1],arr[i] =arr[i],arr[i-1]
#         elif arr[i-1]<=arr[i]<=arr[i+1]:
#             arr[i+1],arr[i] =arr[i],arr[i+1]  


## remove duplicates

arr  =[-1, 2, -3, 4, 5, 6, -7, 8, 9]

print(arr.sort())
print(arr.reverse())
print(arr)
length = len(arr)
j=0
for i in range(length):
    

