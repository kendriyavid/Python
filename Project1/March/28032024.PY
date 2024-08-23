## PREV GREATER ELEMENT

# arr=[10,4,2,20,40,80]
# result=[]
# stack=[]
# for i in range(0,len(arr)):
#     while stack and arr[i]>stack[-1]:
#         stack.pop()
#     if not stack:
#         result.append(-1)
#     else:
#         result.append(stack[-1])
#     stack.append(arr[i])

# print(result)

## NEXT SMALLER ELEMENT
arr=[4,8,5,2,25]
stack=[]
result=[]
for i in range(len(arr)-1,-1,-1):
    while stack and arr[i]<stack[-1]:
        stack.pop()
    if not stack:
        result.append(-1)
    else:
        result.append(stack[-1])
    stack.append(arr[i])
result.reverse()
print(result)