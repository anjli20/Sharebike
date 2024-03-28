from tkinter import *
from tkinter import messagebox, ttk

from PIL import ImageTk

import dbFun
import enum_values
import general
import sharebike_customer

bg_color = '#363636'
main_logo = None


def config(window):
    window.title("Customer | Login")
    window.geometry('600x750')
    window.configure(bg=bg_color)
    width = window.winfo_screenwidth() // 2
    # would leave a 10% of gap from the top and bottom of the screen
    height = int(window.winfo_screenheight() * 0.1)
    # Setting the actual geometry now
    window.geometry('400x600+' + str(width) + '+' + str(height))

    # functions
    def login():
        email = email_e.get()
        password = password_e.get()

        if general.sign_in(enum_values.UserType.CUSTOMER.value, email, password):
            messagebox.showinfo("Information", "Log in Successfully!")

            cust_id = dbFun.get_cust_id(email)
            customer_window = Toplevel()
            sharebike_customer.config(customer_window, cust_id)
            window.withdraw()
            customer_window.deiconify()
        else:
            messagebox.showerror("Error", "Email and Password Mismatch")

        clear()

    def clear():
        email_e.delete(0, END)
        password_e.delete(0, END)

    # def jump_to_register():
    #     import sharebike_register
    #     register_window = Toplevel()
    #     sharebike_register.config(register_window)
    #     window.withdraw()
    #     register_window.deiconify()

    frame = Frame(window, bg=bg_color)

    # heading and logo
    global main_logo
    main_logo = ImageTk.PhotoImage(file="ShareBike.png")
    label = Label(frame, image=main_logo, bg=bg_color, height=250, width=250)
    label.grid(row=0, column=0, columnspan=2)

    login_lbl = Label(frame, text="Customer Log In", bg=bg_color, fg="white", font=('TkMenuFont', 14))
    login_lbl.grid(row=1, column=0, columnspan=2, pady=40)

    # var = StringVar()
    # var.set(enum_values.UserType.CUSTOMER.value)
    #
    # style = ttk.Style()
    # style.configure("Custom.TRadiobutton", background=bg_color, foreground="white")
    #
    # r1 = ttk.Radiobutton(frame, text='Customer', variable=var, value=enum_values.UserType.CUSTOMER.value,
    #                      style="Custom.TRadiobutton")
    # r1.grid(row=2, column=0)
    #
    # r2 = ttk.Radiobutton(frame, text='Operator', variable=var, value=enum_values.UserType.OPERATOR.value,
    #                      style="Custom.TRadiobutton")
    # r2.grid(row=2, column=1)
    #
    # r3 = ttk.Radiobutton(frame, text='Manager', variable=var, value=enum_values.UserType.MANAGER.value,
    #                      style="Custom.TRadiobutton")
    # r3.grid(row=2, column=2)

    # details
    email_lbl = Label(frame, text="Email", bg=bg_color, fg="white", )
    email_lbl.grid(row=2, column=0)

    email_e = Entry(frame, font=("Arial", 13))
    email_e.grid(row=2, column=1, pady=20)

    password_lbl = Label(frame, text="Password ", bg=bg_color, fg="white", )
    password_lbl.grid(row=4, column=0)

    password_e = Entry(frame, font=("Arial", 13))
    password_e.grid(row=4, column=1, pady=20)

    # buttons
    login_btn = Button(frame, text="Log In", bg=bg_color, fg="white", width=10, command=login)
    login_btn.grid(row=5, column=0, pady=30)

    clear_btn = Button(frame, text="Clear", bg=bg_color, fg="white", width=10,command=clear)
    clear_btn.grid(row=5, column=1, pady=30)

    # sign_up_button = Button(frame, text="Create New Account", bg=bg_color, fg="white", command=jump_to_register)
    # sign_up_button.grid(row=6, columnspan=2)

    frame.pack()
