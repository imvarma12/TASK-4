import tkinter as tk
import random

# Function to get computer choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice):
    computer_choice = get_computer_choice()
    result = ""
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win!"
    else:
        result = "You lose!"
    
    # Update the result label and score
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    update_score(result)

# Function to update the score
def update_score(result):
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    
    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score - You: 0, Computer: 0")
    result_label.config(text="")

# Initialize scores
user_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Create a title label
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# Create buttons for user choices
button_frame = tk.Frame(root, bg="#f0f0f0")
rock_button = tk.Button(button_frame, text="Rock", command=lambda: determine_winner('rock'), width=10, bg="#4CAF50", fg="white", font=("Helvetica", 14))
paper_button = tk.Button(button_frame, text="Paper", command=lambda: determine_winner('paper'), width=10, bg="#2196F3", fg="white", font=("Helvetica", 14))
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: determine_winner('scissors'), width=10, bg="#f44336", fg="white", font=("Helvetica", 14))

rock_button.pack(side=tk.LEFT, padx=10)
paper_button.pack(side=tk.LEFT, padx=10)
scissors_button.pack(side=tk.LEFT, padx=10)
button_frame.pack(pady=20)

# Create labels for displaying results and scores
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0")
score_label = tk.Label(root, text="Score - You: 0, Computer: 0", font=("Helvetica", 14), bg="#f0f0f0")

# Create a reset button
reset_button = tk.Button(root, text="Reset Game", command=reset_game, bg="#FF9800", fg="white", font=("Helvetica", 14))

# Layout the labels and reset button
result_label.pack(pady=20)
score_label.pack(pady=20)
reset_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()