import tkinter as tk
from tkinter import ttk

    
class gui(tk.Tk):
    """ Meant to act as the GUI of the calculator.
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
        self.input_text: str = ""
        
        # Main input window frame
        self.input_window = tk.Frame(self, width=480, height=100, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.input_window.pack(side="top")
        
        # Input field where the expression text goes
        self.input_field = tk.Entry(self.input_window, font=('times new roman', 20, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify='right')
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)
        
        # create frame for buttons 
        self.buttons_frame = tk.Frame(self, width=640, height=540, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.buttons_frame.pack(side="bottom")
        
        # create buttons
    
class memory(gui):
    """ Meant to store and validate data inputted into the calculator
    """
    def __init__(self):
        super().__init__()
        # expression is used to hold the whole line of data
        self.expression: list[str] = [""]
        # index is used to hold the index of the data
        self.index: int = 0
    def press_up(self, expression: list[str], index: int) -> list[str]:
        """ When you press the up button, it goes back 1 in the index unless it is equal to or less than 0, where the index stops at 0 to prevent an out of bounds error

        Args:
            expression (list[str]): _description_
            index (int): The index of the expression

        Returns:
            list[str]: The expression in the (index minus 1) unless the index is equal to or less than 0, else it would be zero
        """
        return expression[((index - 1) if index > 0 else 0)]
    def press_down(self, expression: list[str], index: int) -> list[str]:
        """When you press the down button, it goes forward 1 in the index unless it is equal to or greater than 9, where it will default to 9 to save space

        Args:
            expression (list[str]):  1 index is a whole line of numbers and symbols inputted into the calculator, up to 10 lines total.
            index (int): The index of the expression

        Returns:
            list[str]: The expression in the (index plus 1) unless the index is equal to or greater than 9, else it defaults to 9 to save space in memory
        """
        return expression[((index + 1) if index < 9 else 9)]
    
    
class calculation(memory):
    """ Meant to store various functions called by GUI to calculate.
    """
    def __init__(self):
        super().__init__()
    def button_equal(self, expression: list[str], index: int) -> None:
        """ We find what number the expression is equal to and add 1 to the index

        Args:
            expression (list[str]): 1 index is a whole line of numbers and symbols inputted into the calculator, up to 10 lines total.
            result (str): The end result of the mathematical expression
            index (int): The index of the expression
        """
        result = str(eval(expression[index]))
        calculation.input_text.set(result)
        index += 1
        return
    def button_click(self, expression: list[str], index: int, input: str) -> None:
        """ We add the input to the expression through string concatenation

        Args:
            expression (list[str]): 1 index is a whole line of numbers and symbols inputted into the calculator, up to 10 lines total.
            input (str): The symbol inputted by pushing the button.
            index (int): The index of the expression
        """
        expression[index] = expression[index] + str(input)
        calculation.input_text.set(expression[index])
        return 
    def button_clear(self, expression: list[str], index: int) -> None:
        """ We clear the input of the expression through creating an empty string as the input

        Args:
            expression (list[str]): 1 index is a whole line of numbers and symbols inputted into the calculator, up to 10 lines total.
            index (int): The index of the expression
        """
        expression[index] = ""
        calculation.input_text.set("")
        return 

# start calculation class
begin = calculation()

begin.mainloop()
