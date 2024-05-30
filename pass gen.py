import tkinter as tk
import string
import random

def generate_password():
    password_length = int(length_entry.get())
    
    if password_length <= 0:
        password_output.config(text="Please enter a valid length")
        return
    
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    password_output.config(text=password, width=40, height=3)  # Adjust width and height as needed

# Create the Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password",bg="#fe9037", command=generate_password)
generate_button.pack()

password_output = tk.Label(root, text="", width=40, height=3)  # Initial width and height
password_output.pack()

# Run the Tkinter event loop
root.mainloop()
