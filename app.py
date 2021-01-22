from classes import RevenueCenter
from utilities import amsurg_rev
import tkinter as tk
from tkinter import ttk


amsurg = RevenueCenter(amsurg_rev)


root = tk.Tk()
root.title("Revenue Analysis")
root.geometry("600x400")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)


stats = tk.Button(root, text="Calculate Amsurg Stats", bg='green', fg='white', command=amsurg.print_stats)
stats.grid(column=0, row=0,  ipadx=10, ipady=10, sticky='NSEW')

visits_facility = tk.Button(root, text="Calculate Visits by Facility", bg='green', fg='white', command=amsurg.visits_by_facility)
visits_facility.grid(column=0, row=1, ipadx=10, ipady=10, sticky='NSEW')

visits_asu = tk.Button(root, text="Calculate Visits by ASU", bg='green', fg='white', command=amsurg.visits_by_asu)
visits_asu.grid(column=0, row=2, ipadx=10, ipady=10, sticky='NSEW')




root.mainloop()