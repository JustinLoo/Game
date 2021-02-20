from tkinter import*
import random
import time


class Game:
    def __init__(self):
        self.tk()
        self.tk.title("Stick Man game | Real Mape and Fake Mape!")
        
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)