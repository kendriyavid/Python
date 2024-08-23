# import pandas as pd
# import csv
# filename='students.csv'
# variable = pd.read_csv('students.csv')
# variable.head()

# import csv

# filename = 'students.csv'

# with open(filename, 'w', newline='') as csvfile:
#     fields = ['eid', 'ename', 'dept']
#     rows = [['e1', 'amam', 'hr'], ['e2', 'amit', 'finance'],['e3','harsh','it']]
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(fields)
#     csv_writer.writerows(rows)

# wap to count number of rows in a given csv file and print first n rows
# import csv
# with open('students.csv', newline='') as f:
#     reader = csv.reader(f)
#     nlines=0
#     for row in reader:
#         nlines+=1
# print(nlines)

# Next perumuations

# n=1234
# narr = list(str(1234))
# res=[]
# def permutations(narr,mid,n,res):
#     if len(mid)>=len(narr):
#         num = int(''.join(mid))
#         res.append(num)
#         return
    
#     for i in range(len(narr)):
#         if narr[i] not in mid:
#             mid.append(narr[i])
#             permutations(narr,mid,n,res)
#             mid.pop()

# permutations(narr,[],1234,res)
# print(res)

# res.sort()
# for i in range(len(res)):
#     if res[i]>n:
#         print(res[i])
#         break

# str='harshdeep'
# print(str.strip('h'))

# arr=[2,5,1,3,0]
# smallest = 999999
# for i in range(len(arr)):
#     if arr[i]<smallest:
#         smallest = arr[i]
# print(smallest)
# k=2
# arr=[8,7,1,6,5,9]
# arr.reverse()
# print(arr)
# i=0
# j=k-1
# while i<j:
#     arr[i],arr[j] = arr[j],arr[i]
#     i+=1
#     j-=1

# j=k
# i = len(arr)-1
# while j<i:
#     arr[i],arr[j] = arr[j],arr[i]
#     j+=1
#     i-=1
# print(arr)
    
# arr=[1,1,2,2,3,4,4,5]
# j=0
# for i in range(len(arr)):
#     if arr[i]!=arr[j]:
#         arr[j+1] = arr[i]
#         j+=1
# print(arr)

# arr=[4,3,9,2,4,1,10,89,34]
# dicti={}
# for i in range(len(arr)):
#     if arr[i] not in dicti.keys():
#         dicti[arr[i]] = 1
#     else:
#         dicti[arr[i]]+=1

# sarr = dicti.keys()
# print(sarr)

# arr=[1,2,3,2,4,3,1,2]
# dicti={}
# for i in range(len(arr)):
#     if arr[i] not in dicti.keys():
#         dicti[arr[i]] = 1
#     else:
#         dicti[arr[i]]+=1

# narr = zip(dicti.values(),dicti.keys())
# print(narr)
# narr.sort()
# for _,i in narr:
#     print(i)

# n=12222
# arr=[]
# while n>0:
#     digit = n%10
#     arr.append(digit)
#     n//=10
# print(arr[::-1])

# total = 0
# for i in range(len(arr)):
#     total =( total+ (arr[i]*(10**i)))
# print(total)

# string = "a+((b-c)+d)"
# lstring = []
# brackets=['(',')']
# for i in range(len(string)):
#     if string[i] not in brackets:
#         lstring.append(string[i])

# print(''.join(lstring))

# str1 = 'abcdef'
# str2 = 'cefz'

# ns=''
# for i in range(len(str1)):
#     if str1[i] not in str2:
#         ns=ns+str1[i]
# print(ns)

# string='abcdxyz'
# ns = list(string)
# ns.sort()
# print(ns)

# str1='takeuforward'
# str2='forward'

# print(str1.find(str2))
# arr=[10, 90, 49, 2, 1, 5, 23]
# arr.sort()
# print(arr)
# flag=False

# for i in range(0,len(arr)-1,2):
#     arr[i],arr[i+1] = arr[i+1],arr[i]

# # print(arr)
# import math
# n=50
# arr=[]
# ran = math.sqrt(50)
# for i in range(1,int(ran)):
#     num = 50%i
#     if num==0:
#         if num == 50/i:
#             arr.append(num)
#         else:
#             arr.append(i)
#             arr.append(50/i)
# print(arr)
# matrix=[]
# while True:
#     line = input()
#     if line=="":
#         break
#     matrix.append(list(map(int,line.split())))

# print(matrix)
# matrix=[]
# while True:
#     line = input()
#     if line=="":
#         break
#     matrix.append(list(map(int,line.split())))

# number = int(input("enter number"))

# string="0123456789abcdef"
# final=''
# while number>0:
#     i = number%16
#     final+=string[i]
#     number//=16
# print(final[::-1])
matrix=[]

while True:
    line = input()
    if line=="":
        break
    matrix.append(list(map(int,line.split())))

for row in matrix:
    print(row)

nmatrix=[]
def rotate(matrix,nmatrix):
    for row in range(matrix):
        for i in range(row):
            nmatrix[row,i] = matrix[i,row]

print(nmatrix)