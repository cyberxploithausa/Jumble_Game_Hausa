import tkinter
from tkinter import *
import random
from tkinter import messagebox
from random import shuffle

root = tkinter.Tk()
root.geometry("500x600")
root.title("Cinkar Kalma")



amsa =["python", "youtube", "google", "nigeria", "tea", "coffee", "gida", "kasuwa", "makaranta", "asibiti", "shago", "gona", "walda", "noma", "kwano", "waya", "yazeed", "cyberxploit"]

kalmomi = []
for i in amsa:
    kalma = list(i)
    shuffle(kalma)
    kalmomi.append(kalma)

lamba = random.randint(0, len(kalmomi))

def initial():
    global kalmomi, lamba
    label.configure(text=kalmomi[lamba])


def ans_check():
    global kalmomi, lamba, amsa
    user_input = entry.get()
    if user_input == amsa[lamba]:
        messagebox.showinfo("Successful", "Daidai! Ka cinka kalma Daidai")
        Reset()
    else:
        messagebox.showinfo("Error", "Ba daidai bane! Ka cinka kalma ba daidai ba")
        entry.delete(0, END)

def Reset():
    global kalmomi, lamba, amsa
    lamba = random.randint(0, len(kalmomi))
    label.configure(text=kalmomi[lamba])
    entry.delete(0, END)

label = Label(root, font='times 20')
label.pack(pady=30, ipady=10, ipadx=10)

#amsa = StringVar()
entry = Entry(root, font=('times', 15, "bold"))
entry.pack(ipady=5, ipadx=5)

button = Button(root, text='Check', width=15, command=ans_check, bd=2)
button.pack(pady=40)

button1 = Button(root, text='Reset', width=15, command=Reset, bd=2)
button1.pack()

initial()

root.mainloop()