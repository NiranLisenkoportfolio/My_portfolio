import tkinter as tk
from tkinter import ttk 

win = tk.Tk()
win.title("Number guessing game")
win.geometry("600x600")

welcome_message = ttk.Label(font=('arial',12),text='Welcome to the number guessing game:)')
welcome_message.pack()

win.mainloop()