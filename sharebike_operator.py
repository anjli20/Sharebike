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


# initialization
def config(window):
    window.title('ShareBike | Home - Operator')
    # window.eval("tk::PlaceWindow . center")
    # taking the half of whatever screen this code would be running on
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
                text="Let's help our customers",
                bg=bg_color,
                fg="white",  # text color
                font=('TkMenuFont', 14)
            ).pack(pady=20)  # pady is used to create a padding along the y axis

            # Adding Track Button
            tk.Button(
                main_frame,
                text='Track',
                font=("TkHeadingFont", 10),
                bg='#191919',
                fg='white',
                width=10,
                activebackground='#000000',
                activeforeground='white',
                command=lambda: track_button()
            ).pack(pady=5)

            # Adding Charge Button
            tk.Button(
                main_frame,
                text='Charge',
                font=("TkHeadingFont", 10),
                bg='#191919',
                fg='white',
                width=10,
                activebackground='#000000',
                activeforeground='white',
                command=lambda: charge_button()
            ).pack(pady=5)

            # Adding Move Button
            tk.Button(
                main_frame,
                text='Move',
                font=("TkHeadingFont", 10),
                bg='#191919',
                fg='white',
                width=10,
                activebackground='#000000',
                activeforeground='white',
                command=lambda: move_button()
            ).pack(pady=5)

            # Adding Repair Button
            tk.Button(
                main_frame,
                text='Repair',
                font=("TkHeadingFont", 10),
                bg='#191919',
                fg='white',
                width=10,
                activebackground='#000000',
                activeforeground='white',
                command=lambda: repair_button()
            ).pack(pady=5)

        # track_function
        def track_button():
            # widget protection so they don't get modified due to the other frame
            import sharebike_operator_track

            track_window = tk.Toplevel()
            sharebike_operator_track.config(track_window)
            track_window.deiconify()

        # charge fuction
        def charge_button():
            import sharebike_operator_charge

            charge_window = tk.Toplevel()
            sharebike_operator_charge.config(charge_window)
            charge_window.deiconify()

        # return fuction
        def move_button():
            import sharebike_operator_move

            move_window = tk.Toplevel()
            sharebike_operator_move.config(move_window)
            move_window.deiconify()

        # report fuction
        def repair_button():
            import sharebike_operator_repair

            repair_window = tk.Toplevel()
            sharebike_operator_repair.config(repair_window)
            repair_window.deiconify()

    load_main_frame()
