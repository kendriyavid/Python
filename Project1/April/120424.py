## Recursion

# 1 to n

# def onetoN(x,y):
#     if x>y:
#         return
#     print(x)
#     onetoN(x+1,y)
# onetoN(1,5)

# def NtoOne(x):
#     if x==0:
#         return
#     NtoOne(x-1)
#     print(x)
# NtoOne(6)


# def sumofN(x,s):
#     if x<=0:
#         return
#     sumofN(x-1,s+x)
#     print(s)
# sumofN(10,0)
# arr=[1,2,3,4,5,6]

# def revarray(i,l,arr):
#     if i>=l//2:
#         print(arr)
#         return
#     arr[i],arr[l-i-1] =arr[l-i-1],arr[i]
#     revarray(i+1,l,arr)

# revarray(0,len(arr),arr)