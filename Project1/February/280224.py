# arr=[1,2,3,9,5,6,7,8,4]
# lenght = len(arr)
# for i in range(lenght):
#     maximum = i
#     for j in range(i,lenght):
#         if arr[maximum]<arr[j]:
#             maximum = j
#         else:
#             continue
#         print(i,maximum)
#     arr[maximum],arr[i] = arr[i],arr[maximum]
# print(arr)

# for i in range(lenght):
#     for j in range(i,0,-1):
#         if arr[j]<arr[j-1]:
#             arr[j],arr[j-1] = arr[j-1],arr[j]
#         else: 
#             break

# print(arr)

## Bubble Sorting

# for i in range(lenght):
#     for j in range(0,lenght-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#         else:
#             continue
# print(arr)

# for i in range(0,0):
#     print(i)


# RECURSION playlist

# def print10(x):
#     print(x)
#     x = x+1
#     if x<=10:
#         print10(x)
#     else:
#         return

# print10(0)

## print name 5 times

# def printname(x):
#     if x==5:
#         return
#     print("harshdeep")
#     x =x+1
#     printname(x)


# printname(0)
# z = 11
# x=0
# def print1toN(x,z):
#     if z==0:
#         return
#     print(x)
#     x = x+1
#     z=z-1
#     print1toN(x,z)


# print1toN(0,11)

## backtracking 
# def print1toN(x):
#     x = x-1
#     if x==0:
#         return x
#     print(print1toN(x))
#     return x

# print1toN(5)


# def printNto1(x):
#     x =x+1
#     if x==10:
#         return x
#     print(printNto1(x))
#     return x

# printNto1(0)


def print1toN(x):
    if x==0:
        return x
    print1toN(x-1)
    print(x)


# print1toN(6)

# def Print1toN(x):
#     if x==5:
#         return x
#     x = x+1
#     print()


/