# Exception Handeling

# try
# except
#finally

# arr=[1,2,3]
# try:
#     print(arr[4])
# except:
#     print("index out of range")

# num1 = int(input("enter 1"))
# num2 = int(input("enter 2"))

# def divide(x,y):
#     return x/y

# try:
#     print(divide(num1/num2))
# except:
#     print("trying again")

# def getint(x):
#     try:
#         val = int(input(x))
#         return val
#     except ValueError:
#         print("invalid datatype")

# num = getint("input an integer")
# print("input is ", num)

## write a python program that executes divison and handels arithematic error execption by using fucnciotns

# def divide2(x,y):
#     try:
#         return x/y
#     except ArithmeticError:
#         print("arithematic error occured")

# divide2(8,0)

#write the python program to construct the following pattern

# def full_pyramid(n):
# 	for i in range(1, n + 1):
# 		for j in range(n - i):
# 			print(" ", end="")
		
# 		for k in range(1, 2*i):
# 			print("*", end="")

# full_pyramid(5)
		
## pattern
# string operators
# odd or even numbers
# till access specifiers and inheritance


# def isValid(s):
# 	stack = []
# 	dicti = {")": "(", "]": "[", "}": "{"}
# 	for i in s:
# 		print(stack)
# 		if not stack:
# 			if i in dicti:
# 				stack.append(i)
# 			else:
# 				return False
# 		else:
# 			if i in dicti:
# 				stack.append(i)
# 			elif dicti[i] == stack[-1]:
# 				stack.pop()
# 			else:
# 				return False
# 	if not stack:
# 		return True
# 	else:
# 		return False


# print(isValid("()"))

# # generate parenthesis
# def gp(stack,result,arr,n,j,k):
# 	if not stack and j==n:
# 		result.append(arr[:])
# 	if j>n:
# 		return
# 	if k>j:
# 		return
# 	for i in range(["(",")"]):
# 		if stack and i==")":
# 			stack.pop()
# 			gp(stack,result,arr,n,j,k+1)
# 		else:
# 			stack.append("(")
# 			gp(stack,result,arr,n,j+1,k)


# def gp(stack, result, arr, n, j):
#     if not stack and j == n:
#         result.append(arr[:])
#     if j > n:
#         return
#     for i in range(2):  # Use range(2) for indices 0 and 1
#         if not stack and i == 1:  # Check if stack is empty and i is ")"
#             return
#         elif stack and i == 1:  # Pop from stack when encountering ")"
#             stack.pop()
#             gp(stack, result, arr, n, j)
#         else:
#             stack.append("(")
#             gp(stack, result, arr, n, j + 1)

# result = []
# gp([], result, [], 2, 0)
# print(result)

# def gp(stack, result, arr, n, open_count, close_count):
#     if open_count == n and close_count == n:
#         result.append("".join(arr))
#         return

#     if open_count < n:
#         arr.append("(")
#         stack.append("(")
#         gp(stack, result, arr, n, open_count + 1, close_count)
#         arr.pop()  # Backtrack by removing the added "("
#         stack.pop()

#     if close_count < open_count:
#         arr.append(")")
#         stack.pop()  # Pop from stack when encountering ")"
#         gp(stack, result, arr, n, open_count, close_count + 1)
#         arr.pop()  # Backtrack by removing the added ")"

# result = []
# gp([], result, [], 2, 0, 0)
# print(result)


arr = [1,3,2,4]
stack = []
result = []

for i in range(len(arr) - 1, -1, -1):  # corrected range to include 0 index
    while stack and arr[i] > stack[-1]:  # simplified if condition and corrected stack.append
        print(stack)
        stack.pop()
    if not stack:
        result.append(-1)
    else:
        result.append(stack[-1])
    stack.append(arr[i])  # corrected stack append syntax

result.reverse()  # reverse the result list to match the expected output order
print(result)



