## Dutch national flag algorithm

# arr = [1,0,2,0,1]
# x = 0
# y = len(arr)-1
# i=0
# for i in range(len(arr)):
#     while arr[i]==0:
#         arr[i],arr[x] = arr[x],arr[i]
#         x+=1
#     while arr[i]==2:
#         arr[i],arr[y] = arr[y],arr[i]
#         y -=1
    
# print(arr)


# nums = [2,1,0,0,1,2,1,0]
# x = 0
# y = len(nums) - 1
# for i in range(len(nums)):
#     if nums[i] == 0 and i > x:
#         nums[i], nums[x] = nums[x], nums[i]
#         x += 1
#     elif nums[i] == 2 and i < y:
#         nums[i], nums[y] = nums[y], nums[i]
#         y -= 1

# return nums

# arr = [2,1,0,0,1,2,1,0]
# x=0
# y=len(nums)-1
# mid = 0

# while mid<y:
#     if nums[mid]==0:
#         nums[x],nums[mid] = nums[mid],nums[x]
#         mid =  mid+1
#         x = x+1
#     elif nums[mid]==1:
#         mid = mid+1
#     elif nums[mid] == 2:
#         nums[y],nums[mid] = nums[mid],nums[y]
# ]        y=y-1
# print(nums)


##LINKED LISTS
nums  =[-2,1,-3,4,-1,2,1,-5,4]
maximum = 0
sumation = 0
i=0
j=0

while j<len(nums):
    if sumation>=0:
        sumation = sumation+nums[j]
        maximum = max(sumation, maximum)
        j = j+1
    elif sumation<0:
        i = j
        sumation = 0
    
print(maximum)
