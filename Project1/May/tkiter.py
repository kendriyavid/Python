# from tkinter import *

# window=Tk() ## this initializes the window container 
# window.geometry('200x300')  # specifies the size
# window.title("first application")  # title
# label = Label(window,text="hello there")
# label.pack()
# window.mainloop() #this runs the initialized window on the display

# ## LABLE lable is area widget which can hold text or image in a window


# from tkinter import *
# from tkinter import messagebox
# window=Tk()
# window.title("first applciation")
# window.geometry('500x600')
# def hello():
#     messagebox.showwarning(title="heheeh atak",message='heheh ataccked your pc')
# lable=Label(window,text="Click Here")
# button=Button(window,text="Do not Click",command=hello)
# button.pack()
# lable.pack()
# window.mainloop()

from tkinter import *
from tkinter import messagebox
window=Tk()
label=Label(window,text="hello there",background='blue')
window.geometry('400x400')
label.pack()
def text():
    print(entry.get())
def function():
    bool=messagebox.askokcancel(message="Koko Eating bananas",title='yorn')
    if bool:
        print("yes")
def delete():
    entry.delete(len(entry.get())-1,END)
button=Button(window,text='Click me',command=delete,background='red')
button.pack()
entry=Entry(window,font=('Arial',50))
entry.pack()
window.mainloop()


#CANVAS
# from tkinter import *
# from tkinter import Canvas

# window=Tk()
# canvas=Canvas(window,height=500,width=500)
# canvas.pack()
# canvas.create_rectangle(50,50,250,250,width=10,outline='blue')
# window.mainloop()

## Multithreadign practice

# import threading
# import time

# def eating():
#     time.sleep(5)
#     print("iam eating")
# def sleeping():
#     time.sleep(6)
#     print("iam sleepign")
# def hehe():
#     time.sleep(9)
#     print("hereherheh")

# x=threading.Thread(eating)
# try:
#     file = open('document.txt','a')
#     print(file.write("helllo there"))
# except IOError as e:
#     print(e)
# finally:
#     file.close()


