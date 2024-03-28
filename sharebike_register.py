from tkinter import *
from tkinter import messagebox, ttk

from PIL import ImageTk
import enum_values
import general

bg_color = '#363636'
main_logo = None


def config(window):
    window.title("Sign Up")
    window.geometry('500x840')
    window.configure(bg=bg_color)

    # functions
    def signup():
        bank_acc_nbr = bank_acc_nbr_e.get()
        fname = fname_e.get()
        lname = lname_e.get()
        email = email_e.get()
        phnum = phone_e.get()
        password = password_e.get()

        if var.get() == enum_values.UserType.CUSTOMER.value:
            general.sign_up(password, fname, lname, email, phnum, bank_acc_nbr)
        else:
            general.sign_up_inner(var.get(), password, fname, lname, email, phnum)

        messagebox.showinfo("Information", "Register Successfully!")
        clear()

    def clear():
        bank_acc_nbr_e.delete(0, END)
        fname_e.delete(0, END)
        lname_e.delete(0, END)
        email_e.delete(0, END)
        phone_e.delete(0, END)
        password_e.delete(0, END)

    frame = Frame(window, width=400, height=600, bg=bg_color)

    # heading and logo
    global main_logo
    main_logo = ImageTk.PhotoImage(file="ShareBike.png")
    label = Label(frame, image=main_logo, bg=bg_color, height=250, width=250)
    label.grid(row=0, columnspan=3)

    login_lbl = Label(frame, text="Sign Up", bg=bg_color, fg="white", font=('TkMenuFont', 14))
    login_lbl.grid(row=1, column=0, columnspan=3, pady=20)

    var = StringVar()
    var.set(enum_values.UserType.CUSTOMER.value)

    style = ttk.Style()
    style.configure("Custom.TRadiobutton", background=bg_color, foreground="black")

    r1 = ttk.Radiobutton(frame, text='Customer', variable=var, value=enum_values.UserType.CUSTOMER.value, style="Custom.TRadiobutton")
    r1.grid(row=3, column=0)

    r2 = ttk.Radiobutton(frame, text='Operator', variable=var, value=enum_values.UserType.OPERATOR.value, style="Custom.TRadiobutton")
    r2.grid(row=3, column=1)

    r3 = ttk.Radiobutton(frame, text='Manager', variable=var, value=enum_values.UserType.MANAGER.value, style="Custom.TRadiobutton")
    r3.grid(row=3, column=2)

    bank_acc_nbr_label = Label(frame, text="Bank Account Number : ", bg=bg_color, fg='white')
    bank_acc_nbr_label.grid(row=4, column=0)

    bank_acc_nbr_e = Entry(frame, font=("Arial", 13))
    bank_acc_nbr_e.grid(row=4, column=1, pady=20)

    fname_label = Label(frame, text="First Name : ", bg=bg_color, fg='white')
    fname_label.grid(row=5, column=0)

    fname_e = Entry(frame, font=("Arial", 13))
    fname_e.grid(row=5, column=1, pady=20)

    lname_label = Label(frame, text="Last Name : ", bg=bg_color, fg='white')
    lname_label.grid(row=6, column=0)

    lname_e = Entry(frame, font=("Arial", 13))
    lname_e.grid(row=6, column=1, pady=20)

    email_label = Label(frame, text="Email : ", bg=bg_color, fg='white')
    email_label.grid(row=7, column=0)

    email_e = Entry(frame, font=("Arial", 13))
    email_e.grid(row=7, column=1, pady=20)

    phone_label = Label(frame, text="Phone Number : ", bg=bg_color, fg='white')
    phone_label.grid(row=8, column=0)

    phone_e = Entry(frame, font=("Arial", 13))
    phone_e.grid(row=8, column=1, pady=20)

    password_label = Label(frame, text="Password : ", bg=bg_color, fg='white')
    password_label.grid(row=9, column=0)

    password_e = Entry(frame, font=("Arial", 13))
    password_e.grid(row=9, column=1, pady=20)

    # buttons
    signup_btn = Button(frame, text="Sign Up", bg='#191919', fg='white', command=signup)
    signup_btn.grid(row=10, column=0, pady=30)

    clear_btn = Button(frame, text="Clear", bg='#191919', fg='white', command=clear)
    clear_btn.grid(row=10, column=2, pady=30)

    frame.pack()
