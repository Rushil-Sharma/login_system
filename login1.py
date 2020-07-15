from tkinter import *
from tkinter import ttk
import sys
from tkinter import messagebox

yes = 1
no = 2 

fail = yes

top = Tk()
top.title("Login Screen")
top.configure(background="light blue")



labl1 = Label(top, text="Username:-",bg="light blue",fg="red")
username = Entry(top, text="Enter a Username" ,width=50 ,relief="sunken",bd=3, borderwidth=5,bg="white",fg="black")
username.insert(0, 'Enter your user name...')
username.config(fg = 'grey')
labl2 = Label(top, text="Password:-",bg="light blue",fg="red")
password = Entry(top,text="Enter a Password", width=50 ,relief="sunken",bd=3, borderwidth=5,bg="white",fg="black")
password.insert(0, 'Enter your password...')
password.config(fg = 'grey')




def on_entry_click2(event):
    if username.get() == 'Enter your user name...':
        username.delete(0, END) # delete all the text in the entry
        username.config(fg = 'black')


def on_focusout2(event):
    if username.get() == '':
        username.insert(0, 'Enter your user name...')
        username.config(fg = 'grey')

username.bind("<FocusIn>", on_entry_click2)
username.bind("<FocusOut>", on_focusout2)

password_get = len(password.get())
username_get = len(username.get())

def on_entry_click1(event):
    if password.get() == 'Enter your password...':
        password.delete(0, END) # delete all the text in the entry
        password.config(fg = 'black')
    password_get = len(password.get())
    username_get = len(username.get())
    if password_get >= 1 :
        password['show']="*"

i = 1
def on_focusout1(event):
    if password.get() == '':
        password.insert(0, 'Enter your password...')
        password.config(fg = 'grey')


password.bind("<FocusIn>", on_entry_click1)
password.bind("<FocusOut>", on_focusout1)



def sys_exit():
    print("loging out")
    sys.exit(0)
    print("Done")

exit_code = Button(top, text="EXIT",relief="ridge",bd=5,command=sys_exit,padx=20,bg="black",fg="white")

password_get = password.get()
username_get = username.get()

def log_in_command():
    password_get = password.get()   
    username_get = username.get()

    if len(password_get) and len(username_get) >= 6 :
        password_get = password.get()
        username_get = username.get()
        global error
        error = Label(top,text="Please enter a username/password",bg="light blue",fg="red",padx=15)
        error['text'] ="..........................................✅.................................."
        error['fg'] = "dark green"
        fail = "no"
        error.grid(row=4,column=0,columnspan=3)

    elif len(password_get) or len(username_get) <= 5 and len(password_get) or len(username_get) != 0 :
        password_get = password.get()
        username_get = username.get()
        error = Label(top,text="Please enter a username/password",bg="light blue",fg="red",padx=15)
        error['text'] ="Please enter at least 6 charcter username and password  "
        error['fg'] = "dark blue"
        fail = "yes"
        error.grid(row=4,column=0,columnspan=3)

    elif len(password_get) or len(username_get) == 0 :
        password_get = password.get()
        username_get = username.get()
        error = Label(top,text="Please enter a username/password",bg="light blue",fg="red",padx=15)
        error['text'] ="Please enter a username/password"
        error['fg'] = "red"
        fail = "yes"
        error.grid(row=4,column=0,columnspan=3)          

    elif len(password_get) and len(username_get) <= 5 :
        error = Label(top,text="Please enter a username/password",bg="light blue",fg="red",padx=15)
        error['text'] ="Please enter at least 6 charcter username and password"
        error['fg'] = "dark blue"
        fail = "yes"
        error.grid(row=4,column=0,columnspan=3)
       

def save_user_command():
    yes_no = messagebox.askyesno("Save user name ","Are you sure you want to save it ?")
    password_get = ("*")*len(password.get())
    username_get = username.get()
    random123 = ("Username:-",username_get,"...Password:-",password_get)
    if yes_no == True:
        labl_yes = Label(top,text=random123,bg="light blue",fg="black") 
        labl_yes.grid(row=4,column=0,columnspan=3)
    elif yes_no == False:
        print()

save_user = Button(top, text="SAVE USER",relief="ridge",padx=195,bd=5,command=save_user_command,bg="black",fg="white")


log_in = Button(top, text="Next---->",relief="ridge",padx=140,bd=5,command=log_in_command,bg="black",fg="white")



labl1.grid(row=0,column=0)
username.grid(row=0,column=1,columnspan=2)
labl2.grid(row=1,column=0)
password.grid(row=1,column=1,columnspan=2)
exit_code.grid(row=2,column=0)
log_in.grid(row=2,column=2)
save_user.grid(row=3,column=0,columnspan=3)


top.mainloop()