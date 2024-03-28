import tkinter as tk
# using Pillow library for importing images from the system
from PIL import ImageTk
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


# initialization
def config(window, cust_id):
    window.title('ShareBike | Home - Customer')
    window.rowconfigure(0, weight=1)
    window.columnconfigure(0, weight=1)
    width = window.winfo_screenwidth() // 2
    # would leave a 10% of gap from the top and bottom of the screen
    height = int(window.winfo_screenheight() * 0.1)
    # Setting the actual geometry now
    window.geometry('400x600+' + str(width) + '+' + str(height))

    main_frame = tk.Frame(window, width=400, height=600, bg=bg_color)

    view_profile_frame = tk.Frame(window, bg=bg_color)

    for frame in (main_frame, view_profile_frame):
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
            text='Ready to bike along the streets?',
            bg=bg_color,
            fg="white",  # text color
            font=('TkMenuFont', 14)
        ).pack(pady=20)  # pady is used to create a padding along the y axis

        # Adding View Profile Button
        tk.Button(
            main_frame,
            text='View Profile',
            font=("TkHeadingFont", 10),
            bg='#191919',
            fg='white',
            width=15,
            activebackground='#000000',
            activeforeground='white',
            command=lambda: view_profile_button()
        ).pack(pady=5)

        # Adding Rent Button
        tk.Button(
            main_frame,
            text='Rent',
            font=("TkHeadingFont", 10),
            bg='#191919',
            fg='white',
            width=15,
            activebackground='#000000',
            activeforeground='white',
            command=lambda: rent_button()
        ).pack(pady=5)

        # Adding Return Button
        tk.Button(
            main_frame,
            text='Return',
            font=("TkHeadingFont", 10),
            bg='#191919',
            fg='white',
            width=15,
            activebackground='#000000',
            activeforeground='white',
            command=lambda: return_button()
        ).pack(pady=5)

        # Adding Report Button
        tk.Button(
            main_frame,
            text='Report',
            font=("TkHeadingFont", 10),
            bg='#191919',
            fg='white',
            width=15,
            activebackground='#000000',
            activeforeground='white',
            command=lambda: report_button()
        ).pack(pady=5)

        # Pay Button
        tk.Button(
            main_frame,
            text='Pay',
            font=("TkHeadingFont", 10),
            bg='#191919',
            fg='white',
            width=15,
            activebackground='#000000',
            activeforeground='white',
            command=lambda: pay_button()
        ).pack(pady=5)

        # Transaction History Button
        tk.Button(
            main_frame,
            text='History',
            font=("TkHeadingFont", 10),
            bg='#191919',
            fg='white',
            width=15,
            activebackground='#000000',
            activeforeground='white',
            command=lambda: transaction_history_button()
        ).pack(pady=5)

    # view profile function
    def view_profile_button():
        # # widget protection so they don't get modified due to the other frames
        # view_profile_frame.pack_propagate(False)
        # # clearing the widgets of main_frame
        # # clear_widgets(load_main_frame)
        # # raising the view_profile_frame on the top
        # view_profile_frame.tkraise()
        #
        # main_logo = ImageTk.PhotoImage(file="ShareBike.png")
        # logo_widget = tk.Label(view_profile_frame, image=main_logo, bg=bg_color, height=250, width=250)
        # logo_widget.image = main_logo
        # logo_widget.pack()
        #
        # # Back Button
        # tk.Button(
        #     view_profile_frame,
        #     text='BACK',
        #     font=("TkHeadingFont", 10),
        #     bg='#191919',
        #     fg='white',
        #     activebackground='#000000',
        #     activeforeground='white',
        #     command=lambda: load_main_frame()
        # ).pack()
        #
        # print('View Profile button clicked!!!')

        # rent fuction
        import sharebike_customer_profile

        profile_window = tk.Toplevel()
        sharebike_customer_profile.config(profile_window, cust_id)
        profile_window.deiconify()

    def rent_button():
        import sharebike_customer_rent

        rent_window = tk.Toplevel()
        sharebike_customer_rent.config(rent_window, cust_id)
        rent_window.deiconify()

    # return fuction
    def return_button():
        import sharebike_customer_return

        return_window = tk.Toplevel()
        sharebike_customer_return.config(return_window, cust_id)
        return_window.deiconify()

    # report fuction
    def report_button():
        import sharebike_customer_report

        report_window = tk.Toplevel()
        sharebike_customer_report.config(report_window, cust_id)
        report_window.deiconify()

    # pay function
    def pay_button():
        import sharebike_customer_pay

        pay_window = tk.Toplevel()
        sharebike_customer_pay.config(pay_window, cust_id)
        pay_window.deiconify()

    # transaction history function
    def transaction_history_button():
        import sharebike_customer_history

        history_window = tk.Toplevel()
        sharebike_customer_history.config(history_window, cust_id)
        history_window.deiconify()

    load_main_frame()
