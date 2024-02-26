# string = str(input("enter the searching string "))
# substring = str(input("enter the substring to be searched "))

# lens = len(string)
# lenss =len(substring)

# def hashing(str):
#     sum = 0
#     for i in str:
#         sum = sum+ord(i)
#     return int(sum/len(str))
        
# sshash = hashing(substring)

# print(hashing(string))
# eoa = lens-lenss
# print(eoa)
# for i in range(lens-lenss):
#     shash = hashing(string[i:i+lenss])
#     if shash !=sshash:
#         continue
#     else:
#         if string ==string[i:i+lenss]:
#             print("yes exists")
#         else:
#             print("no it doesnot exist")


# for i in range(4):
#     print("Printing")
#     if  i==2:
#         continue
#         print(i)

# fibb number using a for loop in python

# sum=0
# for i in range(10):
#     print(i,sum)
#     sum = sum+i

## factorial

# input = int(input("enter the number"))
# factorial = 1
# index = 1
# for i in range(input+1):
#     print(i,factorial)
#     factorial = factorial*index
#     index = index+1

# ## 

# principal = 10000
# amt = 0
# for i  in range (5):
#     amt = (principal*6*1)/100+ principal
#     principal = amt
#     print(i,amt)

# def phello():
#     print("hello world")

# phello()


# def fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(fibo(n-1) + fibo(n-2))

# nterms = 10

# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(fibo(i))


# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]
# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]

# for i in range(len(X)):
#    for j in range(len(Y[0])):
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]

# for r in result:
#    print(r)


# fruit = "mango";
# # print(fruit[-1])


# index = 0
# while index<len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index = index+1

import tracemalloc

# fname = "harshdeep"
# lname = "singh"
# index = 0
# while index<len(fname):
#     print(fname[index])
#     index = index+1
# # index =0

# while index<len(lname):
#     print(lname[index])
#     index = index+1

# print(fname[0::2])


# greeting = "Hello harsh"
# newGreeting = 'j'+greeting[1:]
# print(newGreeting)


# def myfind(st,ch):
#     index =0
#     while index<=len(st)-1:
#         if st[index]==ch:
#             return index
#         index = index+1
#     return -1


# count = 0
# char = input("enter the char to find")
# str = "harshdeep singh"
# index = 0
# while index<len(str):
#     if str[index] == char:
#         count = count+1
#     index = index+1

# print(count)

# print(fname.upper())
# print(fname.lower())
# print(fname.title() )
# print(fname.strip())
# print(fname.find("i") )
# print(fname.replace("r","j") )
# print("pro" in fname) 


# person = {
#     "name":"harhshdeep singh",
#     "age":10
# }

# name = input("enter the name")
# age =int(input("enter the age"))

# if person["name"] == name and person["age"]==age:
#     print("you are logged in")
# else:
#     print("wrong credentials")

# tracemalloc.start()
# before = tracemalloc.take_snapshot()

# list = [1,2,3,4]
# # for i in list:
# #     print(i)

# vocab = ['hello',"there","myself","alex"]

# after = tracemalloc.take_snapshot()
# for stat in after.compare_to(before, 'lineno')[:2]:
#     print(stat)

# print(list,vocab,empty)
##################################################################################################

## DAY- 14/02/2024



course= ['cse','it','me','ec']
# i=0
# while (i<len(course)):
#     print(course[i])
#     i=i+1

# for i in course:
#     print("my course is",i)

# names=[1,2,3,4]
# print(course*4)
# print(course+names)

# print(course[1:3])

# print(course[-1])

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# matrix[2][2]=5
# print(matrix)


# string = "my name is harsh"
# print(string.split('h'))


# numbers=[1,2,3,4,5,6,7,8,9]
# print(numbers.append(3))
# print(numbers.count(1))
# print(numbers.index(6))
# print(numbers.remove(6))
# print(numbers)

# numbers.sort(reverse=True)
# numbers.m


# # mytup = (1,2,3,4,"harsh",)
# # print(type(mytup))

# def swap(a,b):
#     return b,a

# a=(1,)
# b=(0,)
# print(swap(a,b))

# print(min(numbers))
# print(max(numbers))
# # print(l())


# from math import sin,cos

# k=3.14
# print(sin(k))
# print(cos(k))

# import numpy as np
# x=3
# y=np.sin(x)
# print(y)
# c

 
# harsh = {
#     "subject":"java",
#     "subject2":"python"
# }

# print(harsh)
# harsh["subject"] = "c++"
# print(harsh)
# print(len(harsh))

# count = 0


# products={
#     "p1":"Bottle",
#     "p2":"Bag",
#     "p3":"toothbrush",
#     "p4":"matress",
#     "p5":"car"
# }

# product2 = products.copy()

# print(product2.values())


# // create empty dict allow 4 friends to enter their fav languages as values and keys as their names

friends={}

def check(i,j):
    if i in friends:
        return False
    else:
        return True

for i in range(4):
    i = (input("enter the name"))
    j = (input("enter the language"))
    ch = check(i,j)
    if ch == True:
        friends[i] = j
    else:
        print("name exists")
        i = i-1