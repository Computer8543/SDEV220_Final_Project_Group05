import tkinter as tk
from tkinter import ttk

class memory:
    """ Meant to store and validate data inputted into the calculator
    """
    def __init__(self):
        pass
    expression: list[str] = [""]
    x: int = 0
    def press_up(expression, x):
        return expression[((x - 1) if x > 0 else 0)]
    def press_down(expression, x):
        return expression[((x + 1) if x < 9 else 9)]
    
    
class calculation:
    """ Meant to store various functions called by GUI to calculate.
    """
    def __init__(self):
        pass
    def button_equal():
        pass
    def button_click():
        pass
    def button_clear():
        pass
    
class gui(tk.Tk):
    """ Meant to act as the GUI of the calculator.
    Args:
        tk (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        # Title of window
        self.title("Mario's Italian Restaurant Calculator")
        # Pixel size of window
        self.geometry('640x640')
        # To prevent you from resizing the window
        self.resizable(0,0) 
        
        # initialize input_text variable
        input_text: str = ""
        
        # Main input window frame
        self.input_window = tk.Frame(self, width=480, height=100, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.input_window.pack(side="top")
        
        # Input field where the expression text goes
        input_field = tk.Entry(self.input_window, font=('times new roman', 20, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify='right')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)
        
        # create frame for buttons 
        self.buttons_frame = tk.Frame(self, width=640, height=540, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.buttons_frame.pack(side="bottom")
        
        # create buttons
        

    
    
    

# start three classes
storage = memory
math = calculation
begin = gui()

begin.mainloop()
