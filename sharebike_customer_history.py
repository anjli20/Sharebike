from tkinter import *
from tkinter import ttk
import sqlite3

import customer

bg_color = '#363636'


def config(window, cust_id):
    def view_data():
        data = customer.history(cust_id)
        for item in data:
            row = [item["trip_id"], item["vehicle_id"], item["start_time"], item["end_time"],
                   item["charge"], item["start_station_name"], item["start_postcode"],
                   item["end_station_name"], item["end_postcode"]]
            tree.insert("", END, values=row)

    window.title("Travel History")
    window.geometry('1100x600')
    window.configure(bg=bg_color)

    # heading
    heading_label = Label(window, text="Travel History", font=('Arial', 20, 'bold'), bg=bg_color, fg='white')
    heading_label.pack(pady=20)

    # table
    frame = Frame(window, bg=bg_color)
    frame.pack(fill=BOTH, expand=YES, padx=10, pady=10)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))

    tree = ttk.Treeview(frame, columns=("Trip ID", "Vehicle ID", "Start Time", "End Time", "Charge",
                                        "Start Station", "Start Postcode", "End Station", "End Postcode"),
                        yscrollcommand=Scrollbar.set, xscrollcommand=Scrollbar.set)

    tree.grid(column=0, row=0, sticky='nsew')
    tree['show'] = 'headings'

    scrollbar = Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar_x = Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=scrollbar.set, xscrollcommand=scrollbar_x.set)
    tree.grid(column=0, row=0, sticky='nsew')

    scrollbar.grid(row=0, column=1, sticky='ns')
    scrollbar_x.grid(row=1, column=0, sticky='ew')

    tree.heading("#1", text="Trip ID", anchor='center')
    tree.heading("#2", text="Vehicle ID", anchor='center')
    tree.heading("#3", text="Start Time", anchor='center')
    tree.heading("#4", text="End Time", anchor='center')
    tree.heading("#5", text="Charge", anchor='center')
    tree.heading("#6", text="Origin", anchor='center')
    tree.heading("#7", text="Start Postcode", anchor='center')
    tree.heading("#8", text="Destination", anchor='center')
    tree.heading("#9", text="End Postcode", anchor='center')

    tree.column("#0", width=60, anchor='center')
    tree.column("#1", width=60, anchor='center')
    tree.column("#2", width=120, anchor='center')
    tree.column("#3", width=120, anchor='center')
    tree.column("#4", width=60, anchor='center')
    tree.column("#5", width=100, anchor='center')
    tree.column("#6", width=100, anchor='center')
    tree.column("#7", width=100, anchor='center')
    tree.column("#8", width=100, anchor='center')
    tree.column("#9", width=100, anchor='center')

    s = ttk.Style()
    s.configure('Treeview.Heading', background='black', foreground='dark blue')

    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar.grid(row=0, column=1, sticky='ns')
    scrollbar_x.grid(row=1, column=0, sticky='ew')

    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    view_data()

# window.mainloop()
