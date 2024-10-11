# import math

# class Solution:
#     def __init__(self, number):
#         self.number = number
#         self.array = [1] * self.number
    
#     def sieve(self):
#         end = math.floor(math.sqrt(self.number))
#         for i in range(2, end + 1):  # Corrected loop to include `end`
#             if self.array[i] == 1:
#                 for j in range(i * i, self.number, i):  # Use `j` for the inner loop
#                     self.array[j] = 0
    
#     def get_primes(self):
#         return [i for i in range(2, self.number) if self.array[i] == 1]

# # Example usage:
# number = 50
# solution = Solution(number)
# solution.sieve()
# print(solution.get_primes())


# import math
# class Solution:
#     def __init__(self):
#         self.resarray = []
#         self.markarray = [True]*(90000000)
    
#     def seive(self):
#         self.markarray[0] = False
#         end = math.floor(math.sqrt(90000000))
#         for i in range(2,end+1):
#             if self.markarray[i]:
#                 for j in range(i*i,90000000,i):
#                     self.markarray[j] = False
        
#         for i in range(len(self.markarray)):
#             if self.markarray[i]:
#                 self.resarray.append(i)
    
#     def query(self,number):
#         return self.resarray[number - 1]

# solution = Solution()
# # solution.seive()
# # print(solution.query(1))
# # print(solution.query(2))
# # print(solution.query(3))
# # print(solution.query(10))


# # testcases = int(input())
# # for case in range(testcases):
# n,x = map(int,input().split())
# array = list(map(int,input().split()))
# maximum = float('-inf')
# for i in range(len(array)-1):
#     diff = array[i+1]-array[i]
#     maximum = max(maximum,diff)
# ## endpoint calculation
# maximum = max(maximum,2*(x-array[-1]))
# print(maximum)


## A cover in water

## row of cells 

# string = '#...#..#.#'
# def solve_test_case(string):
#     totalc = 0
#     i = 0
#     while i <= len(string) - 1:
#         # Skip blocked cells
#         if string[i] == "#":
#             i += 1
#             continue
        
#         # Count consecutive empty cells
#         count = 1
#         j = i + 1
#         while j <= len(string) - 1 and string[j] != "#":
#             count += 1
#             j += 1
            
#         # Apply the rule: if segment length <= 2, need all fills
#         # if segment length > 2, only need 2 fills
#         if count <= 2:
#             totalc += count
#         else:
#             return 2
            
#         # Move to next segment
#         i = j
#     return totalc

# def main():
#     t = int(input())  # Number of test cases
#     for _ in range(t):
#         n = int(input())  # Length of string
#         string = input().strip()  # The string representing cells
#         result = solve_test_case(string)
#         print(result)

# if __name__ == "__main__":
#     main()

# def minimum_water_actions(test_cases):
#     results = []
    
#     for _ in range(test_cases):
#         n = int(input().strip())
#         s = input().strip()
        
#         # Initialize a variable to count segments of empty cells
#         segment_count = 0
        
#         # Start traversing the string
#         in_segment = False
#         for char in s:
#             if char == '.':
#                 if not in_segment:
#                     # We've encountered a new segment of empty cells
#                     segment_count += 1
#                     in_segment = True
#             else:
#                 in_segment = False  # Reset on hitting a blocked cell
        
#         results.append(segment_count)
    
#     return results

# # Read number of test cases
# t =3


# results = minimum_water_actions(t)

# # Print all results
# for result in results:
#     print(result)


# def goodArray(array):
#     freq={}
#     for i in range(1,len(arr)):
#         if array[i] not in freq:
#             freq[array[i]] = 1
#         else:
#             freq[array[i]]+=1
#         if len(freq)>2:
#             return "No"
    
#     diff = next(iter(freq.values()))
#     diff  = diff - next(iter(freq.values()))
#     if diff<=1:
#         return "yes"
#     else:
#         return "no"

# def dctry(x,s):
#     flag = False
#     count = 0
#     for i in range(5):
#         if x in s:
#             flag = True
#             break
#         count+=1
#         x+=x
#     if flag:
#         return count
#     else:
#         return -1
# x = "aaaaa"
# s = "a"
# print(dctry(x,s))



# x = "a"
# s = "aaaaa"
# print(dctry(x, s))  # Output should be 4, as it takes 4 concatenations of "a" to get "aaaaa"


# def mostcommon(array,common):
#     flag = False
#     for num in array:
#         if num == common:
#             flag = True
#     if flag:
#         return "no"
#     else:
#         return "yes"


# def forked(a,b,xk,yk,xq,yq):
#     directions = [(1,1),(1,-1),(-1,1),(-1,-1)]
#     seti = set()
#     ## king calculation
#     for i,j in directions:
#         x = xk+(i*a)
#         y = yk+(j*b)
#         print(x,y)
#         seti.add((x,y))
#     ## queen calculation:
#     count = 0
#     print("queen")
#     for i,j in directions:
#         x = xq+(i*a)
#         y = yq+(j*b)
#         print(x,y)
#         if (x,y) in seti:
#             count+=1
#         else:
#             seti.add((x,y))
    
#     return count

# print(forked(2,1,0,0,3,3))



# def count_fork_positions(a, b, xk, yk, xq, yq):
#     knight_moves = [
#         (a,b), (a,-b), (-a,b), (-a,-b),
#         (b,a), (b,-a), (-b,a), (-b,-a)
#     ]
    
#     king_attackers = set()
#     for dx, dy in knight_moves:
#         knight_x = xk - dx
#         knight_y = yk - dy
#         king_attackers.add((knight_x, knight_y))
    
#     count = 0
#     for dx, dy in knight_moves:
#         knight_x = xq - dx
#         knight_y = yq - dy
#         if (knight_x, knight_y) in king_attackers:
#             king_attackers.remove(((knight_x, knight_y)))
#             count += 1
    
#     return count

# def solve_test_cases():
#     t = int(input())  # Number of test cases
#     for _ in range(t):
#         a, b = map(int, input().split())
#         xk, yk = map(int, input().split())
#         xq, yq = map(int, input().split())
#         result = count_fork_positions(a, b, xk, yk, xq, yq)
#         print(result)


# print(count_fork_positions(1, 1, 3, 1, 1, 3))

# def question(n,k,x):
#     low = 0
#     for i in range(1,k+1):
#         low+=i
#     high = 0
#     for i in range(n-k+1,n+1):
#         high+=i
#     if low<=x<=high:
#         return "yes"
#     else:
#         return "no"


def jellyfish(array,a,b,n):
    if b>a:
        return a
    sumation = b
    for i in array:
        sumation+=min()
    return sumation

import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

for _ in range(t):
    n,k,x = map(int,input().split())
    array = list(map(int,input().split()))
    print(jellyfish(array,n,k,x))  # You can process the input data as needed
sys.stdin.close()

