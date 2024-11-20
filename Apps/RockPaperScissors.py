import tkinter as tk
import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper') or \
         (player_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "You lose!"

# Function for when the player makes a choice
def player_choice(choice):
    # List of possible choices
    choices = ['Rock', 'Paper', 'Scissors']
    
    # Computer makes a random choice
    computer_choice = random.choice(choices)
    
    # Determine the winner
    result = determine_winner(choice, computer_choice)
    
    # Display the result and computer's choice
    result_text.set(f"Computer chose: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Result label
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14), height=4)
result_label.pack(pady=20)

# Buttons for player choices
button_rock = tk.Button(root, text="Rock", width=20, height=2, command=lambda: player_choice('Rock'))
button_rock.pack(pady=5)

button_paper = tk.Button(root, text="Paper", width=20, height=2, command=lambda: player_choice('Paper'))
button_paper.pack(pady=5)

button_scissors = tk.Button(root, text="Scissors", width=20, height=2, command=lambda: player_choice('Scissors'))
button_scissors.pack(pady=5)

# Run the application
root.mainloop()
