import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        
        self.display = tk.Entry(master, width=40, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # create buttons for numbers and operations
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 1, 3)
        self.create_button("-", 2, 3)
        self.create_button("*", 3, 3)
        self.create_button("/", 4, 3)
        self.create_button("C", 5, 0)
        self.create_button("sqrt", 5, 1)
        self.create_button("^2", 5, 2)
        
    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, padx=20, pady=10, command=lambda: self.button_click(text))
        button.grid(row=row, column=column)
        
    def button_click(self, text):
        if text == "=":
            self.calculate()
        elif text == "C":
            self.display.delete(0, tk.END)
        elif text == "sqrt":
            self.display.insert(tk.END, str(math.sqrt(float(self.display.get()))))
        elif text == "^2":
            self.display.insert(tk.END, str(float(self.display.get())**2))
        else:
            self.display.insert(tk.END, text)
            
    def calculate(self):
        expression = self.display.get()
        self.display.delete(0, tk.END)
        try:
            self.display.insert(tk.END, str(eval(expression)))
        except:
            self.display.insert(tk.END, "Error")
            
root = tk.Tk()
my_calculator = Calculator(root)
root.mainloop()
