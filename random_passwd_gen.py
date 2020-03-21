#python program to generate random password
#using Tkinter Module

import random
import pyperclip
from tkinter import *
from tkinter.ttk import *

#function for calculation of password
def low():
    entry.delete(0,END)

    #get the length of password
    length = var1.get()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !@#$%^&*()~"
    password=""


    #if strength selected is low
    if var.get()==1:
        for i in range(0,length):
            password=password + random.choice(lower)
        return password
    #if strength selected is medium 
    elif var.get()==0:
        for i in range(0,length):
            password=password + random.choice(upper)
        return password   

    #if strength selected is strong
    elif var.get()==3:
        for i in range(0,length):
            password=password + random.choice(digits)
        return password        
    else:
        print("Please Choose an option") 

#function for generation of password
def generate():
    password1 = low()
    entry.insert(10,password1)

#function for copying password to clipboard
def copyclip():
    random_password = entry.get()
    pyperclip.copy(random_password)

# main function

# create GUI window
root=Tk()
var=IntVar()
var1=IntVar()

# Title of your GUI window
root.title("Random Password Generator BY Coding Planet")

# create label and entry to show
# password generated

Random_password =Label(root,text="Password")
Random_password.grid(row=0)
entry=Entry(root)

entry.grid(row=0,column=1)

# create label for length of password
c_label=Label(root,text="Length")
c_label.grid(row=1)

# create buttons copy which will copy the password
# generated to clipboard and generate which will generate a 
# new random password 

copy_button= Button(root,text="Copy",command=copyclip)
copy_button.grid(row=0,column=2)

generate_button= Button(root,text="Generate",command=generate)
generate_button.grid(row=0,column=3)

# radio buttons for deciding the strength of password 
#default strength is medium

radio_low=Radiobutton(root,text="Low",variable=var,value=1)
radio_low.grid(row=1,column=2,sticky='E')


radio_med=Radiobutton(root,text="Medium",variable=var,value=0)
radio_med.grid(row=1,column=3,sticky='E')


radio_strong=Radiobutton(root,text="Strong",variable=var,value=3)
radio_strong.grid(row=1,column=4,sticky='E')

combo=Combobox(root,textvariable=var1)

# combobox for length of ur password 

combo['values']=(8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
25,26,27,28,29,30,31,32,"Length")

combo.current(0)

combo.bind('<<ComboboxSelected>>')
combo.grid(column=1,row=1)

# time to start the GUI 

root.mainloop()

