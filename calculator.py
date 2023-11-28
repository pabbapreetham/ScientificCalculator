from tkinter import Tk
from tkinter import StringVar, Entry, Button
from math import pi, e, sin, cos, tan, log, log10, ceil, degrees, radians, exp, asin, acos, floor
from tkinter import *


class calculator(Tk):
    def __init__(self):
        super().__init__()

        self.title('Scientific Calculator')
        self.geometry('410x600')  # Adjusted height for better visibility
        self.configure(background="#f0f0f0")  # Set background color
        self.string = StringVar()
        entry = Entry(self, textvariable=self.string, font=('Arial', 14))
        entry.grid(row=0, column=0, columnspan=6, pady=10, ipady=10, sticky='nsew')
        entry.configure(background="white")