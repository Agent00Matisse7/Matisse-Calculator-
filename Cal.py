import tkinter as tk
import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '%': operator.mod,
    '**': operator.pow,
    "==": operator.eq,
    "!=": operator.ne,
    "<": operator.lt,
    "<=": operator.le,
    ">": operator.gt,
    ">=": operator.ge,
    "|": operator.or_
}


current_expression = ""
def update_display(value):
    global current_expression
    if value == 'C':
        current_expression = ""
    elif value == '=':
        try:
            result = str(eval(current_expression))
            current_expression = result
        except:
            current_expression = "Error"
    else:
        current_expression += str(value)
    display.delete(0, tk.END)
    display.insert(0, current_expression)

root = tk.Tk()
root.title("Matisse Calculator")
root.geometry("300x400")
root.resizable(False, False)
display = tk.Entry(root, width=16, font=('Arial', 24), bd=5, relief=tk.SUNKEN, bg= "darkorange", fg= "purple", justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    action = lambda x=text: update_display(x)
    if text in ('C', '='):
        color = 'lightcoral' if text == 'C' else 'lightblue'
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=action, bg="purple")
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=action, bg="purple")

    button.grid(row=row, column=col, sticky="nsew")
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()