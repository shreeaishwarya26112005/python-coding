import tkinter as tk
import random

def determine_winner(player_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    if player_choice == computer_choice:
        result.set("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        result.set("You win! Computer chose " + computer_choice)
    else:
        result.set("You lose! Computer chose " + computer_choice)

def play_rock():
    determine_winner('rock')

def play_paper():
    determine_winner('paper')

def play_scissors():
    determine_winner('scissors')

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create buttons
rock_button = tk.Button(root, text="Rock",bg="#3697f5", command=play_rock)
rock_button.pack(side=tk.LEFT, padx=5, pady=10)

paper_button = tk.Button(root, text="Paper",bg="#fe9037", command=play_paper)
paper_button.pack(side=tk.LEFT, padx=5, pady=10)

scissors_button = tk.Button(root, text="Scissors",bg="#3697f5", command=play_scissors)
scissors_button.pack(side=tk.LEFT, padx=5, pady=10)

# Create label to display result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 14), fg="blue") # Set font size and text color
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
