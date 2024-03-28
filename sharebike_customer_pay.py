import tkinter as tk
# using Pillow library for importing images from the system
from PIL import ImageTk

import customer

# storing not so easy string to remember in a variable so that it can be reusable
bg_color = '#363636'
"""
#function for clearing the widgets
def clear_widgets(frame):
    #selecting all widgets within the frame
    for widget in frame.winfo_children():
        widget.destroy()
"""


# initialization
def config(window, cust_id):
    window.title('ShareBike | Pay - Customer')
    # window.eval("tk::PlaceWindow . center")
    # taking the half of whatever screen this code would be running on
    width = window.winfo_screenwidth() // 2
    # would leave a 10% of gap from the top and bottom of the screen
    height = int(window.winfo_screenheight() * 0.1)
    # Setting the actual geometry now
    window.geometry('400x600+' + str(width) + '+' + str(height))

    main_frame = tk.Frame(window, width=400, height=600, bg=bg_color)
    view_report_frame = tk.Frame(window, bg=bg_color)

    for frame in (main_frame, view_report_frame):
        frame.grid(row=0, column=0)

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
            text="Pay for your bike!",
            bg=bg_color,
            fg="white",  # text color
            font=('TkMenuFont', 14)
        ).pack(pady=20)  # pady is used to create a padding along the y axis

        tk.Label(
            main_frame,
            text="Amount",
            bg=bg_color,
            fg="white",
        ).place(x=120, y=350)

        # global amount

        amount_box = tk.Entry(
            main_frame,
            bg='#191919',
            fg='white',
        )
        amount_box.place(x=200, y=350)

        # Pay Button
        tk.Button(
            main_frame,
            text='Pay',
            font=("TkHeadingFont", 10),
            bg='#191919',
            fg='white',
            width=10,
            activebackground='#000000',
            activeforeground='white',
            command=lambda: pay_button(amount_box)
        ).place(x=155, y=400)

    # pay_function
    def pay_button(amount_box):
        # widget protection so they don't get modified due to the other frames
        view_report_frame.pack_propagate(False)
        # clearing the widgets of main_frame
        # clear_widgets(load_main_frame)
        # raising the view_profile_frame on the top
        view_report_frame.tkraise()

        main_logo = ImageTk.PhotoImage(file="ShareBike.png")
        logo_widget = tk.Label(view_report_frame, image=main_logo, bg=bg_color, height=250, width=250)
        logo_widget.image = main_logo
        logo_widget.pack()

        # Back Button
        tk.Button(
            view_report_frame,
            text='BACK',
            font=("TkHeadingFont", 10),
            bg='#191919',
            fg='white',
            activebackground='#000000',
            activeforeground='white',
            command=lambda: load_main_frame()
        ).pack()

        print('Pay button clicked!!!')

        # integrate with the back end
        amount = amount_box.get()
        customer.pay(cust_id, float(amount))

    load_main_frame()
