## Sliding window 

arr = [1,2,3,4,5,6,7,8,9]
# def maximumsubarray(arr):
#     lenght = len(arr)
#     result = 0
#     for i in range(lenght-2):
#         interes = 0
#         for j in range(i,i+3):
#             interes+=arr[j]
#         print(interes)
#         result = max(interes,result)
#     return result
# print(maximumsubarray(arr))

# def maximumsubarray(arr,k):
#     result=0
#     current = 0
#     for i in range(k):
#         current+=arr[k]
#     result = current
#     for j in range(1,len(arr)-k+1):
#         current-=arr[j-1]
#         current+=arr[j+k-1]


# arr = [12, -1, -7, 8, -15, 30, 16, 28]
# result = []

# for i in range(0,len(arr)-3+1):
#     flag = False
#     for j in range(i,i+3):
#         if arr[j]<0:
#             result.append(arr[j])
#             flag = True
#             break
#     if not flag:
#         result.append(0)
# print(result)


# arr = [12, -1, -7, 8, -15, 30, 16, 28]
# result = []
# stack = []
# for i in range(3):
#     if arr[i]<0:
#         stack.append(arr[i])
# result.append(stack[0])
# for j in range(1,len(arr)-3+1):
#     if arr[j-1]<0:
#         stack.pop(0)
#     if arr[j+3-1]<0:
#         stack.append(arr[j+3-1])
#     if stack:
#         result.append(stack[0])
#     else:
#         result.append(0)
# print(result)

arr = "forxxorfxdofr"
pat = "for"
freq = [0]*26

def atoi(chr):
    return ord(chr)-ord("a")

# Precompute the frequency of the pattern characters
for chr in pat:
    freq[atoi(chr)] += 1

# Adjust for the first window in the arr (first len(pat) characters)
for chr in arr[:len(pat)]:
    freq[atoi(chr)] -= 1

# Check if the first window is an anagram
count = 0
if all(f == 0 for f in freq):
    count += 1

# Now slide the window across the array
for i in range(1, len(arr) - len(pat) + 1):
    # Add the character that enters the window
    freq[atoi(arr[i + len(pat) - 1])] -= 1
    # Remove the character that leaves the window
    freq[atoi(arr[i - 1])] += 1
    
    # Check if the current window is an anagram
    if all(f == 0 for f in freq):
        count += 1

print(count)
