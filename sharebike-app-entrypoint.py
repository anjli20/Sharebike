import tkinter as tk
# using Pillow library for importing images from the system
from PIL import ImageTk
from tkinter import *
import importlib

# storing not so easy string to remember in a variable so that it can be reusable
bg_color = '#363636'
"""
#function for clearing the widgets
def clear_widgets(frame):
    #selecting all widgets within the frame
    for widget in frame.winfo_children():
        widget.destroy()
"""


# initializing the main_frame
def load_main_frame():
    main_frame.pack_propagate(
        False)  # using a function which would prevent the child label element to affect the parent frame element
    # main_frame widgets
    main_logo = ImageTk.PhotoImage(file="ShareBike.png")
    logo_widget = tk.Label(main_frame, image=main_logo, bg=bg_color, height=250, width=250)
    logo_widget.image = main_logo
    logo_widget.pack()

    # adding texts in the main_widget
    tk.Label(
        main_frame,
        text='Ready to bike along the streets?',
        bg=bg_color,
        fg="white",  # text color
        font=('TkMenuFont', 14)
    ).pack(pady=20)  # pady is used to create a padding along the y axis

    # Adding Customer options
    tk.Button(
        main_frame,
        text='Customer',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        width=20,
        activebackground='#000000',
        activeforeground='white',
        command=lambda: view_customer_options()
    ).pack(pady=5)

    # Adding Employee option
    tk.Button(
        main_frame,
        text='Operator',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        width=20,
        activebackground='#000000',
        activeforeground='white',
        command=lambda: view_employee_options()
    ).pack(pady=5)

    # Adding Manager Options
    tk.Button(
        main_frame,
        text='Manager',  # test codesnippi
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        width=20,
        activebackground='#000000',
        activeforeground='white',
        command=lambda: manager_view()
    ).pack(pady=5)

    # Create new account
    tk.Button(
        main_frame,
        text='SIGN UP',  # test codesnippi
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        width=10,
        activebackground='#000000',
        activeforeground='white',
        command=lambda: sign_up()
    ).pack(pady=20)



# view profile function
def view_customer_options():
    import sharebike_customer_login
    login_widow = tk.Toplevel()
    sharebike_customer_login.config(login_widow)
    login_widow.deiconify()


# rent fuction
def view_employee_options():
    import sharebike_operator_login
    login_widow = tk.Toplevel()
    sharebike_operator_login.config(login_widow)
    login_widow.deiconify()


# return fuction
def manager_view():
    import sharebike_manager_login
    login_widow = tk.Toplevel()
    sharebike_manager_login.config(login_widow)
    login_widow.deiconify()


def sign_up():
    import sharebike_register
    register_window = Toplevel()
    sharebike_register.config(register_window)
    register_window.deiconify()



# initialization
root = tk.Tk()
root.title('ShareBike | Home')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
width = root.winfo_screenwidth() // 2
# would leave a 10% of gap from the top and bottom of the screen
height = int(root.winfo_screenheight() * 0.1)
# Setting the actual geometry now
root.geometry('400x600+' + str(width) + '+' + str(height))

main_frame = tk.Frame(root, width=400, height=600, bg=bg_color)

view_profile_frame = tk.Frame(root, bg=bg_color)

for frame in (main_frame, view_profile_frame):
    frame.grid(row=0, column=0)

load_main_frame()

# running the application
root.mainloop()
