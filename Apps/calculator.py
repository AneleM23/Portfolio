import tkinter as tk
from math import sin, cos, tan, radians, sqrt

def evaluate_expression(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception:
        return "Error"

def calculate():
    expression = entry.get()
    result = evaluate_expression(expression)
    entry.delete(0, tk.END)
    entry.insert(0, result)

def add_to_expression(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def scientific_operation(operation):
    try:
        value = float(entry.get())
        if operation == "sqrt":
            result = sqrt(value)
        elif operation == "sin":
            result = sin(radians(value))
        elif operation == "cos":
            result = cos(radians(value))
        elif operation == "tan":
            result = tan(radians(value))
        else:
            result = "Error"
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Main window
root = tk.Tk()
root.title("Calculator")

# Entry box
entry = tk.Entry(root, width=20, font=("Arial", 16), bd=5, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: add_to_expression(t)).grid(row=row, column=col)

# Scientific buttons
tk.Button(root, text="√", padx=20, pady=20, command=lambda: scientific_operation("sqrt")).grid(row=5, column=0)
tk.Button(root, text="sin", padx=20, pady=20, command=lambda: scientific_operation("sin")).grid(row=5, column=1)
tk.Button(root, text="cos", padx=20, pady=20, command=lambda: scientific_operation("cos")).grid(row=5, column=2)
tk.Button(root, text="tan", padx=20, pady=20, command=lambda: scientific_operation("tan")).grid(row=5, column=3)

# Clear button
tk.Button(root, text="Clear", padx=20, pady=20, command=clear).grid(row=6, column=0, columnspan=4)

root.mainloop()
