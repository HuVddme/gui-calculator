import tkinter as tk

calculation = ""

def add_to_calc(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calc():
    global calculation
    # print(calculation)

    try:
        calculation = str(eval(calculation))
        # calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("300x275") #dimension of the calculator
root.configure(bg="green")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), bg="red", fg="blue")
text_result.grid(columnspan=45)

button_1 = tk.Button(root, text="1", command=lambda: add_to_calc(1), width=5, font=("Arial", 14))
button_1.grid(row=2, column=1)

button_2 = tk.Button(root, text="2", command=lambda: add_to_calc(2), width=5, font=("Arial", 14))
button_2.grid(row=2, column=2)

button_3 = tk.Button(root, text="3", command=lambda: add_to_calc(3), width=5, font=("Arial", 14))
button_3.grid(row=2, column=3)

button_4 = tk.Button(root, text="4", command=lambda: add_to_calc(4), width=5, font=("Arial", 14))
button_4.grid(row=3, column=1)

button_5 = tk.Button(root, text="5", command=lambda: add_to_calc(5), width=5, font=("Arial", 14))
button_5.grid(row=3, column=2)

button_6 = tk.Button(root, text="6", command=lambda: add_to_calc(6), width=5, font=("Arial", 14))
button_6.grid(row=3, column=3)

button_7 = tk.Button(root, text="7", command=lambda: add_to_calc(7), width=5, font=("Arial", 14))
button_7.grid(row=4, column=1)

button_8 = tk.Button(root, text="8", command=lambda: add_to_calc(8), width=5, font=("Arial", 14))
button_8.grid(row=4, column=2)

button_9 = tk.Button(root, text="9", command=lambda: add_to_calc(9), width=5, font=("Arial", 14))
button_9.grid(row=4, column=3)

button_0 = tk.Button(root, text="0", command=lambda: add_to_calc(0), width=5, font=("Arial", 14))
button_0.grid(row=5, column=2)

button_plus = tk.Button(root, text="+", command=lambda: add_to_calc("+"), width=5, font=("Arial", 14))
button_plus.grid(row=2, column=4)

button_minus = tk.Button(root, text="-", command=lambda: add_to_calc("-"), width=5, font=("Arial", 14))
button_minus.grid(row=3, column=4)

button_mult = tk.Button(root, text="*", command=lambda: add_to_calc("*"), width=5, font=("Arial", 14))
button_mult.grid(row=4, column=4)

button_div = tk.Button(root, text="/", command=lambda: add_to_calc("/"), width=5, font=("Arial", 14))
button_div.grid(row=5, column=4)

button_open_par = tk.Button(root, text="(", command=lambda: add_to_calc("("), width=5, font=("Arial", 14))
button_open_par.grid(row=5, column=1)

button_close_par = tk.Button(root, text=")", command=lambda: add_to_calc(")"), width=5, font=("Arial", 14))
button_close_par.grid(row=5, column=3)

button_equal = tk.Button(root, text="=", command=evaluate_calc, width=11, font=("Arial", 14))
button_equal.grid(row=6, column=3, columnspan=2)

button_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14))
button_clear.grid(row=6, column=1, columnspan=2)

root.mainloop() #how it runs