import tkinter as tk
# using Pillow library for importing images from the system
from PIL import ImageTk
from tkinter import *

import customer
import dbFun

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
    window.title('ShareBike | Report - Customer')
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
            text="Report a bike!",
            bg=bg_color,
            fg="white",  # text color
            font=('TkMenuFont', 14)
        ).pack(pady=20)  # pady is used to create a padding along the y axis

        tk.Label(
            main_frame,
            text="Location",
            bg=bg_color,
            fg="white",
        ).place(x=170, y=320)

        loc_selected_option = tk.StringVar()

        locations = dbFun.get_locations()
        station_list = []
        for location in locations:
            station_list.append(location[1])

        location_dropdown = tk.OptionMenu(main_frame, loc_selected_option, *station_list)
        location_dropdown.place(x=150, y=350, width=100)

        tk.Label(
            main_frame,
            text="Vehicle ID",
            bg=bg_color,
            fg="white",
        ).place(x=170, y=390)

        vehicle_selected_option = tk.StringVar()

        vehicle_ids = [""]

        vehicle_dropdown = tk.OptionMenu(main_frame, vehicle_selected_option, *vehicle_ids)
        vehicle_dropdown.place(x=150, y=420, width=100)

        def on_selected_location(name, index, mode):
            selected_loc = loc_selected_option.get()
            vehicle_dropdown['menu'].delete(0, END)

            selected_loc_id = dbFun.get_loc_id(selected_loc)
            vehicle_ids = customer.get_local_vehicles(selected_loc_id)

            for vehicle_id in vehicle_ids:
                vehicle_dropdown['menu'].add_command(label="vehicle" + str(vehicle_id) + "[" + dbFun.get_type(
                    vehicle_id) + "]" + "---" + dbFun.check_status(vehicle_id),
                                                     command=lambda v=vehicle_id: vehicle_selected_option.set(v))

        loc_selected_option.trace("w", on_selected_location)

        tk.Label(
            main_frame,
            text="Status",
            bg=bg_color,
            fg="white",
        ).place(x=180, y=460)

        status_selected_option = tk.StringVar()
        status_options = ['LOWPOWER', 'BROKEN']
        dropdown = tk.OptionMenu(main_frame, status_selected_option, *status_options)
        dropdown.place(x=150, y=490, width=100)

        # Report Button
        tk.Button(
            main_frame,
            text='Report',
            font=("TkHeadingFont", 10),
            bg='#191919',
            fg='white',
            width=10,
            activebackground='#000000',
            activeforeground='white',
            command=lambda: report_button(vehicle_selected_option, loc_selected_option, status_selected_option)
        ).place(x=155, y=540)

    # view_report_function
    def report_button(vehicle_selected_option, loc_selected_option, status_selected_option):
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

        print('View report button clicked!!!')

        # integrate with the back end
        vehicle_id = vehicle_selected_option.get()
        status = status_selected_option.get()
        location_id = dbFun.get_loc_id(loc_selected_option.get())
        customer.report(int(vehicle_id), status, int(location_id))

    load_main_frame()
