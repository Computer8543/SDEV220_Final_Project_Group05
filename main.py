import tkinter as tk


# expression is used to hold the whole line of data
expression: list[str] = ["", "", "", "", "", "", "", "", "", ""]
        
# index is used to hold the index of the data
index: int = 0



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
        
        # Main input window frame
        self.input_window = tk.Frame(self, width=480, height=100, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.input_window.pack(side="top")
        
        # equation is the name of the StringVar() object, and thus will display on the input box of the calculator
        self.equation = tk.StringVar()
        
        
        # Input field where the expression text goes
        self.input_field = tk.Entry(self.input_window, font=('times new roman', 20, 'bold'), textvariable=self.equation, width=50, bg="#eee", bd=2, justify='right')
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)
        self.input_field.focus_set()
        
        
        # create frame for buttons 
        self.buttons_frame = tk.Frame(self, width=640, height=540, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        self.buttons_frame.pack()
        
        # first row of buttons
        
        self.left_parenthesis_button = tk.Button(self.buttons_frame, text = "(", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click("(")).grid(row = 0, column = 3, padx = 1, pady = 1)
        self.right_parenthesis_button = tk.Button(self.buttons_frame, text = ")", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click(")")).grid(row = 0, column = 4, padx = 1, pady = 1)
        # fix up and down buttons
        self.up_button = tk.Button(self.buttons_frame, text = "Up", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.press_up()).grid(row = 0, column = 2, padx = 1, pady = 1)
        self.down_button = tk.Button(self.buttons_frame, text = "Down", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.press_down()).grid(row = 0, column = 1, padx = 1, pady = 1)
        self.division_button = tk.Button(self.buttons_frame, text = "/", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click("/")).grid(row = 0, column = 5, padx = 1, pady = 1)
        
        # second row of buttons
        self.nine_button = tk.Button(self.buttons_frame, text = "9", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click(9)).grid(row = 1, column = 4, padx = 1, pady = 1)
        self.eight_button = tk.Button(self.buttons_frame, text = "8", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click(8)).grid(row = 1, column = 3, padx = 1, pady = 1)
        self.seven_button = tk.Button(self.buttons_frame, text = "7", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click(7)).grid(row = 1, column = 2, padx = 1, pady = 1)
        self.exponentation_button = tk.Button(self.buttons_frame, text = "**", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click("**")).grid(row = 1, column = 1, padx = 1, pady = 1)
        self.multiplication_button = tk.Button(self.buttons_frame, text = "*", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click("*")).grid(row = 1, column = 5, padx = 1, pady = 1)
        
        # third row of buttons
        self.clear_button = tk.Button(self.buttons_frame, text = "Clear", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_clear()).grid(row = 2, column = 1, padx = 1, pady = 1) 
        self.four_button = tk.Button(self.buttons_frame, text = "4", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click(4)).grid(row = 2, column = 2, padx = 1, pady = 1)
        self.five_button = tk.Button(self.buttons_frame, text = "5", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click(5)).grid(row = 2, column = 3, padx = 1, pady = 1)
        self.six_button = tk.Button(self.buttons_frame, text = "6", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click(6)).grid(row = 2, column = 4, padx = 1, pady = 1)
        self.subtraction_button = tk.Button(self.buttons_frame, text = "-", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click("-")).grid(row = 2, column = 5, padx = 1, pady = 1)
        
        # fourth row of buttons
        self.one_button = tk.Button(self.buttons_frame, text = "1", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click(1)).grid(row = 3, column = 2, padx = 1, pady = 1)
        self.two_button = tk.Button(self.buttons_frame, text = "2", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click(2)).grid(row = 3, column = 3, padx = 1, pady = 1)
        self.three_button = tk.Button(self.buttons_frame, text = "3", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click(3)).grid(row = 3, column = 4, padx = 1, pady = 1)
        self.addition_button = tk.Button(self.buttons_frame, text = "+", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click("+")).grid(row = 3, column = 5, padx = 1, pady = 1)
        
        # fifth row of buttons
        self.zero_button = tk.Button(self.buttons_frame, text = "0", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click(0)).grid(row = 4, column = 2, padx = 1, pady = 1)
        self.decimal_point_button = tk.Button(self.buttons_frame, text = ".", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_click(".")).grid(row = 4, column = 3, padx = 1, pady = 1)
        self.equal_button = tk.Button(self.buttons_frame, text = "=", foreground= "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command= lambda: self.button_equal()).grid(row = 4, column = 5, padx = 1, pady = 1) 
        
        # begin mainloop
        self.mainloop()
        
    def press_up(self) -> list[str]:
        """ When you press the up button, it goes back 1 in the index unless it is equal to or less than 0, where the index stops at 0 to prevent an out of bounds error

        Args:
            expression (list[str]): _description_
            index (int): The index of the expression

        Returns:
            list[str]: The expression in the (index minus 1) unless the index is equal to or less than 0, else it would be zero
        """
        global expression
        global index
        return expression[((index - 1) if index > 0 else 0)]
    
    def press_down(self) -> list[str]:
        """When you press the down button, it goes forward 1 in the index unless it is equal to or greater than 9, where it will default to 9 to save space

        Args:
            expression (list[str]):  1 index is a whole line of numbers and symbols inputted into the calculator, up to 10 lines total.
            index (int): The index of the expression

        Returns:
            list[str]: The expression in the (index plus 1) unless the index is equal to or greater than 9, else it defaults to 9 to save space in memory
        """
        global expression
        global index
        return expression[((index + 1) if index < 9 else 9)]
    
    
    def button_equal(self) -> str:
        """ We find what number the expression is equal to 
        and add 1 to the index unless it is 9, 
        where we set the index back to 0. If it creates an error, 
        make an error message.
        Args:
            expression (list[str]): 1 index is a whole line of numbers and symbols inputted into the calculator, up to 10 lines total.
            result (str): The end result of the mathematical expression
            index (int): The index of the expression
        """
        global expression
        global index
        
        
        try:
            expression[index] = self.equation.get()
            result = eval(str(expression[index]))
            if index < 9:
                index += 1
            else:
                index = 0
            return self.equation.set(result)
        except:
            self.equation.set(" error ")
            expression[index] = ""
            return
    
        
    def button_click(self, input) -> str:
        """ We add the input to the expression through string concatenation

        Args:
            expression (list[str]): 1 index is a whole line of numbers and symbols inputted into the calculator, up to 10 lines total.
            input (str): The symbol inputted into the function
            index (int): The index of the expression
        """
        global expression
        global index
        
        expression[index] = expression[index] + str(input)
        return self.equation.set(expression[index]) 
    
    def button_clear(self) -> None:
        """ We clear the input of the expression through creating an empty string as the input

        Args:
            expression (list[str]): 1 index is a whole line of numbers and symbols inputted into the calculator, up to 10 lines total.
            index (int): The index of the expression
        """
        global expression
        global index
        
        expression[index] = ""
        self.equation.set("")
        return
      
      
     
       

# initalize gui class
begin = gui()

