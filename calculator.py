from tkinter import *

# Window
root = Tk()
root.title("Colorful Calculator")
root.geometry("350x500")
root.config(bg="#4FC3F7")

# Entry Box
entry = Entry(root, font=("Arial", 24), bd=8, relief=RIDGE, justify=RIGHT)
entry.pack(fill=BOTH, padx=10, pady=15)

# Functions
def click(value):
    entry.insert(END, value)

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

# Button Frame
frame = Frame(root, bg="#1e1e2f")
frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    row_frame = Frame(frame, bg="#1e1e2f")
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            Button(
                row_frame,
                text=btn,
                font=("Arial", 18, "bold"),
                bg="#81D4FA",
                fg="white",
                width=5,
                height=2,
                command=calculate
            ).pack(side=LEFT, expand=True, fill="both", padx=3, pady=3)
        else:
            Button(
                row_frame,
                text=btn,
                font=("Arial", 18, "bold"),
                bg="#3949ab",
                fg="white",
                width=5,
                height=2,
                command=lambda b=btn: click(b)
            ).pack(side=LEFT, expand=True, fill="both", padx=3, pady=3)

# Clear Button
Button(
    root,
    text="CLEAR",
    font=("Arial", 18, "bold"),
    bg="#d50000",
    fg="white",
    command=clear
).pack(fill="x", padx=10, pady=10)

root.mainloop()