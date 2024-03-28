from tkinter import *

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


def config(window):
    window.title("Track Vehicle")
    window.geometry("500x400")
    window.configure(background=bg_color)
    lbl = Label(window, text="Vehicle Details", font=('Arial', '15'))
    lbl.place(x=10,y=30)
    lbl["bg"] = bg_color
    lbl["fg"] = "white"
    lbl = Label(window, text="Vehicle Number --- Current Location", font=('Arial', '10'))
    lbl.place(x=10, y=60)
    lbl["bg"] = bg_color
    lbl["fg"] = "yellow"
    name_box = Listbox(window)
    name_box.place(x=10, y=90, width=250, height=80)
    populate_vehicle_status(name_box)


def populate_vehicle_status(name_box):
    vehicle_dtls = employee.track_vehicle()
    for vehicle_id, vehicle_dtls in vehicle_dtls.items():
        total_info = "vehicle" + str(vehicle_id) + "[" + dbFun.get_type(
                    vehicle_id) + "]" + "---" + dbFun.check_status(vehicle_id) + "---" + vehicle_dtls[3]
        name_box.insert(END, total_info)
