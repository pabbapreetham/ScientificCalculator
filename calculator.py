from tkinter import Tk
from tkinter import StringVar, Entry, Button
from math import pi, e, sin, cos, tan, log, log10, ceil, degrees, radians, exp, asin, acos, floor
from tkinter import *


class calculator(Tk):
    def __init__(self):
        super().__init__()

        self.title('Scientific Calculator')
        self.geometry('410x410')
        self.configure(background="white")
        self.string = StringVar()
        entry = Entry(self, textvariable=self.string)
        entry.grid(row=0, column=0, columnspan=6)
        entry.configure(background="white")        


calculator()


  
        
