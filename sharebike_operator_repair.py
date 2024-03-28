import re
import tkinter as tk
# using Pillow library for importing images from the system
from PIL import ImageTk
from tkinter import *
import time

import dbFun
import employee

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
    window.title('ShareBike | Repair - Operator')
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
            text="Repair a bike!",
            bg=bg_color,
            fg="white",  # text color
            font=('TkMenuFont', 14)
        ).pack(pady=20)  # pady is used to create a padding along the y axis

        tk.Label(
            main_frame,
            text="Select Vehicle ID",
            bg=bg_color,
            fg="white",
        ).place(x=150, y=320)

        selected_option = populate_dropdown(main_frame)

        # Repair Button
        btn = tk.Button(
            main_frame,
            text='Repair',
            font=("TkHeadingFont", 10),
            bg='#191919',
            fg='white',
            activebackground='#000000',
            activeforeground='white',
            command=lambda: repair_button(selected_option)
        )
        btn.place(x=180, y=450)

        if selected_option.get() == 'No Vehicle':
            btn.configure(state="disabled")

    def populate_dropdown(move_vehicle_window):
        # selection = name_box.curselection()
        # print(selection)
        # print(name_box.get(selection[0]))
        # fetched_string_array = name_box.get(selection[0]).split("---")
        # current_location = fetched_string_array[1]
        filtered_location = []
        vehicle_dtls = employee.track_vehicle()
        for vehicle_id, vehicle_dtls in vehicle_dtls.items():
            if vehicle_dtls[2] == 'BROKEN':
                total_info = "vehicle" + str(vehicle_id) + "[" + dbFun.get_type(
                    vehicle_id) + "]" + "---" + dbFun.check_status(vehicle_id) + "---" + vehicle_dtls[3]
                filtered_location.append(total_info)
        clicked = StringVar(move_vehicle_window)
        if len(filtered_location) < 1:
            filtered_location.append("No Vehicle")
        clicked.set(filtered_location[0])
        drop = OptionMenu(move_vehicle_window, clicked, *filtered_location)
        drop.place(x=130, y=360, width="150")
        if filtered_location[0] == "No Vehicle":
            drop.configure(state="disabled")
        return clicked

    def repair_button(optionbox_selection):
        selected_option = optionbox_selection.get()
        fetched_string_array = selected_option.split("---")
        vehicle_id = re.findall(r'\d+', fetched_string_array[0])[0]
        selected_location = fetched_string_array[0]
        location_dct = employee.fetch_all_location_info_in_dict()
        location = find_location_id(location_dct, fetched_string_array[2])
        time1 = time.time()
        employee.update_vehicle_charge(vehicle_id, time1, "VACANT", location)
        tk.messagebox.showinfo("Vehicle Repaired", "Vehicle " + selected_option + " has  been repaired")

    def find_location_id(location_dct, to_match):
        for key, value in location_dct.items():
            if value == to_match:
                return key

    load_main_frame()
