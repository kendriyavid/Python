## write a program to create multiple files in python directories
# import os
# try:
#     os.mkdir("testdir")
#     os.chdir('testdir')
#     number=int(input("Enter the number of files to be created"))
#     basename='file'
#     for i in range(number):
#         with open(f'file{i}','w') as f:
#             f.write(f'this is file{i}')
#         f.close()
# except Exception as e:
#     print("exception occured",e)
# finally:
#     print('program exited successfully')


## Multithreading

# import time
# import threading

# def eat():
#     time.sleep(5)
#     print('eating')

# def drink():
#     time.sleep(5)
#     print('drinking')

# def fly():
#     time.sleep(5)
#     print('flying')

# x=threading.Thread(target=eat,args=())
# x.start()
# y=threading.Thread(target=drink,args=())
# y.start()
# z=threading.Thread(target=fly,args=())
# z.start()
# print(threading.active_count())

# print(threading._main_thread)

# import os
# r,w=os.pipe()
# number=os.fork()
# if number:
#     os.close(w)
#     r=os.fdopen(r,'r')
#     print("parent reading")
#     str=r.read()
#     print(str)
#     r.close()
# else:
#     os.close(r)
#     w=os.fdopen(w,'w')
#     print("child writing")
#     w.write('childis writing')
#     w.close()


## Graphical User interface TKINTER
 
# from tkinter import *
# window=Tk()
# canvas=Canvas(height=200,width=200)
# canvas.create_line(100,0,0,200)
# canvas.create_line(100,0,200,200)
# canvas.create_line(0,200,200,200)
# canvas.pack()
# window.mainloop()

# ## 
# import os
# r,w=os.pipe()
# process=os.fork()
# if process:
#     os.close(w)
#     print("parent reading")
#     r=os.fdopen(r,'r')
#     str=r.read()
#     print(str)
#     r.close()
# else:
#     os.close(r)
#     print("child is reading")
#     w=os.fdopen(w,'w')
#     w.write("writing in to the pipes")
#     w.close()


## POLYMORPHISM
# method overriding
# class Animal:
#     def speak():
#         print("I am animal")
# class Cat(Animal):
#     def speak():
#         print("I am cat")
# class Dog(Animal):
#     def speak():
#         print("I am dog")
# def Speak(Animal):
#     Animal.speak()
# d1=Dog()
# c1=Cat()
# Speak(d1)

## POLYMORPHISM
# -METHOD OVERRRIDING
# -METHOD OVERLOADING
# - RUNTIME POLYMORPHGSIM
# - STATIC POLYMORPHGSIM

# class animal:
#     def speak():
#         print("i am")
# class dog(animal):
#     def speak():
#         print('i am dog')
# class cat(animal):
#     def speak():
#         print('I am cat')

# import os
# import threading
# process=os.fork()
# r,w=os.pipe()
# if process:
#     os.close(w)
#     print("reading from pipe")
#     r=os.fdopen(r,'r')
#     str=r.read()
#     print(str)
#     r.close()
# else:
#     os.close(r):
#     print("writing to pipe")
#     w=os.fdopen(w,'w')
#     w.write("hello there")
#     w.close()
# import os
# print(os.stat('document1.txt'))
# print(os.path.gettime())


# string=str(input())
# letters=26
# sumation=0
# for i in string:
#     sumation+=ord(i)

# totaldiv=sumation//65
# print(totaldiv)
# remainder=sumation%65
# result=0
# if totaldiv>1:
#     result=letters*(totaldiv-1)+remainder
# else:
#     result=remainder
# print(result+1)
# n=13
# nops=1
# number=2
# while number<=n:
#     nops+=1
#     number*=2
# print(nops+((n-1)-(number/2)))

## Fractional Knapsack

# w=50
# values=[60,100,120]
# weight=[10,20,30]
# dicti={}
# for i in range(len(values)):
#     dicti[values[i]/weight[i]]=[values[i],weight[i]]
# print(dicti)
# wsum=0
# narr=dicti.keys()
# print(reversed(sorted(narr)))
# i=0
# while wsum<w:
#     if wsum==w:
#         break
#     if w-wsum>=dicti[narr[i]][1]:
#         wsum+=dicti[narr[i]][1]
#     else:
#         wsum+=(w-wsum)*dicti[narr[i]]
#     i+=1

# ## OVerlapping intevals
# arr=[900, 940, 950, 1100, 1500, 1800]
# dep=[910, 1200, 1120, 1130, 1900, 2000]
# narr=sorted(zip(arr,dep))
# resarr=[narr[0]]
# def overlap(resarr,i):
#     return resarr[-1][1] > interval[0]
# maxcount=0

# def overlapcheck(narr):
#     count=0
#     for i in range[1:]:
#         if overlap(resarr,i):
#             count+=1
#             maxcount=max(count,maxcount)
#             inteval=[min(resarr[-1][0],narr[i][0]),max(resarr[-1][1],narr[i][1])]
#             res.pop()
#             res.append(inteval)
#         else:
#             count=1
#             res.append(narr[i])

# arr=[2,3,1,1,4]
# i=0
# count=0
# while i<=len(arr)-1:
#     mj=0
#     cj=arr[i]
#     for j in range(i,i+arr[i]):
#         cj=arr[i]+arr[j]
#         if cj>mj:
#             mj=cj
#     i=i+arr[j]
#     count+=1

# print(count)

arr=['t','t','p','p','t','p']
count=0
k=1
for i in range(len(arr)):
    if arr[i]=="p":
        lend=i-k
        if lend<0:
            lend=0
        rend=i+k
        if i+k>=len(arr):
            rend=len(arr)-1
        subarr=arr[lend:rend+1]
        for j in range(len(subarr)):
            if subarr[j]=="t":
                arr[j]=='c'
                count+=1
                break
print(count)


        