# # import tkinter as tk
# # from tkinter import messagebox

# # def submit():
# #     response = messagebox.askyesno("Confirmation", "Do you want to submit?")
# #     if response:
# #         print("Data submitted successfully!")
# #     else:
# #         print("Submission canceled.")

# # root = tk.Tk()
# # root.geometry("200x100")

# # b1 = tk.Button(root, text='Submit', command=submit)
# # b1.pack()

# # root.mainloop()

# import threading
# import os

# def talk():
#     print('twice is assigned to thread:{}'.format(threading.current_thread().name))
#     print("sfioioiefjse {}".format(os.getpid()))
# def tasks2():
#     print('twice is assigned to thread:{}'.format(threading.current_thread().name))
#     print("sfioioiefjse {}".format(os.getpid()))

# if __name__=='__main__':

# wap tofin the longst word from list
# wap to create multiple text file inside the single directory
#inheritance, polymorphism etc
#opeator overloading
# opertators arithematic, logical, boolean
# conversion binary to hexadecimal tec
# exception handeling 
# wap to create class for modeling triangle 
# explain the concept of the pipes as data stream in python

# class Node:
#     def __init__(self,val=None):
#         self.left=None
#         self.val=val
#         self.right=None

# class Tree:
#     def __init__(self,root=None):
#         self.root=root 
# resarr=[0]*len(arr)
# def permtrans(i,j,arr,node,height,resarr):
#     if i>=j:
#         return None
#     maximum=arr.index(max(arr[i:j]))
#     resarr[maximum]=height
#     if not node:
#         node=Tree(Node(maximum))
#     node.left=permtrans(i,maximum,arr,node,height+1,resarr)
#     node.right=permtrans(maximum+1,j,arr,node,height+1,resarr)
#     return node
# permtrans(0,len(arr),arr,None,0,resarr)
# print(resarr)


arr=[3,5,8,15,19]
low=0
target=7
high=len(arr)-1
prev=0
while low<=high:
    mid=(low+high)//2
    if arr[mid]>=target:
        prev=mid
        low=mid+1
    elif target<mid:
        high=mid-1
print(prev)

