# ## vanilla binary search

# # 
# # high = len(arr)-1
# # low = 0
# # index=-1
# # target =7
# # while(low<=high):
# #     mid = (high+low)//2
# #     if(arr[mid]==target):
# #         index = mid
# #         break
# #     elif(arr[mid]>target):
# #         high = mid-1
# #     else:
# #         low = mid+1
# # print(index)

# ## lower bound target=>index
# # arr = [1,2,3,4,5,6,7,8,9]
# # i = 0
# # j = len(arr)-1
# # target = 6
# # index = -1
# # while(i<=j):
# #     mid = (i+j)//2
# #     if(target<=arr[mid]):
# #         j= mid-1
# #         index = mid
# #     else:
# #         i = mid+1
# # print(index)

# # first position of true
# # arr = [False,False,False,False,True,True,True]
# # i=0
# # j=len(arr)-1
# # index=-1
# # while(i<=j):
# #     mid = (i+j)//2
# #     if(arr[mid]):
# #         j = mid-1
# #         index = mid
# #     else:
# #         i = mid+1

# # print(index)

# ## element in rotated sorted array
# # arr = [7,8,9,1,2,3,4,5,6]
# # i =0
# # j = len(arr)-1
# # index=-1
# # target = 9
# # while(i<=j):
# #     mid = (i+j)//2
# #     if(arr[mid]<arr[j]):
# #         ## this portion is sorted
# #         if(arr[mid]==target):
# #             index = mid
# #             break
# #         elif(arr[mid]>target>arr[j]):
# #             i =  mid+1
# #         else:
# #             j = mid-1
# #     else:
# #         if(arr[mid]==target):
# #             index = mid
# #             break
# #         elif(arr[mid]<target<arr[i]):
# #             j = mid-1
# #         else:
# #             i = mid+1
# # print(index)

# # rotated sorted with duplicates

# # arr = [7,8,1,2,3,3,3,4,5,6]
# # i = 0
# # j = len(arr)-1
# # index = -1
# # target = 8
# # while(i<=j):
# #     mid = (i+j)//2

# # number = int(input())
# # i =0
# # j=float('inf')
# # index = -1
# # def func(mid,target):
# #     return mid*mid<=target

# # while(i<=j):
# #     mid =(i//2)+(j//2)
# #     print(mid)
# #     if(func(mid,number)):
# #         index = mid
# #         i = mid+1
# #     else:
# #         j = mid-1
# # print(index)

# # number = int(input())
# # power = int(input())
# # i=0
# # j = number
# # index = -1
# # def func(mid,power,number):
# #     result =1
# #     while(power!=0):
# #         if(power%2!=0):
# #             result = result*mid
# #             power-=1
# #         else:
# #             mid = mid*mid
# #             power/=2
# #     return result<=number
# # while(i<=j):
# #     mid = i+(j-i//2)
# #     if(func(mid,power,number)):
# #         index = mid
# #         j = mid-1
# #     else:
# #         i = mid+1
# # print(index)


# # piles = [3,6,7,11], h = 8

# # i = 0
# # j = sum(piles)

# # hr questions
# # introduction
# # dbms
# # javascript+ reactjs

# # oops+js oops
# # python - revision, js revision

# # shallow vs deep copy
# # importing
# # sorting
# ## lambda
# ## python file handeling
# ## file operations
# ## map and reduce
# # a=4
# # b=5
# # x = lambda a,b:a+b
# # print(x(a,b))

# # from abc import ABC, abstractmethod

# ## python file handleing
# # f = open("hello.txt",'w')
# # # for lines in f:
# # #     print(lines)
# # f.write("harshdeepsingh")
# # f.close()

# # try:
# #     f= open("hello.txt",'a')
# #     f.write("Harshsdeep singh is good ")
# # except:
# #     print("error occured")
# # else:
# #     print("done")
# # finally:
# #     print("file operations completed")


# ## total number of employee in each city
# # select city,count(*) from employee
# # group by city;

# ## second highest ssalary
# # select min(salary) from(
# #     select * from employee
# #     order by salary desc
# #     limit 2
# # );

# # select department,min(salary) as minimum_of_dept from employee
# # group by department

# # select department, min(salary) as second_ghigest from (
# #     select department,salary from employee
# #     order by department 
# # )
# # arr=[4,5,6,7,0,1,2]
# # i=0
# # j=len(arr)-1
# # index=-1
# # while(i<j):
# #     mid = (i+j)//2
# #     if(arr[mid]>arr[j]):
# #         if(arr[mid]<arr[index]):
# #             index=mid
# #         j=mid-1
# #     else:
# #         if(arr[i]<arr[index]):
# #             index = i
# #         i=mid+1
# # print(arr[index])

# # // bubble sorting
# # arr=[9,8,7,6,5,4,3,2,1]
# #     for j in range(len(arr)-1,i,-1):
# #         print(i,j,j-1)
# #         if(arr[j]<arr[j-1]):
# #             arr[j],arr[j-1] = arr[j-1],arr[j]
# # print(arr)

# ## selection sorting
# # for i in range(0,len(arr)-1):
# #     minidx=0
# #     for j in range(i+1,len(arr-1)):
# #         if (arr[minidx]>arr[j]):
# #             arr[minidx] = j
# #     arr[minidx],arr[i] = arr[i],arr[minidx]

# # def merge(arr,low,high,mid):
# #     i=low
# #     j=mid
# #     while(i<=mid and j<=len(arr)-1):
# #         temp=float('inf')


# # def mergesorting(low,high,arr):
# #     if(low>=high):
# #         return
# #     mid = (low+high)//2
# #     mergesorting(low,mid,arr)
# #     mergesorting(mid+1,high,arr)
# #     merge(arr,low,high,mid)

# # def dfs(node):
# #     if not node.left and not node.right
# #         return 0
# #     l = dfs(node.left)
# #     r = dfs(node.right)
# #     return 1+max(l,r)


# # class Node:
# #     def __init__(self,val=None):
# #         self.val=None
# #         self.left=left
# #         self.right=right

# # class Tree:
# #     def __init__(self):
# #         self.root = None
    
# #     def dfs(node):
# #         if not node.left and not node.right:
# #             return
# #         dfs(node.left)
# #         dfs(node.right)
    
# #     def bfs(node):
# #         queue=[node]
# #         while(queue):
# #             nlevel=[]
# #             for cnode in queue:
# #                 ##do the operation
# #                 if(cnode.left):
# #                     nlevel.append(cnode.left)
# #                 if(cnode.right):
# #                     nlevel.append(cnode.right)
# #             queue=nlevel

# ## treee views


# seti  =set()
# seti.add()
# seti.remove()
# len(seti)

# combined = zip(arr1,arr2)


# arr = [[0]*3 for x in range(0,3)]
# print(arr)

# lower upper isalnum is num


# file = open("input.txt",'w')
# file.write(" ")


# try:
#     file = open("input.input.txt")
# else:


# string = ""
# print(string.split('e'))
import copy

# Example class to demonstrate copying
class Person:
    def __init__(self, name, details):
        self.name = name
        self.details = details
    
    def __repr__(self):
        return f"Person(name={self.name}, details={self.details})"

def demonstrate_copy_types():
    # Original complex object
    original_list = [1, [2, 3], {'a': 4}]
    
    # 1. Assignment (Not a Copy)
    print("1. Assignment (Reference)")
    assigned_list = original_list
    assigned_list[1][0] = 'X'
    print("Original list after modification:", original_list)
    print("Assigned list:", assigned_list)
    print("Are they the same object?", original_list is assigned_list)
    
    # 2. Shallow Copy
    print("\n2. Shallow Copy")
    shallow_copy = copy.copy(original_list)
    shallow_copy[1][0] = 'Y'  # Modifies nested mutable object
    print("Original list after shallow copy modification:", original_list)
    print("Shallow copy:", shallow_copy)
    print("Are they the same object?", original_list is shallow_copy)
    
    # 3. Deep Copy
    print("\n3. Deep Copy")
    deep_copy = copy.deepcopy(original_list)
    deep_copy[1][0] = 'Z'  # Does not affect original
    print("Original list after deep copy modification:", original_list)
    print("Deep copy:", deep_copy)
    print("Are they the same object?", original_list is deep_copy)
    
    # 4. Complex Object Example with Custom Class
    print("\n4. Custom Class Copy Demonstration")
    # Create an original person with nested dictionary
    original_person = Person("Alice", {"age": 30, "hobbies": ["reading", "coding"]})
    
    # Shallow copy
    shallow_person = copy.copy(original_person)
    shallow_person.details["hobbies"].append("swimming")
    print("Original person after shallow copy modification:", original_person)
    print("Shallow copy:", shallow_person)
    
    # Deep copy
    deep_person = copy.deepcopy(original_person)
    deep_person.details["hobbies"].append("painting")
    print("Original person after deep copy modification:", original_person)
    print("Deep copy:", deep_person)

# Uncomment to run the demonstration
# demonstrate_copy_types()