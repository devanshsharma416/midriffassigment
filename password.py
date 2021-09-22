from tkinter import *
import random, string


root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("Javatpoint - PASSWORD Password_Generator")
Label(root, text = 'PASSWORD Password_Generator TOOL' , font = ('calibri 16 bold')).pack()
Label(root, text ='Javatpoint', font ='calibri 16 bold').pack(side = BOTTOM)

password_label = Label(root, text = ' Select PASSWORD LENGTH', font = 'Calibri 12 bold').pack()
password_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = password_len , width = 18).pack()

pass_str = StringVar()
def Password_Generator():
    password = ''

    for x in range(0,4):
        Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(password_len.get()- 4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(root, text = "GENERATE PASSWORD" , command = Password_Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

root.mainloop() 