import tkinter as tk
from tkinter import StringVar
import random
import string

def generate_password():
    length = int(length_var.get())
    characters = ""

    if use_letters.get() and not use_uppercase.get():
        characters += string.ascii_lowercase
    elif use_letters.get() and use_uppercase.get():
        characters += string.ascii_letters

    if use_numbers.get():
        characters += string.digits
    if use_special.get():
        characters += string.punctuation

    #Error Message
    if not characters:
        error_label.config(text="Select at least one option.", fg="red")
        return

    # Clear any previous error message
    error_label.config(text="")

    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

    password_text.delete(1.0, tk.END)  # Clear previous content
    password_text.insert(tk.END, password)
    password_text.tag_configure("center", justify="center")
    password_text.tag_add("center", 1.0, "end")


def copy_password():
    window.clipboard_clear()
    window.clipboard_append(password_var.get())
    window.update()

def update_length(value):
    length_var.set(str(int(value)))

# Create the main window
window = tk.Tk()
window.title("Password Generator")

window.geometry("350x500")
window.resizable(False, False)

# Password generation variables
length_var = StringVar()
length_var.set("12")  # Default password length
use_letters = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_special = tk.BooleanVar(value=True)
use_uppercase = tk.BooleanVar(value=True)

label_font = ("Helvetica", 14)
button_font = ("Helvetica", 12)

# Title label
title_label = tk.Label(window, text="Password Generator", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=5)

# Text widget for generated password
password_var = StringVar()
password_text = tk.Text(window, height=2, width=25, wrap=tk.WORD, font=label_font)
password_text.grid(row=1, column=0, columnspan=2, pady=5)

copy_button = tk.Button(window, text="Copy Password", command=copy_password, font=button_font)
copy_button.grid(row=2, column=0, columnspan=2, pady=5)

# Password length slider
length_slider = tk.Scale(window, from_=4, to=32, orient=tk.HORIZONTAL, length=200,
                         variable=length_var, command=update_length, font=label_font)
length_slider.grid(row=3, column=0, columnspan=2, pady=5)

# Group checkboxes and labels into a frame
options_frame = tk.Frame(window)
options_frame.grid(row=4, column=0, columnspan=2, pady=5)

tk.Label(options_frame, text="Use Letters", font=label_font).grid(row=0, column=0, pady=2, padx=10, sticky=tk.W)
tk.Checkbutton(options_frame, variable=use_letters).grid(row=0, column=1, pady=2, padx=10, sticky=tk.E)

tk.Label(options_frame, text="Use Numbers", font=label_font).grid(row=1, column=0, pady=2, padx=10, sticky=tk.W)
tk.Checkbutton(options_frame, variable=use_numbers).grid(row=1, column=1, pady=2, padx=10, sticky=tk.E)

tk.Label(options_frame, text="Use Special", font=label_font).grid(row=2, column=0, pady=2, padx=10, sticky=tk.W)
tk.Checkbutton(options_frame, variable=use_special).grid(row=2, column=1, pady=2, padx=10, sticky=tk.E)

tk.Label(options_frame, text="Use Uppercase", font=label_font).grid(row=3, column=0, pady=2, padx=10, sticky=tk.W)
tk.Checkbutton(options_frame, variable=use_uppercase).grid(row=3, column=1, pady=2, padx=10, sticky=tk.E)

# Error label for displaying validation errors
error_label = tk.Label(window, text="", font=("Helvetica", 10), fg="red")
error_label.grid(row=5, column=0, columnspan=2, pady=5)

generate_button = tk.Button(window, text="Generate Password", command=generate_password, font=button_font)
generate_button.grid(row=6, column=0, columnspan=2, pady=5)

# Configure row and column weights for centering
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)
window.grid_rowconfigure(6, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Main loop
window.mainloop()