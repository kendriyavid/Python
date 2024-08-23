from tkinter import *
# from tkinter import messagebox
window=Tk()
def click():
    # while True:
        msg=messagebox.showwarning(message="Say Hello", title="Hello World")
window.geometry('500x500')
label=Label(window,text="Hello there",bg='red')
label.pack()
button=Button(window,text='Donot Click',command=click,bg="blue")
button.pack()
entry=Entry(font=("Arial",20))
entry.pack()
window.mainloop()

# from tkinter import *
# window=Tk()
# canvas=Canvas(width=200,height=200)
# canvas.create_rectangle(200,200,100,100)
# canvas.pack()
# window.mainloop()
import os
import threading 
import time
def talk():
    time.sleep(3)
    print(os.getpid())
def talk2():
    time.sleep(4)
    print(os.getpid())
x=threading.Thread(target=talk,args=())
x.start()
y=threading.Thread(target=talk2,args=())
y.start()

x.join()
y.join()

print(threading.current_thread())
print("done")