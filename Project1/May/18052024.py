# arr=[True,True,True,False,False,False]
# i=0
# j=len(arr)-1
# indx=0
# while j>=i:
#     mid=(i+j)//2
#     if arr[mid]:
#         indx=mid
#         i=mid+1
#     else:
#         j=mid-1
# print(indx)

#AGGRCOWS
arr=[1,2,8,4,9]
c=3
i=1
j=max(arr)
indx=-1
arr.sort()
def distfunc(arr, dist, c):
    count = 1  
    last_position = arr[0] 

    for i in range(1, len(arr)):
        if arr[i] - last_position >= dist:
            count += 1  
            last_position = arr[i]  
            if count == c:  
                return True
    return False

while i<=j:
    mid=(i+j)//2
    if distfunc(arr,mid,c):
        indx=mid
        i=mid+1
    else:
        j=mid-1

print(indx)
