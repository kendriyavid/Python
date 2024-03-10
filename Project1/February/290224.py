print("harshdeep")

# bubble sorting

# arr=[1,2,3,4,5,6,7,8,9]
# print(arr)


# lenght = len(arr)

# for i in range(lenght):
#     for j in range(0,lenght-i-1):
#         if arr[j]<arr[j+1]:
#             arr[j],arr[j+1] =arr[j+1],arr[j]
        

# print(arr)


## insertion sorting

# for i in range(lenght):
#     maximum =i
#     for j in range(i,lenght):
#         if arr[maximum]<arr[j]:
#             maximum = j
#     arr[maximum],arr[i] = arr[i],arr[maximum]

# print(arr)


## selection sorting

# for i in range(lenght):
#     for j in range(i,0,-1):
#         if arr[j]>arr[j-1]:
#             arr[j],arr[j-1] =arr[j-1],arr[j]
        
# print(arr)


## RECURSION

# printing 1toN


# def onetoN(x):
#     if x>5:
#         return
#     x =x+1
#     print(x)
#     onetoN(x)

# onetoN(0)


# def OnetoN(x):
#     if x==0:
#         return
#     OnetoN(x-1)
#     print(x)

# OnetoN(5)
    
# def NtoOne(x):
#     if x>5:
#         return
#     NtoOne(x+1)
#     print(x)

# NtoOne(1)


# Sum of 1 to N
# sum = 0

# def Sum1toN(sum,x):
#     if x==0:
#         return 0
#     sum=Sum1toN(sum,x-1)
#     sum = sum+ x
#     print(x,sum)
#     return sum


# print(Sum1toN(sum,10))


# mul = 0

# def mul1toN(mul,x):
#     if x==1:
#         return 1
#     mul = mul1toN(mul,x-1)
#     mul = mul*x
#     return mul

# print(mul1toN(mul,5))

## recursive solution

# sum=0

# def Sum1toN(x,sum):
#     if x==0:
#         print(sum)
#         return
#     sum = sum+x
#     Sum1toN(x-1,sum)

# Sum1toN(5,sum)


# def Print1toN(x):
#     if x==0:
#         return
#     Print1toN(x-1)
#     print(x)

# Print1toN(10)


# def PrintNto1(x,y):
#     if x>y:
#         return
#     PrintNto1(x+1,y)
#     print(x)

# PrintNto1(0,10)

## functional recursion
# def Multiply(x):
#     if x==0:
#         return 1
#     return Multiply(x-1)*x

# print(Multiply(5))

## parameterized recursion

# mul=1
# def multiply(mul,x):
#     if x==0:
#         print(mul)
#         return
#     mul = mul*x
#     multiply(mul,x-1)

# multiply(mul,10)

# Reversing array using recursion

arr=[1,2,3,4,5,6,7,8,9]

# def ReverseArray(arr,length,x):
#     if x>=length//2:
#         arr[x],arr[length-x-1] = arr[length-x-1],arr[x]
#         return arr
#     ReverseArray(arr,length,x+1)
#     arr[x],arr[length-x-1] = arr[length-x-1],arr[x]
#     return arr

# print(ReverseArray(arr,len(arr),0))

# def reversearray(arr,len,x):
#     if x>=len//2:
#         arr[x],arr[len-x-1] = arr[len-x-1],arr[x]
#         return arr
#     reversearray(arr,len,x+1)
#     arr[x],arr[len-x-1] = arr[len-x-1],arr[x]
#     return arr

# print(reversearray(arr,len(arr),0))
# string = "abbaa"
# def checkpalindrome(string,len,x):
#     if x>=len//2:
#         if string[x] == string[len-x-1]:
#             return True
#         else:
#             return False
#     bool = checkpalindrome(string,len,x+1)
#     if bool:
#         if string[x] == string[len-x-1]:
#             return True
#         else:
#             return False
#     else:
#         return False
    
# print(checkpalindrome(string,len(string),0))


## printing the subsequence using recursion

arr=[1,2,3,4,5,6,7,8,9]

def printsubsequence(arr,len,x):
    if x>=len:
        print(arr)
    ## adding
        
    