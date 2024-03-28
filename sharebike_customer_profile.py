from tkinter import *
from PIL import ImageTk

import customer

bg_color = '#363636'
main_logo = None


def config(window, cust_id):
    window.title("Profile")
    window.geometry('800x1000')
    window.configure(bg=bg_color)

    # functions
    # instead of entry block create a function to display the corresponding data value from the database for the required field
    def show():
        data = customer.view_profile(cust_id)

        fname_content["text"] = data["fname"]
        lname_content["text"] = data["lname"]
        email_content["text"] = data["email"]
        phone_content["text"] = data["phnum"]
        account_content["text"] = data["bank_acc_nbr"]
        balance_content["text"] = data["balance"]
        password_content["text"] = data["password"]

    frame = Frame(window, bg=bg_color)

    # heading and logo
    global main_logo
    main_logo = ImageTk.PhotoImage(file="ShareBike.png")
    label = Label(frame, image=main_logo, bg=bg_color, height=250, width=250)
    label.grid(row=0, columnspan=3)

    login_lbl = Label(frame, text="Profile", bg=bg_color, fg="white", font=("Arial", 30))
    login_lbl.grid(row=1, column=0, columnspan=3, pady=20)

    # details
    fname_label = Label(frame, text="First Name : ", bg=bg_color, fg="white", font=("Arial", 16))
    fname_label.grid(row=2, column=0)

    lname_label = Label(frame, text="Last Name : ", bg=bg_color, fg="white", font=("Arial", 16))
    lname_label.grid(row=3, column=0)

    email_label = Label(frame, text="Email : ", bg=bg_color, fg="white", font=("Arial", 16))
    email_label.grid(row=4, column=0)

    phone_label = Label(frame, text="Phone Number. : ", bg=bg_color, fg="white", font=("Arial", 16))
    phone_label.grid(row=5, column=0)

    bank_acc_nbr_label = Label(frame, text="Bank Account Number : ", bg=bg_color, fg="white", font=("Arial", 16))
    bank_acc_nbr_label.grid(row=6, column=0)

    balance_label = Label(frame, text="Balance : ", bg=bg_color, fg="white", font=("Arial", 16))
    balance_label.grid(row=7, column=0)

    password_label = Label(frame, text="Password : ", bg=bg_color, fg="white", font=("Arial", 16))
    password_label.grid(row=8, column=0)

    # entrybox
    fname_content = Label(frame, font=("Arial", 13), bg=bg_color, fg="white")
    fname_content.grid(row=2, column=1, pady=20)

    lname_content = Label(frame, font=("Arial", 13), bg=bg_color, fg="white")
    lname_content.grid(row=3, column=1, pady=20)

    email_content = Label(frame, font=("Arial", 13), bg=bg_color, fg="white")
    email_content.grid(row=4, column=1, pady=20)

    phone_content = Label(frame, font=("Arial", 13), bg=bg_color, fg="white")
    phone_content.grid(row=5, column=1, pady=20)

    account_content = Label(frame, font=("Arial", 13), bg=bg_color, fg="white")
    account_content.grid(row=6, column=1, pady=20)

    balance_content = Label(frame, font=("Arial", 13), bg=bg_color, fg="white")
    balance_content.grid(row=7, column=1, pady=20)

    password_content = Label(frame, font=("Arial", 13), bg=bg_color, fg="white")
    password_content.grid(row=8, column=1, pady=20)

    show()

    frame.pack()

# window.mainloop()
