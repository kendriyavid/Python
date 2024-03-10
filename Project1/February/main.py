# arr= [10, 4, 3, 50, 23, 90]

# precomputation (sorting the array)

# x = -1
# y=-1
# z=-1

# for i in arr:
#     print(i,x,y,z)
#     if i>x:
#         z = y
#         y=x
#         x=i
#         print(i,x,y,z)
#     elif i>y:
#         z=y
#         y=i
#     elif i>z:
#         z=i
#     else:
#         continue

# print(x,y,z)


# sorting the array
# selection sort

# arr= [10, 4, 3, 50, 23, 90]

# lenght = len(arr)

# for i in range(lenght-1):
#     maximum = i
#     for j in range(i+1,lenght):
#         print(arr[i],arr[j],j)
#         if arr[maximum]<arr[j]:
#             maximum =j
#         else:
#             continue
        
#     temp = arr[i]
#     arr[i] = arr[maximum]
#     arr[maximum] = temp
#     print("inbetween",arr,arr[maximum])

## selection sorting

# # arr= [10, 4, 3, 50, 23, 90]
# lenght= len(arr)
# for i in range(lenght):
#     maximum = i
#     for j in range(i,lenght):
#         if arr[maximum]<arr[j]:
#             maximum = j
#         else:
#             continue
#     temp  =arr[i]
#     arr[i]  =arr[maximum]
#     arr[maximum] = temp

# # print(arr)

# for i in range(lenght-1):
#     if arr[i]>arr[i+1]:
#         print(arr[i+1])
#         break
#     elif i == i+1:
#         continue

## putting all zeros to the end of the array

# arr =[ 1, 2, 0, 4, 3, 0,0, 5, 0]
# print(arr)
# length = len(arr)

# for i in range(length-1):
#     j=i+1
#     if arr[i] !=0:
#         continue
#     elif arr[i]==0 and arr[j] ==0:
#         if length<=j+1:
#             break
#         else:
#             temp = arr[j+1]
#             arr[j+1] = arr[i]
#             arr[i] = temp
#     elif arr[i] ==0:
#         temp = arr[i]
#         arr[i] = arr[j]
#         arr[j] = temp
    
#     print(arr,"hi",i,j)

# print(arr)


arr = [7, 2, 9, 4, 6, 1, 3, 8, 5]
print(arr)

lenght = len(arr)

for i in range(int(lenght/2)):
    j = (lenght-1)-i
    if arr[i]%2==0:
        continue
    elif arr[i]%2!=0:
        temp = arr[i]
        arr[i]  =arr[j]
        arr[j]= temp

print(arr)