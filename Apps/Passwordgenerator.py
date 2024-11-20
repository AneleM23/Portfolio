import tkinter as tk
import random
import string

# Function to generate a random password based on user preferences
def generate_password():
    length = int(length_entry.get())  # Get the length of the password from the user
    include_uppercase = uppercase_var.get()  # Whether to include uppercase letters
    include_numbers = numbers_var.get()  # Whether to include numbers
    include_symbols = symbols_var.get()  # Whether to include special characters

    # Define the characters to use in the password
    characters = string.ascii_lowercase  # Always include lowercase letters

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    # Generate the password by randomly selecting characters from the 'characters' string
    password = ''.join(random.choice(characters) for i in range(length))

    # Display the generated password in the result label
    result_text.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets on the window

# Password length input
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

# Checkboxes for user preferences
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var).pack(pady=5)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(pady=5)
tk.Checkbutton(root, text="Include Special Characters", variable=symbols_var).pack(pady=5)

# Button to generate the password
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Result label to display the generated password
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), width=30, height=2, relief="solid")
result_label.pack(pady=10)

# Run the application
root.mainloop()
