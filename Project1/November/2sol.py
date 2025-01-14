# # def gcd(a, b):
# #     while b:
# #         a, b = b, a % b
# #     return abs(a)

# # def minRoutes(pickLoc, baseX0, baseY0):
# #     slopes = set()  # Set to store unique normalized slopes
    
# #     for pickX, pickY in pickLoc:
# #         # Calculate dx and dy
# #         dx = pickX - baseX0
# #         dy = pickY - baseY0
        
# #         # Skip the base point itself
# #         if dx == 0 and dy == 0:
# #             continue
        
# #         # Reduce slope to simplest form using gcd
# #         g = gcd(dx, dy)
# #         dx //= g
# #         dy //= g
        
# #         # Normalize direction
# #         # Ensure all slopes are represented consistently
# #         if dx < 0 or (dx == 0 and dy < 0):
# #             dx, dy = -dx, -dy
        
# #         # Add the normalized slope to the set
# #         slopes.add((dx, dy))
    
# #     # Return the number of unique slopes
# #     return len(slopes)

# # def main():
# #     # Input
# #     pickLoc = []
# #     pickLoc_rows, pickLoc_cols = map(int, input().split())
# #     for _ in range(pickLoc_rows):
# #         pickLoc.append(list(map(int, input().split())))
    
# #     baseX0 = int(input())
# #     baseY0 = int(input())
    
# #     # Solve and print result
# #     result = minRoutes(pickLoc, baseX0, baseY0)
# #     print(result)

# # if __name__ == "__main__":
# #     main()


# def min_merge_operations(arr):
#     left = 0
#     right = len(arr) - 1
#     operations = 0

#     while left < right:
#         if arr[left] == arr[right]:
#             left += 1
#             right -= 1
#         elif arr[left] < arr[right]:
#             arr[left + 1] += arr[left]
#             left += 1
#             operations += 1
#         else:
#             arr[right - 1] += arr[right]
#             right -= 1
#             operations += 1

#     return operations

# # Input
# n = int(input())
# arr = [int(input()) for _ in range(n)]

# # Function call and output
# print(min_merge_operations(arr))




# class Animal:
#     def eat(self):
#         print("I eat food")
# class Dog(Animal):
#     def speak(self):
#         print("woof")
# class germanShepard(Dog):
#     def coat(self):
#         print("golden color")

# an1 = Animal()
# dg1 = Dog()
# gsh1 = germanShepard()
# an1.eat()
# print("dog")
# dg1.eat()
# dg1.speak()
# gsh1.coat()
# gsh1.eat()
# gsh1.speak()
